from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    documentation = """
        Test documents, you can put anything to it
    """

    schema = {
        'arg1': {
            'type': 'string',
            'info': 'first argument of method',
            'example': 'foo, bar, baz'
        },
        'arg2': {
            'type': 'integer',
            'info': 'second argument of method',
            'example': '1, 2, 3'
        }
    }

    return_schema = {
        'type': 'list',
        'info': 'list of parameters',
        'example': '[1, 2, 3], ["foo", "bar", "baz"]'
    }

    def run(self, arg1, arg2):
        return_value = [arg1, arg1, arg1]

        return return_value
