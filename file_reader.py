from pypdf import PdfReader, PageObject
from typing import Protocol
from pypdf import PdfReader


class IReader(Protocol):
    def extract_text(self, page_number: int) -> str:
        ...

    @property
    def pages(self) -> list[PageObject]:
        ...


class PdfFileReader:
    def __init__(self, pdf_reader: PdfReader) -> None:
        self.__pdf_reader = pdf_reader

    def extract_text(self, page_number: int = 1) -> str:
        return self.__pdf_reader.pages[page_number].extract_text()

    @property
    def pages(self) -> list[PageObject]:
        return self.__pdf_reader.pages
