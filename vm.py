
import time
import copy

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
IF = 4
GO = 5
ZERO = 6
ONE = 7
TOTAL_OP = 6
DEBUG = True

class VM:
    # def __init__(self, state = []):
    #     self.state = state
    #     self.canidates = []

    def parse_code(self, code):
        self.code = []
        while code >= TOTAL_OP:
            m = code % TOTAL_OP
            code = code // TOTAL_OP
            self.code.append(m)
        self.code.append(code)
        return self.code

    def run(self, state):
        self.tape = copy.copy(state)
        # self.head = len(self.state)
        # self.stack = []
        self.head = 0
        # self.parse_code(code)
        self.pc = 0
        self.gas = 1000

        try:
            while True:
                if self.gas < 0:
                    break
                self.gas -= 1
                self.step()
        except:
            print('except')


    def step(self):
        # print('head', self.head, self.tape[self.head])
        # print('pc', self.pc)
        # print('local_vars', self.local_vars)
        if self.code[self.pc] == LEFT:
            if DEBUG:
                print('LEFT')
            self.head -= 1
            if self.head < 0:
                raise
            self.pc += 1

        elif self.code[self.pc] == RIGHT:
            if DEBUG:
                print('RIGHT', self.tape, self.head)
            self.head += 1
            if len(self.tape) >= self.head:
                self.tape.extend([0]*(self.head - len(self.tape) + 1))
            self.pc += 1

        elif self.code[self.pc] == UP:
            if DEBUG:
                print('UP')
            self.tape[self.head] += 1
            self.pc += 1

        elif self.code[self.pc] == DOWN:
            if DEBUG:
                print('DOWN')
            self.tape[self.head] -= 1
            self.pc += 1

        elif self.code[self.pc] == IF:
            if DEBUG:
                print('IF')
            if self.tape[self.head] == 0:
                while self.code[self.pc] != GO:
                    self.pc += 1
                    # print(self.pc)
            else:
                self.pc += 1

        elif self.code[self.pc] == GO:
            if DEBUG:
                print('GO')
            if self.tape[self.head] > 0:
                while self.code[self.pc] != IF:
                    self.pc -= 1
                    # print(self.pc)
            else:
                self.pc += 1


# print(VM().parse_code(35))
# print(VM().parse_code(10))
# print(VM().parse_code(6))
# print(VM().parse_code(5))

vm = VM()
vm.code = [4, RIGHT, UP, 5]
vm.run([1])

