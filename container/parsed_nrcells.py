from typing import List

from prettytable import prettytable

from parsed.nrcells import ParsedNrCells
from utils.to_get import ToGet as Toget


class NrcellsDataContainer:
    def __init__(self) -> None:
        self.container: list[ParsedNrCells] = list()

    def add(self, obj: ParsedNrCells) -> None:
        if isinstance(obj, ParsedNrCells):
            if not self.data_in_container(obj=obj):
                self.container.append(obj)
            else:
                raise TypeError("Not Parsed Nrcells type")

    def data_in_container(self, obj: ParsedNrCells):
        duplicates = [
            item
            for item in self.container
            if Toget.is_compare(item.locCode, obj.locCode)
        ]

        return len(duplicates) > 0
