from pypdf import DocumentInformation
from typing import Optional
from typing import Protocol
from pypdf import PdfReader


OptionalStr = Optional[str]


class IFileMetadata(Protocol):
      @property
      def title(self) -> OptionalStr:
          ...

      @property
      def author(self) -> OptionalStr:
          ...

      @property
      def number_of_pages(self) -> int:
          ...

      @property
      def metadata(self) -> Optional[DocumentInformation]: 
          ...


class PdfFileMetadata:
    def __init__(self, pdf_reader: PdfReader) -> None:
        self.pdf_reader = pdf_reader

    @property
    def title(self) -> OptionalStr:
        if self.pdf_reader.metadata is None:
            return None
        
        return self.pdf_reader.metadata.title
    
    @property
    def author(self) -> OptionalStr:
        if self.pdf_reader.metadata is None:
            return None
        
        return self.pdf_reader.metadata.author

    @property
    def number_of_pages(self) -> int:
        return len(self.pdf_reader.pages)
    
    @property
    def metadata(self) -> Optional[DocumentInformation]:
        return self.pdf_reader.metadata
