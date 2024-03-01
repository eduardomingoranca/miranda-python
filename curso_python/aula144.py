# Polimorfismo em Python Orientado a Objetos
# Polimorfismo eh o principio que permite que
# classes deridavas de uma mesma superclasse
# tenham metodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do metodo = Mesmo nome e quantidade
# de parametros (retorno nao faz parte da assinatura)
# Opiniao + principios que contam:
# Assinatura do metodo: nome, parametros e retorno iguais
# SO"L"ID
# Principio da substituicao de liskov
# Objetos de uma superclasse devem ser substituiveis
# por objetos de uma subclasse sem quebrar a aplicacao.
# Sobrecarga de metodos (overload)  🐍 = ❌
# Sobreposicao de metodos (override) 🐍 = ✅
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao Nao enviada')


notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)