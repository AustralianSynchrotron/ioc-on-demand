from random import choice
from string import ascii_uppercase, digits

DEFAULT_PREFIXES = (
  'APPARATUS', 'APPLIANCE', 'BLACKBOX', 'CONTRAPTION', 'DEVICE', 'DOODAD',
  'DOOHICKEY', 'EQUIPMENT', 'GADGET', 'GEAR', 'GIZMO', 'IMPLEMENT',
  'INSTRUMENT', 'JIG', 'MACHINE', 'RIG', 'SETUP', 'THINGAMAJIG', 'TOOL',
  'WHATSIT', 'WIDGET',
)

class HostnameGenerator:

    def __init__(self, *, prefixes=DEFAULT_PREFIXES):
        self._prefixes = prefixes

    def __next__(self):
        prefix = choice(self._prefixes)
        end = self._make_end()
        return '{prefix}-{end}'.format(prefix=prefix, end=end)

    def _make_end(self):
        return choice(digits) + choice(digits) + choice(ascii_uppercase)
