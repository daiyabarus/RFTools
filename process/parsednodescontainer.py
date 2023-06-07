from typing import List

from prettytable import PrettyTable

from models.parsedradionodes import ParsedRadiNodes
from utils.to_get import ToGet as Toget


class ParsedRadioNodesContainer:
    def __init__(self) -> None:
        self.container: list[ParsedRadiNodes] = list()

    def add(self, obj: ParsedRadiNodes) -> None:
        if isinstance(obj, ParsedRadiNodes):
            if not self.data_in_container(obj=obj):
                self.container.append(obj)
            else:
                raise TypeError("Not ParsedNrCells data")

    def data_in_container(self, obj: ParsedRadiNodes):
        duplicates = [
            item
            for item in self.container
            if Toget.is_compare(item.locCode, obj.locCode)
            and Toget.is_compare(item.nodeId, obj.nodeId)
        ]
        return len(duplicates) > 0

    def get_length(self) -> int:
        return len(self.container)

    def print_container(self) -> None:
        for obj in self.container:
            print(obj)

    def print_table(self) -> None:
        x = PrettyTable()
        x.field_names = ParsedRadiNodes.get_header_loccode()

        for obj in self.container:
            x.add_row(obj.get_list_loccode())
        print(x)
        print(f"total elements: {len(self.container)}")
        print("\n\n")

    def get_contents(self) -> List[list[str]]:
        l_data = list()
        for obj in self.container:
            l_data.append(obj.get_list_loccode())
        return l_data

    def get_loccode_from_radionodes(self, loccode: str) -> ParsedRadiNodes:
        for item in self.container:
            if item.locCode == loccode:
                return item
        return None
