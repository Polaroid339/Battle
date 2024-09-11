import os
import time
import random

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def batalha():
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

    while hp > 0 and inimigohp > 0:
        tackle += random.randint(1, 7)
        watergun += random.randint(1, 8)
        critico = random.randint(1, 13)
        inimicrit = random.randint(1, 13)
        status = random.randint(1, 7)
        atkinimigo = 0
        dano = 0
        danoinimi = 0

        print("=" * 58)
        print("")
        print(f"Charmander LVL 10  HP: [{"[" * int(inimigohp / 4)}{"-" * int(25 - (inimigohp / 4))}] {inimigohp}%")
        print(f"Squirtle   LVL 10  HP:  {moststatus}  [{"[" * int(hp / 4)}{"-" * int(25 - (hp / 4))}] {hp}%")
        print(f"""
[1] Tackle
[2] Water Gun
[3] Growl
[4] Protect

[5] Poções ({pocoes})
[6] Correr\n""")


        opcao = int(input("> Digite a opcao: "))

        dano = 0
        danoinimi = 0

        match opcao:
            case 1:
                if critico == 1:
                    print_slow("Squirtle usou Tackle")
                    print_slow("Foi um dano crítico!\n")
                    dano = tackle + danocritico
                    print_slow("...")
                    time.sleep(1)
                else:
                    print_slow("Squirtle usou Tackle\n")
                    dano = tackle
                    print_slow("...")
                    time.sleep(1)

            case 2:
                if critico == 1:
                    print_slow("Squirtle usou Water Gun")
                    print_slow("Foi um dano crítico!")
                    print_slow("Foi Muito Efetivo!\n")
                    dano = watergun + danocritico
                    print_slow("...")
                    time.sleep(1)
                else:
                    print_slow("Squirtle usou Water Gun")
                    print_slow("Foi Muito Efetivo!\n")
                    dano = watergun
                    print_slow("...")
                    time.sleep(1)
            case 3:
                print_slow("Squirtle usou Growl")
                print_slow("O ataque de Squirtle aumentou!\n")
                tackle += 10
                watergun += 10
                print_slow("...")
                time.sleep(1)

            case 4:
                print_slow("Squirtle usou Protect\n")
                print_slow("...")
                time.sleep(1)
                if protect > 0:
                    print_slow("Mas falha!\n")
                    print_slow("...")
                    time.sleep(1)
                else:
                    protect += 1

            case 5:
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
            case 6:
                print_slow("Você escapou da batalha!")
                break
            case _:
                print_slow("Comando invalido\n")
                print_slow("...")
                time.sleep(1)
                dano = 0

        atkinimigo = random.randint(1, 3)

        match atkinimigo:
            case 1:
                if protect == 1:
                    print_slow("\nCharmander usou Scratch")
                    print_slow("Mas Squirtle defendeu!")
                    time.sleep(2)
                else:
                    if inimicrit == 1:
                        print_slow("\nCharmander usou Scratch")
                        print_slow("Foi um dano crítico!")
                        danoinimi = (random.randint(20, 23) + danocritico)
                        time.sleep(2)
                    else:
                        print_slow("\nCharmander usou Scratch")
                        danoinimi = random.randint(20, 23)
                        time.sleep(2)
            case 2:
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
                            danoinimi = (random.randint(13, 20) + danocritico)
                            time.sleep(2)
                    else:
                        print_slow("\nCharmander usou Ember")
                        print_slow("Mas foi pouco efetivo!")
                        if status == 1:
                            print_slow("\nSquirtle foi queimado!")
                            burn = 1
                            danoinimi = random.randint(13, 20)
                            time.sleep(2)
            case 3:
                if tackle <= 5 or watergun <= 5:
                    print_slow("\nCharmander usou Leer")
                    print_slow("O ataque de Squirtle não pode diminuir mais!")
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
            moststatus = ""

        critico = 0
        inimicrit = 0
        protect = 0
        inimigohp -= dano
        hp -= danoinimi
        os.system('cls')
    print(hp)

batalha()
