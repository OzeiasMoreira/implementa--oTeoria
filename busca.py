import time

class FSM:
    def __init__(self):
        self.states = {}
        self.initial_state = None
        self.accept_states = set()

    def add_state(self, name):
        self.states[name] = {}

    def add_accept_state(self, name):
        self.accept_states.add(name)

    def add_transition(self, from_state, char, to_state):
        if from_state in self.states:
            self.states[from_state][char] = to_state

    def polyfill(self, trap_state):
        for state in self.states:
            for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if char not in self.states[state]:
                    self.states[state][char] = trap_state

    def accepts(self, char):
        current_state = self.initial_state
        if char in self.states[current_state]:
            next_state = self.states[current_state][char]
            return next_state in self.accept_states
        return False

class PatternRecognition:
    def __init__(self):
        self.count = 0
        self.machine = None

    def create_fsm(self, search_char):
        machine = FSM()
        machine.add_state('ONE')
        machine.add_state('TWO')
        machine.add_state('TRAP')
        machine.initial_state = 'ONE'
        machine.add_accept_state('TWO')
        machine.add_transition('ONE', search_char, 'TWO')
        machine.polyfill('TRAP')
        return machine

    def fsm_check(self, char, search_char):
        if not self.machine:
            self.machine = self.create_fsm(search_char)
        return self.machine.accepts(char)

    def check_word(self, word, search_key):
        self.machine = None
        if len(word) >= len(search_key):
            for i in range(len(word) - len(search_key) + 1):
                flag = True
                for j in range(len(search_key)):
                    if word[i + j] != search_key[j]:
                        flag = False
                        break
                if flag:
                    self.count += 1
                    return True
        return False

    def search_in_file(self, filename, search_key):
        start_time = time.time()
        self.count = 0
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.strip().split()
                    for word in words:
                        self.check_word(word, search_key)
            execution_time = (time.time() - start_time) * 1000
            return {'occurrences': self.count, 'execution_time': execution_time}
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado")
            return None
        except Exception as e:
            print(f"Erro ocorrido: {str(e)}")
            return None

if __name__ == "__main__":
    pr = PatternRecognition()
    filename = "sample.txt"
    search_key = "teste"
    result = pr.search_in_file(filename, search_key)
    if result:
        print(f"Chave '{search_key}' encontrada {result['occurrences']} vezes")
        print(f"Tempo de execução: {result['execution_time']:.2f} ms")
