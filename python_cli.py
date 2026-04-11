import argparse
from collections import Counter

def count_letters(s, minimum=1):
    return {k: v for k,v in Counter(s).items() if v >= minimum}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('letters',type=str, metavar='SOME TEXT', help='Enter some text to be evaluated.')
    parser.add_argument('--minimum','-m','-min', type=int, dest='mini', help='minimum number of occurences')
    args = parser.parse_args()
    print(args)
    results = count_letters(args.letters, args.mini)
    print(results)

