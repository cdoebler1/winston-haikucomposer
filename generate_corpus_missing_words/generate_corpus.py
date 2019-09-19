"""Produce new haiku from training corpus of existing haiku."""
import sys
import logging
import random
import json
from collections import defaultdict
from count_syllables import count_syllables
from string import punctuation

logging.disable(logging.CRITICAL)  # comment-out to enable debugging messages
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def load_training_file():
    """Return a text file as a string."""
    with open('Training.json') as f_obj:
        files = json.load(f_obj)
    print(files)
    raw_haiku = ''
    for file in files:
        file = file + '.txt'
        with open(file) as f:
            raw_haiku = raw_haiku + f.read()
    return raw_haiku


def prep_training(raw_haiku):
    """Load string, remove newline, split words on spaces, and return list."""
    # corpus = raw_haiku.replace('\n', ' ').strip(punctuation).lower().split()
    corpus = raw_haiku.replace('\n', ' ').replace('"', '')
    corpus = corpus.lower().replace(',', '').replace('.', '').split()
    return corpus


def main():
    """Give user choice of building a haiku or modifying an existing haiku."""
    intro = """\n
    A thousand monkeys at a thousand typewriters...
    or one computer...can sometimes produce a haiku.\n"""
    print("{}".format(intro))

    raw_haiku = load_training_file()
    corpus = prep_training(raw_haiku)
    json_string = json.dumps(corpus)
    f = open('corpus.json', 'w')
    f.write(json_string)
    f.close()
    print("\nCorpus save as corpus.json")


if __name__ == '__main__':
    main()
