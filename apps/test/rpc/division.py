from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    def run(self, number1, number2):
        return number1 / number2
