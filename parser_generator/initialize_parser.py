from .game import Game
from .service import Service


def get_price(game): 
    game = Game(game).output()

    # Original stores -----------------------------------------------
    # Epicgames has a great API but, but they also have perfectly configured get request routes, so I do through them 
    epicgames = Service('https://www.epicgames.com/store/en-US/product/{}/home', game, '-', 'div', 'css-qh9qd6')
    playstationstore = Service('https://store.playstation.com/ru-ru/search/{}', game, '%20', 'span', 'price')
    microsoftstore = Service('https://www.microsoft.com/ru-ru/search?q={}', game, '+', 'div', 'c-price')
    #Doesnt work yet
    try:
        uplay = Service('https://store.ubi.com/ru/search?cgid={}-all-games'.format(game), game, '-', 'span', 'price-sales standard-price')
    except:
        uplay = Service('https://store.ubi.com/ru/search?cgid=', game, '-', 'span', 'price-sales standard-price')
    # Steam also has an excellent api but also have a perfect get requests XD
    steam = Service('https://store.steampowered.com/search/?term={}', game, '+', 'div', 'col search_price discounted responsive_secondrow')



    # Custom stores -------------------------------------------------
    steampay = Service('https://steampay.com/game/{}', game, '-', 'div', 'product__current-price')
    gabestore = Service('https://gabestore.ru/game/{}', game, '-', 'div', 'b-card__price-currentprice')
    icegames = Service('https://icegames.store/goods/?s={}', game, '+', 'div', 'price wmr')
    gamefarm = Service('https://gamefarm.ru/buy/{}', game, '%20', 'span', 'price_count price_in_list')
    steambuy = Service('https://steambuy.com/catalog/?q={}', game, '-', 'div', 'product-item__cost')

    prices = {
        'epicgames': epicgames.output(),
        'playstationstore': playstationstore.output(),
        'microsoftstore': microsoftstore.output(),
        'steam': steam.output(),
        # ---------------------------
        'steampay': steampay.output(), 
        'gabestore': gabestore.output(),
        'icegames': icegames.output(),
        'gamefarm': gamefarm.output(),
        'steambuy': steambuy.output()
        }

    return prices


