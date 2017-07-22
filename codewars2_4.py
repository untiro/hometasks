class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def upd(self, chsell_in, chquality):
        self.sell_in += chsell_in
        self.quality += chquality
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50 and "Aged Brie" not in self.name:
            self.quality = 50


items = []

items += [Item('+5 Dexterity Vest', 10, 20)]
items += [Item('Aged Brie', 2, 0)]
items += [Item('Elixir of the Mongoose', 5, 7)]
items += [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items += [Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items += [Item('Conjured Mana Cake', 3, 6)]


def update_quality():
    for i in range(len(items)):
        if 'Aged Brie' in items[i].name and items[i].quality < 50:
            items[i].upd(-1, 1)
        elif 'Aged Brie' in items[i].name and items[i].quality >= 50:
            items[i].upd(-1, 0)
        elif 'Sulfuras' in items[i].name:
            pass  # items[i].upd(0, 0)
        elif 'backstage passes' in items[i].name.lower():
            if items[i].sell_in <= 0:
                items[i].quality = 0
                items[i].upd(-1, 0)
            elif 5 < items[i].sell_in <= 10:
                items[i].upd(-1, 2)
            elif items[i].sell_in <= 5:
                items[i].upd(-1, 3)
            else:
                items[i].upd(-1, 1)
        elif 'Conjured' in items[i].name:
            if items[i].sell_in < 0:
                items[i].upd(-1, -4)
            else:
                items[i].upd(-1, -2)
        else:
            if items[i].sell_in < 0:
                items[i].upd(-1, -2)
            else:
                items[i].upd(-1, -1)


'''
def update_quality():
    for i in range(len(items)):    
        if 'Aged Brie' in items[i].name and items[i].quality:
        and 'backstage passes' in items[i].name.lower():
            if items[i].quality>0:
                if items[i].name!='Sulfuras, Hand of Ragnaros':
                    items[i].quality=items[i].quality - 1
        else:
            if items[i].quality<50:
                items[i].quality=items[i].quality + 1
                if items[i].name=='Backstage passes to a TAFKAL80ETC concert':
                    if items[i].sell_in<11:
                        if items[i].quality<50:
                            items[i].quality=items[i].quality + 1
                    if items[i].sell_in<6:
                        if items[i].quality<50:
                            items[i].quality = items[i].quality + 1
        if items[i].name != 'Sulfuras, Hand of Ragnaros':
            items[i].sell_in = items[i].sell_in - 1
        if items[i].sell_in<0:
            if items[i].name!='Aged Brie':
                if items[i].name!='Backstage passes to a TAFKAL80ETC concert':
                    if items[i].quality>0:
                        if items[i].name !='Sulfuras, Hand of Ragnaros':
                            items[i].quality=items[i].quality - 1
                else:
                    items[i].quality = items[i].quality - items[i].quality
            else:
                if items[i].quality < 50:
                    items[i].quality=items[i].quality + 1
                    '''