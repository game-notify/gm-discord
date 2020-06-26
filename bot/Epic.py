import os
import requests

class Epic:
    def __init__(self, *args, **kwargs):
        self.url=os.getenv('EPIC_GAMES_API')
        self.product_url = 'https://www.epicgames.com/store/de/product/'
        self.offers=[]

    def get_offer_data(self):
        return requests.get(self.url).json()['data']['Catalog']['searchStore']['elements']

    def get_offers(self):
        for offer in self.get_offer_data():
            url = self.product_url+offer['productSlug']
            new_price = offer['price']['totalPrice']['fmtPrice']['intermediatePrice']
            if new_price == '0' : new_price+=',00 €'
            self.offers.append({
                'title': offer['title'],
                'description': offer['description'],
                'orgPrice': offer['price']['totalPrice']['fmtPrice']['originalPrice'],
                'newPrice': new_price,
                'url': url,
            })
        return self.offers
