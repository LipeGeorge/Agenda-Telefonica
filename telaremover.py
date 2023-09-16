#--encoding:utf-8--#

#Imports usados nessa parte do código.
import db
import telainicial
import os

def mostrar(): #Função para chamar todas as outras funções.
	os.system('cls||clear') #Nesta linha, encontra-se a execução de um sistema para a translação de tela.
	cabecalho()
	notificacao()
	print('=============================| Remoção de Contato |=============================')
	escolha()

def cabecalho(): #Função para recepção do usuário.
	print('=============================| AGENDA DE CONTATOS |=============================')

def notificacao(): #Função para a apresentação de notificação da tela.
	print('---| Notificação: Caso você não saiba o ID do contato, verifique no início. |---')

def escolha(): #Função para a interpretação da ação que o usuário deseja fazer.
	print('------------------------------------------[V]: Voltar ao início-----------------')

	temcontato = db.listar()

	if (len(temcontato) > 0):
		
		i = input('Informe o ID do contato: ')
		
		if i.lower() == 'v':
			telainicial.mostrar()

		elif (not i.isnumeric()):
			print('Por favor, digite apenas a ID do contato ou a opção de retorno.')
			escolha()

		else:
			i = int(i)
			if existcontato(i) == False:
				print('Você não tem nenhum contato com esta ID. Tente Novamente.')
				escolha()
			else:
				contato = db.buscar_por_id(i)
				print('------| Dados do contato a ser removido:')
				print('|Nome:', contato['nome'], '\n|Sobrenome:', contato['sobrenome'], '\n|Número de telefone:', contato['numero_telefone'], '\n|Tipo de contato:', contato['tipo_contato'])
				print('')
				print('Você tem certeza que deseja remover este contato?')
				print('[S]: Sim      [N]: Não')
				resposta = str(input('Selecione a opção para avançar: '))
				resposta = resposta.lower()
				if (resposta == 's'):
					db.apagar(i)
					print('Contato deletado com sucesso.')
					telainicial.mostrar()
				elif (resposta == 'n'):
					telainicial.mostrar()
				else:
					print('Por favor, digite apenas a letra de sua respectiva função. Tente uma segunda vez.')
					print('Você tem certeza que deseja remover este contato?')
					print('[S]: Sim      [N]: Não')
					resposta = str(input('Selecione a opção para avançar: '))
					resposta = resposta.lower()
					if (resposta == 's'):
						db.apagar(i)
						print('Contato deletado com sucesso.')
						telainicial.mostrar()
					elif (resposta == 'n'):
						telainicial.mostrar()
					else:
						print('Por favor, digite apenas a letra de sua respectiva função. Tente uma terceira e última vez.')
						print('Você tem certeza que deseja remover este contato?')
						print('[S]: Sim      [N]: Não')
						resposta = str(input('Selecione a opção para avançar: '))
						resposta = resposta.lower()
						if (resposta == 's'):
							db.apagar(i)
							print('Contato deletado com sucesso.')
							telainicial.mostrar()
						elif (resposta == 'n'):
							telainicial.mostrar()
						else:
							print('Você excedeu o número de tentativas. Tente desde o início.')
							escolha()
	else:
		print('\n')
		print('****************Não há contatos para remoção na sua agenda.**********************')
		print('Voltando ao início em: 3 .. 2 .. 1')
		telainicial.mostrar()

def existcontato(i):
	contato = db.buscar_por_id(i)

	if contato == None:
		return False
	else:
		return True