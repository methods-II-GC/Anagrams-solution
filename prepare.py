#!/usr/bin/env python
"""Prepares language modeling data."""

import argparse
import gzip

import nltk  # type: ignore


def main(args: argparse.Namespace) -> None:
    with gzip.GzipFile(args.gz, "rt") as source, open(
        args.tok, "w"
    ) as sink:
        for line in source:
            tokens = nltk.word_tokenize(line)
            print(" ".join(tokens).casefold(), file=sink)

            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gz", help="path to input .gz file")
    parser.add_argument("tok", help="path for output .tok file")
    main(parser.parse_args())
