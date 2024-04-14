class Hotel:
    price_of_room = {}
    nums = []
    types = []
    max_ppls = []
    comforts = []
    booked_dates = []
    price_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort_price = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    food_price = {'без питания': 0, 'завтрак': 280, 'полумансион': 1000}

    def __init__(self, ptr):
        ptr = ptr.split()
        self.num = int(ptr[0])
        self.type = ptr[1]
        self.max_ppl = int(ptr[2])
        self.comfort = ptr[3]
        Hotel.nums.append(self.num)
        Hotel.types.append(self.type)
        Hotel.max_ppls.append(self.max_ppl)
        Hotel.comforts.append(self.comfort)
        Hotel.booked_dates.append([])
        Hotel.price_of_room[self.num] = Hotel.price_type[self.type] * self.max_ppl * Hotel.comfort_price[self.comfort]


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
    def placing_people(self):
        option = []
        prices_of_options = {}
        for i in Hotel.max_ppls:
            if i == self.pl:
                option.apppend(Hotel.max_ppls.index(i)+1)
        if not option:
            for number in option:
                prices_of_options[number] = Hotel.price_of_room[number]
            prices_of_options = sorted(prices_of_options.items(),key=lambda x: x[1])







with open('booking.txt', encoding='utf-8') as f:
    for n in f:
        Clients(n)

print(Hotel.price_of_room)