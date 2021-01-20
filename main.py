"""
    GREGORIO HONORATO
    Telegram: @grehgono
    Whatsapp: (19) 99250-9913
    Email: greghono@gmail.com
    SCRIPT DE EXTRACAO DO https://g1.globo.com/rss/g1/tecnologia/
"""

from scripts import *

class G1XML:
    def __init__(self):
        Conexao()
        self.print(f'INICIANDO A EXTRACAO DO {URL}')
        
        try: self.xml = BeautifulSoup(get(URL, timeout=30).text, 'lxml')
        except Exception as e: self.print(f'ERRO ENCONTRADO NA REQUISICAO DO {URL}:{e}'); return
        
        self.extrairDados()
    
    @log
    def extrairDados(self):
        ' FAZ TODO O PAPEL DE EXTRACAO E NAVEGACAO NO XML '
        limite_texto = slice(160)
        
        x = lambda y: self.xml.find(y).text                          # FAZ O find DA TAG DESEJADA SEM PRECISAR REPETIR CODIGO
        l = lambda x: sub('<.*|]*>', '', x).strip()                  # FAZ LIMPEZA DE TAGS QUE APARECEM NA DESCRICAO

        tags = {'titulo': x('title'), 'link': findall('<link\/>\n?.*', self.xml.find('item').prettify())[0].split(' ')[1], 'descricao': l(x('description')), \
                'categoria': x('category'), 'media': self.xml.find('media:content')['url']}
        self.persistiDados([f"'{x}'" for x in tags.keys()], [f"'{x}'" for x in tags.values()])
        
        for cont, tag in enumerate(self.xml.findAll('item')):
            
            x = lambda y: tag.find(y).text                           # SIM!!! ESTA REPETINDO CODIGO, NESSA ETAPA ISSO ACONECE PORQUE A PAGINA TEM O ITEM[0] DIFERENTE DOS OUTROS                         
            
            ' A TAG LINK ESTA FORA DO PADRAO HTML, PARA ISSO FOI UTILIZADO UMA EXPRESSAO REGULAR PARA REALIZAR A EXTRACAO '
            
            tags = {'titulo': x('title'), 'link': findall('<link\/>\n?.*', tag.prettify())[0].split(' ')[1], 'descricao': l(x('description')), 'categoria': x('category'), 'media': tag.find('media:content')['url']}
            print(tags['titulo'], tags['link'], tags['categoria'], cont)
            self.persistiDados([f"'{x}'" for x in tags.keys()], [f"'{x}'" for x in tags.values()])
            
    @Conexao.conexao_banco
    def persistiDados(self, cols, iten): 
        cmd = f"INSERT INTO G1({', '.join(cols)}) VALUES({','.join(iten)});"
        self.print(f"COMANDO EXECUTADO: {cmd}")
        return cmd
            
    def __del__(self): self.print('FINALIZANDO O SCRIPT DE EXTRACAO DO G1')
        
    def print(self, msg, tipo=True): Log(msg, tipo)

G1XML()