from db.context import Context
from services.adsService import AdsService

if __name__ == '__main__':
    context = Context()

    query = "tag2 tag1"
    service = AdsService(context)
    result = service.getByTags(query)
    print(result)
