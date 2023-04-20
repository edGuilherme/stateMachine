from statemachine import StateMachine, State


class Mundo(StateMachine):
    fome = 0
    vida = 10

    dorme = State(initial=True)
    come = State()
    luta = State()

    dormindo = dorme.to(dorme) # inicial
    faminto = dorme.to(come)
    comendo = come.to(come)
    lutando = come.to(luta)
    ganhando = luta.to(dorme)

    cycle = (
            faminto
    )

    cycle2 = (
            comendo
    )

    cycle3 = (
        lutando
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_dorme(self):
        self.fome += 1
        print("é esse " + str(self.fome))
        if self.vida < 10:
            self.vida += 1
        if self.fome >= 4:  # faminto - vai comer
            self.cycle() # não funciona
        print("O troll está dormindo")

    def on_exit_dorme(self):
        pass

    def on_enter_come(self):  # comendo - na floresta
        self.fome -= 3
        self.vida -= 1
        print("O troll está na floresta comendo")

    def on_enter_luta(self):
        print("O troll começou a lutar")



sm = Mundo()
sm.cycle()
print(sm.current_state.id)
sm.cycle3()
print(sm.current_state.id)








