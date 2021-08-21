""" Parsing the contents of a pdf file.
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import os
import random


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quotes = []
        with open(tmp, "r", encoding='utf-8-sig') as t:
            for index, line in enumerate(t):
                parsed = line.strip().split('-')
                if parsed != ['']:
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)
        return quotes
