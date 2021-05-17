from db.base import Base, Session, engine
from db.context import Context
from services.adsService import AdsService

Base.metadata.create_all(engine)

session = Session()
adsService = AdsService(Context())

# american
burgerTags = ['fast-food', 'burger', 'american', 'amerykańska', 'meat', 'mięso', 'beef', 'wołowina', 'loaf', 'bułka', 'dinner', 'obiad', 'tłuste', 'fat']
adsService.create('Burger', 'Burger amerykański, fast-food', 'http://127.0.0.1:5000/api/image?path=burger.jpg', [{'value': tag} for tag in burgerTags])
burritoTags = ['fast-food', 'burrito', 'american', 'amerykańska', 'tortilla', 'naleśnik', 'mięso', 'meat', 'bean', 'fasola', 'dinner', 'obiad', 'ostry', 'spicy']
adsService.create('Buritto', 'Buritto meksykańskie - fast-food', 'http://127.0.0.1:5000/api/image?path=buritto.jpg', [{'value': tag} for tag in burritoTags])
honeyPancakesTags = ['breakfast', 'śniadanie', 'naleśnik', 'pancakes', 'deser', 'dessert', 'sweet', 'słodkie', 'amerykańska', 'american', 'miód', 'honey']
adsService.create('Pancakes', 'Naleśniki amerykańskie z miodem - danie śniadaniowe lub deserowe', 'http://127.0.0.1:5000/api/image?path=pancakes.jpg', [{'value': tag} for tag in honeyPancakesTags])

# breakfast
scrambledEggsTags = ['breakfast', 'śniadanie', 'eggs', 'jajka', 'jajecznica', 'scrambled']
adsService.create('Jajecznica', 'Jajecznica z patelni, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=jajecznica.jpg', [{'value': tag} for tag in scrambledEggsTags])
sandwichesTags = ['breakfast', 'śniadanie', 'kanapki', 'sandwiches', 'pieczywo', 'bread', 'błonnik', 'fiber', 'świeże', 'fresh', 'pieczywo', 'baking']
adsService.create('Kanapki', 'Kanaki wiosenne, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=kanapki.jpg', [{'value': tag} for tag in sandwichesTags])
bananaPancakesTags = ['breakfast', 'śniadanie', 'naleśniki', 'pancakes', 'banan', 'banana', 'marmolada', 'marmalade', 'sweet', 'słodkie']
adsService.create('Naleśniki', 'Plaski bananowe z marmoladą, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=naleśniki.jpg', [{'value': tag} for tag in bananaPancakesTags])

# italian
toscanChickenTags = ['dinner', 'obiad', 'italian', 'włoska', 'kurczak', 'chicken', 'sos', 'sauce', 'meat', 'mięso', 'krem', 'creme', 'pomidory', 'tomatoes']
adsService.create('Kurczak Po toskańsku', 'Kurczak po Toskańsku w sosie kremowym, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakPoToskańsku.jpg', [{'value': tag} for tag in toscanChickenTags])
pizzaTags = ['fast-food', 'pizza', 'włoska', 'italian', 'dough', 'ciasto', 'ser', 'cheese', 'pomidory', 'tomatoes', 'oliwa', 'oil', 'tłuste', 'fat']
adsService.create('Pizza', 'Pizza neapolitańska, fast-food', 'http://127.0.0.1:5000/api/image?path=pizza.jpg', [{'value': tag} for tag in pizzaTags])
risottoTags = ['dinner', 'obiad', 'włoska', 'risotto', 'italian', 'ryż', 'rice', 'papryka', 'paprica', 'kurczak', 'chicken']
adsService.create('Risotto', 'Risotto z kurczakiem, danie główne', 'http://127.0.0.1:5000/api/image?path=risotto.jpg', [{'value': tag} for tag in risottoTags])
spaghettiTags = ['dinner', 'obiad', 'włoska', 'italian', 'spaghetti', 'spagetti', 'makaron', 'pasta', 'ser', 'cheese', 'pomidory', 'tomatoes', 'meat', 'mięso']
adsService.create('Spaghetti', 'Spaghetti bolognese, danie główne', 'http://127.0.0.1:5000/api/image?path=spagetti.jpg', [{'value': tag} for tag in spaghettiTags])

# oriental
koreanChickenTags = ['oriental', 'orientalna', 'chicken', 'kurczak', 'meat', 'mięso', 'dinner', 'obiad', 'ostry', 'spicy', 'sauce', 'sos']
adsService.create('Kurczak po koreańsku', 'Kurczak po koreańsku na ostro, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakKoreansku.jpg', [{'value': tag} for tag in koreanChickenTags])
vietnamChickenTags = ['oriental', 'orientalna', 'chicken', 'kurczak', 'meat', 'mięso', 'dinner', 'obiad', 'paprica', 'papryka', 'ostry', 'spicy', 'sweet', 'słodki']
adsService.create('Kurczak po wietnamsku', 'Kurczak po wietnamsku w pięciu smakach, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakWietnamski.webp', [{'value': tag} for tag in vietnamChickenTags])
sushiTags = ['oriental', 'orientalna', 'ryba', 'fish', 'raw', 'surowa', 'ryż', 'rice', 'fast-food', 'łosoś', 'salmon']
adsService.create('Sushi', 'Sushi z łososia, fast-food', 'http://127.0.0.1:5000/api/image?path=sushi.jpg', [{'value': tag} for tag in sushiTags])

#polish
bigosTags = ['polish', 'dinner', 'obiad', 'kurczak', 'kapusta', 'cabbage', 'mięso', 'mean', 'grzyby', 'mushrooms']
adsService.create('Bigos', 'Bigos polski, danie główne', 'http://127.0.0.1:5000/api/image?path=bigos.jpg', [{'value': tag} for tag in bigosTags])
bunTags = ['polish', 'drożdżówka', 'bun', 'sweet', 'słodkie', 'mak', 'poppy', 'pieczywo', 'baking', 'deser', 'dessert']
adsService.create('Drożdżówka', 'drożdżówka z makiem, danie deserowe', 'http://127.0.0.1:5000/api/image?path=drozdzowka.jpg', [{'value': tag} for tag in bunTags])
hoovesTags = ['polish', 'kopytka', 'hooves', 'dinner', 'obiad', 'kluski', 'noodles', 'tłuste', 'fat']
adsService.create('Kopytka', 'Kopytka ze skwarkami, danie główne', 'http://127.0.0.1:5000/api/image?path=kopytka.jpg', [{'value': tag} for tag in hoovesTags])
dumplingsTags = ['polish', 'pierogi', 'ruskie', 'dumplings', 'ser', 'cheese', 'zmiemniaki', 'potatoes', 'dinner', 'obiad']
adsService.create('Pierogi ruskie', 'Pierogi ruskie, danie główne', 'http://127.0.0.1:5000/api/image?path=pierogi.jpg', [{'value': tag} for tag in dumplingsTags])
porkChopTags = ['polish', 'schabowy', 'kotlet', 'pork', 'chop', 'meat', 'mięso', 'wieprzowina', 'dinner', 'obiad']
adsService.create('Kotlet schabowy', 'Kotlet schabowy, danie główne', 'http://127.0.0.1:5000/api/image?path=schabowy.jpg', [{'value': tag} for tag in porkChopTags])

session.close()
