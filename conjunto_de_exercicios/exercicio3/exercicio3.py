# Exercício 3: Crie uma classe Funcionario com atributos salario e cargo. Implemente um método aumentar_salario (percentual)
# Essa classe deve herdar de uma outra classe Pessoa, com os atributos nome, e-mail, telefone. E-mail e telefone são atributos opcionais.
# Instancie 3 pessoas e 3 funcionários aleatórios. Alguns com e outros sem e-mail ou telefone.

class Pessoa:
    def __init__(self, nome, email = None, telefone = None):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self): # Caso não tenha sigo passado um email ou telefone como parâmetro na instanciação, será mostrado "não informado"
        return "Nome: {}, email: {}, telefone: {}.".format(self.nome,
                                                           self.email if self.email is not None else "não informado",
                                                           self.telefone if self.telefone is not None else "não informado")

class Funcionario(Pessoa):
    def __init__(self, nome, salario, cargo, email = None, telefone = None):
        super().__init__(nome, email, telefone) # super() se refere à classe Pessoa
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return "Nome: {}, email: {}, telefone: {}. Esta pessoa também é funcionário, salário: R${}, cargo: {}.".format(self.nome,
                                                                                                                       self.email if self.email is not None else "não informado",
                                                                                                                       self.telefone if self.telefone is not None else "não informado",
                                                                                                                       self.salario,
                                                                                                                       self.cargo)

    def aumentar_salario(self, percentual):
        salario_antigo = self.salario
        self.salario += self.salario * percentual * 0.01
        print("O salário de {} foi aumentado em {}% (de R${} para R${}).".format(self.nome, percentual, salario_antigo, self.salario))

pessoa1 = Pessoa("Matheus")
pessoa2 = Pessoa("Ana", "ana@gmail.com")
pessoa3 = Pessoa("Beatriz", "beatriz@gmail.com", 99999999)
funcionario1 = Funcionario("João", 1000, "Chefe", "joao@gmail.com")
funcionario2 = Funcionario("Bruno", 2000, "Gerente")
funcionario3 = Funcionario("Tiago", 100, "Colaborador")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print(funcionario1)
funcionario2.aumentar_salario(10)
print(funcionario2)
funcionario3.aumentar_salario(100)
print(funcionario3)
