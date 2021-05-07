from Models import Ad, Tag
from db.context import Context

tag1 = Tag("first")
tag2 = Tag("second")
ad1 = Ad('ad1', 'ad1Desc', 'ad1Path', [tag1, tag2])

print("Id przed: ", ad1.id)

context = Context()
context.addAd(ad1)

print("Id po: ", ad1.id)
print("z bazy: ", context.getAd(ad1.id))