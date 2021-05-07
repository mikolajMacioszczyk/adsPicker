from Models import Ad, Tag, ad_tags_association
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
                ad.tags[i].unUse()
                ad.tags[i] = fromDb
                fromDb.use()
        self.session.commit()
        self.session.add(ad)
        self.session.commit()

    def updateAd(self, adId, updated):
        fromDb = self.getAdById(adId)
        if fromDb is None:
            return None
        fromDb.update(updated)
        for i in range(0, len(fromDb.tags)):
            self.updateAd(fromDb, i)
        self.session.commit()
        return fromDb

    def _updateTag(self, ad, index):
        tag = ad.tags[index]
        tagFromDb = self.getTagByValue(tag.value)
        if tagFromDb is None:
            self.session.add(tag)
        else:
            ad.tags[index].unUse()
            ad.tags[index] = tagFromDb
            tagFromDb.use()

    def removeAd(self, adId):
        fromDb = self.getAdById(adId)
        if fromDb is None:
            return False
        for tag in fromDb.tags:
            self._unhookTag(tag)
        self.session.commit()
        self.session.delete(fromDb)
        self.session.commit()
        return True

    def _unhookTag(self, tag):
        tag.unUse()
        if tag.useCount == 0:
            self.session.query(ad_tags_association).filter(tag_id=tag.id).delete()
            self.session.commit()
            self.session.delete(tag)

    def getTagById(self, tagId):
        return self.session.query(Tag).get(tagId)

    def getTagByValue(self, value):
        return self.session.query(Tag).filter_by(value=value).one_or_none()

    def addTag(self, tag):
        self.session.add(tag)
        self.session.commit()

    def __del__(self):
        self.session.close()

