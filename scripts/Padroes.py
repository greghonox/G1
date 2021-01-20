"""
    GREGORIO HONORATO
    Telegram: @grehgono
    Whatsapp: (19) 99250-9913
    Email: greghono@gmail.com
    SCRIPT DE EXTRACAO DO https://g1.globo.com/rss/g1/tecnologia/
    
	DESENVOLVIDO PARA CRIAR DADOS PADROES COMO DATA E HORA, MOEDA, MEDIDAS ENTRE OUTROS.
"""

from datetime import datetime

class DateTime():
    def __init__(self):
        ' CRIADO PARA TRAZER UM PADRAO DE DATA NO SISTEMA '
        self.format = '%d/%m/%Y %H:%M:%S'

    def __repr__(self): return datetime.now().strftime(self.format)

    def __str__(self): return datetime.now().strftime(self.format)

    def __add__(self, v):
        return self.__repr__() +' '+ v