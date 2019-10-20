from .create_note import create_note
from .open_note import open_note
from .config import Config
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(usage='pystickynote <open/create> <name>')
    parser.add_argument('action', choices=['open', 'create'], help='Action to run. Either "open" or "create".')
    parser.add_argument('name', help='Stickynote\'s name to save to', type=str)
    args = parser.parse_args()
    config = Config()
    if args.action == 'create':
        create_note(args.name, config)
    elif args.action == 'open':
        open_note(args.name, config)
    exit(0)

if __name__ == "__main__":
    main()