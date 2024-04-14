class Hotel:
    nums = []
    types = []
    max_ppls = []
    comforts = []
    price_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort_price = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    food_price = {'без питания': 0, 'завтрак': 280, 'полумансион': 1000}

    def __init__(self, ptr):
        ptr = ptr.split()
        self.num = ptr[0]
        self.type = ptr[1]
        self.max_ppl = ptr[2]
        self.comfort = ptr[3]
        Hotel.nums.append(self.num)
        Hotel.types.append(self.type)
        Hotel.max_ppls.append(self.max_ppl)
        Hotel.comforts.append(self.comfort)



with open('fund.txt', encoding='utf-8') as f:
    for n in f:
        Hotel(n)


