# Importação das bibliotecas necessárias
from datetime import date, datetime, timedelta
from os import getcwd, path, listdir, chdir
import datetime
import os
import pathlib

## Bibliotecca PyMuPDF
#[Documentação]('https://pymupdf.readthedocs.io/en/latest/installation.html')

### Instalação
!pip install --upgrade pymupdf

### Importando a biblioteca
import fitz as fz

### Lendo o arquivo
with fz.open(file_test) as file:
        contexts = ''
        for page in file:
                contexts += page.get_text()
