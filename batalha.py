import os
import time
import random

level: int = 1
lvlpoints: int = 0


def batalha(jogador: str, inimigo: str, lvl, inimilvl, pocoes: int):

    def print_slow(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    hp = 100 + (lvl/2)
    hpinicial = 100 + (lvl/2)
    inimigohp = 100 + (inimilvl/2)
    inimigohpini = 100 + (inimilvl/2)

    ataque1 = 10 + (lvl/4)
    ataque2 = 35 + (lvl/4)
    proteger = 0
    burn = 0
    moststatus = ""
    danocritico = 30
    poweratk = 0
    invespes = 0

    while hp > 0 and inimigohp > 0:

        os.system('cls')
        ataque1 += random.randint(1, 5)
        ataque2 += random.randint(1, 5)
        critico = random.randint(1, 10)
        inimicrit = random.randint(1, 10)
        status = random.randint(1, 7)
        atkinimigo = 0
        dano = 0
        danoinimi = 0

        print("\n", "="*68, "\n")
        print(f" {inimigo} LVL {inimilvl}  HP: [{
              "["*int(inimigohp/4)}", end='')
        print(f"{"-"*int((inimigohpini/4)-(inimigohp/4))}][{int(inimigohp)}]")
        print(f"\n {jogador}  LVL {lvl} {moststatus} HP: [{
              "["*int(hp/4)}{"-"*int((hpinicial/4)-(hp/4))}][{int(hp)}]")
        print("\n", "="*68)
        print(f"""
[1] Ataque Rápido
[2] Ataque Pesado
[3] Fortalecer
[4] Proteger

[5] Poções ({pocoes})
[6] Correr\n""")

        opcao = int(input("> Digite a opcao: "))
        print("\n", "="*48, "\n")

        dano = 0
        danoinimi = 0

        if invespes == 1:
            print_slow(f"{jogador} precisa recuperar o folego...\n")
            invespes -= 1
            print_slow("...")
            time.sleep(1)

        else:
            match opcao:
                case 1:
                    if critico == 1:
                        dano = ataque1 + danocritico
                        print_slow(f"{jogador} usou Ataque Rápido")
                        print_slow("Foi um dano crítico!\n")
                        print_slow("...")
                        time.sleep(1)
                    else:
                        print_slow(f"{jogador} usou Ataque Rápido\n")
                        dano = ataque1
                        print_slow("...")
                        time.sleep(1)

                case 2:
                    if critico == 1:
                        print_slow(f"{jogador} usou Ataque Pesado")
                        print_slow("Foi um ataque poderoso!")
                        print_slow("Foi um dano crítico!\n")
                        dano = ataque2 + danocritico
                        invespes += 1
                        print_slow("...")
                        time.sleep(1)
                    else:
                        print_slow(f"{jogador} usou Ataque Pesado")
                        print_slow("Foi um ataque poderoso!\n")
                        dano = ataque2
                        invespes += 1
                        print_slow("...")
                        time.sleep(1)

                case 3:
                    print_slow(f"{jogador} usou Fortalecer")
                    print_slow(f"O ataque de {jogador} aumentou!\n")
                    ataque1 += 10
                    ataque2 += 10
                    print_slow("...")
                    time.sleep(1)

                case 4:
                    print_slow(f"{jogador} usou Proteger\n")
                    print_slow("...")
                    time.sleep(1)
                    if proteger > 0:
                        print_slow("Mas falha!\n")
                        print_slow("...")
                        time.sleep(1)
                    else:
                        proteger += 1

                case 5:
                    if pocoes > 0:
                        if hp >= hpinicial:
                            print_slow("Sua vida já está cheia!\n")
                            print_slow("...")
                            time.sleep(1)
                        else:
                            print_slow(f"{jogador} usou uma Poção\n")
                            hp += 25
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

        if poweratk == 1:
            if proteger == 1:
                print_slow(f"\n{inimigo} usou Guilhotina")
                print_slow(f"Mas {jogador} defendeu!")
                poweratk -= 1
                time.sleep(2)
            else:
                print_slow(
                    f"\n{inimigo} usou Guilhotina, foi um ataque poderoso!")
                danoinimi = 65
                poweratk -= 1
                time.sleep(2)
        else:
            atkinimigo = random.randint(1, 4)

            match atkinimigo:
                case 1:
                    if proteger == 1:
                        print_slow(f"\n{inimigo} usou Investida")
                        print_slow(f"Mas {jogador} defendeu!")
                        time.sleep(2)
                    else:
                        if inimicrit == 1:
                            print_slow(f"\n{inimigo} usou Investida")
                            print_slow("Foi um dano crítico!")
                            danoinimi = 15 + (inimilvl/4) + danocritico
                            time.sleep(2)
                        else:
                            print_slow(f"\n{inimigo} usou Investida")
                            danoinimi = 15 + (inimilvl/4)
                            time.sleep(2)
                case 2:
                    if proteger == 1:
                        print_slow(f"\n{inimigo} usou Labaredas")
                        print_slow("Mas {jogador} defendeu!")
                        time.sleep(2)

                    else:
                        if inimicrit == 1:
                            print_slow(f"\n{inimigo} usou Labaredas")
                            print_slow("Foi um dano crítico!")
                            danoinimi = 20 + (inimilvl/4) + danocritico
                            time.sleep(2)
                            if status == 1:
                                print_slow(f"\n{jogador} foi queimado!")
                                burn = 1
                                time.sleep(2)
                        else:
                            print_slow(f"\n{inimigo} usou Labaredas")
                            danoinimi = 20 + (inimilvl/4)
                            time.sleep(2)
                            if status == 1:
                                print_slow(f"\n{jogador} foi queimado!")
                                burn = 1
                                time.sleep(2)
                case 3:
                    if ataque1 <= 10 or ataque2 <= 10:
                        print_slow(f"\n{inimigo} usou Enfraquecer")
                        print_slow(f"O ataque de {
                            jogador} não pode diminuir mais!")
                        time.sleep(2)

                    else:
                        print_slow(f"\n{inimigo} usou Enfraquecer")
                        print_slow(f"O ataque de {jogador} diminuiu!")
                        ataque1 -= 5
                        ataque2 -= 5
                        time.sleep(2)

                case 4:
                    print_slow(f"\n{inimigo} prepara um ataque poderoso...")
                    poweratk += 1
                    time.sleep(2)

        if burn == 1:
            print_slow(f"\n{jogador} sofreu dano de queimadura!")
            hp -= 10
            time.sleep(2)

        if burn == 1:
            moststatus = "[BRN]"
        else:
            moststatus = ""

        critico = 0
        inimicrit = 0
        proteger = 0
        inimigohp -= dano
        hp -= danoinimi
        os.system('cls')

    if hp <= 0 or inimigohp <= 0:
        if inimigohp <= 0:
            print_slow(f"{inimigo} foi Derrotado!")
            print_slow(f"Você ganhou! {int(inimigohpini/4)} pontos de EXP!")
            global level

            if level < 100:
                global lvlpoints
                lvlpoints += int(inimigohpini/4)
                if lvlpoints >= (hpinicial*2):
                    print_slow(f"O seu nível aumentou! LVL {level}")
                    level += 1
                    lvlpoints = 0
            else:
                print("Level máximo!")

        elif hp <= 0:
            print_slow(f"{jogador} foi Derrotado!")
            print_slow("Você perdeu!")
