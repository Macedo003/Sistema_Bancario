from abc import ABC, abstractmethod
import contas

class Pessoa:
    def __init__(self,nome:str, sobrenome:str) -> None:
        self.nome: str = nome
        self.sobrenome = sobrenome
    

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome:str):
        self._nome = nome


    @property
    def sobrenome(self):
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self,sobrenome:str):
        self._sobrenome = sobrenome

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.sobrenome!r}'
        return f'({class_name},{attrs})'

class Cliente(Pessoa):
    def __init__(self, nome: str, sobrenome: str) -> None:
        super().__init__(nome, sobrenome)
        self.conta: contas.Conta | None = None


if __name__ =='__main__':
    c1 = Cliente('Gabriel','Macedo')
    c1_conta = contas.ContaCorrente(1,2546,1000,0)
    print(c1)
    print(c1_conta)