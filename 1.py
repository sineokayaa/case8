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
    count_one_place = 0
    count_second_place = 0
    count_semiluxe = 0
    count_luxe = 0

    def __init__(self, ptr):
        ptr = ptr.split()
        self.num = int(ptr[0])
        self.type = ptr[1]
        if self.type == 'одноместный':
            Hotel.count_one_place += 1
        if self.type == 'двухместный':
            Hotel.count_second_place += 1
        if self.type == 'полулюкс':
            Hotel.count_semiluxe += 1
        if self.type == 'люкс':
            Hotel.count_luxe += 1
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
    all_days = []
    data_income = {}
    data_without_income = {}

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
        for days in need_dates:
            if days not in Clients.all_days:
                Clients.all_days.append(days)
                Clients.data_income[days] = 0
                Clients.data_without_income[days] = 0
        return need_dates

    def placing_people(self):
        option = []

        prices_of_options = {}
        number_chosen = 0
        food_chosen = ''
        need_dates = Clients.need_dates(self)
        for i in Hotel.max_ppls:  # num of room

            if str(Hotel.max_ppls[i]) == self.pl:
                if set(need_dates) & set(Hotel.booked_dates[i - 1]) == set():
                    option.append(i)
        if option != []:  # в опшн у нас номера комнат,совпадающих по вместимости с нужной нам!
            for number in option:
                prices_of_options[number] = Hotel.price_of_room[number]  # соединяем номер с его ценой
            prices_of_options = dict(
                sorted(prices_of_options.items(), key=lambda x: x[1], reverse=True))  # сначала самые дорогие номера
            for room in prices_of_options:
                if prices_of_options[room] <= int(self.sum) * int(self.pl):
                    number_chosen = room
                    summ_of_room = prices_of_options[room]
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
                    if answer == ['Да']:
                        Hotel.booked_dates[room - 1] += need_dates
                        for dates in need_dates:
                            Clients.data_income[dates] += summ_of_room + Hotel.food_price[food_chosen] * int(self.pl)
                        break
                    else:
                        print(f'{self.name}, хорошо, поищем другие варианты')
                        if room == list(prices_of_options.keys())[-1]:
                            for dates in need_dates:
                                Clients.data_without_income[dates] += int(self.sum)
                            print(f'{self.name}, не можем вас заселить')
                        else:
                            continue
                else:
                    continue
            if number_chosen == 0:
                for dates in need_dates:
                    Clients.data_without_income[dates] += int(self.sum)
                print(f'{self.name}, не можем вас заселить')
        else:
            for i in Hotel.max_ppls:
                if Hotel.max_ppls[i] == int(self.pl) + 1:
                    if set(need_dates) & set(Hotel.booked_dates[i - 1]) == set():
                        option.append(i)
            if option != []:  # в опшн у нас номера комнат,совпадающих по вместимости с нужной нам!
                for number in option:
                    prices_of_options[number] = Hotel.price_of_room[number] * 0.7  # соединяем номер с его ценой
                prices_of_options = dict(
                    sorted(prices_of_options.items(), key=lambda x: x[1], reverse=True))  # сначала самые дорогие номера
                for room in prices_of_options:
                    if prices_of_options[room] <= int(self.sum) * int(self.pl):
                        number_chosen = room
                        summ_of_room = prices_of_options[room]
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
                        if answer == ['Да']:
                            Hotel.booked_dates[room - 1] += need_dates
                            for dates in need_dates:
                                Clients.data_income[dates] += summ_of_room + Hotel.food_price[food_chosen] * int(
                                    self.pl)
                            break
                        else:
                            print(f'{self.name}, хорошо, поищем другие варианты')
                            if room == list(prices_of_options.keys())[-1]:
                                for dates in need_dates:
                                    Clients.data_without_income[dates] += int(self.sum)
                                print(f'{self.name}, не можем вас заселить')
                            else:
                                continue
                    else:
                        continue
                if number_chosen == 0:
                    for dates in need_dates:
                        Clients.data_without_income[dates] += int(self.sum)
                    print(f'{self.name}, не можем вас заселить')
            else:
                for dates in need_dates:
                    Clients.data_without_income[dates] += int(self.sum)
                return (f'{self.name}, не можем вас заселить')


with open('booking.txt', encoding='utf-8') as f:
    for n in f:
        client = Clients(n)
        client.placing_people()

with open('results.txt', 'w', encoding='utf-8') as res:
    for day in Clients.all_days:
        count_booked = 0
        count_one_place_b = 0
        count_second_place_b = 0
        count_semiluxe_b = 0
        count_luxe_b = 0
        for room in Hotel.booked_dates:
            if day in room:
                if Hotel.types[Hotel.booked_dates.index(room)] == 'одноместный':
                    count_one_place_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == 'двухместный':
                    count_second_place_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == 'полулюкс':
                    count_semiluxe_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == 'люкс':
                    count_luxe_b += 1
                count_booked += 1


        print(f'Количество занятых номеров на {day}: {count_booked}', file=res)
        print(f'Количество свободных номеров на {day}: {len(Hotel.nums) - count_booked}', file=res)
        print(f'Процент загруженности гостиницы на {day}: {round(count_booked / len(Hotel.nums) * 100, 2)}%', file=res)
        print(
            f'Процент загруженности одноместных номеров на {day}: '
            f'{round(count_one_place_b / Hotel.count_one_place * 100, 2)}%',
            file=res)
        print(
            f'Процент загруженности двухместных номеров на {day}: '
            f'{round(count_second_place_b / Hotel.count_second_place * 100, 2)}%',
            file=res)
        print(
            f'Процент загруженности полулюкс номеров на {day}:'
            f' {round(count_semiluxe_b / Hotel.count_semiluxe * 100, 2)}%',
            file=res)
        print(f'Процент загруженности люкс номеров на {day}: '
              f'{round(count_luxe_b / Hotel.count_luxe * 100, 2)}%',
              file=res)
        print(f'Полученный доход за {day}: {Clients.data_income[day]}', file=res)
        print(f'Упущенный доход за {day}: {Clients.data_without_income[day]}', file=res)
        print(file=res)
