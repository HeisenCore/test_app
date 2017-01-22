from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    schema = {
        'arg1': {
            'type': 'datetime'
        }
    }

    def run(self, arg1):
        return arg1
