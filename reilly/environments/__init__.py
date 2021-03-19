from .environment import Environment
from .hierarchical_environment import HierarchicalEnvironment
from .causal_environment import CausalEnvironment
from .gym import *
from .text import TextEnvironment, TextNeighbor
from .medical_treatment import MedicalTreatment
from .medical_treatment_collider import MedicalTreatmentCollider


def ENVIRONMENTS():
    import sys
    import inspect
    module = sys.modules[__name__]
    return [
        value
        for _, value in module.__dict__.items()
        if inspect.isclass(value)
        and issubclass(value, Environment)
        and value != Environment
    ]
