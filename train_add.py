import json
import time
import hashlib
import sys

import requests

import vm

class VM(vm.VM):
    def train(self, code = 0):
        t0 = time.time()
        for code in range(code, code+10000000):
            self.parse_code(code)
            # code += 1
            # if code % 10000000 == 0:
            #     print(code, code/(time.time() - t0))

            if 4 not in self.code:
                continue
            if 5 not in self.code:
                continue
            self.run([1, 1, 0])
            if self.gas > 0 and self.tape == [0, 0, 2]:
                self.run([1, 2, 0])
                if self.gas > 0 and self.tape == [0, 0, 3]:
                    self.run([2, 2, 0])
                    if self.gas > 0 and self.tape == [0, 0, 4]:
                        print(code, self.code, self.tape, self.gas)

host = sys.argv[1]
secret = 'hello'

vm = VM()
# while True:
#     timestamp = int(time.time())
#     # timestamp = 1681295648
#     rsp = requests.post('http://'+host, data=json.dumps({
#         'timestamp': timestamp,
#         'otp': hashlib.sha256((secret+str(timestamp)).encode('utf8')).hexdigest()}))
#     task = rsp.json()['task']
#     print(task)
#     vm.train(task)

# 22885275 [3, 0, 2, 2, 0, 3, 4, 3, 1, 2] [0, 0, 3] 989
# 22931931 [3, 0, 2, 2, 0, 3, 5, 3, 1, 2] [0, 0, 3] 989

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
IF = 4
GO = 5

vm.code = [IF, DOWN, RIGHT, RIGHT, UP, LEFT, LEFT, GO, RIGHT, IF, DOWN, RIGHT, UP, LEFT, GO]
vm.run([100, 2, 0])
print(vm.tape)
