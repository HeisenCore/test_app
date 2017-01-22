import datetime

from heisen.rpc.base import RPCBase
from heisen.core.scheduler.scheduler import scheduler


class RPC(RPCBase):
    def run(self):
        scheduler.add_job(
            test,
            'date',
            run_date=datetime.datetime.now() + datetime.timedelta(seconds=5),
        )


def test():
    with open('/tmp/scheduler_test.txt', 'a') as f:
        f.write('{}\n'.format(
            datetime.datetime.now().isoformat()
        ))
