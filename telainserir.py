#--encoding:utf-8--#

#Imports usados nessa parte do código.
import db
import telainicial
import os

def mostrar(): #Função para a chamada de todas as outras funções.
	os.system('cls||clear')#Nesta linha, encontra-se a execução de um sistema para a translação de tela.
	cabecalho()
	informacoes_contato()

def cabecalho(): #Função para recepção e indicação de onde o usurário está.
	print('=============================| AGENDA DE CONTATOS |=============================')
	print('----------------------------| Inserir Novo Contato |---------------------------')

def informacoes_contato(): #Função para executar a ação de inserção de dados.

	contato = {}

	i = input('informe qual será a ID do contato: ')
	
	if (not i.isnumeric()):
		print('Por favor, digite uma ID válida.')
		informacoes_contato()
	else:
		if existcontato(i) == True:
			print('Você já tem um contato com esta ID. Escolha outra ID.')
			informacoes_contato()
		else:
			contato['id'] = i
			contato['nome'] = str(input('Digite o primeiro nome: '))
			contato['sobrenome'] = str(input('Digite o sobrenome: '))
			contato['numero_telefone'] = str(input('Número de Contato: '))

			print('=========> Tipo de Contato <=========')
			print('[1]: Cônjugue   [2]: Namorado')
			print('[3]: Amigo(a)   [4]: Família')
			print('[5]: Trabalho   [6]: Conhecido')

			t = str(input('Selecione o tipo de contato: '))
			t = t.lower()
			tc = typecontact(t)

			if tc != 'erro':
				contato['tipo_contato'] = tc
				db.inserir_contato(contato)
				telainicial.mostrar()
			else:
				print('Digite apenas uma das opções sugeridas.')
				print('=========> Tipo de Contato <=========')
				print('[1]: Cônjugue   [2]: Namorado')
				print('[3]: Amigo(a)   [4]: Família')
				print('[5]: Trabalho   [6]: Conhecido')

				t = str(input('Selecione o novo tipo do contato: '))
				t = t.lower()
				tc = typecontact(t)

				if tc != 'erro':
					contato['tipo_contato'] = tc
					db.inserir_contato(contato)
					telainicial.mostrar()
				else:
					print('Número de tentativas excedido. Recomece.')
					informacoes_contato()

def typecontact(t): #Função para verificar o tipo de contato.

	if (t == '1' or t == 'conjugue' or t == 'cônjugue'):
		return 'Conjugue'
	elif (t == '2' or t == 'namorado'):
		return 'Namorado(a)'
	elif (t == '3' or t == 'amigo'):
		return 'Amigo(a)'
	elif (t == '4' or t == 'familia' or t == 'família'):
		return 'Familia'
	elif (t == '5' or t == 'trabalho'):
		return 'Trabalho'
	elif (t == '6' or t == 'conhecido'):
		return 'Conhecido'
	else:
		return 'erro'

def existcontato(i):
	contato = db.buscar_por_id(i)

	if contato == None:
		return False
	else:
		return True
