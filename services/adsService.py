from Models.ad import Ad
from Models.tag import Tag
from spacy.lang.pl import Polish
from spacy.lang.en import English
# from nltk.stem import PorterStemmer
import re

SIMILAR_COUNT = 10


class AdsService:
    def __init__(self, context, wordService):
        self.__wordService = wordService
        self.__context = context

    def getById(self, adId):
        return self.__context.getAdById(adId)

    def getByTitle(self, title):
        return self.__context.getAdByTitle(title)

    def create(self, title, description, imagePath, tagsList):
        created = Ad(title, description, imagePath, self._tagsFromList(tagsList))
        return self.__context.addAd(created)

    def update(self, adId, title, description, imagePath, tagsList):
        updated = Ad(title, description, imagePath, self._tagsFromList(tagsList))
        return self.__context.updateAd(adId, updated)

    @staticmethod
    def _tagsFromList(tagsList):
        # ps = PorterStemmer()
        # return [Tag(ps.stem(tag['value'])) for tag in tagsList]
        return [Tag(tag['value']) for tag in tagsList]

    def remove(self, adId):
        return self.__context.removeAd(adId)

    def getByTags(self, query, maxCount=1, language='pl'):
        words = self._getMeaningfulWords(query.lower(), language)
        results = self._countMatches(words)
        if results:
            return [res[0] for res in results[:maxCount]]
        else:
            return self.getAny(maxCount)

    def _countMatches(self, words):
        results = {}
        for word in words:
            similarGroup = self.__wordService.findClosest(word)
            print(f"\033[92m similar group for word {word}: {str(similarGroup)}\033[0m")
            for similar in similarGroup:
                for ad in self.__context.getAdsByTags([similar]):
                    if ad not in results:
                        results[ad] = 1
                    else:
                        results[ad] += 1
        return sorted(results.items(), key=lambda kv: kv[1], reverse=True)

    @staticmethod
    def _getMeaningfulWords(query, language):
        if language == 'pl':
            nlp = Polish()
        elif language == 'en':
            nlp = English()
        else:
            raise ValueError(f'unsupported language {language}')

        query = re.sub(r'[^\w\s]', '', query)
        # ps = PorterStemmer()

        token_list = [token.text for token in nlp(query)]
        filtered_query = []
        for word in token_list:
            lexeme = nlp.vocab[word]
            if not lexeme.is_stop:
                # filtered_query.append(ps.stem(word))
                filtered_query.append(word)
        return filtered_query

    def getAny(self, maxCount=1):
        result = self.__context.getAds(maxCount)
        if len(result) > 0:
            return result[:maxCount]
        return [Ad.default()]
