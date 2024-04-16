def need_dates(data_start, days):
    need_dates = []
    data_start = data_start.split('.')
    for i in range(int(days)):
        if int(data_start[0]) + int(i) <= 9:
            new_data = '0' + str(int(data_start[0]) + int(i)) + '.' + data_start[1] + '.' + data_start[2]
        else:
            new_data = str(int(data_start[0]) + int(i)) + '.' + data_start[1] + '.' + data_start[2]
        need_dates.append(new_data)
    return need_dates

print(need_dates('10.03.2024', 7))
