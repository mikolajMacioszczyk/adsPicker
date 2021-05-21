from Models.ad import Ad
from Models.tag import Tag
from spacy.lang.pl import Polish
from spacy.lang.en import English
import stanza
import re

SIMILAR_COUNT = 5


class AdsService:
    def __init__(self, context, wordService):
        self.__wordService = wordService
        self.__context = context
        stanza.download('en')
        stanza.download('pl')
        self.stanza_en = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
        self.stanza_pl = stanza.Pipeline(lang='pl', processors='tokenize,mwt,pos,lemma')

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
            value = self._lematize(tag['value'], tag['lang'])
            similar = self.__wordService.findClosest(value)
            allSimilar.update(similar)
        return Ad(title, description, imagePath, self._tagsFromList(tagsList, True), self._tagsFromList(allSimilar))

    def _lematize(self, text, lang):
        if lang == 'pl':
            stanza_nlp = self.stanza_pl
        elif lang == 'en':
            stanza_nlp = self.stanza_en
        else:
            raise ValueError(f'unsupported language {lang}')
        doc = stanza_nlp(text)
        lemmatized = [word.lemma for sent in doc.sentences for word in sent.words]
        return re.sub(r'[^\w\s]', '', ' '.join(lemmatized))

    @staticmethod
    def _tagsFromList(tagsList, isWrapped=False):
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

    def _getMeaningfulWords(self, query, language):
        if language == 'pl':
            nlp = Polish()
        elif language == 'en':
            nlp = English()
        else:
            raise ValueError(f'unsupported language {language}')

        query = self._lematize(query, language)

        token_list = [token.text for token in nlp(query)]
        filtered_query = []
        for word in token_list:
            lexeme = nlp.vocab[word]
            if not lexeme.is_stop:
                filtered_query.append(word)
        return filtered_query

    def getAny(self, maxCount=1):
        result = self.__context.getAds(maxCount)
        if len(result) > 0:
            return result[:maxCount]
        return []
