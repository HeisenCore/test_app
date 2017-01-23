from heisen.core.log import logger
from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    def run(self, arg1):
        logger.test_log(arg1)
        1/0
