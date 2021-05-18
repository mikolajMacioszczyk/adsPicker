import numpy as np
from scipy import spatial

GLOVE_MODEL_FILENAME = 'glove.6B.100d.txt'


class WordService:
    def __init__(self):
        self._embeddings_dict = {}
        self._loadGlove()

    def _loadGlove(self):
        with open(GLOVE_MODEL_FILENAME, 'r', encoding='utf8') as f:
            for line in f:
                values = line.split()
                word = values[0]
                vector = np.asarray(values[1:], "float32")
                self._embeddings_dict[word] = vector

    def findClosest(self, typedWord, count=10):
        if typedWord in self._embeddings_dict:
            embedding = self._embeddings_dict[typedWord]
            similar = sorted(self._embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(self._embeddings_dict[word], embedding))
        else:
            similar = [typedWord]
        return similar[:count]
