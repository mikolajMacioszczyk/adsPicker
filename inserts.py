from db.base import Base, Session, engine
from db.context import Context
from services.adsService import AdsService
from services.wordService import WordService

Base.metadata.create_all(engine)
session = Session()

adsService = AdsService(Context(), WordService())

# american
burgerTags = [('fast-food', 'en'), ('fast', 'en'), ('burger', 'en'), ('american', 'en'), ('amerykańska', 'pl'), ('meat', 'en'), ('mięso', 'pl'), ('beef', 'en'),
              ('wołowina', 'pl'), ('loaf', 'en'), ('bułka', 'pl'), ('dinner', 'en'), ('obiad', 'pl'), ('tłuste', 'pl'), ('fat', 'en'), ('hot', 'en'), ('ciepło', 'pl')]
adsService.create('Burger', 'Burger amerykański, fast-food', 'http://127.0.0.1:5000/api/image?path=burger.jpg', [{'value': tag[0], 'lang': tag[1]} for tag in burgerTags])
burritoTags = [('fast-food', 'en'), ('fast', 'en'), ('burrito', 'en'), ('american', 'en'), ('amerykańska', 'pl'), ('tortilla', 'en'), ('naleśnik', 'pl'), ('mięso', 'pl'),
               ('meat', 'en'), ('bean', 'en'), ('fasola', 'pl'), ('dinner', 'en'), ('obiad', 'pl'), ('ostry', 'pl'), ('spicy', 'en'),  ('hot', 'en'), ('ciepło', 'pl')]
adsService.create('Buritto', 'Buritto meksykańskie - fast-food', 'http://127.0.0.1:5000/api/image?path=buritto.jpg', [{'value': tag[0], 'lang': tag[1]} for tag in burritoTags])
honeyPancakesTags = [('breakfast', 'en'), ('śniadanie', 'pl'), ('naleśnik', 'pl'), ('pancakes', 'en'), ('deser', 'pl'), ('dessert', 'en'), ('sweet', 'en'), ('słodkie', 'pl'),
                     ('przekąska', 'pl'), ('snack', 'en'), ('amerykańska', 'pl'), ('american', 'en'), ('miód', 'pl'), ('honey', 'en')]
adsService.create('Pancakes', 'Naleśniki amerykańskie z miodem - danie śniadaniowe lub deserowe', 'http://127.0.0.1:5000/api/image?path=pancakes.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in honeyPancakesTags])

# breakfast
scrambledEggsTags = [('breakfast', 'en'), ('śniadanie', 'pl'), ('fast', 'en'), ('eggs', 'en'), ('jajka', 'pl'), ('jajecznica', 'pl'), ('scrambled', 'en'),
                     ('hot', 'en'), ('ciepło', 'pl'), ('onion', 'en'), ('cebula', 'pl')]
adsService.create('Jajecznica', 'Jajecznica z patelni, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=jajecznica.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in scrambledEggsTags])
sandwichesTags = [('breakfast', 'en'), ('śniadanie', 'pl'), ('kanapki', 'pl'), ('sandwiches', 'en'), ('pieczywo', 'pl'),
                  ('bread', 'en'), ('błonnik', 'pl'), ('fiber', 'en'), ('vegan', 'en'), ('wegetariańskie', 'pl'), ('świeże', 'pl'),
                  ('fresh', 'en'), ('vegetables', 'en'), ('warzywa', 'pl'), ('pieczywo', 'pl'), ('baking', 'en')]
adsService.create('Kanapki', 'Kanaki wiosenne, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=kanapki.webp',
                  [{'value': tag[0], 'lang': tag[1]} for tag in sandwichesTags])
bananaPancakesTags = [('breakfast', 'en'), ('śniadanie', 'pl'), ('naleśniki', 'pl'), ('pancakes', 'en'), ('banan', 'pl'),
                      ('banana', 'en'), ('marmolada', 'pl'), ('marmalade', 'en'), ('sweet', 'en'), ('słodkie', 'pl'), ('vegan', 'en')]
adsService.create('Naleśniki', 'Plaski bananowe z marmoladą, danie śniadaniowe', 'http://127.0.0.1:5000/api/image?path=naleśniki.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in bananaPancakesTags])
applePieTags = [('deser', 'pl'), ('dessert', 'en'), ('apple', 'en'), ('jabłko', 'pl'), ('pie', 'en'), ('ciasto', 'pl'),
                ('ciepło', 'pl'), ('hot', 'en'), ('słodkie', 'pl'), ('sweet', 'en'), ('wypiek', 'pl'), ('baking', 'en')]
adsService.create('Szarlotka', 'Szarlotka na ciepło, danie deserowe', 'http://127.0.0.1:5000/api/image?path=szarlotka.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in applePieTags])

# italian
toscanChickenTags = [('dinner', 'en'), ('obiad', 'pl'), ('italian', 'en'), ('włoska', 'pl'), ('kurczak', 'pl'), ('chicken', 'en'),
                     ('sos', 'pl'), ('sauce', 'en'), ('meat', 'en'), ('mięso', 'pl'), ('główne', 'pl'), ('main', 'en'),
                     ('krem', 'pl'), ('creme', 'en'), ('pomidory', 'pl'), ('tomatoes', 'en'), ('hot', 'en'), ('ciepło', 'pl')]
adsService.create('Kurczak Po toskańsku', 'Kurczak po Toskańsku w sosie kremowym, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakPoToskańsku.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in toscanChickenTags])
pizzaTags = [('fast-food', 'en'), ('fast', 'en'), ('pizza', 'en'), ('włoska', 'pl'), ('italian', 'en'), ('dough', 'en'), ('ciasto', 'pl'), ('ser', 'pl'),
             ('cheese', 'en'), ('pomidory', 'pl'), ('tomatoes', 'en'), ('oliwa', 'en'), ('oil', 'en'), ('tłuste', 'pl'), ('fat', 'en'), ('hot', 'en'), ('ciepło', 'pl')]
adsService.create('Pizza', 'Pizza neapolitańska, fast-food', 'http://127.0.0.1:5000/api/image?path=pizza.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in pizzaTags])
risottoTags = [('dinner', 'en'), ('obiad', 'pl'), ('włoska', 'pl'), ('risotto', 'en'), ('italian', 'en'), ('ryż', 'pl'), ('rice', 'pl'),
               ('papryka', 'pl'), ('paprica', 'en'), ('kurczak', 'pl'), ('chicken', 'en'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Risotto', 'Risotto z kurczakiem, danie główne', 'http://127.0.0.1:5000/api/image?path=risotto.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in risottoTags])
spaghettiTags = [('dinner', 'en'), ('obiad', 'pl'), ('włoska', 'pl'), ('italian', 'en'), ('spaghetti', 'en'), ('makaron', 'pl'),
                 ('pasta', 'en'), ('główne', 'pl'), ('main', 'en'), ('ser', 'pl'), ('cheese', 'en'), ('pomidory', 'pl'),
                 ('tomatoes', 'en'), ('meat', 'en'), ('mięso', 'pl'), ('hot', 'en'), ('ciepło', 'pl')]
adsService.create('Spaghetti', 'Spaghetti bolognese, danie główne', 'http://127.0.0.1:5000/api/image?path=spagetti.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in spaghettiTags])

# oriental
koreanChickenTags = [('oriental', 'en'), ('orientalna', 'pl'), ('chicken', 'en'), ('kurczak', 'pl'), ('meat', 'en'), ('mięso', 'pl'),
                     ('dinner', 'en'), ('obiad', 'pl'), ('ostry', 'pl'), ('spicy', 'en'), ('sauce', 'en'), ('sos', 'pl'),
                     ('hot', 'en'), ('ciepło', 'pl'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Kurczak po koreańsku', 'Kurczak po koreańsku na ostro, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakKoreansku.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in koreanChickenTags])
vietnamChickenTags = [('oriental', 'en'), ('orientalna', 'pl'), ('chicken', 'en'), ('kurczak', 'pl'), ('meat', 'en'), ('mięso', 'pl'),
                      ('dinner', 'en'), ('obiad', 'pl'), ('paprica', 'en'), ('papryka', 'pl'), ('ostry', 'pl'), ('spicy', 'en'),
                      ('hot', 'en'), ('ciepło', 'pl'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Kurczak po wietnamsku', 'Kurczak po wietnamsku w pięciu smakach, danie główne', 'http://127.0.0.1:5000/api/image?path=kurczakWietnamski.webp',
                  [{'value': tag[0], 'lang': tag[1]} for tag in vietnamChickenTags])
sushiTags = [('oriental', 'en'), ('orientalna', 'pl'), ('ryba', 'pl'), ('fish', 'en'), ('raw', 'en'), ('surowa', 'pl'),
             ('ryż', 'pl'), ('rice', 'en'), ('fast-food', 'en'), ('fast', 'en'), ('łosoś', 'pl'), ('salmon', 'en'),
             ('cold', 'en'), ('zimno', 'pl'), ('przekąska', 'pl'), ('snack', 'en')]
adsService.create('Sushi', 'Sushi z łososia, fast-food', 'http://127.0.0.1:5000/api/image?path=sushi.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in sushiTags])

#polish
bigosTags = [('polish', 'en'), ('dinner', 'en'), ('obiad', 'pl'), ('kurczak', 'pl'), ('kapusta', 'pl'), ('cabbage', 'en'), ('mięso', 'pl'),
             ('meat', 'en'), ('grzyby', 'pl'), ('mushrooms', 'en'), ('hot', 'en'), ('ciepło', 'pl'), ('appetizer', 'en'), ('przystawka', 'pl')]
adsService.create('Bigos', 'Bigos polski, danie główne', 'http://127.0.0.1:5000/api/image?path=bigos.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in bigosTags])
bunTags = [('polish', 'en'), ('polski', 'pl'), ('drożdżówka', 'pl'), ('bun', 'en'), ('sweet', 'en'), ('słodkie', 'pl'),
           ('mak', 'pl'), ('poppy', 'en'), ('pieczywo', 'pl'), ('baking', 'en'), ('deser', 'pl'), ('dessert', 'en'),
           ('cold', 'en'), ('zimno', 'pl'), ('przekąska', 'pl'), ('snack', 'en')]
adsService.create('Drożdżówka', 'drożdżówka z makiem, danie deserowe', 'http://127.0.0.1:5000/api/image?path=drozdzowka.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in bunTags])
hoovesTags = [('polish', 'en'), ('polski', 'pl'), ('kopytka', 'pl'), ('hooves', 'en'), ('dinner', 'en'), ('obiad', 'pl'), ('kluski', 'pl'),
              ('noodles', 'en'), ('tłuste', 'pl'), ('fat', 'en'), ('hot', 'en'), ('ciepło', 'pl'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Kopytka', 'Kopytka ze skwarkami, danie główne', 'http://127.0.0.1:5000/api/image?path=kopytka.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in hoovesTags])
dumplingsTags = [('polish', 'en'), ('polski', 'pl'), ('pierogi', 'pl'), ('ruskie', 'pl'), ('dumplings', 'en'), ('ser', 'pl'),
                 ('cheese', 'en'), ('ziemniaki', 'pl'), ('potatoes', 'en'), ('dinner', 'en'), ('obiad', 'pl'), ('hot', 'en'),
                 ('ciepło', 'pl'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Pierogi ruskie', 'Pierogi ruskie, danie główne', 'http://127.0.0.1:5000/api/image?path=pierogi.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in dumplingsTags])
porkChopTags = [('polish', 'en'), ('polski', 'pl'), ('schabowy', 'pl'), ('kotlet', 'en'), ('pork', 'en'), ('chop', 'en'),
                ('meat', 'en'), ('mięso', 'pl'), ('wieprzowina', 'pl'), ('dinner', 'en'), ('obiad', 'pl'), ('hot', 'en'),
                ('ciepło', 'pl'), ('główne', 'pl'), ('main', 'en')]
adsService.create('Kotlet schabowy', 'Kotlet schabowy, danie główne', 'http://127.0.0.1:5000/api/image?path=schabowy.jpg',
                  [{'value': tag[0], 'lang': tag[1]} for tag in porkChopTags])

session.close()
