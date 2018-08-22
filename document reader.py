from docx import Document
from docx.shared import Pt
import subprocess

filename = raw_input("Pls input the file location: \n")

document = Document(filename)

paragraphs = document.paragraphs

for x in paragraphs:
	print(x.text)
	subprocess.call(["espeak.exe", x.text])