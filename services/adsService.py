from Models.ad import Ad
from spacy.lang.pl import Polish
from spacy.lang.en import English
from nltk.stem import PorterStemmer
import re


class AdsService:
    def __init__(self, context):
        self.context = context

    def getByTags(self, query, maxCount=1, language='pl', useGlove=False):
        words = self._getMeaningfulWords(query, language)
        if useGlove:
            raise NotImplemented()
        else:
            results = self._countMatches(words)
            if results:
                return max(results.items(), key=lambda kv: kv[1])[:maxCount]
            else:
                return self.getAny(maxCount)

    def _countMatches(self, words):
        results = {}
        for word in words:
            for ad in self.context.getAdsByTags([word]):
                if ad not in results:
                    results[ad] = 1
                else:
                    results[ad] += 1
        return results

    @staticmethod
    def _getMeaningfulWords(query, language):
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

    def getAny(self, maxCount=1):
        result = self.context.getAds(maxCount)
        if len(result) > 0:
            return result[:maxCount]
        return [Ad.default()]
