from Models.ad import Ad
from Models.tag import Tag
from db.base import Base, Session, engine

Base.metadata.create_all(engine)

session = Session()

shapeTag = Tag("shape")
rectangleTag = Tag("rectangle")
circleTag = Tag("circle")
squareTag = Tag("square")

blueTag = Tag("blue")
redTag = Tag("red")
greenTag = Tag("green")

ad1 = Ad("red", "rectangle", "rectangle.png", [shapeTag, rectangleTag, redTag])
ad2 = Ad("blue", "circle", "circle.png", [shapeTag, circleTag, blueTag])
ad3 = Ad("green", "square", "square.png", [shapeTag, rectangleTag, squareTag, greenTag])

session.add(shapeTag)
session.add(rectangleTag)
session.add(circleTag)
session.add(squareTag)
session.add(blueTag)
session.add(redTag)
session.add(greenTag)
session.add(ad1)
session.add(ad2)
session.add(ad3)

session.commit()
session.close()
