from Models.ad import Ad
from Models.tag import Tag
from spacy.lang.pl import Polish
from spacy.lang.en import English
# from nltk.stem import PorterStemmer
import re

SIMILAR_COUNT = 5


class AdsService:
    def __init__(self, context, wordService):
        self.__wordService = wordService
        self.__context = context

    def getById(self, adId):
        return self.__context.getAdById(adId)

    def getByTitle(self, title):
        return self.__context.getAdByTitle(title)

    def create(self, title, description, imagePath, tagsList):
        created = self._createAdWithTags(title, description, imagePath, tagsList)
        return self.__context.addAd(created)

    def update(self, adId, title, description, imagePath, tagsList):
        updated = self._createAdWithTags(title, description, imagePath, tagsList)
        return self.__context.updateAd(adId, updated)

    def _createAdWithTags(self, title, description, imagePath, tagsList):
        allSimilar = set()
        for tag in tagsList:
            similar = self.__wordService.findClosest(tag['value'])
            allSimilar.update(similar)
        return Ad(title, description, imagePath, self._tagsFromList(tagsList, True), self._tagsFromList(allSimilar))

    @staticmethod
    def _tagsFromList(tagsList, isWrapped=False):
        # ps = PorterStemmer()
        # return [Tag(ps.stem(tag['value'])) for tag in tagsList]
        if isWrapped:
            return [Tag(tag['value']) for tag in sorted(tagsList, key=lambda t: t['value'])]
        else:
            return [Tag(tag) for tag in sorted(tagsList, key=lambda t: t)]

    def remove(self, adId):
        return self.__context.removeAd(adId)

    def getByTags(self, query, maxCount=1, language='pl'):
        words = self._getMeaningfulWords(query.lower(), language)
        results = self._countMatches(words)
        if results:
            return results[:maxCount]
        else:
            return self.getAny(maxCount)

    def _countMatches(self, words):
        results = {}
        adIdToAdMapping = {}
        for word in words:
            for ad in self.__context.getAdsByTags([word]):
                if ad.id not in results:
                    results[ad.id] = 1
                    adIdToAdMapping[ad.id] = ad
                else:
                    results[ad.id] += 1
        sortedByVal = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
        return [adIdToAdMapping[adId] for adId, _ in sortedByVal]

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
