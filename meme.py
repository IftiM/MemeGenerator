"""Creating a meme project.

We are creating a meme project where it will generate random
image and random quotes from given directories. User will also
be able to use command line interface for picture path, body,
meme message, and author.
"""

import os
import random
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesCSV.csv',
                       './_data/DogQuotes/DogQuotesPDF.pdf']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine.MemeEngine('./MemeGenerator/images')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Path, body and author")
    parser.add_argument('--path', type=str,
                        default='./MemeGenerator/images/test.jpg')
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
