from statemachine import StateMachine, State
import random


# https://pypi.org/project/python-statemachine/

class Mundo(StateMachine):
    # estados iniciais do mundo
    fome = 0  # fome do troll
    vida = 10  # vida do troll
    briga = 0  # variável para controlar a entrada na batalha

    # estados
    dorme = State(initial=True)  # inicial
    come = State()
    luta = State()
    morre = State()

    # transições - nem todas serão\precisam ser usadas
    dormindo = dorme.to(dorme)
    faminto = dorme.to(come)
    comendo = come.to(come)
    satisfeito = come.to(dorme)
    lutando = come.to(luta)
    ganhando = luta.to(dorme)
    perdendo = luta.to(morre)

    # eventos - todas as possibilidades de transições
    cycle1 = (dormindo)
    cycle2 = (faminto)
    cycle3 = (comendo)
    cycle4 = (satisfeito)
    cycle5 = (lutando)
    cycle6 = (ganhando)
    cycle7 = (perdendo)

    # cycle(x,y) = (x.to(y)) # o ideal seria fazer assim, com um só evento recebendo as entradas, mas não consegui implementar dessa forma.

    def on_enter_dorme(self):
        print("O troll está dormindo")
        self.fome += 1
        print("O troll está com " + str(self.fome) + " " + "de fome.")
        if self.vida < 10:
            self.vida += 1
        if self.fome >= 4:  # faminto - vai comer
            print("Como \"fome > 4\", o troll está faminto e vai comer.")
            self.cycle2()  # dorme para come

    def on_exit_dorme(self):
        pass

    def on_enter_come(self):  # comendo - na floresta
        self.fome += 1
        print("O troll está na floresta comendo \\ -3 de fome \\ +1 em briga (probabilidade de encontrar inimigo)")
        if self.fome >= 0:  # tentativa de impedir que a var. fome não seja negativa - não funcionou tão bem
            self.fome -= 3
        print("O troll está com " + str(self.fome) + " " + "de fome.")
        self.vida -= 1
        self.briga += 1
        if self.briga >= 2:  # valor para teste - pode ser aleatório junto com o incremento de briga. Por exemplo
            # if briga%10=0: ENTRA EM ESTADO DE LUTA/BATALHA
            self.cycle5()  # come para luta

    def on_enter_luta(self):
        self.fome += 1
        print("O troll começou a lutar")
        self.ataqueTroll = random.randint(2, 4)
        self.ataqueInimigo = random.randint(1, 2)
        self.vidaInimigo = random.randint(1, 4)
        print("Vida troll: " + str(self.vida))
        print("Vida inimigo: " + str(self.vidaInimigo))
        print("Ataque troll: " + str(self.ataqueTroll))
        print("Ataque inimigo: " + str(self.ataqueInimigo))
        emBatalha = True
        while emBatalha:
            self.turno = random.randint(1, 2)
            if self.turno == 1:  # duas possibilidades de batalha: Troll ataca ou Inimigo ataca - é aleatório, ou seja, Troll ou inimigo podem atacar vezes seguidas/por turnos seguidos.
                print("Troll ataca")
                self.vidaInimigo -= self.ataqueTroll
                if self.vidaInimigo <= 0:
                    print("Venceu! Troll volta pra caverna")
                    emBatalha = False
                    self.cycle6()
            if self.turno == 2:
                print("Inimigo ataca")
                self.vida -= self.vidaInimigo
                if self.vida <= 0:
                    print("Morreu")
                    emBatalha = False
                    self.cycle7()


sm = Mundo()  # começa o mundo - dormindo
sm.cycle1()  # dorme
sm.cycle1()  # dorme
sm.cycle1()  # continua dormindo - vai comer pois fome > 4
# acima ele entra em 'come' e briga = 1
sm.cycle3()  # come de novo - briga += 1 - se torna briga = 2 e entra em modo de batalha









