from cliff.command import Command as CliffCommand

from heisen.core import rpc_call


class Command(CliffCommand):
    def get_parser(self, prog_name):
        parser = super(Command, self).get_parser(prog_name)
        parser.add_argument('num1', nargs='?', default='.')
        parser.add_argument('num2', nargs='?', default='.')

        return parser

    def take_action(self, parsed_args):
        print rpc_call.self.test.division(
            int(parsed_args.num1),
            int(parsed_args.num2)
        )
