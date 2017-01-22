from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    schema = {
        'arg1': {
            'type': 'string'
        },
        'arg2': {
            'type': 'integer',
            'min': 10
        },
        'arg3': {
            'type': 'list',
            'allowed': ['agent', 'client', 'supplier']
        }
    }

    def run(self, arg1, arg2, arg3):
        return (arg1, arg2, arg3)
