from statemachine import StateMachine, State


class Mundo(StateMachine):

    vida = 10
    fome = 0
    dorme = State(initial=True)
    come = State()
    luta = State()

    dormindo = dorme.to(come)
    comendo = come.to(dorme)
    lutando = luta.to(dorme)

    cycle = (
            dormindo
            | comendo | lutando

    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_dorme(self):
        self.fome += 1
        print("O troll está dormindo" )

    def on_exit_dorme(self):
        pass

    def on_enter_come(self):
        self.fome -= 3
        print("O troll está comendo" )

    def on_enter_luta(self):
        print("O troll está lutando" )


sm = Mundo()
sm.cycle
sm.cycle















