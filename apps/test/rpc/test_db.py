from heisen.rpc.base import RPCBase
from heisen.core.db import db


class RPC(RPCBase):
    def run(self, key, value):
        db.test.test_collection.insert_one({key: value})

        return list(db.test.test_collection.find())
