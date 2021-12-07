class GildedRose(object):
    MAX_QUALITY = 50

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        BACKSTAGE_PASS_STRING = "Backstage passes to a TAFKAL80ETC concert"
        SULFURAS_STRING = "Sulfuras, Hand of Ragnaros"
        AGED_BRIE_STRING = "Aged Brie"
        
        for item in self.items:
            if item.name == AGED_BRIE_STRING or item.name == BACKSTAGE_PASS_STRING:
                if item.quality < self.MAX_QUALITY:
                    self.increment_quality(item)
                    if item.name == BACKSTAGE_PASS_STRING:
                        if item.sell_in < 11:
                            self.increment_quality(item)
                        if item.sell_in < 6:
                            self.increment_quality(item)
            else:
                if item.quality > 0 and item.name != SULFURAS_STRING:
                    self.decrement_quality(item)
                    #if item.name != SULFURAS_STRING:
                     #   self.decrement_quality(item)
            
            item.sell_in = item.sell_in - 1 if item.name != SULFURAS_STRING else item.sell_in
            if item.sell_in < 0:
                if item.name == AGED_BRIE_STRING:
                    self.increment_quality(item)
                else:
                    if item.name != BACKSTAGE_PASS_STRING:
                        if item.quality > 0:
                            if item.name != SULFURAS_STRING:
                                self.decrement_quality(item)
                    else:
                        item.quality = 0

    def decrement_quality(self, item):
        item.quality -= 1

    def increment_quality(self, item):
        item.quality = self.MAX_QUALITY if item.quality + 1 > self.MAX_QUALITY else item.quality + 1

    