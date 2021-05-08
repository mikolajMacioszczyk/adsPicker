from Models import Ad, Tag
from db.context import Context
from services.adsService import AdsService

if __name__ == '__main__':
    context = Context()

    query = "Jakiś mój przykładowy tekst, który ma sprawdzić"
    service = AdsService(context)
    result = service.getByTags(query)
    print(result)
    # ads = context.getAdsByTag('tag2')
    # for ad in ads:
    #     print(ad)
