from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedGsmNodesEnum(eEnum):
    site = "site"
    msc = "msc"
    bsc = "bsc"
    Locationcode = "Locationcode"


class ParsedGsmNodesIndex:
    def __init__(self) -> None:
        self.site = 0
        self.msc = 1
        self.bsc = 2
        self.Locationcode = 3
        self.last_index = 4


class ParsedGsmNodes:
    def __init__(
        self,
        site: str,
        msc: str,
        bsc: str,
        Locationcode: str,
    ) -> None:
        self.site = site
        self.msc = msc
        self.bsc = bsc
        self.Locationcode = Locationcode

    def __str__(self) -> str:
        scr = f"site: {self.site}" + "\n"
        scr += f"msc: {self.msc}" + "\n"
        scr += f"bsc: {self.bsc}" + "\n"
        scr += f"Locationcode: {self.Locationcode}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.site,
            self.msc,
            self.bsc,
            self.Locationcode,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "site",
            "msc",
            "bsc",
            "Locationcode",
        ]
