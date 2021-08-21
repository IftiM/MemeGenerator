Project Meme Generator
Udacity Intermediate Python
Student Name: Iftikhar Mustafa
July 11th, 2021

This project is an automated meme generator. We have some pictures in a folder, from where the script is able to pick any one image randomly. Then collects some sentences from some given files, which could be in docx, txt, pdf or csv format. Once it collects the sentences it breaks them into two-part - body of the quote, and author. The script then chooses only one of these quotes randomly and place on top the image on a random location.

User may also use command line interface. The script offers three optional CLI arguments.
--body (a string quote body)
--author (a string quote author)
--path (an image path)

The script can also create a web interface using Flask. User may click to randomize the images and texts on top of it. User also have the option to generate a meme using an image link, and own body of the quote, and name of the author.

All the required project dependencies have been listed in the requirements.txt. User may create a new virtual environment and copy all the required packages from requirements.txt. User also needs to install 'pdftotext' using the following link: https://pypi.org/project/pdftotext .
