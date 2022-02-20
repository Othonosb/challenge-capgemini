import re

password = input('escolha uma senha: ')
senhavalida = 0

while True:
    if (len(password) < 6):
        senhavalida = -1
        print(f'sua senha é fraca pois tem apenas {len(password)} caracteres')
        break
    elif not re.search("[A-Z]", password):
        senhavalida = -1
        break
    elif not re.search("[a-z]", password):
        senhavalida = -1
        break
    elif not re.search("[0-9]", password):
        senhavalida = -1
        break
    elif not re.search("[!@#$%^&*()-+_]", password):
        senhavalida = -1
        break
    else:
        senhavalida == 0
        print("senha forte!")
        break

if senhavalida == - 1:
    print("você precisa do padrão abaixo de senha")
    print("a senha precisa ter no mínimo 6 caracteres")
    print("a senha precisa ter no mínimo 1 digito")
    print("a senha precisa ter no mínimo 1 letra em maiúsculo")
    print("a senha precisa ter no mínimo 1 letra em minúsculo")
    print("a senha precisa ter no mínimo 1 caractere especial")
    print("os caracteres especiais são esses: !@#$%^&*()-+")
