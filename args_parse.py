''' Argparse
    Here --a is optional, to run this from command line
    type python args_parse.py --a=99 2 3 4 5
    output: 99
            2
            3
            4
            5 
    or 
    type python args_parse.py 2 3 4 5
    output: 1
            2
            3
            4
            5
'''

import argparse 


def get_sum(args): 
    print(args.a)
    print(args.b)
    print(args.c)
    print(args.d)
    print(args.e)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adding purpose")
    parser.add_argument('--a', type=int, default=1, help="value of a")
    parser.add_argument('b', type=int, help="value of b")
    parser.add_argument('c', type=int, help="value of c")
    parser.add_argument('d', type=int, help="value of d")
    parser.add_argument('e', type=int, help="value of e")
    args = parser.parse_args()

    get_sum(args)
