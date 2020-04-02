import xml.etree.ElementTree as ET
import sys

def get_child(parent, name):
    for child in parent:
        if child.tag == name:
            return child
    return None

class Token:
    def __init__(self, word, lemma, begin, end, pos):
        self.word = word
        self.lemma = lemma
        self.begin = begin
        self.end = end
        self.pos = pos

    def __repr__(self):
        return self.word

def parse_token(token_elem):
    word = get_child(token_elem, 'word').text
    lemma = get_child(token_elem, 'lemma').text
    begin = get_child(token_elem, 'CharacterOffsetBegin').text
    end = get_child(token_elem, 'CharacterOffsetEnd').text
    pos = get_child(token_elem, 'POS').text
    return Token(
        word,
        lemma,
        begin,
        end,
        pos
    )

class Sentence:
    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        str = ""
        for t in self.tokens:
            str += " %s" % t.__repr__()
        return str

def parse_sentence(sent_elem):
    tokens = []
    for token in sent_elem[0]:
        tokens.append(parse_token(token))
    return Sentence(tokens)

class Document:
    def __init__(self, sentences):
        self.sentences = sentences

class HulthParser:
    def parse(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        sentences = []
        for sent in root[0][0]:
            sent = parse_sentence(sent)
            sentences.append(sent)
        return sentences
