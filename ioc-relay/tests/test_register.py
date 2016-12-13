import asyncio
from unittest.mock import call, ANY
import json

import numpy as np
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
    register.subscribe(ws, 'the_pv')
    assert MockPV.call_args[0][0] == 'the_pv'
    assert 'the_pv' in register._pvs
    assert ws in register._subscribers['the_pv']


def test_subscribe_only_creates_pv_once(register, MockPV):
    ws1, ws2 = object(), object()
    register.subscribe(ws1, 'X')
    register.subscribe(ws2, 'X')
    assert MockPV.call_count == 1


def test_serializes_numpy_arrays(register):
    payload = register._make_payload(pvname='xxx', value=np.array([1,2,3]),
                                     type='time_double', char_value='')
    data = json.loads(payload)
    assert data['value'] == [1, 2, 3]


def test_returns_char_value_for_char_waveforms(register):
    payload = register._make_payload(pvname='xxx', value=np.array([]),
                                     type='time_char', char_value='the_string')
    data = json.loads(payload)
    assert data['value'] == 'the_string'
