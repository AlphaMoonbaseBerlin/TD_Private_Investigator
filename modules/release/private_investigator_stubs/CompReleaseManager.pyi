from _typeshed import Incomplete
from typing import Union

Suspect = Union[textDAT, COMP]

class CompReleaseManager:
    ownerComp: Incomplete
    def __init__(self, ownerComp) -> None: ...
    def createStubs(self, target: textDAT, meta: dict): ...
    def prepare(self, target: Suspect, meta: dict): ...
    def run_prerelease(self, target: COMP): ...
    def Release(self, target_component: COMP): ...