from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from .pdf_loader import load_pdf
from .section_splitter import split_by_section
from utils.logger import logger


class DocumentLoader:

    def __init__(
        self,
        folder_path="knowledge_base"
    ):
        self.folder_path = folder_path

    def load_documents(self):

        all_chunks = []

        splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
        )

        pdf_files = Path(
            self.folder_path
        ).glob("*.pdf")

        for pdf_file in pdf_files:

            logger.info(
                f"Processing {pdf_file.name}"
            )

            full_text = load_pdf(str(pdf_file)
)
            logger.info(type(full_text))

            sections = split_by_section(
                full_text
            )

            for section_name, text in sections.items():

                chunks = splitter.split_text(
                    text
                )
                logger.info(
                    f"Created {chunks} chunks for section: {section_name}"
                )

                for chunk in chunks:

                    all_chunks.append(
                        Document(
                            page_content=chunk,
                            metadata={
                                "source":
                                    pdf_file.name,
                                "section":
                                    section_name
                            }
                        )
                    )

        logger.info(
            f"Created {len(all_chunks)} chunks"
        )
        logger.info(
            f"chunks: {all_chunks}"
        )
        return all_chunks