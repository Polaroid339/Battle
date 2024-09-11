# Feito por Victor Oliveira v1.6

import random
import os
import time


def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


print_slow("\nINICIANDO BATALHA POKÉMON!")


# Variaveis
hp = 100
inimigohp = 100

tackle = 10
watergun = 15
growl = 0
protect = 0
pocoes = 2
burn = 0
moststatus = ""
danocritico = 10

if burn == 1:
    watergun -= 5
    tackle -= 5
else:
    pass


# Loop Principal
while hp > 0 and inimigohp > 0:

    tackle += random.randint(1, 7)
    watergun += random.randint(1, 8)
    critico = random.randint(1, 13)
    inimicrit = random.randint(1, 13)
    status = random.randint(1, 7)
    atkinimigo = 0

    print("")
    print("="*58)
    print("")
    print(f"Charmander LVL 10  HP: [{
          "["*int(inimigohp/4)}{"-"*int(25-(inimigohp/4))}] {inimigohp}%")
    print("""                                      ⢀⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠈⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⣜⠃⠀⠀⠀⢘⢳⢆⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⢀⠔⠉⠀⠀⠀⠀⣜⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⢸⠀⡀⠀⠀⠀⠀⠈⠉⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀
                                ⠀⡤⢄⣳⣦⠤⠤⠤⠄⣄⡲⡪⠀⡇⠀⢀⡀⢤⠀⠀⠀⢠⠒⢋⠤⠀
                                ⠘⢝⠁⠈⠙⠷⠒⠒⠾⠓⢎⠀⠀⠁⠉⠁⠈⢛⠆⠀⠀⠈⢷⣿⠀⣆
                                ⠀⠀⠑⢄⠀⡘⠀⠀⠀⠀⠀⠣⡀⠀⠀⣀⠔⠁⠀⠀⠀⢀⠃⠹⢷⡄
                                ⠀⠀⠀⠀⠑⡇⠀⠀⠀⠀⠀⠀⢡⠀⠈⡄⠀⠀⠀⠀⠀⠈⠣⢤⡼⠀
                                ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡆⠀⠰⠀⠀⠀⠀⠀⠀⠀⡌⡇⠀
                                ⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⢀⠌⢠⠃⠀
                                ⠀⠀⠀⠀⡐⠉⠣⡀⠀⠀⠀⠀⢀⠃⠂⠐⡎⠁⠒⠂⠈⠀⣠⠏⠀⠀
                                ⠀⠀⠀⠀⡀⠀⠀⠈⠒⡤⠀⠠⠊⠀⠀⠀⡠⣀⣀⠠⢄⠾⠃⠀⠀⠀
                                ⠀⠀⣀⡤⠚⠲⠀⠀⠸⡁⠀⢘⠄⠀⠀⣠⠋⠁⠀⠉⠁⠀⠀⠀⠀⠀
                                ⠀⠈⠛⡊⠂⠀⠀⠒⠂⠁⠀⠘⢖⣔⣶⡲⠃
           ⠀⠀⠀⠀⠀⠀⣀⠤⠐⠒⠒⠂⠠⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⡠⢠⠂⠀⠀⠀⠡⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⢰⣷⣾⠀⠀⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠜⢨⠢⠔⡀⠀⠠⠘⠛⠛⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⢀⣀⣀⠀⠀⠀⠰⠀⠀⠀⠀⠡⡀⠀⠈⠀⠒⠂⠄⡀⢀⠀⡀⠀
⠀⡴⠊⠀⠀⠀⠉⢆⠀⡔⢣⠀⠀⠀⠀⠐⡤⣀⠀⠀⠀⠀⠀⣀⠄⠀⠀
⢸⠀⠀⠀⢠⠀⠀⠈⣼⠀⠀⠣⠀⠀⠀⡰⡀⠀⠉⠀⠀⠰⠉⠀⠁⠠⢄
⢰⠀⠀⠀⠀⠇⠀⢀⢿⠀⢀⠇⡐⠀⠈⠀⠈⠐⠠⠤⠤⠤⠀⠀⠀⠀⢨
⠀⢓⠤⠤⠊⠀⠀⢸⠀⠣⠀⡰⠁⠀⠀⡀⠀⠀⠀⠸⠀⢰⠁⠐⠂⠈⠁
⠀⠀⠑⢀⠀⠀⠀⠈⣄⠖⠉⠑⢄⠠⠊⠀⠢⢄⣠⣃⣀⡆⠀⠀⠀⠀⠀""")
    print("="*58)
    print(f"\nSquirtle LVL 8  {moststatus}  HP: [{
          "["*int(hp/4)}{"-"*int(25-(hp/4))}] {hp}%")
    print(f"""
[1] Tackle
[2] Water Gun
[3] Growl
[4] Protect

[5] Poções ({pocoes})
[6] Correr\n""")

    atk = int(input("> Selecione a opção: "))
    print("")
    print("="*48)
    print("")

    # Ataques do jogador
    if atk == 1:
        if critico == 1:
            print_slow("Squirtle usou Tackle")
            print_slow("Foi um dano crítico!\n")
            inimigohp -= (tackle + danocritico)
            print_slow("...")
            time.sleep(1)
        else:
            print_slow("Squirtle usou Tackle\n")
            inimigohp -= tackle
            print_slow("...")
            time.sleep(1)

    elif atk == 2:
        if critico == 1:
            print_slow("Squirtle usou Water Gun")
            print_slow("Foi um dano crítico!")
            print_slow("Foi Muito Efetivo!\n")
            inimigohp -= (watergun + danocritico)
            print_slow("...")
            time.sleep(1)
        else:
            print_slow("Squirtle usou Water Gun")
            print_slow("Foi Muito Efetivo!\n")
            inimigohp -= watergun
            print_slow("...")
            time.sleep(1)

    elif atk == 3:
        print_slow("Squirtle usou Growl")
        print_slow("O ataque de Squirtle aumentou!\n")
        tackle += 10
        watergun += 10
        print_slow("...")
        time.sleep(1)

    elif atk == 4:
        print_slow("Squirtle usou Protect\n")
        print_slow("...")
        time.sleep(1)
        if protect > 0:
            print_slow("Mas falha!\n")
            print_slow("...")
            time.sleep(1)
        else:
            protect += 1

    elif atk == 5:
        if pocoes > 0:
            if hp >= 100:
                print_slow("Sua vida já está cheia!\n")
                print_slow("...")
                time.sleep(1)
            else:
                print_slow("Squirtle usou uma Poção\n")
                hp += 20
                pocoes -= 1
                burn = 0
                moststatus = ""
                print_slow("...")
                time.sleep(1)
        else:
            print_slow("Você não tem poções para usar!\n")
            print_slow("...")
            time.sleep(1)

    elif atk == 6:
        print_slow("Você escapou da batalha!")
        break

    else:
        print_slow("Comando invalido\n")
        print_slow("...")
        time.sleep(1)

    # Ataques do inimigo
    atkinimigo = random.randint(1, 3)

    if atkinimigo == 1:
        if protect == 1:
            print_slow("\nCharmander usou Scratch")
            print_slow("Mas Squirtle defendeu!")
            time.sleep(2)

        else:
            if inimicrit == 1:
                print_slow("\nCharmander usou Scratch")
                print_slow("Foi um dano crítico!")
                hp -= (random.randint(20, 23) + danocritico)
                time.sleep(2)
            else:
                print_slow("\nCharmander usou Scratch")
                hp -= random.randint(20, 23)
                time.sleep(2)

    elif atkinimigo == 2:
        if protect == 1:
            print_slow("\nCharmander usou Ember")
            print_slow("Mas Squirtle defendeu!")
            time.sleep(2)

        else:
            if inimicrit == 1:
                print_slow("\nCharmander usou Ember")
                print_slow("Foi um dano crítico!")
                print_slow("Mas foi pouco efetivo!")
                if status == 1:
                    print_slow("\nSquirtle foi queimado!")
                    burn = 1
                hp -= (random.randint(13, 20) + danocritico)
                time.sleep(2)
            else:
                print_slow("\nCharmander usou Ember")
                print_slow("Mas foi pouco efetivo!")
                if status == 1:
                    print_slow("\nSquirtle foi queimado!")
                    burn = 1
                hp -= random.randint(13, 20)
                time.sleep(2)

    elif atkinimigo == 3:
        if tackle <= 5 or watergun <= 5:
            print_slow("\nCharmander usou Leer")
            print_slow(
                "O ataque de Squirtle não pode diminuir mais!")
            time.sleep(2)

        else:
            print_slow("\nCharmander usou Leer")
            print_slow("O ataque de Squirtle diminuiu!")
            tackle -= 5
            watergun -= 5
            time.sleep(2)

    if burn == 1:
        print_slow("\nSquirtle sofreu dano de queimadura!")
        hp -= 5
        time.sleep(2)

    if burn == 1:
        moststatus = "[BRN]"
    else:
        pass

    # Resets
    critico = 0
    inimicrit = 0
    protect = 0
    os.system('cls')

    if hp <= 0 or inimigohp <= 0:
        if inimigohp <= 0:
            print_slow("Charmander foi Derrotado!")
            print_slow("Você ganhou!")

        elif hp <= 0:
            print_slow("Squirtle foi Derrotado!")
            print_slow("Você perdeu!")

print_slow("\nFim de jogo!")
print_slow("Made by Victor Oliveira\n")
