# Exercício 2: Crie uma classe ContaBancaria com atributos titular, saldo e numero, implemente métodos para depositar
# e sacar dinheiro, e faça verificações de coerência, como impedir o saque se o saldo estiver negativo.

class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def __str__(self):
        return "A conta é de {} (nº {}) e tem R${} de saldo.".format(self.titular, self.numero, self.saldo)

    def sacar_valor(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor;
        else:
            print("Não é possível realizar a operação de saque.")

    def depositar_valor(self, valor):
        self.saldo += valor

conta1 = ContaBancaria("Matheus", 1000, 25)
print(conta1)
conta1.sacar_valor(100)
print(conta1)
conta1.sacar_valor(1000)
print(conta1)
conta1.depositar_valor(200)
print(conta1)
conta1.sacar_valor(1000)
print(conta1)
