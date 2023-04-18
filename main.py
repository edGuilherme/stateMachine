from statemachine import StateMachine, State


class Mundo(StateMachine):

    fome = 0
    dormindo = State(initial=True)
    come = State()

    cycle = (
            dormindo.to(come)
            | come.to(dormindo)

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

    def on_exit_come(self):
        pass

    def atualiza(self):
        if self.estado == 1:
            self.fome +=1
            print(self.fome)
            if self.fome >= 4:
                self.cycle()
        elif self.estado == 2:
            self.fome -=3
            print(self.fome)
            if self.fome < 4:
                self.cycle()



sm = Mundo()
sm.atualiza()
sm.atualiza()
sm.atualiza()
sm.atualiza()
sm.atualiza()






