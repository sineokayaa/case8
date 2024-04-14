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

class Clients:
    names = []
    data_books = []
    pls = []
    data_arrs = []
    days = []
    sums = []

    def __init__(self, ptr):
        ptr = ptr.split()
        self.data_book = ptr[0]
        self.name = ptr[1] + ' ' + ptr[2] + ' ' + ptr[3]
        self.pl = ptr[4]
        self.data_arr = ptr[5]
        self.days = ptr[6]
        self.sum = ptr[7]
        Clients.data_books.append(self.data_book)
        Clients.names.append(self.name)
        Clients.pls.append(self.pl)
        Clients.data_arrs.append(self.data_arr)
        Clients.days.append(self.days)
        Clients.sums.append(self.sum)


with open('booking.txt', encoding='utf-8') as f:
    for n in f:
        Clients(n)
print(Clients.data_arrs)

