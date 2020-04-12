#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class funcionario:
    def __init__(self):
        self.nome = None
        self.salario = 0
    
    def exibir_dados(self):
        print("Nome do funcionario:", self.nome)
        print("Salario do funcionario:", self.salario)
        
    def exibir(self):
        print("\n")
        n = input("Nome do funcionario:")
        s = int(input("Digite o salario:"))
        self.funcionario = n
        self.salario = s
        
        if s > 1500:
            print("Salario ok")
        else:
            print("Salario não ok")
        
dados_funcionario = funcionario()
dados_funcionario.exibir()

funcionario1 = funcionario()
funcionario1.exibir()


# In[ ]:


class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome
        self.lista_disciplinas = []

    def adicionar_disciplina(self, disc):
        self.lista_disciplinas.append(disc)

    def exibir(self):
        print("RA: ", self.ra)
        print("Nome: ", self.nome)
        print("Disciplinas: ", self.lista_disciplinas)


aluno1 = Aluno(9999999, "Paulo")
aluno1.adicionar_disciplina("Linguagem de Programação II")
aluno1.adicionar_disciplina("Banco de Dados")
aluno1.exibir()


# In[ ]:


class Livro:
    # construtor recebe valores iniciais que serão atribuidos aos atributos
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Preço: ", self.preco)


# cria objeto
outro_livro = Livro("Titulo do Livro", "Nome do autor do livro", 50.0)
outro_livro.exibir_dados()

# cria outro objeto
livro1 = Livro("Titulo", "nome do autor", 30)
# modifica o preço
livro1.preco = 29.90
livro1.exibir_dados()

