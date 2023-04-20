import json
import time
import hashlib
import sys

import requests

import vm

class VM(vm.VM):
    def train(self, code, test):
        t0 = time.time()
        for code in range(code, code+10000000):
            self.parse_code(code)

            if 4 not in self.code or 5 not in self.code:
                continue

            for inputs, validator in test:
                self.run(inputs)
                if self.gas <= 0 or self.tape[validator[0]] != validator[1]:
                    break
                # print(code, self.code, self.tape, self.gas)
            else:
                print(code, self.code, self.tape, self.gas)

if len(sys.argv):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    IF = 4
    GO = 5
    ZERO = 6
    ONE = 7

    vm = VM()
    vm.code = [IF, DOWN, RIGHT, RIGHT, UP, LEFT, LEFT, GO, RIGHT, IF, DOWN, RIGHT, UP, LEFT, GO]
    vm.run([100, 2, 0])
    print(vm.tape)

# 22885275 [3, 0, 2, 2, 0, 3, 4, 3, 1, 2] [0, 0, 3] 989
# 22931931 [3, 0, 2, 2, 0, 3, 5, 3, 1, 2] [0, 0, 3] 989
else:
    host = sys.argv[1]
    secret = 'hello'

    vm = VM()
    while True:
        timestamp = int(time.time())
        # timestamp = 1681295648
        rsp = requests.post('http://%s/add' % host, data=json.dumps({
            'timestamp': timestamp,
            'otp': hashlib.sha256((secret+str(timestamp)).encode('utf8')).hexdigest()}))
        task = rsp.json()['task']
        test = rsp.json()['test']
        print(task, test)
        vm.train(task, test)
