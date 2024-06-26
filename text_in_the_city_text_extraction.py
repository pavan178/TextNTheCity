# -*- coding: utf-8 -*-
"""text-in-the-city-text-extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KFerSq6ZNgsaFvTWLxBSgC9Ej4giMsv

# Text and the City - Text Extraction

This notebook demonstrates how to extract the "Inhalt" (content) from PDF files.

Note: This notebook does not cover how to fine-tune a BERT-like model for multi-label classification; for that, please refer to the other provided notebook.

The notebook was executed on a free instance of Google Colab with 12.7 GB RAM, but it can be easily adapted to a regular Jupyter Notebook that can be run anywhere.

## Install dependencies
"""

! pip install pypdf2

"""## Load Data

To access Google Drive documents, grant Google Colab access to your drive.

In this code, we assume that you have a zipped file named `Text and the City - 30.01.2024.zip` containing all the PDFs.

Feel free to change the file name as needed.
"""

from google.colab import drive
import os

drive.mount('/content/drive')

DRIVE_DIR = "/content/drive/MyDrive/"

EXEL_FILE_NAME = "Text and the City - 30.01.2024.zip"

assert EXEL_FILE_NAME in os.listdir(DRIVE_DIR)

"""Extract all PDF files in Google Colab."""

import zipfile

zip_file_path = DRIVE_DIR + EXEL_FILE_NAME

extracted_dir = '/content'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

"""## Extract Data

Extract the text from all PDF files and try to identify a "Begründung" section, starting with "Begründung" and ending with three empty spaces. If this section is not found, the file is skipped.

> NOTE:
>
> This implementation is basic, and there is room for improvement. Consider exploring additional keywords or alternative methods for extracting the relevant section.
"""

from PyPDF2 import PdfReader
import os
import pandas as pd

pdfs_directory = EXEL_FILE_NAME[:-4] + "/"

files_without_reason_section = [] # Begründung
data = []
for file_name in os.listdir(pdfs_directory):
  text = ""
  reader = PdfReader(pdfs_directory + file_name)
  for page in reader.pages:
      text += page.extract_text()
  try:
    content = "Begründung" + text.split("Begründung")[1].split("   ")[0]
    data.append([file_name, content])
  except IndexError:
    files_without_reason_section.append(file_name)
    content = None


df = pd.DataFrame(data, columns=["Name des pdf Dokuments", "Inhalt"])

print("Files without Begründung section: ", files_without_reason_section)

df