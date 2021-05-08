from Models.ad_tags import Ad, Tag
from db.base import Base, Session, engine

Base.metadata.create_all(engine)

session = Session()

tag1 = Tag("tag1")
tag2 = Tag("tag2")
tag3 = Tag("tag3")

ad1 = Ad("ad1Title", "ad1Desc", "ad1Image", [tag1, tag2])
ad2 = Ad("ad2Title", "ad2Desc", "ad2Image", [tag2, tag3])

session.add(tag1)
session.add(tag2)
session.add(tag3)
session.add(ad1)
session.add(ad2)

session.commit()
session.close()
