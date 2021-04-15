import os
from watchdog.events import PatternMatchingEventHandler
import time
from watchdog.observers import Observer

def moverArquivo(path,pastaDestino):
	"""caminho='/home/dagnei/Documentos/projetos/auto-mv/pasta-teste1'
	mover=caminho+'/'+arquivo
	"""
	
	arquivo=path[33:len(path)]
	print(arquivo)
	arquivoNovo=pastaDestino+'/'+arquivo
	os.rename(path,arquivoNovo)



def formato_arquivo(arquivo):
	arquivo_rev=arquivo[::-1]
	inicio_extensao=arquivo_rev.index('.')
	extensao_rev=arquivo_rev[:inicio_extensao+1]
	extensao=extensao_rev[::-1]
	return extensao


def escolhe_pasta(formato):
	if formato=='.txt':
		pasta="/home/dagnei/Documentos/Arquivos-Baixados/Arquivos-Texto"
	elif formato in ['.doc','.docx','.pdf','.ppt','.pps']:
		pasta ="/home/dagnei/Documentos/Arquivos-Baixados/Documentos"
	elif formato in ['.png','.jpeg','.gif']:
		pasta="/home/dagnei/Documentos/Arquivos-Baixados/Imagens"
	elif formato in ['.xls','.xlsx','.csv']:
		pasta="/home/dagnei/Documentos/Arquivos-Baixados/Panilhas-Databases"
	elif formato == '.zip':
		pasta="/home/dagnei/Documentos/Arquivos-Baixados/Arquivos-Zip"
	else:
		pasta ="/home/dagnei/Documentos/Arquivos-Baixados/Outros"

	return pasta



if __name__=='__main__':
	patterns='*'
	ingnore_patterns=''
	ignore_directories=False
	case_sensitive=True
	MyEventHandler=PatternMatchingEventHandler(patterns,ingnore_patterns,ignore_directories,case_sensitive)

def on_created(event):
	formato=formato_arquivo(event.src_path)
	pastadestino=escolhe_pasta(formato)
	print('created',event.src_path)
	moverArquivo(event.src_path,pastadestino)


#moverArquivo('teste.txt','/home/dagnei/Documentos/projetos/auto-mv/pasta-teste2')
pasta="/home/dagnei/Documentos/organizar"
eventos= MyEventHandler
eventos.on_created=on_created
observer=Observer()
observer.schedule(eventos,pasta,recursive=True)

observer.start()
try:
	while True:

		time.sleep(15)

except KeyboardInterrupt:
	observer.stop()


