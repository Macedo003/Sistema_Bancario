from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
   
   
    @abstractmethod
    def sacar(self,valor):
        ...
    
    
    def depositar (self,valor):
        self.saldo += valor
        self.detalhes(f'Deposito: {valor:.2f}')
    


    def detalhes(self, msg =''):
        print(f'O seu saldo é {self.saldo:.2f} {msg} ')


    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r},{self.saldo!r}'
        return f'({class_name},{attrs})'
    

class ContaPoupanca(Conta):
    def sacar (self,valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque: {valor:.2f}')
            return self.saldo
        
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'Valor Saque negado: {valor:.2f}')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r},{self.saldo!r}, {self.limite!r}'
        return f'({class_name},{attrs})'
        

if __name__ =='__main__':
    cp1 = ContaPoupanca(111,222,100)
    cp1.sacar(1)
    cc1= ContaCorrente(123,456,0,3000)
    cc1.sacar(10)
    cc1.sacar(1000)