# import os
# from typing import List

# from prettytable import PrettyTable

from models.parsednrcells import ParsedNrCells, ParsedNrCellsIndex
from models.parsedradionodes import ParsedRadiNodes, ParsedRadiNodesIndex
from models.parsedsites import ParsedSites, ParsedSitesIndex
from process.parsednodescontainer import ParsedRadioNodesContainer
from process.parsednrcellscontainer import ParsedNrcellsContainer
from process.parsedsitescontainer import ParsedSitesContainer
from utils.excel_reader import ExcelReader


class ParsedSheet:
    SHEET_NRCELLS = "nrCells"
    SHEET_RADIONODES = "radioNodes"
    SHEET_SITES = "sites"


class CollectParsedNrcells(ExcelReader):
    def __init__(self, excel_path: str, excel_profile: str) -> None:
        super().__init__(excel_path, excel_profile)

    def get_parsed_nrcells_data_container(self) -> ParsedNrcellsContainer:
        container = ParsedNrcellsContainer()
        idx = ParsedNrCellsIndex()

        wsname = ParsedSheet.SHEET_NRCELLS
        if wsname not in self.dtheader:
            raise KeyError(f"{wsname}'s sheet not found!")

        header_row = self.dtheader[wsname]
        ws = self.wb[wsname]
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            obj = ParsedNrCells(
                nodeId=row[idx.nodeId],
                locCode=row[idx.locCode],
                gNbDuFunctionId=row[idx.gNbDuFunctionId],
                administrativeState=row[idx.administrativeState],
                availabilityStatus=row[idx.availabilityStatus],
                cellBarred=row[idx.cellBarred],
                cellLocalId=row[idx.cellLocalId],
                cellReservedForOperator=row[idx.cellReservedForOperator],
                cellState=row[idx.cellState],
                nCGI=row[idx.nCGI],
                nCI=row[idx.nCI],
                nRPCI=row[idx.nRPCI],
                nRSectorCarrier=row[idx.nRSectorCarrier],
                nRTAC=row[idx.nRTAC],
                operationalState=row[idx.operationalState],
                qQualMin=row[idx.qQualMin],
                qRxLevMin=row[idx.qRxLevMin],
                rachRootSequence=row[idx.rachRootSequence],
                ssbDuration=row[idx.ssbDuration],
                ssbFrequency=row[idx.ssbFrequency],
                ssbFrequencyAutoSelected=row[idx.ssbFrequencyAutoSelected],
                ssbOffset=row[idx.ssbOffset],
                ssbPeriodicity=row[idx.ssbPeriodicity],
                ssbSubCarrierSpacing=row[idx.ssbSubCarrierSpacing],
                subCarrierSpacing=row[idx.subCarrierSpacing],
                tddLteCoexistence=row[idx.tddLteCoexistence],
                tddSpecialSlotPattern=row[idx.tddSpecialSlotPattern],
                tddUlDlPattern=row[idx.tddUlDlPattern],
                arfcnDL=row[idx.arfcnDL],
                arfcnUL=row[idx.arfcnUL],
                bSChannelBwDL=row[idx.bSChannelBwDL],
                bSChannelBwUL=row[idx.bSChannelBwUL],
                azimuth=row[idx.azimuth],
                erpSectorStatusDesc=row[idx.erpSectorStatusDesc],
                freq=row[idx.freq],
                bandList=row[idx.bandList],
                pLMNIdList=row[idx.pLMNIdList],
                essScPairId=row[idx.essScPairId],
                NRCellDUuserLabel=row[idx.NRCellDUuserLabel],
                erpSectorTech=row[idx.erpSectorTech],
            )

            container.add(obj=obj)
        return container

    def get_parsed_radio_data_container(self) -> ParsedRadioNodesContainer:
        container = ParsedRadioNodesContainer()
        idx = ParsedRadiNodesIndex()

        wsname = ParsedSheet.SHEET_RADIONODES
        if wsname not in self.dtheader:
            raise KeyError(f"{wsname}'s sheet not found!")

        header_row = self.dtheader[wsname]
        ws = self.wb[wsname]
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            obj = ParsedRadiNodes(
                nodeId=row[idx.nodeId],
                eNBId=row[idx.eNBId],
                locCode=row[idx.locCode],
                Subnetwork=row[idx.Subnetwork],
                system=row[idx.system],
                swVersionId=row[idx.swVersionId],
                swRelease=row[idx.swRelease],
                Vendor=row[idx.Vendor],
                mocn=row[idx.mocn],
                gNBId=row[idx.gNBId],
                hwType=row[idx.hwType],
                siteLocation=row[idx.siteLocation],
                bfnOffset=row[idx.bfnOffset],
            )
            container.add(obj=obj)
        return container

    def get_parsed_sites_data_container(self) -> ParsedSitesContainer:
        container = ParsedSitesContainer()
        idx = ParsedSitesIndex()

        wsname = ParsedSheet.SHEET_SITES
        if wsname not in self.dtheader:
            raise KeyError(f"{wsname}'s sheet not found!")

        header_row = self.dtheader[wsname]
        ws = self.wb[wsname]
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            obj = ParsedSites(
                locCode=row[idx.locCode],
                siteName=row[idx.siteName],
                siteIsd=row[idx.siteIsd],
                parent=row[idx.parent],
                csd=row[idx.csd],
                cma=row[idx.cma],
                er=row[idx.er],
                prv=row[idx.prv],
                latitude=row[idx.latitude],
                longitude=row[idx.longitude],
                towerType=row[idx.towerType],
                rnc=row[idx.rnc],
                bsc=row[idx.bsc],
                GSM=row[idx.GSM],
                UMTS=row[idx.UMTS],
                LTE=row[idx.LTE],
                NR=row[idx.NR],
                NBIOT=row[idx.NBIOT],
                csdUid=row[idx.csdUid],
                mocnNodes=row[idx.mocnNodes],
                azimuthCount=row[idx.azimuthCount],
                avgAntennaHeight=row[idx.avgAntennaHeight],
                lte_shifted=row[idx.lte_shifted],
            )
            container.add(obj=obj)
        return container
