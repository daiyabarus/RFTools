from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedLteCellsEnum(eEnum):
    Cell = "Cell"
    ERBS = "ERBS"
    locCode = "locCode"
    sectorCarrierRef = "sectorCarrierRef"
    TAC = "TAC"
    CellID = "CellID"
    ECI = "ECI"
    PCI = "PCI"
    earfcnDL = "earfcnDL"
    Azimuth = "Azimuth"
    BW = "BW"
    ERPSectorStatusDesc = "ERPSectorStatusDesc"
    hbw = "hbw"
    antennaHeight = "antennaHeight"
    vbw = "vbw"
    antennaType = "antennaType"
    electricalAntennaTilt = "electricalAntennaTilt"
    maxTxPower = "maxTxPower"
    transmit = "transmit"
    configuredPower = "configuredPower"
    isd = "isd"
    totalSum = "totalSum"
    lteTechnology = "lteTechnology"
    catm1 = "catm1"
    rru = "rru"
    productName = "productName"
    plmnReserved = "plmnReserved"
    primaryUpperLayerInd = "primaryUpperLayerInd"
    freqBand = "freqBand"
    essScPairId = "essScPairId"
    cellRange = "cellRange"
    freq = "freq"


class ParsedLteCellsIndex:
    def __init__(self) -> None:
        self.Cell = 0
        self.ERBS = 1
        self.locCode = 2
        self.sectorCarrierRef = 3
        self.TAC = 4
        self.CellID = 5
        self.ECI = 6
        self.PCI = 7
        self.earfcnDL = 8
        self.Azimuth = 9
        self.BW = 10
        self.ERPSectorStatusDesc = 11
        self.hbw = 12
        self.antennaHeight = 13
        self.vbw = 14
        self.antennaType = 15
        self.electricalAntennaTilt = 16
        self.maxTxPower = 17
        self.transmit = 18
        self.configuredPower = 19
        self.isd = 20
        self.totalSum = 21
        self.lteTechnology = 22
        self.catm1 = 23
        self.rru = 24
        self.productName = 25
        self.plmnReserved = 26
        self.primaryUpperLayerInd = 27
        self.freqBand = 28
        self.essScPairId = 29
        self.cellRange = 30
        self.freq = 31
        self.last_index = 32


class ParsedLteCells:
    def __init__(
        self,
        Cell: str,
        ERBS: str,
        locCode: str,
        sectorCarrierRef: str,
        TAC: str,
        CellID: str,
        ECI: str,
        PCI: str,
        earfcnDL: str,
        Azimuth: str,
        BW: str,
        ERPSectorStatusDesc: str,
        hbw: str,
        antennaHeight: str,
        vbw: str,
        antennaType: str,
        electricalAntennaTilt: str,
        maxTxPower: str,
        transmit: str,
        configuredPower: str,
        isd: str,
        totalSum: str,
        lteTechnology: str,
        catm1: str,
        rru: str,
        productName: str,
        plmnReserved: str,
        primaryUpperLayerInd: str,
        freqBand: str,
        essScPairId: str,
        cellRange: str,
        freq: str,
    ) -> None:
        self.Cell = Cell
        self.ERBS = ERBS
        self.locCode = locCode
        self.sectorCarrierRef = sectorCarrierRef
        self.TAC = TAC
        self.CellID = CellID
        self.ECI = ECI
        self.PCI = PCI
        self.earfcnDL = earfcnDL
        self.Azimuth = Azimuth
        self.BW = BW
        self.ERPSectorStatusDesc = ERPSectorStatusDesc
        self.hbw = hbw
        self.antennaHeight = antennaHeight
        self.vbw = vbw
        self.antennaType = antennaType
        self.electricalAntennaTilt = electricalAntennaTilt
        self.maxTxPower = maxTxPower
        self.transmit = transmit
        self.configuredPower = configuredPower
        self.isd = isd
        self.totalSum = totalSum
        self.lteTechnology = lteTechnology
        self.catm1 = catm1
        self.rru = rru
        self.productName = productName
        self.plmnReserved = plmnReserved
        self.primaryUpperLayerInd = primaryUpperLayerInd
        self.freqBand = freqBand
        self.essScPairId = essScPairId
        self.cellRange = cellRange
        self.freq = freq

    def __str__(self) -> str:
        scr = f"Cell: {self.Cell}" + "\n"
        scr += f"ERBS: {self.ERBS}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"sectorCarrierRef: {self.sectorCarrierRef}" + "\n"
        scr += f"TAC: {self.TAC}" + "\n"
        scr += f"CellID: {self.CellID}" + "\n"
        scr += f"ECI: {self.ECI}" + "\n"
        scr += f"PCI: {self.PCI}" + "\n"
        scr += f"earfcnDL: {self.earfcnDL}" + "\n"
        scr += f"Azimuth: {self.Azimuth}" + "\n"
        scr += f"BW: {self.BW}" + "\n"
        scr += f"ERPSectorStatusDesc: {self.ERPSectorStatusDesc}" + "\n"
        scr += f"hbw: {self.hbw}" + "\n"
        scr += f"antennaHeight: {self.antennaHeight}" + "\n"
        scr += f"vbw: {self.vbw}" + "\n"
        scr += f"antennaType: {self.antennaType}" + "\n"
        scr += f"electricalAntennaTilt: {self.electricalAntennaTilt}" + "\n"
        scr += f"maxTxPower: {self.maxTxPower}" + "\n"
        scr += f"transmit: {self.transmit}" + "\n"
        scr += f"configuredPower: {self.configuredPower}" + "\n"
        scr += f"isd: {self.isd}" + "\n"
        scr += f"totalSum: {self.totalSum}" + "\n"
        scr += f"lteTechnology: {self.lteTechnology}" + "\n"
        scr += f"catm1: {self.catm1}" + "\n"
        scr += f"rru: {self.rru}" + "\n"
        scr += f"productName: {self.productName}" + "\n"
        scr += f"plmnReserved: {self.plmnReserved}" + "\n"
        scr += f"primaryUpperLayerInd: {self.primaryUpperLayerInd}" + "\n"
        scr += f"freqBand: {self.freqBand}" + "\n"
        scr += f"essScPairId: {self.essScPairId}" + "\n"
        scr += f"cellRange: {self.cellRange}" + "\n"
        scr += f"freq: {self.freq}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.Cell,
            self.ERBS,
            self.locCode,
            self.sectorCarrierRef,
            self.TAC,
            self.CellID,
            self.ECI,
            self.PCI,
            self.earfcnDL,
            self.Azimuth,
            self.BW,
            self.ERPSectorStatusDesc,
            self.hbw,
            self.antennaHeight,
            self.vbw,
            self.antennaType,
            self.electricalAntennaTilt,
            self.maxTxPower,
            self.transmit,
            self.configuredPower,
            self.isd,
            self.totalSum,
            self.lteTechnology,
            self.catm1,
            self.rru,
            self.productName,
            self.plmnReserved,
            self.primaryUpperLayerInd,
            self.freqBand,
            self.essScPairId,
            self.cellRange,
            self.freq,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "Cell",
            "ERBS",
            "locCode",
            "sectorCarrierRef",
            "TAC",
            "CellID",
            "ECI",
            "PCI",
            "earfcnDL",
            "Azimuth",
            "BW",
            "ERPSectorStatusDesc",
            "hbw",
            "antennaHeight",
            "vbw",
            "antennaType",
            "electricalAntennaTilt",
            "maxTxPower",
            "transmit",
            "configuredPower",
            "isd",
            "totalSum",
            "lteTechnology",
            "catm1",
            "rru",
            "productName",
            "plmnReserved",
            "primaryUpperLayerInd",
            "freqBand",
            "essScPairId",
            "cellRange",
            "freq",
        ]
