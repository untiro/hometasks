class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        print(self.name, self.sell_in, self.quality)

    def upd(self, chsell_in, chquality, flag):
        self.sell_in += chsell_in

        self.quality += chquality

        if self.quality > 50 and chquality > 0 and 'backstage passes' not in self.name.lower():
            self.quality = 50

        if 'backstage passes' in self.name.lower() and (self.quality - chquality) <= 50 and self.quality > 50:
            self.quality = 50

        if 'backstage passes' in self.name.lower() and self.quality < 50 and self.sell_in == 10:
            self.quality += 1
        elif 'backstage passes' in self.name.lower() and self.quality < 50 and self.sell_in == 5:
            self.quality += 1
        if self.quality < 0:
            self.quality = 0
        print(self.name, self.sell_in, self.quality, flag)


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
            items[i].upd(-1, 1, '1')
        elif 'Aged Brie' in items[i].name and items[i].quality >= 50:
            items[i].upd(-1, 0, '2')
        elif 'Sulfuras' in items[i].name:
            pass  # items[i].upd(0, 0)
        elif 'backstage passes' in items[i].name.lower():
            if items[i].sell_in <= 1:
                items[i].quality = 0
                items[i].upd(-1, 0, '3')
            elif 5 < items[i].sell_in <= 10:
                items[i].upd(-1, 2, '4')
            elif items[i].sell_in <= 5:
                items[i].upd(-1, 3, '5')
            else:
                items[i].upd(-1, 1, '6')
        elif 'Conjured' in items[i].name:
            if items[i].sell_in <= 0:
                items[i].upd(-1, -4, '7')
            else:
                items[i].upd(-1, -2, '8')
        else:
            if items[i].sell_in <= 0:
                items[i].upd(-1, -2, '9')
            else:
                items[i].upd(-1, -1, '10')