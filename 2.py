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
