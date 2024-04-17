import random
import RU_LOCAL as RU


class Hotel:
    price_of_room = {}
    nums = []
    types = []
    max_ppls = {}
    comforts = []
    booked_dates = []
    price_type = {RU.ONE_PLACE: 2900, RU.SECOND_PLACE: 2300, RU.SEMILUXE: 3200, RU.LUXE: 4100}
    comfort_price = {RU.STANDART: 1, RU.STANDART_UP: 1.2, RU.APART: 1.5}
    food_price = {RU.HALF_BOARD: 1000, RU.BREAKFAST: 280, RU.WITHOUT_FOOD: 0}
    count_one_place = 0
    count_second_place = 0
    count_semiluxe = 0
    count_luxe = 0

    def __init__(self, ptr):
        ptr = ptr.split()
        self.num = int(ptr[0])
        self.type = ptr[1]
        if self.type == RU.ONE_PLACE:
            Hotel.count_one_place += 1
        if self.type == RU.SECOND_PLACE:
            Hotel.count_second_place += 1
        if self.type == RU.SEMILUXE:
            Hotel.count_semiluxe += 1
        if self.type == RU.LUXE:
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
                        f'{self.name}, {RU.OPTION_ROOM}: {number_chosen}, '
                        f'{RU.OPTION_COMFORT}: {Hotel.comforts[number_chosen - 1]}, {RU.OPTION_FOOD}: {food_chosen}')
                    answer = random.choices([RU.YES, RU.NO], weights=[75, 25])
                    if answer == [RU.YES]:
                        Hotel.booked_dates[room - 1] += need_dates
                        for dates in need_dates:
                            Clients.data_income[dates] += summ_of_room + Hotel.food_price[food_chosen] * int(self.pl)
                        break
                    else:
                        print(f'{self.name}, {RU.OTHER_OPTION}')
                        if room == list(prices_of_options.keys())[-1]:
                            for dates in need_dates:
                                Clients.data_without_income[dates] += int(self.sum) * int(self.pl)
                            print(f'{self.name}, {RU.CANT_BOOK}')
                        else:
                            continue
                else:
                    continue
            if number_chosen == 0:
                for dates in need_dates:
                    Clients.data_without_income[dates] += int(self.sum) * int(self.pl)
                print(f'{self.name}, {RU.CANT_BOOK}')
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
                            f'{self.name}, {RU.OPTION_ROOM}: {number_chosen}, '
                            f'{RU.OPTION_COMFORT}: {Hotel.comforts[number_chosen - 1]}, {RU.OPTION_FOOD}: {food_chosen}')
                        answer = random.choices([RU.YES, RU.NO], weights=[75, 25])
                        if answer == [RU.YES]:
                            Hotel.booked_dates[room - 1] += need_dates
                            for dates in need_dates:
                                Clients.data_income[dates] += summ_of_room + Hotel.food_price[food_chosen] * int(
                                    self.pl)
                            break
                        else:
                            print(f'{self.name}, {RU.OTHER_OPTION}')
                            if room == list(prices_of_options.keys())[-1]:
                                for dates in need_dates:
                                    Clients.data_without_income[dates] += int(self.sum) * int(self.pl)
                                print(f'{self.name}, {RU.CANT_BOOK}')
                            else:
                                continue
                    else:
                        continue
                if number_chosen == 0:
                    for dates in need_dates:
                        Clients.data_without_income[dates] += int(self.sum) * int(self.pl)
                    print(f'{self.name}, {RU.CANT_BOOK}')
            else:
                for dates in need_dates:
                    Clients.data_without_income[dates] += int(self.sum) * int(self.pl)
                print(f'{self.name}, {RU.CANT_BOOK}')


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
                if Hotel.types[Hotel.booked_dates.index(room)] == RU.ONE_PLACE:
                    count_one_place_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == RU.SECOND_PLACE:
                    count_second_place_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == RU.SEMILUXE:
                    count_semiluxe_b += 1
                elif Hotel.types[Hotel.booked_dates.index(room)] == RU.LUXE:
                    count_luxe_b += 1
                count_booked += 1

        print(f'{RU.BOOKED_ROOMS} {day}: {count_booked}', file=res)
        print(f'{RU.NOT_BOOKED_ROOMS} {day}: {len(Hotel.nums) - count_booked}', file=res)
        print(f'{RU.PERC_BOOKED_HOTEL} {day}: {round(count_booked / len(Hotel.nums) * 100, 2)}%', file=res)
        print(
            f'{RU.PERC_BOOKED_ONE_PLACE} {day}: '
            f'{round(count_one_place_b / Hotel.count_one_place * 100, 2)}%',
            file=res)
        print(
            f'{RU.PERC_BOOKED_SECOND_PLACE} {day}: '
            f'{round(count_second_place_b / Hotel.count_second_place * 100, 2)}%',
            file=res)
        print(
            f'{RU.PERC_BOOKED_SEMILUXE} {day}:'
            f' {round(count_semiluxe_b / Hotel.count_semiluxe * 100, 2)}%',
            file=res)
        print(f'{RU.PERC_BOOKED_LUXE} {day}: '
              f'{round(count_luxe_b / Hotel.count_luxe * 100, 2)}%',
              file=res)
        print(f'{RU.GET_INCOME} {day}: {Clients.data_income[day]}', file=res)
        print(f'{RU.MISSED_INCOME} {day}: {Clients.data_without_income[day]}', file=res)
        print(file=res)
