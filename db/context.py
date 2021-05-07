from Models import Ad, Tag
from base import Base, Session, engine


class Context:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def getAdById(self, adId):
        return self.session.query(Ad).get(adId)

    def getAdByTitle(self, title):
        return self.session.query(Tag).filter_by(title=title).one_or_none()

    def addAd(self, ad):
        for i in range(0, len(ad.tags)):
            tag = ad.tags[i]
            fromDb = self.getTagByValue(tag.value)
            if fromDb is None:
                self.session.add(tag)
            else:
                ad.tags[i] = fromDb
        self.session.commit()
        self.session.add(ad)
        self.session.commit()

    def getTagById(self, tagId):
        return self.session.query(Tag).get(tagId)

    def getTagByValue(self, value):
        return self.session.query(Tag).filter_by(value=value).one_or_none()

    def addTag(self, tag):
        self.session.add(tag)
        self.session.commit()

    def __del__(self):
        self.session.close()

