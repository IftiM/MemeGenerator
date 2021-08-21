""" Quotemodel taking body and author - two portion of the texts
derived from the documents, and returning an output.
"""

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return (f'{self.body} - {self.author}')
