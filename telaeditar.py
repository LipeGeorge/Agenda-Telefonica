#--encoding:utf-8--#

#Imports usados nessa parte do código.
import db
import telainicial
import os
import string

#Abaixo são as funções criadas para este campo de edição dos nossos "contatos" da "agenda".

def mostrar():#Função geral, que irá chamar todas as outras.
	os.system('cls||clear')#Nesta linha, encontra-se a execução de um sistema para a translação de tela.
	cabecalho()
	notificacao()
	print('=============================| Edição de Contatos |=============================')
	escolha()

def cabecalho(): #Função para apresentar um detalhe como cabeçalho.
	print('=============================| AGENDA DE CONTATOS |=============================')

def notificacao(): #Função para notificações.
	print('---| Notificação: Caso você não saiba o ID do contato, verifique no início. |---')

def escolha(): #Função para ler a escolha do usuário.
	print('------------------------------------------[V]: Voltar ao início-----------------')

	temcontato = db.listar()

	if len(temcontato) > 0:

		i = input('Informe o número da ID do contato: ')

		if i.lower() == 'v':
			telainicial.mostrar()

		elif (not i.isnumeric()):
			print('Por favor, digite apenas a ID do contato ou a opção de retorno.')
			escolha()

		else:
			i = int(i)
			if existcontato(i) == False:
				print('Você não tem um contato com essa ID. Tente novamente.')
				escolha()
			else:
				contato = db.buscar_por_id(i)
				print('------| Dados antigos do contato:')
				print('|Nome:', contato['nome'], '\n|Sobrenome:', contato['sobrenome'], '\n|Número de telefone:', contato['numero_telefone'], '\n|Tipo de contato:', contato['tipo_contato'])
				print('')
				atualizar(i)
	else:
		print('\n')
		print('****************Não há contatos para edição na sua agenda.**********************')
		print('\n')
		telainicial.mostrar()

def atualizar(id): #Função para executar a edição à escolha do contato.

	contato = {}

	contato['id'] = id
	contato['nome'] = str(input('Digite o novo primeiro nome: '))
	contato['sobrenome'] = str(input('Digite o novo sobrenome: '))
	contato['numero_telefone'] = str(input('Digite o novo número de contato: '))

	print('=========> Tipo de Contato <=========')
	print('[1]: Cônjugue   [2]: Namorado')
	print('[3]: Amigo(a)   [4]: Família')
	print('[5]: Trabalho   [6]: Conhecido')

	t = str(input('Selecione o novo tipo do contato: '))
	t = t.lower()
	tc = typecontact(t)

	if tc != 'erro':
		contato['tipo_contato'] = tc
		db.atualizar_contato(contato)
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
			db.atualizar_contato(contato)
			telainicial.mostrar()
		else:
			print('Número de tentativas excedido. Recomece.')
			escolha()

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
