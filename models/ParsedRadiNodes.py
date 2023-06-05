from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedRadiNodesEnum(eEnum):
    nodeId = "nodeId"
    eNBId = "eNBId"
    locCode = "locCode"
    Subnetwork = "Subnetwork"
    system = "system"
    swVersionId = "swVersionId"
    swRelease = "swRelease"
    Vendor = "Vendor"
    mocn = "mocn"
    gNBId = "gNBId"
    hwType = "hwType"
    siteLocation = "siteLocation"
    bfnOffset = "bfnOffset"


class ParsedRadiNodesIndex:
    def __init__(self) -> None:
        self.nodeId = 0
        self.eNBId = 1
        self.locCode = 2
        self.Subnetwork = 3
        self.system = 4
        self.swVersionId = 5
        self.swRelease = 6
        self.Vendor = 7
        self.mocn = 8
        self.gNBId = 9
        self.hwType = 10
        self.siteLocation = 11
        self.bfnOffset = 12
        self.last_index = 13


class ParsedRadiNodes:
    def __init__(
        self,
        nodeId: str,
        eNBId: str,
        locCode: str,
        Subnetwork: str,
        system: str,
        swVersionId: str,
        swRelease: str,
        Vendor: str,
        mocn: str,
        gNBId: str,
        hwType: str,
        siteLocation: str,
        bfnOffset: str,
    ) -> None:
        self.nodeId = nodeId
        self.eNBId = eNBId
        self.locCode = locCode
        self.Subnetwork = Subnetwork
        self.system = system
        self.swVersionId = swVersionId
        self.swRelease = swRelease
        self.Vendor = Vendor
        self.mocn = mocn
        self.gNBId = gNBId
        self.hwType = hwType
        self.siteLocation = siteLocation
        self.bfnOffset = bfnOffset

    def __str__(self) -> str:
        scr = f"nodeId: {self.nodeId}" + "\n"
        scr += f"eNBId: {self.eNBId}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"Subnetwork: {self.Subnetwork}" + "\n"
        scr += f"system: {self.system}" + "\n"
        scr += f"swVersionId: {self.swVersionId}" + "\n"
        scr += f"swRelease: {self.swRelease}" + "\n"
        scr += f"Vendor: {self.Vendor}" + "\n"
        scr += f"mocn: {self.mocn}" + "\n"
        scr += f"gNBId: {self.gNBId}" + "\n"
        scr += f"hwType: {self.hwType}" + "\n"
        scr += f"siteLocation: {self.siteLocation}" + "\n"
        scr += f"bfnOffset: {self.bfnOffset}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.nodeId,
            self.eNBId,
            self.locCode,
            self.Subnetwork,
            self.system,
            self.swVersionId,
            self.swRelease,
            self.Vendor,
            self.mocn,
            self.gNBId,
            self.hwType,
            self.siteLocation,
            self.bfnOffset,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "nodeId",
            "eNBId",
            "locCode",
            "Subnetwork",
            "system",
            "swVersionId",
            "swRelease",
            "Vendor",
            "mocn",
            "gNBId",
            "hwType",
            "siteLocation",
            "bfnOffset",
        ]
