from heisen.core.mail import Email
from heisen.rpc.base import RPCBase


class RPC(RPCBase):
    def run(self):
        context = {
            'user': {
                'name': 'K1',
                'age': 101,
                'email': 'me@k1h.ir'
            }
        }

        Email(
            'info@test.com',
            subject={'context': context, 'filename': 'subject.txt'},
            content={'context': context, 'filename': 'content.html'},
        ).send_email(context['user']['email'])
