from abc import ABC, abstractmethod


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class BaseItem(ABC):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

    @abstractmethod
    def update_quality(self):
        pass


class Item(BaseItem):
    def update_quality(self):
        pass


class NormalItem(BaseItem):

    def update_quality(self) -> None:
        cls = self.__class__
        if cls.MIN_QUALITY <= self.quality <= cls.MAX_QUALITY:
            quality = self.quality - 1 if self.sell_in > 0 else self.quality - 2
            self.quality = max(quality, cls.MIN_QUALITY)
        self.sell_in -= 1


class AgedBrie(BaseItem):

    def update_quality(self):
        cls = self.__class__
        if cls.MIN_QUALITY <= self.quality <= cls.MAX_QUALITY:
            quality = self.quality + 1 if self.sell_in > 0 else self.quality + 2
            self.quality = min(cls.MAX_QUALITY, quality)
        self.sell_in -= 1


class Sulfuras(BaseItem):
    MAX_QUALITY = 80
    MIN_QUALITY = 80

    def update_quality(self):
        pass


class BackstagePasses(BaseItem):

    def update_quality(self):
        cls = self.__class__
        if cls.MIN_QUALITY <= self.quality <= cls.MAX_QUALITY:
            if self.sell_in <= 0:
                self.quality = 0
            else:
                quality = self.quality + 3 if 0 <= self.sell_in <= 5 else \
                    self.quality + 2 if 5 < self.sell_in <= 10 else self.quality + 1
                self.quality = min(cls.MAX_QUALITY, quality)
        self.sell_in -= 1


class Conjured(BaseItem):

    def update_quality(self):
        cls = self.__class__
        if cls.MIN_QUALITY <= self.quality <= cls.MAX_QUALITY:
            quality = self.quality - 2 if self.sell_in > 0 else self.quality - 4
            self.quality = max(quality, cls.MIN_QUALITY)
        self.sell_in -= 1
