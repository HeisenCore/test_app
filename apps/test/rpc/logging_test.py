from heisen.core.log import logger
from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    def run(self, arg1, arg2):
        logger.debug(arg1)
        logger.error(arg2)
