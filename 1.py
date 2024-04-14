import random


class Hotel:
    price_of_room = {}
    nums = []
    types = []
    max_ppls = {}
    comforts = []
    booked_dates = []
    price_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort_price = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    food_price = {'полупансион': 1000, 'завтрак': 280, 'без питания': 0}

    def __init__(self, ptr):
        ptr = ptr.split()
        self.num = int(ptr[0])
        self.type = ptr[1]
        self.max_ppl = int(ptr[2])
        self.comfort = ptr[3]
        Hotel.nums.append(self.num)
        Hotel.types.append(self.type)
        Hotel.max_ppls[self.num] = self.max_ppl
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

    def need_dates(self):
        need_dates = []
        first_data = self.data_arr.split('.')
        for i in range(int(self.days)):
            if int(first_data[0]) + int(i) <= 9:
                new_data = '0' + str(int(first_data[0]) + int(i)) + '.' + first_data[1] + '.' + first_data[2]
            else:
                new_data = str(int(first_data[0]) + int(i)) + '.' + first_data[1] + '.' + first_data[2]
            need_dates.append(new_data)
        return need_dates

    def placing_people(self):
        option = []
        prices_of_options = {}
        summ_of_room = 0
        summ_of_food = 0
        number_chosen = 0
        food_chosen = ''
        need_dates = Clients.need_dates(self)
        print(need_dates)
        for i in Hotel.max_ppls:
            if str(i) == self.pl:
                #print(need_dates)
                #print(Hotel.booked_dates[Hotel.max_ppls.index(i)])
                print(f'aaaa {Hotel.booked_dates[Hotel.max_ppls[i]-1]}')
                if set(need_dates) & set(Hotel.booked_dates[Hotel.max_ppls[i]-1]) == set():
                    option.append(Hotel.max_ppls[i] + 1)
        print(option)
        if not option:  # в опшн у нас номера комнат,совпадающих по вместимости с нужной нам!
            for number in option:
                prices_of_options[number] = Hotel.price_of_room[number]  # соединяем номер с его ценой
            prices_of_options = dict(
                sorted(prices_of_options.items(), key=lambda x: x[1], reverse=True))  # сначала самые дорогие номера
            #print(prices_of_options)
            for room in prices_of_options:
                if prices_of_options[room] <= int(self.sum) * int(self.pl):
                    number_chosen = room
                    summ_of_room = prices_of_options[room] * int(self.pl)
                    summ_of_food = int(self.sum) * int(self.pl) - summ_of_room
                    for j in Hotel.food_price:
                        if summ_of_food < Hotel.food_price[j] * int(self.pl):
                            continue
                        else:
                            food_chosen = j
                            break
                    print(
                        f'{self.name}, мы можем вам предложить следующий вариант: Номер комнаты: {number_chosen}, '
                        f'Степень комфортности: {Hotel.comforts[number_chosen - 1]}, Вид питания: {food_chosen}')
                    answer = random.choices(['Да', 'Нет'], weights=[75, 25])
                    if answer == 'Да':
                        Hotel.booked_dates[room - 1].append(need_dates)
                    else:
                        continue
                else:
                    continue
            if number_chosen == 0:
                print('Не можем вас заселить')
        else:
            for i in Hotel.max_ppls:
                if i == int(self.pl) + 1:
                    if set(need_dates) & set(Hotel.booked_dates[Hotel.max_ppls[i]]) == set():
                        option.append(Hotel.max_ppls[i] + 1)
            if not option:  # в опшн у нас номера комнат,совпадающих по вместимости с нужной нам!
                for number in option:
                    prices_of_options[number] = Hotel.price_of_room[number]  # соединяем номер с его ценой
                prices_of_options = dict(
                    sorted(prices_of_options.items(), key=lambda x: x[1], reverse=True))  # сначала самые дорогие номера
                #print(prices_of_options)
                for room in prices_of_options:
                    if prices_of_options[room] <= int(self.sum) * int(self.pl):
                        number_chosen = room
                        summ_of_room = prices_of_options[room] * int(self.pl)
                        summ_of_food = int(self.sum) * int(self.pl) - summ_of_room
                        for j in Hotel.food_price:
                            if summ_of_food < Hotel.food_price[j] * int(self.pl):
                                continue
                            else:
                                food_chosen = j
                                break
                        print(
                            f'{self.name}, мы можем вам предложить следующий вариант: Номер комнаты: {number_chosen}, '
                            f'Степень комфортности: {Hotel.comforts[number_chosen - 1]}, Вид питания: {food_chosen}')
                        answer = random.choices(['Да', 'Нет'], weights=[75, 25])
                        if answer == 'Да':
                            Hotel.booked_dates[room - 1].append(need_dates)
                        else:
                            continue
                    else:
                        continue
                if number_chosen == 0:
                    print('Не можем вас заселить')


with open('booking.txt', encoding='utf-8') as f:
    for n in f:
        client = Clients(n)
        #print(client.need_dates())
        client.placing_people()

#print(Hotel.price_of_room)
