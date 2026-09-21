import random
import time

simbols = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
password = ""
not_enough = True

while not_enough:
    print("-~- Digite o tamanho da senha -~-")
    length = int(input("Tamanho: "))
    if length < 6:
        print("A senha deve ter no mínimo 6 caracteres.")
    else:
        for i in range(length):
            password += random.choice(simbols)
        time.sleep(0.5)
        print("Senha gerada:", password)
        time.sleep(2)
        liked = input("Você gostou da senha? (s/n): ")
        if liked == "s":
            not_enough = False
        else:
            password = ""
            time.sleep(1)
            print(' ')
            print("Gerando uma nova senha...")
            print(' ')
            time.sleep(2)

print(' ')
print('-~-'*25)
print('Senha final:', password)
