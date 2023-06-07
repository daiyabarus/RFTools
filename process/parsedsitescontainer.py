from typing import List

from prettytable import PrettyTable

from models.parsedsites import ParsedSites
from utils.to_get import ToGet


class ParsedSitesContainer:
    def __init__(self) -> None:
        self.container: List[ParsedSites] = []

    def add(self, obj: ParsedSites) -> None:
        if isinstance(obj, ParsedSites):
            if not self.data_in_container(obj=obj):
                self.container.append(obj)
            else:
                raise TypeError("Data already exists in the container")

    def data_in_container(self, obj: ParsedSites) -> bool:
        duplicates = [
            item
            for item in self.container
            if ToGet.is_compare(item.locCode, obj.locCode)
        ]
        return len(duplicates) > 0

    def get_length(self) -> int:
        return len(self.container)

    def print_container(self) -> None:
        for obj in self.container:
            print(obj)

    def print_table(self) -> None:
        x = PrettyTable()
        x.field_names = ParsedSites.get_header_loccode()

        for obj in self.container:
            x.add_row(obj.get_list_loccode())
        print(x)
        print(f"total elements: {len(self.container)}")
        print("\n\n")

    def get_contents(self) -> List[List[str]]:
        l_data = []
        for obj in self.container:
            l_data.append(obj.get_list_loccode())
        return l_data

    def get_loccode_from_nrcells(self, loccode: str) -> ParsedSites:
        for item in self.container:
            if item.locCode == loccode:
                return item
        return None
