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