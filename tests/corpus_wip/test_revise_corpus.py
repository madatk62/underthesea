from unittest import TestCase
from underthesea.corpus.revise_corpus import revise_corpus


class TestReviseCorpus(TestCase):
    def test(self):
        corpus_name = "VLSP2013-WTK"
        revise_corpus(corpus_name)
