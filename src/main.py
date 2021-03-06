from argparse import ArgumentParser
from spacemaps.analyse import run_analysis
from spacemaps.stream import create_stream


def main():
    args = create_parser().parse_args()
    with create_stream(args.filename) as stream:
        for result in run_analysis(stream, args.limit):
            print(result.id)


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('filename', help='the filename to process')
    parser.add_argument('limit', type=int, help='the number of ids to return')
    return parser


if __name__ == '__main__':
    main()
