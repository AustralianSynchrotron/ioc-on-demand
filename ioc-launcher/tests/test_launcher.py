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
    expected_call = call('test', host_config=ANY, tty=True)
    assert docker_client.create_container.call_args == expected_call


def test_launcher_returns_id(docker_client, launcher):
    docker_client.create_container.return_value = {'Id': '1a2b3c'}
    result = run_coro(launcher.launch(image='test', network='host', tty=True))
    assert result == '1a2b3c'
