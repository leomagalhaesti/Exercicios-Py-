#!/usr/bin/python3

import sys


if len(sys.argv) == 1:
	
	
	
	
    comando = input("Digite add ou update:")
    username = input("Fornecedor nome do usuário:")
	
	
    if comando == "add":
        senha= input ("Digite abaixo a senha do usuario: /n")
        with open ("password.txt") as f:
                f.write("{}:{}/n".format(username,senha))
    elif comando == "update":
        senhaAtual = input("Digite sua senha atual: /n")
        with open("password.txt") as f:
                conteudo = f.readlines()
                for linha in conteudo:
                        nome = linha.strip(":/n").split(":")[0]
                        senha = linha.strip(":/n").split(":")[1]
                        if nome == username:
                                if senhaAtual == senha:
                                        print("Senha correta")
