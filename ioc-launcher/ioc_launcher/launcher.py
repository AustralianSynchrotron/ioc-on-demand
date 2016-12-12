import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

from .utils import HostnameGenerator


class Launcher:
    def __init__(self, *, docker_client, max_workers, hostname_generator=None):
        executor = ThreadPoolExecutor(max_workers=max_workers)
        self._docker = AsyncDockerClient(docker_client, executor=executor)
        self._hostname_generator = hostname_generator or HostnameGenerator()

    async def launch(self, *, image, network, tty=False):
        host_config = await self._docker.create_host_config(network_mode=network)
        hostname = next(self._hostname_generator)
        ioc = await self._docker.create_container(image,
                                                  hostname=hostname,
                                                  host_config=host_config,
                                                  tty=tty)
        await self._docker.start(ioc)
        return hostname


class AsyncDockerClient:
    '''Run DockerClient methods in an executor.

    Copied from https://github.com/jupyter/tmpnb and modified for asyncio.
    '''
    def __init__(self, docker_client, *, executor, loop=None):
        self._docker_client = docker_client
        self._executor = executor
        self._loop = loop or asyncio.get_event_loop()

    def __getattr__(self, name):
        '''Creates an async function, based on docker_client.name that runs in the
        executor. If name is not a callable, returns the attribute directly.
        '''
        fn = getattr(self._docker_client, name)

        # Make sure it really is a function first
        if not callable(fn):
            return fn

        async def method(*args, **kwargs):
            bound_fn = partial(fn, *args, **kwargs)
            return await self._loop.run_in_executor(self._executor, bound_fn)

        return method
