import pandas as pd


def clean(input_file):
    df = pd.read_csv(input_file)
    return df


if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser()
    parse.add_argument('input', help='diabetes file')
    parse.add_argument('output', help='cleaned diabetes file')
    args = parse.parse_args()
    cleaned = clean(args.input)
    cleaned.to_csv(args)
