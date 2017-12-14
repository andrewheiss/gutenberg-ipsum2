import markovify
import nltk
import re

# Use nltk to tag the parts of speech. Using spacy is theoretically faster, but
# it made it so that the generated text was the same every time ¯\_(ツ)_/¯
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
