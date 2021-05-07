from Models import Ad, Tag
from db.context import Context

if __name__ == '__main__':
    context = Context()

    ads = context.getAdsByTag('tag2')
    for ad in ads:
        print(ad)
