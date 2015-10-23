__author__ = "Ellis"
__version__ = "Python 3.5"

import urllib.request

#Step one:  Make program read the quote contained in the filename.

def read_text():
    path = '/Users/Ellis/GitHub/movies_quotes.txt'
    quote = open(path)
    content = quote.read()
    print(content)
    quote.close()

#Step two: Make program check for profanity words in quote

    check_profanity(content)
def check_profanity(text_scan):
    text = urllib.parse.quote(text_scan)
    connection = urllib.request.urlopen('http://www.wdyl.com/profanity?q='+text)
    output = connection.read()
    print(output)

    if 'true' in str(output):
        print("Profanity Alert!!!")

    elif 'false' in str(output):
        print("Document is good to GO!")

    else:
        print("Could not read document")
    connection.close()

read_text()
