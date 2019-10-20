from .core import create_note, open_note, list_notes
from .config import Config
from .paths import NOTES_PATH
import json
from argparse import ArgumentParser
from uuid import uuid4

new_id = str(uuid4())

def main():
    parser = ArgumentParser(usage='pystickynote <open/create/list> <name/all>')
    parser.add_argument('action', choices=['open', 'create', 'list'], help='Action to run. Either "open" or "create".')
    parser.add_argument('name', help='Stickynote\'s name to save to', nargs='?', default=new_id)
    args = parser.parse_args()
    config = Config()
    if args.action == 'create':
        if args.name == new_id:
            print('Please Provide A Name for Your Note.')
        else:
            with open(NOTES_PATH, 'r+') as json_file:
                obj = json.load(json_file)
                for k, v in obj.items():
                    if args.name == k:
                        print('Note with that name found, please use the open command to edit/delete.')
                        exit(1)
            create_note(args.name, config)
    elif args.action == 'open':
        if args.name == new_id:
            print('Please Provide The Name of The Note.')
        else:
            open_note(args.name, config)
    elif args.action == 'list':
        list_notes()
    exit(0)

if __name__ == "__main__":
    main()