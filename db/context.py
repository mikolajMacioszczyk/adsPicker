from Models import Ad, Tag
from base import Base, Session, engine


class Context:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def getAd(self, adId):
        return self.session.query(Ad).get(adId)

    def addAd(self, ad):
        for tag in ad.tags:
            self.session.add(tag)
        self.session.commit()
        self.session.add(ad)
        self.session.commit()

    def getTag(self, tagId):
        return self.session.query(Tag).get(tagId)

    def __del__(self):
        self.session.close()

