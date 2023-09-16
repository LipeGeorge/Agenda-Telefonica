#--encoding:utf-8--#

#Imports usados nessa parte do código.
import db 
import telainserir
import telaeditar
import telaremover
import telasair
import telainicial
import os

#Valores globais usados nessa parte do código.
pagina = 1
tamanho = 5

def mostrar(): #Função para chamar todas as outras.
	os.system('cls||clear')#Nesta linha, encontra-se a execução de um sistema para a translação de tela. 
	cabecalho()
	notificacoes()
	informacao_contatos(pagina)
	paginas()
	opcoes()
	interpretar_escolha()


def cabecalho(): #Função para apresentação.
	print('=============================| AGENDA DE CONTATOS |=============================')

def notificacoes(): #Função par notificação.
	print(' =============================|    Bem Vindo!    |=============================')

def informacao_contatos(pagina): #Função para listar os contatos da Agenda.

	limite = (pagina * tamanho)
	first = (pagina * tamanho) - tamanho

	contatos = db.listar()
			
	if (limite > len(contatos)): #Verificação de contatos na agenda, caso não tenha, executará a função erro().
		limite = len(contatos)

	if (len(contatos) > 0):
		print('  ==================| Você tem', len(contatos), 'contato(s) em sua agenda. |=================')
		print('ID\t Nome\t\t\t','Número de Telefone\tTipo de Contato')
		for i in range(first, limite):

			contato = contatos[i]
			
			print(contato['id'],'\t', contato['nome'], contato['sobrenome'],'\t', contato['numero_telefone'],'\t','\t', contato['tipo_contato'])
		print('')
	else:
		erro()

def erro(): #Função executada caso não haja nenhum contato na agenda.
	print('  ==================| Você tem 0 contatos em sua agenda. |=================')
	print('   =================| Faça amigos para obter algum contato. |=============')

def paginas(): #Função para indicar em que página o usuário está e quantas páginas há na agenda.
	
	global pagina
	contatos = db.listar()

	total = len(contatos) / 5
	total = round(total + 0.5)

	if pagina > total:
		pagina = pagina - 1
		mostrar()
	else:
		print('-----------------------------------------------------------| Página', pagina, 'de', total, '|--')
		print('                    [A] Página Anterior    [P] Próxima Página                   ')
		print('--------------------------------------------------------------------------------')

def opcoes(): #Função para apresentar quais comandos o contato pode utilizar.
	print('[I]: Inserir Contato    [E]: Editar Contato')
	print('[D]: Deletar Contato    [S]: Sair')

def interpretar_escolha(): #Função para interpretar e excutar de acordo com a escolha do usuário.

	global pagina

	contatos = db.listar()

	e = str(input('O que desejas fazer? '))
	e = e.upper()

	if (e == 'A'):

		pagina = pagina - 1

		if (pagina <= 0):
			pagina = 1
			mostrar()
		else:
			mostrar()

	elif (e == 'P'):
		contatos = db.listar()
		total = len(contatos) / 5
		total = round(total + 0.5)

		if (pagina >= total):
			pagina = pagina - 1
			print('Você já está na última página.')
			interpretar_escolha()
		else:
			
			if (len(contatos) <= 5):
				print('########Você não contém contatos o suficiente para ter mais de uma aba.########')
				telainicial.mostrar()
			else:
				pagina = pagina + 1
				mostrar()

	elif (e == 'I'):
		telainserir.mostrar()
	elif (e == 'E'):
		telaeditar.mostrar()
	elif (e == 'D'):
		telaremover.mostrar()
	elif (e == 'S'):
		telasair.mostrar()
	else:
		print('Por favor, digite apenas a letra de sua respectiva função:')
		opcoes()
		interpretar_escolha()