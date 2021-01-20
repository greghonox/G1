"""
    GREGORIO HONORATO
    Telegram: @grehgono
    Whatsapp: (19) 99250-9913
    Email: greghono@gmail.com
    SCRIPT DE EXTRACAO DO https://g1.globo.com/rss/g1/tecnologia/
    
    DESENVOLVIDO PARA REALIZAR A CONEXAO COM BANCO DE DADOS.
    SE FOR USAR OUTRO SGBD É SÓ MUDAR OS IMPORTS(NA MAIORIA DOS CASOS)
"""

from os import getcwd
from os.path import isfile
from sqlite3 import connect
from platform import platform

brr = '\\' if('windows' in platform().lower()) else '/' # ISSO PREPARA O SCRIPT PARA TANTO NO WINDOWS COMO NO LINUX

BANCO_DADOS = getcwd() + brr + 'g1.db'

class Conexao:
    global dialogo
    dialogo = f"SISTEMA DE SCRAPT G1"
    
    def __init__(self):
        if(not isfile(BANCO_DADOS)):
            print(f'CRIANDO BANCO DE DADOS {BANCO_DADOS}')
            bd = connect(BANCO_DADOS)
            bd.execute("CREATE TABLE G1 (codigo INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, link TEXT, descricao TEXT, categoria TEXT, media TEXT);")
            bd.commit()       

    def conexao_banco(func, db=BANCO_DADOS):
        def method(cls, titulo, valores):
            try:
                cmd = func(cls, titulo, valores)
                banco = connect(db)
                banco.execute(cmd)
                banco.commit()
                return f"\n{dialogo} COMANDO EXECUTADO C/ SUCESSO: {cmd}\n"
            except Exception as erro: return f"\n\n*******ERRO C/ BANCO DE DADOS: (|{erro}|) COMANDO EXECUTADO:{cmd} *********\n\n"
            finally: banco.close()
        return method