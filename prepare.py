#!/usr/bin/env python
"""Prepares language modeling data."""

import argparse
import gzip
import logging
import urllib.request

import nltk  # type: ignore


DATA_URL = "http://www.statmt.org/wmt14/training-monolingual-news-crawl/news.2007.en.shuffled.gz"


def main(args: argparse.Namespace) -> None:
    # This is just a fancy way to download the file from Python.
    response = urllib.request.urlopen(DATA_URL)
    with gzip.GzipFile(fileobj=response) as source, open(
        args.tok, "w"
    ) as sink:
        for lineno, bline in enumerate(source, 1):
            # The GzipFile object gives us `bytes`, not `str`.
            # Therefore we decode before doing further work.
            line = bline.decode("utf8")
            # The tokenizer is case-independent so we casefold first.
            line = line.casefold()
            tokens = nltk.word_tokenize(line)
            print(" ".join(tokens), file=sink)
            # This logs information every 100k sentences.
            if not lineno % 100000:
                logging.info(f"{lineno:,} sentences processed")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level="INFO")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tok", help="path for output file")
    main(parser.parse_args())
