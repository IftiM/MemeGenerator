"""A Flask app for the meme project.

This Flask app for the meme project will generate random
image and random quotes from given directories. User will be able
to clink to generate random image and quotes, also be able to
choose a picture with web link, add own quote and name.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)
meme = MemeEngine.MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesCSV.csv',
                   './_data/DogQuotes/DogQuotesPDF.pdf']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = None
    quote = None

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(image_url, allow_redirects=True)

    image_name = random.randint(0, 100000000)
    tmp = f'./tmp/{image_name}.jpg'
    img = open(tmp, 'wb')
    img.write(r.content)
    img.close()

    meme = MemeEngine.MemeEngine('./static')
    path = meme.make_meme(tmp, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
