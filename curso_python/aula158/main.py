"""
Exercicio com Abstracao, Heranca, Encapsulamento e Polimorfismo
Criar um sistema bancario (extremamente simples) que tem clientes, contas e
um banco. A ideia eh que o cliente tenha uma conta (poupanca ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa 
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Heranca)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregacao da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agencia, numero da conta e saldo
    Contas devem ter metodo para deposito
    Conta (super classe) deve ter o metodo sacar abstrato (Abstracao e
    polimorfismo - as subclasses que implementam o metodo sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregacao)
Banco sera responsavel autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregacao)
    * Checar se a agencia eh daquele banco
    * Checar se o cliente eh daquele banco
    * Checar se a conta eh daquele banco
So sera possivel sacar se passar na autenticacao do banco (descrita acima)
Banco autentica por um metodo.
"""
import contas
