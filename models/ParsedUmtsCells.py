from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedUmtsCellsEnum(eEnum):
    utranCell = "utranCell"
    nodeB = "nodeB"
    locCode = "locCode"
    cellId = "cellId"
    sc = "sc"
    lac = "lac"
    rac = "rac"
    uarfcnUl = "uarfcnUl"
    uarfcnDl = "uarfcnDl"
    azimuth = "azimuth"
    HBW = "HBW"
    erpSectorStatusDesc = "erpSectorStatusDesc"
    frequency = "frequency"


class ParsedUmtsCellsIndex:
    def __init__(self) -> None:
        self.utranCell = 0
        self.nodeB = 1
        self.locCode = 2
        self.cellId = 3
        self.sc = 4
        self.lac = 5
        self.rac = 6
        self.uarfcnUl = 7
        self.uarfcnDl = 8
        self.azimuth = 9
        self.HBW = 10
        self.erpSectorStatusDesc = 11
        self.frequency = 12
        self.last_index = 13


class ParsedUmtsCells:
    def __init__(
        self,
        utranCell: str,
        nodeB: str,
        locCode: str,
        cellId: str,
        sc: str,
        lac: str,
        rac: str,
        uarfcnUl: str,
        uarfcnDl: str,
        azimuth: str,
        HBW: str,
        erpSectorStatusDesc: str,
        frequency: str,
    ) -> None:
        self.utranCell = utranCell
        self.nodeB = nodeB
        self.locCode = locCode
        self.cellId = cellId
        self.sc = sc
        self.lac = lac
        self.rac = rac
        self.uarfcnUl = uarfcnUl
        self.uarfcnDl = uarfcnDl
        self.azimuth = azimuth
        self.HBW = HBW
        self.erpSectorStatusDesc = erpSectorStatusDesc
        self.frequency = frequency

    def __str__(self) -> str:
        scr = f"utranCell: {self.utranCell}" + "\n"
        scr += f"nodeB: {self.nodeB}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"cellId: {self.cellId}" + "\n"
        scr += f"sc: {self.sc}" + "\n"
        scr += f"lac: {self.lac}" + "\n"
        scr += f"rac: {self.rac}" + "\n"
        scr += f"uarfcnUl: {self.uarfcnUl}" + "\n"
        scr += f"uarfcnDl: {self.uarfcnDl}" + "\n"
        scr += f"azimuth: {self.azimuth}" + "\n"
        scr += f"HBW: {self.HBW}" + "\n"
        scr += f"erpSectorStatusDesc: {self.erpSectorStatusDesc}" + "\n"
        scr += f"frequency: {self.frequency}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.utranCell,
            self.nodeB,
            self.locCode,
            self.cellId,
            self.sc,
            self.lac,
            self.rac,
            self.uarfcnUl,
            self.uarfcnDl,
            self.azimuth,
            self.HBW,
            self.erpSectorStatusDesc,
            self.frequency,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "utranCell",
            "nodeB",
            "locCode",
            "cellId",
            "sc",
            "lac",
            "rac",
            "uarfcnUl",
            "uarfcnDl",
            "azimuth",
            "HBW",
            "erpSectorStatusDesc",
            "frequency",
        ]
