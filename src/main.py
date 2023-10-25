import os.path
import sys

import argparse

from kcwiki import Quests


def run(output):
    parser = argparse.ArgumentParser(description='kcwiki parser')
    subparsers = parser.add_subparsers(dest='command', help='commands')

    parser_command1 = subparsers.add_parser('kcQuests', help='kcQuests项目原格式')
    parser_command1.add_argument('-d', '--download', help='Need download new items data')
    # parser_command1.add_argument('output', type=str, help='Output path')

    parser_command2 = subparsers.add_parser('conntower', help='For ConningTower')
    # parser_command2.add_argument('arg', type=int, help='Argument')

    args = parser.parse_args()

    if args.command == 'kcQuests':
        quests = Quests()
        quests.set_output(output)
        quests.query_raw_text()
        if args.download == 1:
            quests.query_solt_items()
        else:
            quests.load_solt_items()
        quests.parse()
        quests.save_json_kcq()
        print('Success')
    elif args.command == 'conntower':
        print('ConningTower')
    else:
        parser.print_help()


if __name__ == '__main__':
    script_path = os.path.abspath(__file__)

    root_path = os.path.dirname(os.path.dirname(script_path))
    print(root_path)
    run(root_path)

