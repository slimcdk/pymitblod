'''
Main for pymitblod
'''
import argparse
import logging
from . import MitBlod, Institutions

def main():
    '''
    Main method
    '''
    parser = argparse.ArgumentParser("pymitblod")
    parser.add_argument("--log", action="store", required=False)
    parser.add_argument("--username", action="store", required=True)
    parser.add_argument("--password", action="store", required=True)
    parser.add_argument("--institution", action="store", required=True)
    args = parser.parse_args()

    _configureLogging(args)

    #mitblod = MitBlod(args.username, args.password, Institutions.REGION_SYDDANMARK.name())

def _configureLogging(args):
    if args.log:
        numeric_level = getattr(logging, args.log.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % args.log)
        
        logging.basicConfig(level=numeric_level)

if __name__ == "__main__":
    main()