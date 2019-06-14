import argparse
parser = argparse.ArgumentParser(description='Process some integers.',
prog="my")
parser.add_argument('--foo', help='foo help')
parser.add_argument('-t',help='time to display')
args = parser.parse_args[1]
print(args)
