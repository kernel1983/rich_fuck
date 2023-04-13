
import time
import copy

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
IF = 4
GO = 5
TOTAL_OP = 6

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
            pass


    def step(self):
        # print('head', self.head, self.tape[self.head])
        # print('local_vars', self.local_vars)
        if self.code[self.pc] == LEFT:
            # print('LEFT')
            self.head -= 1
            self.pc += 1

        elif self.code[self.pc] == RIGHT:
            # print('RIGHT')
            self.head += 1
            self.pc += 1

        elif self.code[self.pc] == UP:
            # print('UP')
            self.tape[self.head] += 1
            self.pc += 1

        elif self.code[self.pc] == DOWN:
            # print('DOWN')
            self.tape[self.head] -= 1
            self.pc += 1

        elif self.code[self.pc] == IF:
            # print('IF')
            if self.tape[self.head] == 0:
                while self.code[self.pc] != GO:
                    self.pc += 1
                    # print(self.pc)
            else:
                self.pc += 1

        elif self.code[self.pc] == GO:
            # print('GO')
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

# vm = VM([0])
# vm.code = [4, 0, 0, 0, 0, 5]
# vm.run()

