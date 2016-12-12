import asyncio
from unittest.mock import call, ANY

import pytest

from ioc_relay.register import Register


@pytest.fixture
def register():
    loop = asyncio.get_event_loop()
    yield Register(loop=loop)


@pytest.fixture
def MockPV(mocker):
    yield mocker.patch('ioc_relay.register.PV', autospec=True, spec_set=True)


def test_subscribes_pvs(register, MockPV):
    ws = object()
    register.subscribe(ws, 'X')
    assert MockPV.call_args == call('X', callback=ANY)
    assert 'X' in register._pvs
    assert ws in register._subscribers['X']


def test_subscribe_only_creates_pv_once(register, MockPV):
    ws1, ws2 = object(), object()
    register.subscribe(ws1, 'X')
    register.subscribe(ws2, 'X')
    assert MockPV.call_count == 1
