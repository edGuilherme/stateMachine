from statemachine import StateMachine, State


class Mundo(StateMachine):

    fome = 0
    vida = 10
    dormindo = State(initial=True)
    come = State()
    luta = State()


    cycle = (
            dormindo.to(come)
            | come.to(dormindo) | come.to(luta) | dormindo.to(luta)

    )


    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_dormindo(self):
        self.estado = 1
        print("O troll está dormindo")

    def on_exit_dormindo(self):
        pass

    def on_enter_come(self):
        self.estado = 2;
        print("O troll está na floresta comendo")

    def on_enter_luta(self):
        self.estado = 3;
        print("O troll começou a lutar")


    def atualiza(self):
        if self.estado == 1: #dormindo
            self.fome +=1
            if self.vida < 10:
                self.vida +=1
            if self.fome >= 4: #faminto - vai comer
                self.cycle()

        elif self.estado == 2: #comendo - na floresta
            self.fome -=3
            self.vida -=1
            if self.fome < 4: #fome diminui - vai dormir
                self.cycle()

    def batalha(self):
        self.cycle



sm = Mundo()
sm.atualiza()
sm.atualiza()
sm.atualiza()
sm.atualiza()
sm.atualiza()
sm.batalha()







