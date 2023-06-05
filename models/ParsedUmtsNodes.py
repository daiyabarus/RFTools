from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedUmtsNodesEnum(eEnum):
    nodeB = "nodeB"
    locCode = "locCode"
    rnc = "rnc"
    nodeBFunctionIubLink = "nodeBFunctionIubLink"
    Vendor = "Vendor"


class ParsedUmtsNodesIndex:
    def __init__(self) -> None:
        self.nodeB = 0
        self.locCode = 1
        self.rnc = 2
        self.nodeBFunctionIubLink = 3
        self.Vendor = 4
        self.last_index = 5


class ParsedUmtsNodes:
    def __init__(
        self,
        nodeB: str,
        locCode: str,
        rnc: str,
        nodeBFunctionIubLink: str,
        Vendor: str,
    ) -> None:
        self.nodeB = nodeB
        self.locCode = locCode
        self.rnc = rnc
        self.nodeBFunctionIubLink = nodeBFunctionIubLink
        self.Vendor = Vendor

    def __str__(self) -> str:
        scr = f"nodeB: {self.nodeB}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"rnc: {self.rnc}" + "\n"
        scr += f"nodeBFunctionIubLink: {self.nodeBFunctionIubLink}" + "\n"
        scr += f"Vendor: {self.Vendor}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.nodeB,
            self.locCode,
            self.rnc,
            self.nodeBFunctionIubLink,
            self.Vendor,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "nodeB",
            "locCode",
            "rnc",
            "nodeBFunctionIubLink",
            "Vendor",
        ]
