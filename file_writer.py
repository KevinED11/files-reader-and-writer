from file_metadata import IFileMetadata
from file_reader import IReader
from pathlib import Path
from typing import Protocol
from _types import ListStr
from functools import cache, cached_property


class IWriter(Protocol):
    def write(self) -> None:
        ...


class TxtFileWriter:
    def __init__(
        self, txt_file: Path, file_metadata: IFileMetadata, reader: IReader
    ) -> None:
        self.__txt_file = txt_file
        self.__reader = reader
        self.__file_metadata = file_metadata

    def __content_to_write(self) -> ListStr:
        return [
            f"{self.__file_metadata.title}",
            f"Number of pages: {self.__file_metadata.number_of_pages}",
            *(page.extract_text() for page in self.__reader.pages),
        ]

    def __check_existing_file(self) -> bool:
        return Path(self.__txt_file).resolve().exists()

    def __check_existing_content(self) -> bool:
        return Path(self.__txt_file).resolve().stat().st_size != 0

    def write(self) -> None:
        if not self.__check_existing_file() or not self.__check_existing_content():
            with open(self.__txt_file, "w+") as file:
                file.write("\n\n".join(self.__content_to_write()))
