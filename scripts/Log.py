"""
    GREGORIO HONORATO
    Telegram: @grehgono
    Whatsapp: (19) 99250-9913
    Email: greghono@gmail.com
    SCRIPT DE EXTRACAO DO https://g1.globo.com/rss/g1/tecnologia/
    
	DESENVOLVIDO PARA GERAR LOG.TXT DOS EVENTOS DESEJADO
"""

from scripts.Padroes import DateTime

def log(func):
	def method(*args):
		' DECORADOR AUXILIAR '
		try:
			argumentos = func(*args)
			log = argumentos[0] if(isinstance(argumentos, tuple)) else argumentos
			dialog = DateTime() + log + " "

			try: tipo = argumentos[1]
			except: tipo = True
			
			try: log = argumentos[2]
			except: log = None

			Log(msg=dialog, tipo=tipo, guiLog=log)
			return argumentos
		except Exception as erro: return f"ERRO EM GERAR LOG {func} --- {args}"
	return method

class Log:
	def __init__(self, msg, tipo=True, arq=r'log.txt'):
		''' 
			GERA O LOG ... 
			PARAMETROS: MSG - MENSAGEM DO EVENTO
			TIPO: True Informacao ; False Erro ; None CUIDADO
		'''
		try:
			self.arq = arq			
			tipo = " -- INFORMACAO" if(tipo) else " -- CUIDADO" if(not tipo) else ' -- ERRO'
			msg = '{:<180}'.format(DateTime() + ' ' + msg[:180])
			dialog = msg + tipo
			self.log(dialog)
		except Exception as erro: 
			msg = f"ERRO OCORRIDO EM IMPRIMIR LOG({erro}) -- {msg}"
			print(msg)
   
	def log(self, msg):  
		print(msg)
		with open(self.arq, 'a') as arq: arq.write(msg+'\n')
