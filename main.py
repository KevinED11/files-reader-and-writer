from pathlib import Path
from pdf_reader import PdfFileReader, IReader
from pypdf import PdfReader
from pdf_writer import TxtFileWriter, IWriter
from pdf_metadata import PdfFileMetadata, IFileMetadata


class PdfFileReaderAndWriter:
    def __init__(self, pdf_reader: IReader, file_writer: IWriter, 
                 file_metadata: IFileMetadata) -> None:
        self.pdf_reader = pdf_reader
        self.file_writer = file_writer
        self.metadata = file_metadata


def main() -> None:
    # Paths
    pdf_path = Path("./aprendiendo-git.pdf")
    txt_file = Path("./libro.txt")
    
    # Reader, writer and metadata files
    reader = PdfReader(pdf_path)

    pdf_reader = PdfFileReader(pdf_reader=reader)
    pdf_metadata = PdfFileMetadata(pdf_reader=reader)

    txt_file_writer = TxtFileWriter(txt_file=txt_file, reader=pdf_reader, 
                                    file_metadata=pdf_metadata)
    print(pdf_reader.extract_text(page_number=1))
    txt_file_writer.write()


    program = PdfFileReaderAndWriter(pdf_reader=pdf_reader, file_writer=txt_file_writer, 
                                     file_metadata=pdf_metadata)
    



if __name__ == "__main__":
    main()
