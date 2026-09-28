import time

words = {
    "CRINGE": "algo vergonhoso ou constrangedor",
    "STALKEAR": "investigar a vida de alguém online",
    "VDD": "abreviação da palavra 'verdade'",
    "BISCOITAR": "postar algo apenas para chamar a atenção",
    "HATER": "pessoa que está constantemente criticando os outros",
    "VLW": "abreviação da palavra 'valeu'"
}
confused = True
while confused:
    print(' ')
    print('-~'*5)
    word = input("Digite uma palavra que você não saiba o sígnificado (tudo maiúsculo)")
    if word in words.keys():
        time.sleep(0.2)
        print(' ')
        print('-~'*5)
        print('Aqui está o sígnificado da palavra:')
        time.sleep(1)
        print(word + ' - ' + words[word])
        time.sleep(3)
        still_cofused = input("Você ainda quer saber o significado de alguma palavra? (s/n)")
        if still_cofused != "s":
            confused = False
    else:
        time.sleep(0.2)
        print(' ')
        print('-~'*5)
        print('desculpe, não temos esta palavra no dicionário')
        time.sleep(1)
        still_cofused = input("Você ainda quer saber o significado de alguma palavra? (s/n)")
        if still_cofused != "s":
            confused = False
