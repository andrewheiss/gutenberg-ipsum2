#!/usr/bin/env python3
import markovify
import argparse
import random
from pos_tagging import POSifiedText 

# Get command line arguments
parser = argparse.ArgumentParser(description='Generate random text with Markov chains!')
parser.add_argument('corpus', type=argparse.FileType('r+'),
                    help='corpus of training text')
parser.add_argument('num_sentences', type=int, default=5, nargs='?',
                    help='the number of sentences to output (default: 5)')
args = parser.parse_args()

# Save arguments
corpus = args.corpus
num_sentences = args.num_sentences

# Use corpus to train model
state_size = random.randrange(2, 4)  # Vary the state size for kicks
text = corpus.read()
text_model = markovify.Text(text, state_size = state_size)

# Generate a sentence. If it's valid (i.e. not None), add it to the list of
# sentences until the list is the correct size.
x = 0
sentences = []

while x <= num_sentences:
    generated_sentence = text_model.make_sentence()

    if generated_sentence is not None:
        sentences.append(generated_sentence)
        x += 1

# All done!
print(' '.join(sentences))
