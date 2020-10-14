# Convert-Book-to-Audio
import pyttsx3# pip install pyttsx3
import PyPDF2# pip install PyPDf2

book = open('Book of Python.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(9, pages):
    page = pdfreader.getPage(9)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
