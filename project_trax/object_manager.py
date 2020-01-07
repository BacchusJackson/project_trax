from project_trax.objects.coin_purse import CoinPurse
from project_trax.objects.hero import DefaultHero

import click


class ObjectManager():
    object_types = {}

    def __init__(self):
        self.object_types['coin purse'] = CoinPurse
        self.object_types['hero'] = DefaultHero
        self.objects = {}
        self.heros = {}

    def add(self, object_type):
        obj = self.object_types.get(object_type.lower())
        if not bool(obj):
            raise KeyError
        new_obj = obj()
        if isinstance(new_obj, DefaultHero):
            self.heros[new_obj.name] = new_obj
        return new_obj
        
