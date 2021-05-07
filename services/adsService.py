from Models import Ad


class AdsService:

    def __init__(self, context):
        self.context = context

    def getByTags(self, tags):
        # TODO: Search by tags
        pass

    def getAny(self):
        result = self.context.getAds(1)
        if len(result) > 0:
            return result[0]
        return Ad.default()

