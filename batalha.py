import os
import time
import random

level: int = 1
lvlpoints: int = 0


def batalha(jogador: str, inimigo: str, lvl, inimilvl, pocoes: int):

    os.system('cls')

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
    cooldown = 0

    while hp > 0 and inimigohp > 0:

        os.system('cls')

        print("="*66)
        print(f"\n{inimigo} LVL {inimilvl}  HP: [{
              "["*int(inimigohp/4)}", end='')
        print(f"{"-"*int((inimigohpini/4)-(inimigohp/4))
                 }][{int((inimigohp/inimigohpini)*100)}%]\n")
        print("="*66)
        print(f"\n{jogador}  LVL {lvl} {
              moststatus} HP: [{"["*int(hp/4)}", end='')
        print(f"{"-"*int((hpinicial/4)-(hp/4))}][{int((hp/hpinicial)*100)}%]")
        print(f"""
[1] Ataque Rápido --- Dano Base [{int(ataque1)}]
[2] Ataque Pesado --- Dano Base [{int(ataque2)}]; 1 turno de cooldown
[3] Fortalecer ------ Aumenta em 10 os ataques
[4] Proteger -------- Protege por 1 turno

[5] Poções ({pocoes})
[6] Correr\n""")

        critico = random.randint(1, 10)
        inimicrit = random.randint(1, 10)
        status = random.randint(1, 7)
        esquiva = random.randint(1, 20)
        inimiesquiva = random.randint(1, 20)
        atkinimigo = 0
        dano = 0
        danoinimi = 0

        while True:
            try:
                opcao = int(input("> Digite a opção: "))
                if 1 <= opcao <= 6:
                    print("")
                    print("="*48, "\n")
                    break
                else:
                    print_slow("\nOpção inválida. Digite um número válido.\n")
            except ValueError:
                print_slow("\nComando invalido. Digite um número válido.\n")

        dano = 0
        danoinimi = 0

        if cooldown == 1:
            print_slow(f"{jogador} precisa recuperar o folego...\n")
            cooldown -= 1
            print_slow("...")
            time.sleep(1)

        else:
            match opcao:
                case 1:
                    if inimiesquiva == 1:
                        print_slow(f"{jogador} usou Ataque Rápido")
                        print_slow(f"Mas {inimigo} Esquiva!\n")
                        dano = 0
                        print_slow("...")
                        time.sleep(1)

                    else:
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
                    if inimiesquiva == 1:
                        print_slow(f"{jogador} usou Ataque Pesado")
                        print_slow(f"Mas {inimigo} Esquiva!\n")
                        dano = 0
                        print_slow("...")
                        time.sleep(1)

                    else:
                        if critico == 1:
                            print_slow(f"{jogador} usou Ataque Pesado")
                            print_slow("Foi um ataque poderoso!")
                            print_slow("Foi um dano crítico!\n")
                            dano = ataque2 + danocritico
                            cooldown += 1
                            print_slow("...")
                            time.sleep(1)

                        else:
                            print_slow(f"{jogador} usou Ataque Pesado")
                            print_slow("Foi um ataque poderoso!\n")
                            dano = ataque2
                            cooldown += 1
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

        if poweratk == 1:
            if esquiva == 1:
                print_slow(f"\n{inimigo} usou Guilhotina")
                print_slow(f"{jogador} se esquiva do ataque...\n")
                print_slow("...")
                time.sleep(2)

            elif proteger == 1:
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
                    if esquiva == 1:
                        print_slow(f"\n{inimigo} usou Investida")
                        print_slow(f"{jogador} se esquiva do ataque...\n")
                        print_slow("...")
                        time.sleep(2)

                    elif proteger == 1:
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
                    if esquiva == 1:
                        print_slow(f"\n{inimigo} usou Labaredas")
                        print_slow(f"{jogador} se esquiva do ataque...\n")
                        print_slow("...")
                        time.sleep(2)

                    elif proteger == 1:
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
                    if ataque1 <= 20 or ataque2 <= 20:
                        print_slow(f"\n{inimigo} usou Enfraquecer")
                        print_slow(f"O ataque de {
                            jogador} não pode diminuir mais!")
                        time.sleep(2)

                    else:
                        print_slow(f"\n{inimigo} usou Enfraquecer")
                        print_slow(f"O ataque de {jogador} diminuiu!")
                        ataque1 -= 10
                        ataque2 -= 10
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
                lvlpoints += int(inimilvl*100)
                if lvlpoints >= (lvl*100):
                    level += 1
                    print_slow(f"O seu nível aumentou! LVL {level}")
                    lvlpoints = lvlpoints - (lvl*100)
            else:
                print("Level máximo!")

        elif hp <= 0:
            print_slow(f"{jogador} foi Derrotado!")
            print_slow("Você perdeu!")
