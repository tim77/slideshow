import argparse
parser = argparse.ArgumentParser(description='Process some integers.',
		prog="my")
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()

