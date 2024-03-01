# Usando subprocess para executar e comandos externos
# subprocess eh um modulo do Python para executar
# processos e comandos externos no seu programa.
# O metodo mais simples para atingir o objetivo eh usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saida, entrada e erros
# - capture_output -> captura a saida e erro para uso posterior
# - text -> Se True, entradas e saidas serao tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrao da plataforma (geralmente UTF-8).
# - shell -> Se True, tera acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executavel que iniciara o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificacao de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4
import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32

cmd = ['ls -lah /']
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding,
    shell=True,
)

print()

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)