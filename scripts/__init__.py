"""
    GREGORIO HONORATO
    Telegram: @grehgono
    Whatsapp: (19) 99250-9913
    Email: greghono@gmail.com
    SCRIPT DE EXTRACAO DO https://g1.globo.com/rss/g1/tecnologia/
"""
from requests import get
from re import sub, findall
from bs4 import BeautifulSoup

from scripts.Log import *
from scripts.Padroes import *
from scripts.Conexao import Conexao

URL = 'https://g1.globo.com/rss/g1/tecnologia'
__version__ = '1.0'