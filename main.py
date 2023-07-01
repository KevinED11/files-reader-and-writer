from pathlib import Path
from file_reader import PdfFileReader, IReader
from pypdf import PdfReader
from file_writer import TxtFileWriter, IWriter
from file_metadata import PdfFileMetadata, IFileMetadata
from _types import OptionalStr


class FileReaderAndWriter:
    def __init__(
        self, file_reader: IReader, file_writer: IWriter, file_metadata: IFileMetadata
    ) -> None:
        self.__file_reader = file_reader
        self.__file_writer = file_writer
        self.__file_metadata = file_metadata

    def extract_text(self, page_number: int = 1) -> str:
        return self.__file_reader.extract_text(page_number=page_number)

    def write(self) -> None:
        self.__file_writer.write()

    @property
    def title(self) -> OptionalStr:
        return self.__file_metadata.title

    @property
    def author(self) -> OptionalStr:
        return self.__file_metadata.author

    @property
    def number_of_pages(self) -> int:
        return self.__file_metadata.number_of_pages


def main() -> None:
    pdf_path = Path("./aprendiendo-git.pdf")
    txt_file = Path("./libro.txt")

    reader = PdfReader(pdf_path)

    pdf_reader = PdfFileReader(pdf_reader=reader)
    pdf_metadata = PdfFileMetadata(pdf_reader=reader)
    file_writer = TxtFileWriter(
        txt_file=txt_file, reader=pdf_reader, file_metadata=pdf_metadata
    )

    program = FileReaderAndWriter(
        file_reader=pdf_reader, file_writer=file_writer, file_metadata=pdf_metadata
    )

    program.write()
    text = program.extract_text(page_number=1)
    print(text)


if __name__ == "__main__":
    main()
