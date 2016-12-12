import asyncio
from unittest.mock import create_autospec, call, ANY

import pytest
from docker import Client

from ioc_launcher.launcher import Launcher


@pytest.fixture
def docker_client():
    yield create_autospec(Client, instance=True, spec_set=True)


@pytest.fixture
def launcher(docker_client):
    yield Launcher(docker_client=docker_client, max_workers=1)


def run_coro(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def test_launcher_calls_create_container(docker_client, launcher):
    run_coro(launcher.launch(image='test', network='host', tty=True))
    create_expected_call = call('test', hostname=ANY, host_config=ANY, tty=True)
    assert docker_client.create_container.call_args == create_expected_call


def test_launcher_uses_hostname_generator(docker_client):
    launcher = Launcher(docker_client=docker_client, max_workers=1,
                        hostname_generator=iter(['THE_HOSTNAME']))
    response = run_coro(launcher.launch(image='test', network='host', tty=True))
    assert docker_client.create_container.call_args[1]['hostname'] == 'THE_HOSTNAME'
    assert response == 'THE_HOSTNAME'
