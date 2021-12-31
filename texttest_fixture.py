from gilded_rose import GildedRose, NormalItem, Sulfuras, AgedBrie, BackstagePasses, Conjured

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
             NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             AgedBrie(name="Aged Brie", sell_in=2, quality=0),
             NormalItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=32),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=32),
             Conjured(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 9
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print(f"-------- day %{day} --------")
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
