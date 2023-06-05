from typing import List

from utils.to_get import ExclusiveEnum as eEnum


class ParsedNrCellsEnum(eEnum):
    nRCellDUId = "nRCellDUId"
    nodeId = "nodeId"
    locCode = "locCode"
    gNbDuFunctionId = "gNbDuFunctionId"
    administrativeState = "administrativeState"
    availabilityStatus = "availabilityStatus"
    cellBarred = "cellBarred"
    cellLocalId = "cellLocalId"
    cellReservedForOperator = "cellReservedForOperator"
    cellState = "cellState"
    nCGI = "nCGI"
    nCI = "nCI"
    nRPCI = "nRPCI"
    nRSectorCarrier = "nRSectorCarrier"
    nRTAC = "nRTAC"
    operationalState = "operationalState"
    qQualMin = "qQualMin"
    qRxLevMin = "qRxLevMin"
    rachRootSequence = "rachRootSequence"
    ssbDuration = "ssbDuration"
    ssbFrequency = "ssbFrequency"
    ssbFrequencyAutoSelected = "ssbFrequencyAutoSelected"
    ssbOffset = "ssbOffset"
    ssbPeriodicity = "ssbPeriodicity"
    ssbSubCarrierSpacing = "ssbSubCarrierSpacing"
    subCarrierSpacing = "subCarrierSpacing"
    tddLteCoexistence = "tddLteCoexistence"
    tddSpecialSlotPattern = "tddSpecialSlotPattern"
    tddUlDlPattern = "tddUlDlPattern"
    arfcnDL = "arfcnDL"
    arfcnUL = "arfcnUL"
    bSChannelBwDL = "bSChannelBwDL"
    bSChannelBwUL = "bSChannelBwUL"
    azimuth = "azimuth"
    erpSectorStatusDesc = "erpSectorStatusDesc"
    freq = "freq"
    bandList = "bandList"
    pLMNIdList = "pLMNIdList"
    essScPairId = "essScPairId"
    NRCellDUuserLabel = "NRCellDUuserLabel"
    erpSectorTech = "erpSectorTech"


class ParsedNrCellsIndex:
    def __init__(self) -> None:
        self.nRCellDUId = 0
        self.nodeId = 1
        self.locCode = 2
        self.gNbDuFunctionId = 3
        self.administrativeState = 4
        self.availabilityStatus = 5
        self.cellBarred = 6
        self.cellLocalId = 7
        self.cellReservedForOperator = 8
        self.cellState = 9
        self.nCGI = 10
        self.nCI = 11
        self.nRPCI = 12
        self.nRSectorCarrier = 13
        self.nRTAC = 14
        self.operationalState = 15
        self.qQualMin = 16
        self.qRxLevMin = 17
        self.rachRootSequence = 18
        self.ssbDuration = 19
        self.ssbFrequency = 20
        self.ssbFrequencyAutoSelected = 21
        self.ssbOffset = 22
        self.ssbPeriodicity = 23
        self.ssbSubCarrierSpacing = 24
        self.subCarrierSpacing = 25
        self.tddLteCoexistence = 26
        self.tddSpecialSlotPattern = 27
        self.tddUlDlPattern = 28
        self.arfcnDL = 29
        self.arfcnUL = 30
        self.bSChannelBwDL = 31
        self.bSChannelBwUL = 32
        self.azimuth = 33
        self.erpSectorStatusDesc = 34
        self.freq = 35
        self.bandList = 36
        self.pLMNIdList = 37
        self.essScPairId = 38
        self.NRCellDUuserLabel = 39
        self.erpSectorTech = 40
        self.last_index = 41


class ParsedNrCells:
    def __init__(
        self,
        nRCellDUId: str,
        nodeId: str,
        locCode: str,
        gNbDuFunctionId: str,
        administrativeState: str,
        availabilityStatus: str,
        cellBarred: str,
        cellLocalId: str,
        cellReservedForOperator: str,
        cellState: str,
        nCGI: str,
        nCI: str,
        nRPCI: str,
        nRSectorCarrier: str,
        nRTAC: str,
        operationalState: str,
        qQualMin: str,
        qRxLevMin: str,
        rachRootSequence: str,
        ssbDuration: str,
        ssbFrequency: str,
        ssbFrequencyAutoSelected: str,
        ssbOffset: str,
        ssbPeriodicity: str,
        ssbSubCarrierSpacing: str,
        subCarrierSpacing: str,
        tddLteCoexistence: str,
        tddSpecialSlotPattern: str,
        tddUlDlPattern: str,
        arfcnDL: str,
        arfcnUL: str,
        bSChannelBwDL: str,
        bSChannelBwUL: str,
        azimuth: str,
        erpSectorStatusDesc: str,
        freq: str,
        bandList: str,
        pLMNIdList: str,
        essScPairId: str,
        NRCellDUuserLabel: str,
        erpSectorTech: str,
    ) -> None:
        self.nRCellDUId = nRCellDUId
        self.nodeId = nodeId
        self.locCode = locCode
        self.gNbDuFunctionId = gNbDuFunctionId
        self.administrativeState = administrativeState
        self.availabilityStatus = availabilityStatus
        self.cellBarred = cellBarred
        self.cellLocalId = cellLocalId
        self.cellReservedForOperator = cellReservedForOperator
        self.cellState = cellState
        self.nCGI = nCGI
        self.nCI = nCI
        self.nRPCI = nRPCI
        self.nRSectorCarrier = nRSectorCarrier
        self.nRTAC = nRTAC
        self.operationalState = operationalState
        self.qQualMin = qQualMin
        self.qRxLevMin = qRxLevMin
        self.rachRootSequence = rachRootSequence
        self.ssbDuration = ssbDuration
        self.ssbFrequency = ssbFrequency
        self.ssbFrequencyAutoSelected = ssbFrequencyAutoSelected
        self.ssbOffset = ssbOffset
        self.ssbPeriodicity = ssbPeriodicity
        self.ssbSubCarrierSpacing = ssbSubCarrierSpacing
        self.subCarrierSpacing = subCarrierSpacing
        self.tddLteCoexistence = tddLteCoexistence
        self.tddSpecialSlotPattern = tddSpecialSlotPattern
        self.tddUlDlPattern = tddUlDlPattern
        self.arfcnDL = arfcnDL
        self.arfcnUL = arfcnUL
        self.bSChannelBwDL = bSChannelBwDL
        self.bSChannelBwUL = bSChannelBwUL
        self.azimuth = azimuth
        self.erpSectorStatusDesc = erpSectorStatusDesc
        self.freq = freq
        self.bandList = bandList
        self.pLMNIdList = pLMNIdList
        self.essScPairId = essScPairId
        self.NRCellDUuserLabel = NRCellDUuserLabel
        self.erpSectorTech = erpSectorTech

    def __str__(self) -> str:
        scr = f"nRCellDUId: {self.nRCellDUId}" + "\n"
        scr += f"nodeId: {self.nodeId}" + "\n"
        scr += f"locCode: {self.locCode}" + "\n"
        scr += f"gNbDuFunctionId: {self.gNbDuFunctionId}" + "\n"
        scr += f"administrativeState: {self.administrativeState}" + "\n"
        scr += f"availabilityStatus: {self.availabilityStatus}" + "\n"
        scr += f"cellBarred: {self.cellBarred}" + "\n"
        scr += f"cellLocalId: {self.cellLocalId}" + "\n"
        scr += f"cellReservedForOperator: {self.cellReservedForOperator}" + "\n"
        scr += f"cellState: {self.cellState}" + "\n"
        scr += f"nCGI: {self.nCGI}" + "\n"
        scr += f"nCI: {self.nCI}" + "\n"
        scr += f"nRPCI: {self.nRPCI}" + "\n"
        scr += f"nRSectorCarrier: {self.nRSectorCarrier}" + "\n"
        scr += f"nRTAC: {self.nRTAC}" + "\n"
        scr += f"operationalState: {self.operationalState}" + "\n"
        scr += f"qQualMin: {self.qQualMin}" + "\n"
        scr += f"qRxLevMin: {self.qRxLevMin}" + "\n"
        scr += f"rachRootSequence: {self.rachRootSequence}" + "\n"
        scr += f"ssbDuration: {self.ssbDuration}" + "\n"
        scr += f"ssbFrequency: {self.ssbFrequency}" + "\n"
        scr += f"ssbFrequencyAutoSelected: {self.ssbFrequencyAutoSelected}" + "\n"
        scr += f"ssbOffset: {self.ssbOffset}" + "\n"
        scr += f"ssbPeriodicity: {self.ssbPeriodicity}" + "\n"
        scr += f"ssbSubCarrierSpacing: {self.ssbSubCarrierSpacing}" + "\n"
        scr += f"subCarrierSpacing: {self.subCarrierSpacing}" + "\n"
        scr += f"tddLteCoexistence: {self.tddLteCoexistence}" + "\n"
        scr += f"tddSpecialSlotPattern: {self.tddSpecialSlotPattern}" + "\n"
        scr += f"tddUlDlPattern: {self.tddUlDlPattern}" + "\n"
        scr += f"arfcnDL: {self.arfcnDL}" + "\n"
        scr += f"arfcnUL: {self.arfcnUL}" + "\n"
        scr += f"bSChannelBwDL: {self.bSChannelBwDL}" + "\n"
        scr += f"bSChannelBwUL: {self.bSChannelBwUL}" + "\n"
        scr += f"azimuth: {self.azimuth}" + "\n"
        scr += f"erpSectorStatusDesc: {self.erpSectorStatusDesc}" + "\n"
        scr += f"freq: {self.freq}" + "\n"
        scr += f"bandList: {self.bandList}" + "\n"
        scr += f"pLMNIdList: {self.pLMNIdList}" + "\n"
        scr += f"essScPairId: {self.essScPairId}" + "\n"
        scr += f"NRCellDUuserLabel: {self.NRCellDUuserLabel}" + "\n"
        scr += f"erpSectorTech: {self.erpSectorTech}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.nRCellDUId,
            self.nodeId,
            self.locCode,
            self.gNbDuFunctionId,
            self.administrativeState,
            self.availabilityStatus,
            self.cellBarred,
            self.cellLocalId,
            self.cellReservedForOperator,
            self.cellState,
            self.nCGI,
            self.nCI,
            self.nRPCI,
            self.nRSectorCarrier,
            self.nRTAC,
            self.operationalState,
            self.qQualMin,
            self.qRxLevMin,
            self.rachRootSequence,
            self.ssbDuration,
            self.ssbFrequency,
            self.ssbFrequencyAutoSelected,
            self.ssbOffset,
            self.ssbPeriodicity,
            self.ssbSubCarrierSpacing,
            self.subCarrierSpacing,
            self.tddLteCoexistence,
            self.tddSpecialSlotPattern,
            self.tddUlDlPattern,
            self.arfcnDL,
            self.arfcnUL,
            self.bSChannelBwDL,
            self.bSChannelBwUL,
            self.azimuth,
            self.erpSectorStatusDesc,
            self.freq,
            self.bandList,
            self.pLMNIdList,
            self.essScPairId,
            self.NRCellDUuserLabel,
            self.erpSectorTech,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "nRCellDUId",
            "nodeId",
            "locCode",
            "gNbDuFunctionId",
            "administrativeState",
            "availabilityStatus",
            "cellBarred",
            "cellLocalId",
            "cellReservedForOperator",
            "cellState",
            "nCGI",
            "nCI",
            "nRPCI",
            "nRSectorCarrier",
            "nRTAC",
            "operationalState",
            "qQualMin",
            "qRxLevMin",
            "rachRootSequence",
            "ssbDuration",
            "ssbFrequency",
            "ssbFrequencyAutoSelected",
            "ssbOffset",
            "ssbPeriodicity",
            "ssbSubCarrierSpacing",
            "subCarrierSpacing",
            "tddLteCoexistence",
            "tddSpecialSlotPattern",
            "tddUlDlPattern",
            "arfcnDL",
            "arfcnUL",
            "bSChannelBwDL",
            "bSChannelBwUL",
            "azimuth",
            "erpSectorStatusDesc",
            "freq",
            "bandList",
            "pLMNIdList",
            "essScPairId",
            "NRCellDUuserLabel",
            "erpSectorTech",
        ]
