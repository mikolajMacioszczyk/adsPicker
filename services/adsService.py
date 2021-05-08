from Models import Ad
from spacy.lang.pl import Polish
from spacy.lang.en import English
from nltk.stem import PorterStemmer
import re


class AdsService:
    def __init__(self, context):
        self.context = context

    def getByTags(self, query, language='pl'):
        words = self._getMeaningfulWords(query, language)
        # use glove
        # wyszukać odpowiadające wraz z licznością
        # jeśli są jakieś:
        # sortując według liczności wybrać najbardziej trafne
        # w przeciwnym wypadku:
        # daj obojętnie jakiego
        # TODO: Search by tags
        return words
        pass

    def _getMeaningfulWords(self, query, language):
        if language == 'pl':
            nlp = Polish()
        elif language == 'en':
            nlp = English()
        else:
            raise ValueError(f'unsupported language {language}')

        query = re.sub(r'[^\w\s]', '', query)
        ps = PorterStemmer()

        token_list = [token.text for token in nlp(query)]
        filtered_query = []
        for word in token_list:
            lexeme = nlp.vocab[word]
            if not lexeme.is_stop:
                filtered_query.append(ps.stem(word))
        return filtered_query

    def getAny(self):
        result = self.context.getAds(1)
        if len(result) > 0:
            return result[0]
        return Ad.default()
