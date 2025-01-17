"""Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End"""
import os
from typing import Union
Suspect = Union[textDAT, COMP]
import functools, pathlib
import naiveStubser

class CompReleaseManager:
    """
	CompReleaseManager description
	"""

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        pass

    def createStubs(self, target: textDAT, meta: dict):
        pass

    def prepare(self, target: Suspect, meta: dict):
        pass

    def run_prerelease(self, target: COMP):
        pass

    def Release(self, target_component: COMP):
        pass