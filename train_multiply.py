import json
import time
import hashlib
import sys

import requests

import vm

class VM(vm.VM):
    def train(self, code, test):
        for code in range(code, code+10000000):
            self.parse_code(code)

            if 4 not in self.code or 5 not in self.code:
                continue

            for inputs, validator in test:
                self.run(inputs)
                if self.gas <= 0 or self.tape[validator[0]] != validator[1]:
                    break
            else:
                print(code, self.code, self.tape, self.gas)

host = sys.argv[1]
secret = 'hello'

vm = VM()
while True:
    timestamp = int(time.time())
    # timestamp = 1681295648
    rsp = requests.post('http://%s/multiply' % host, data=json.dumps({
        'timestamp': timestamp,
        'otp': hashlib.sha256((secret+str(timestamp)).encode('utf8')).hexdigest()}))
    task = rsp.json()['task']
    test = rsp.json()['test']
    print(task)
    vm.train(task, test)

