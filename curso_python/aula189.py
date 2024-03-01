# (Parte 1) Basico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) eh um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisicao ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisicao do cliente deve incluir dados como:
# - O metodo HTTP
#     - leitura (safe) - GET, HEAD (cabecalhos), OPTIONS (metodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereco do recurso a ser acessado (/users/)
# - Os cabecalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessario, de acordo com o metodo HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabecalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)