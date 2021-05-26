from Models.ad import Ad
from Models.tag import Tag
from Models.ad_tags import ad_tags_association, hidden_ad_tags_association
from db.base import Base, Session, engine
from sqlalchemy import exc


class Context:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def getAdById(self, adId):
        return self.session.query(Ad).get(adId)

    def getAdByTitle(self, title):
        return self.session.query(Ad).filter_by(title=title).one_or_none()

    def getAdsByTags(self, tags):
        return self.session.query(Ad).filter(Ad.hiddenTags.any(Tag.value.in_(tags))).all()

    def addAd(self, ad):
        self._adTags(ad)
        try:
            self.session.commit()
            self.session.add(ad)
            self.session.commit()
            return ad
        except exc.SQLAlchemyError:
            print("Context: cannot create ad: ", ad)
            return None

    def getAds(self, limit, offset=0):
        return self.session.query(Ad).limit(limit).offset(offset).all()

    def updateAd(self, adId, updated):
        fromDb = self.getAdById(adId)
        if fromDb is None:
            return None
        self._removeTags(fromDb)
        self._adTags(updated)
        try:
            fromDb.update(updated)
            self.session.commit()
            return fromDb
        except exc.SQLAlchemyError:
            print("Context: cannot remove ad: ", fromDb)
            return None

    def _adTags(self, ad):
        try:
            for tag in ad.tags:
                self.session.add(tag)
        except exc.SQLAlchemyError:
            print("Context: cannot add hidden tags: ", ad.tags)
            return None
        try:
            for tag in ad.hiddenTags:
                self.session.add(tag)
        except exc.SQLAlchemyError:
            print("Context: cannot add hidden tags: ", ad.hiddenTags)

    def _removeTags(self, ad):
        try:
            for tag in ad.tags:
                self.session.query(ad_tags_association).filter_by(tag_id=tag.id).delete()
                self.session.delete(tag)
                self.session.commit()
        except exc.SQLAlchemyError:
            print("Context: cannot delete tags: ", ad.tags)
            return None
        try:
            for tag in ad.hiddenTags:
                self.session.query(hidden_ad_tags_association).filter_by(tag_id=tag.id).delete()
                self.session.delete(tag)
                self.session.commit()
        except exc.SQLAlchemyError:
            print("Context: cannot delete hidden tags: ", ad.hiddenTags)

    def removeAd(self, adId):
        fromDb = self.getAdById(adId)
        if fromDb is None:
            return False
        self._removeTags(fromDb)
        try:
            self.session.commit()
            self.session.delete(fromDb)
            self.session.commit()
            return True
        except exc.SQLAlchemyError:
            print("Context: cannot delete ad: ", fromDb)
            return False

    def getTagById(self, tagId):
        return self.session.query(Tag).get(tagId)

    def getTagByValue(self, value):
        return self.session.query(Tag).filter_by(value=value).first()

    def addTag(self, tag):
        self.session.add(tag)
        self.session.commit()

    def __del__(self):
        try:
            self.session.close()
        except AttributeError as err:
            print(err)
