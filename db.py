#--encoding:utf-8--#

#Aqui são os recursos usados do sqlite

#Imports usados nessa parte do código.
import sqlite3 
import os

conexao = sqlite3.connect("agenda_telefonica.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

def criar_tabela(): #Função para a criação da tabela que será utilizada.

	query = """
	CREATE TABLE IF NOT EXISTS agenda_telefonica(
	id INTEGER NOT NULL UNIQUE,
	nome VARCHAR(80) NOT NULL,
	sobrenome VARCHAR(90) NOT NULL,
	numero_telefone VARCHAR(90) NOT NULL,
	tipo_contato VARCHAR(90) NOT NULL)
	"""

	cursor.execute(query)

def inserir_contato(contato): #Função para a inserção de dados para a tabela criada.

	query = """
	INSERT INTO agenda_telefonica(
	id, nome, sobrenome, numero_telefone, tipo_contato) 
	VALUES (?,?,?,?,?)
	"""
	valores = [contato['id'], contato['nome'], contato['sobrenome'], contato['numero_telefone'], contato['tipo_contato']]

	cursor.execute(query, valores)
	conexao.commit()


def atualizar_contato(contato): #Função para a edição de algum dado presente na tabela.

	query = """
	UPDATE agenda_telefonica SET nome = ?, sobrenome = ?, numero_telefone = ?, tipo_contato = ? WHERE id = ? 
	"""
	pessoa = [contato['nome'], contato['sobrenome'], contato['numero_telefone'], contato['tipo_contato'], contato['id']]
	cursor.execute(query, pessoa)
	conexao.commit()

def apagar(id): #Função para apagar dados da tabela.

	query = """
	DELETE FROM agenda_telefonica WHERE id = ?
	"""
	pessoa = [id]
	cursor.execute(query, pessoa)
	conexao.commit()

def buscar_por_id(id): #Função para listar um dado específico da tabela. Nesse caso está buscando por uma "ID" indicada na hora da inserção.

		query = """
		SELECT * FROM agenda_telefonica WHERE id = ?
		"""
		pessoa = [id]
		cursor.execute(query, pessoa)
		individuo = cursor.fetchone()
		return individuo

def listar(): #Função para listar todos os dados da tabela.

		query = """
		SELECT * FROM agenda_telefonica
		"""
		cursor.execute(query)
		contatos = cursor.fetchall()
		return contatos


criar_tabela() #Essa chamada de função é necessária para criar a tabela. Mas, como queremos criar ela apenas uma vez, para que não se repita outras vezes, indicamos um IF NOT EXIST dentro do código dela.
