
from .plugin import SimStatePlugin


class SimStateConfiguration(SimStatePlugin):

    __slots__ = [ 'symbolic_ip_max_targets', 'jumptable_symbolic_ip_max_targets' ]

    def __init__(self,
                 symbolic_ip_max_targets=None,
                 jumptable_symbolic_ip_max_targets=None,
                 ):
        super(SimStateConfiguration, self).__init__()

        self.symbolic_ip_max_targets = 256 if symbolic_ip_max_targets is None else symbolic_ip_max_targets
        self.jumptable_symbolic_ip_max_targets = 16384 \
            if jumptable_symbolic_ip_max_targets is None else jumptable_symbolic_ip_max_targets

    def copy(self, memo):  # pylint:disable=unused-argument
        s = SimStateConfiguration()

        for slot in SimStateConfiguration.__slots__:
            setattr(s, slot, getattr(self, slot))

        return s

    def merge(self, _others, _merge_conditions, _common_ancestor=None):
        return self.copy(None)

    def widen(self, _others):
        return self.copy(None)


from ..sim_state import SimState
SimState.register_default('config', SimStateConfiguration)
