from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedSitesEnum(eEnum):
    locCode = "locCode"
    siteName = "siteName"
    siteIsd = "siteIsd"
    parent = "parent"
    csd = "csd"
    cma = "cma"
    er = "er"
    prv = "prv"
    latitude = "latitude"
    longitude = "longitude"
    towerType = "towerType"
    rnc = "rnc"
    bsc = "bsc"
    GSM = "GSM"
    UMTS = "UMTS"
    LTE = "LTE"
    NR = "NR"
    NBIOT = "NBIOT"
    csdUid = "csdUid"
    mocnNodes = "mocnNodes"
    azimuthCount = "azimuthCount"
    avgAntennaHeight = "avgAntennaHeight"
    lte_shifted = "lte_shifted"


class ParsedSitesIndex:
    def __init__(self) -> None:
        self.locCode = 0
        self.siteName = 1
        self.siteIsd = 2
        self.parent = 3
        self.csd = 4
        self.cma = 5
        self.er = 6
        self.prv = 7
        self.latitude = 8
        self.longitude = 9
        self.towerType = 10
        self.rnc = 11
        self.bsc = 12
        self.GSM = 13
        self.UMTS = 14
        self.LTE = 15
        self.NR = 16
        self.NBIOT = 17
        self.csdUid = 18
        self.mocnNodes = 19
        self.azimuthCount = 20
        self.avgAntennaHeight = 21
        self.lte_shifted = 22
        self.last_index = 23


class ParsedSites:
    def __init__(
        self,
        locCode: str,
        siteName: str,
        siteIsd: str,
        parent: str,
        csd: str,
        cma: str,
        er: str,
        prv: str,
        latitude: str,
        longitude: str,
        towerType: str,
        rnc: str,
        bsc: str,
        GSM: str,
        UMTS: str,
        LTE: str,
        NR: str,
        NBIOT: str,
        csdUid: str,
        mocnNodes: str,
        azimuthCount: str,
        avgAntennaHeight: str,
        lte_shifted: str,
    ) -> None:
        self.locCode = locCode
        self.siteName = siteName
        self.siteIsd = siteIsd
        self.parent = parent
        self.csd = csd
        self.cma = cma
        self.er = er
        self.prv = prv
        self.latitude = latitude
        self.longitude = longitude
        self.towerType = towerType
        self.rnc = rnc
        self.bsc = bsc
        self.GSM = GSM
        self.UMTS = UMTS
        self.LTE = LTE
        self.NR = NR
        self.NBIOT = NBIOT
        self.csdUid = csdUid
        self.mocnNodes = mocnNodes
        self.azimuthCount = azimuthCount
        self.avgAntennaHeight = avgAntennaHeight
        self.lte_shifted = lte_shifted

    def __str__(self) -> str:
        scr = f"locCode: {self.locCode}" + "\n"
        scr += f"siteName: {self.siteName}" + "\n"
        scr += f"siteIsd: {self.siteIsd}" + "\n"
        scr += f"parent: {self.parent}" + "\n"
        scr += f"csd: {self.csd}" + "\n"
        scr += f"cma: {self.cma}" + "\n"
        scr += f"er: {self.er}" + "\n"
        scr += f"prv: {self.prv}" + "\n"
        scr += f"latitude: {self.latitude}" + "\n"
        scr += f"longitude: {self.longitude}" + "\n"
        scr += f"towerType: {self.towerType}" + "\n"
        scr += f"rnc: {self.rnc}" + "\n"
        scr += f"bsc: {self.bsc}" + "\n"
        scr += f"GSM: {self.GSM}" + "\n"
        scr += f"UMTS: {self.UMTS}" + "\n"
        scr += f"LTE: {self.LTE}" + "\n"
        scr += f"NR: {self.NR}" + "\n"
        scr += f"NBIOT: {self.NBIOT}" + "\n"
        scr += f"csdUid: {self.csdUid}" + "\n"
        scr += f"mocnNodes: {self.mocnNodes}" + "\n"
        scr += f"azimuthCount: {self.azimuthCount}" + "\n"
        scr += f"avgAntennaHeight: {self.avgAntennaHeight}" + "\n"
        scr += f"lte_shifted: {self.lte_shifted}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.locCode,
            self.siteName,
            self.siteIsd,
            self.parent,
            self.csd,
            self.cma,
            self.er,
            self.prv,
            self.latitude,
            self.longitude,
            self.towerType,
            self.rnc,
            self.bsc,
            self.GSM,
            self.UMTS,
            self.LTE,
            self.NR,
            self.NBIOT,
            self.csdUid,
            self.mocnNodes,
            self.azimuthCount,
            self.avgAntennaHeight,
            self.lte_shifted,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "locCode",
            "siteName",
            "siteIsd",
            "parent",
            "csd",
            "cma",
            "er",
            "prv",
            "latitude",
            "longitude",
            "towerType",
            "rnc",
            "bsc",
            "GSM",
            "UMTS",
            "LTE",
            "NR",
            "NBIOT",
            "csdUid",
            "mocnNodes",
            "azimuthCount",
            "avgAntennaHeight",
            "lte_shifted",
        ]
