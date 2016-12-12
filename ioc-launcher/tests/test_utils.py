import re

from ioc_launcher.utils import HostnameGenerator


def test_hostname_generator():
    generator = HostnameGenerator(prefixes=('GADGET',))
    hostname = next(generator)
    assert re.match(r'GADGET-[A-Z0-9]{3}', hostname)
