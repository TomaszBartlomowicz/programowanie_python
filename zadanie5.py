class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        """Dodaje przejście do innego stanu na podstawie symbolu wejściowego."""
        self.transitions[input_symbol] = next_state

    def next_state(self, input_symbol):
        """Zwraca kolejny stan dla danego symbolu wejściowego."""
        return self.transitions.get(input_symbol, None)

class MooreMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state, is_initial=False):
        """Dodaje stan do automatu, opcjonalnie ustawiając go jako początkowy."""
        self.states[state.name] = state
        if is_initial:
            self.initial_state = state

    def process(self, inputs):
        """Przetwarza sekwencję symboli wejściowych."""
        current_state = self.initial_state
        outputs = []

        for input_symbol in inputs:
            if current_state is None:
                break
            outputs.append(current_state.name)
            current_state = current_state.next_state(input_symbol)

        if current_state:
            outputs.append(current_state.name)

        return outputs

# Przykład automatu Moore'a
s1 = State("S1")
s2 = State("S2")
s3 = State("S3")

s1.add_transition("a", s2)
s1.add_transition("b", s1)
s2.add_transition("a", s2)
s2.add_transition("b", s3)
s3.add_transition("a", s1)
s3.add_transition("b", s3)

fsm = MooreMachine()
fsm.add_state(s1, is_initial=True)
fsm.add_state(s2)
fsm.add_state(s3)

# Przykładowe wejście
data = ["a", "b", "a", "a", "b"]
output = fsm.process(data)
print(output)
