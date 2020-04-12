#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Funcionario():
    def __init__(self):
        self.nome1 = "Karla"
        self.nome2 = "Julia"
        self.nome3 = "José"
        self.nome4 = "Andre"
        print("Nomes de funcionarios da empresa COSMO A.i")
    
    def imprime(self):
        print("Nomes 1 a 4" % (self.nome1, nome2, nome3, nome4))
        
Funcionario1 = Funcionario()
Funcionario1.nome1


# In[ ]:


Funcionario1.nome2


# In[ ]:


Funcionario1.nome3


# In[ ]:


Funcionario1.nome4


# In[ ]:


class Frutas():
    def __init__(self):
        self.nome1 = "Uva"
        self.nome2 = "Pera"
        self.nome3 = "Mamão"
        self.nome4 = "Kwi"
        print("Futas do mercado")

Frutas1 = Frutas()
Frutas1.nome1


# In[ ]:


Frutas1.nome2


# In[ ]:


Frutas1.nome3


# In[ ]:


Frutas1.nome4


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




