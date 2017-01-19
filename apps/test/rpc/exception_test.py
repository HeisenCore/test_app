from heisen.rpc.base import RPCBase


class Test(Exception):
    pass


class RPC(RPCBase):
    def run(self):
        raise Test('test')
