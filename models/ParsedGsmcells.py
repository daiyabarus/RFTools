from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedGsmcellsEnum(eEnum):
    cell = "cell"
    locCode = "locCode"
    ci = "ci"
    lac = "lac"
    ncc = "ncc"
    bcc = "bcc"
    bcchno = "bcchno"
    Azimuth = "Azimuth"
    frequency = "frequency"


class ParsedGsmcellsIndex:
    def __init__(self) -> None:
        self.cell = 0
        self.locCode = 1
        self.ci = 2
        self.lac = 3
        self.ncc = 4
        self.bcc = 5
        self.bcchno = 6
        self.Azimuth = 7
        self.frequency = 8
        self.last_index = 9


class ParsedGsmcells:
    def __init__(
        self,
        cell: str,
        locCode: str,
        ci: str,
        lac: str,
        ncc: str,
        bcc: str,
        bcchno: str,
        Azimuth: str,
        frequency: str,
    ) -> None:
        self.cell = cell
        self.locCode = locCode
        self.ci = ci
        self.lac = lac
        self.ncc = ncc
        self.bcc = bcc
        self.bcchno = bcchno
        self.Azimuth = Azimuth
        self.frequency = frequency

    def __str__(self) -> str:
        scr = f"cell: {self.cell}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"ci: {self.ci}" + "\n"
        scr += f"lac: {self.lac}" + "\n"
        scr += f"ncc: {self.ncc}" + "\n"
        scr += f"bcc: {self.bcc}" + "\n"
        scr += f"bcchno: {self.bcchno}" + "\n"
        scr += f"Azimuth: {self.Azimuth}" + "\n"
        scr += f"frequency: {self.frequency}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.cell,
            self.locCode,
            self.ci,
            self.lac,
            self.ncc,
            self.bcc,
            self.bcchno,
            self.Azimuth,
            self.frequency,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "cell",
            "locCode",
            "ci",
            "lac",
            "ncc",
            "bcc",
            "bcchno",
            "Azimuth",
            "frequency",
        ]
