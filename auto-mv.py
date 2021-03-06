import os
from watchdog.events import PatternMatchingEventHandler
import time
from watchdog.observers import Observer

def moverArquivo(path,pastaDestino):

	
	arquivo=path[33:len(path)]
	# 33 é a posição na string onde começa o nome do arquivo
	
	print(arquivo)
	arquivoNovo=pastaDestino+'/'+arquivo
	os.rename(path,arquivoNovo)



def formato_arquivo(arquivo):
	arquivo_rev=arquivo[::-1]
	inicio_extensao=arquivo_rev.index('.')
	extensao_rev=arquivo_rev[:inicio_extensao+1]
	extensao=extensao_rev[::-1]
	return extensao


def escolhe_pasta(formato): #Formatos de arquivos que uso com mais frequencia.
	if formato=='.txt':
		pasta="Path - arquivos texto"
	elif formato in ['.doc','.docx','.pdf','.ppt','.pps']:
		pasta ="Path - documentos"
	elif formato in ['.png','.jpeg','.gif']:
		pasta="Path - Imagens"
	elif formato in ['.xls','.xlsx','.csv']:
		pasta="Path - Panilhas-Databases"
	elif formato == '.zip':
		pasta="Path - Arquivos-Zip"
	else:
		pasta ="Path - Outros"

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



pasta="Path - pasta a ser monitorada"
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


