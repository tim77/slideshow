import argparse
parser = argparse.ArgumentParser(description='Process some integers.',
prog="my")
parser.add_argument('--foo',type=int, help='foo help')
parser.add_argument('-t',type=int,help='time to display',metavar='N')
parser.add_argument('--path','-p',type=str,help='path to search images')
args = parser.parse_args()
print(args.t)
