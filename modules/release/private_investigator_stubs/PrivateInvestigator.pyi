"""Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End"""
from typing import Union, List
import os
Suspect = Union[DAT, COMP]

class PrivateInvestigator:
    """
	PrivateInvestigator description
	"""

    def __init__(self, ownerComp):
        self.ownerComp: COMP = ownerComp
        pass

    @property
    def PrefabAuthor(self):
        pass

    @property
    def Author(self):
        pass

    def possible_suspects(self, op_type: str):
        pass

    def ReinitSuspects(self):
        pass

    def Scan(self):
        pass

    def Update(self):
        pass

    @property
    def State(self):
        pass

    def Add(self, operator: Suspect):
        pass

    def Dirty(self):
        pass

    def SaveAllDirty(self):
        pass

    def SaveItems(self, items: List[COMP]):
        pass

    def Save(self, operator: COMP):
        pass

    def Release(self, operator: COMP):
        pass

    def Get_Dirt(self, operator: Suspect):
        pass

    def Get_Info(self, operator: Suspect):
        pass

    def Edit(self, operator: Suspect):
        pass

    def View(self, operator: Suspect):
        pass

    def Reload(self, operator: Suspect):
        pass