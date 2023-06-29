from pdf_metadata import IFileMetadata
from pdf_reader import IReader
from pathlib import Path
from typing import Protocol
from _types import ListStr



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

    def write(self) -> None:
        with open(self.__txt_file, "w+") as file:
            file.write("\n\n".join(self.__content_to_write()))
