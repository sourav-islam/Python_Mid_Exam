# All requirements are fulfilled in the Python_Mid_Exam doc question .

class Star_cinema:
    _hall_list = []

    def _entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        
        super().__init__()
        self._entry_hall((rows, cols, hall_no))  # Pass as tuple

    def entry_shows(self, id, movie_name, time):
        
        show_tuple = (id, movie_name, time)
        self.__show_list.append(show_tuple)
        seat_list = [['free' for _ in range(self._cols)] for _ in range(self._rows)]
        self.__seats[id] = seat_list

    def book_seats(self, id, tup):
        if id in self.__seats:
            print(f'{id} is valid')
            for t in tup:
                r, c = t
                if r < self._rows and c < self._cols:
                    if self.__seats[id][r][c] == 'free':
                        self.__seats[id][r][c] = 'book'
                        print(f'Seat ({r}, {c}) booked successfully.')
                    else:
                        print(f'Seat ({r}, {c}) is already booked.')
                else:
                    print(f"Seat ({r}, {c}) is out of range.")
        else:
            print(f'{id} is an invalid show ID')

    def view_show_list(self):
        print('Running shows are:')
        for s_list in self.__show_list:
            print(f'Movie_Name: {s_list[1]:<20} Time: {s_list[2]}')

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f'Available seats for show ID {id}:')
            print(f'(rows, cols)')
            for i in range(len(self.__seats[id])):
                for j in range(len(self.__seats[id][i])):
                    if self.__seats[id][i][j] == 'free':
                        print(f'Seat ({i}, {j})')

            print('\nMatrix Form:')
            for k in range(len(self.__seats[id])):
                print(self.__seats[id][k])
        else:
            print(f'{id} is a invalid ID of running shows')
    
    def get_show_list(self):
        return self.__show_list

    def get_seats(self):
        return self.__seats


# Object create
hall = Hall(5, 4, 30)
hall.entry_shows('111', 'Titanic(111)', '15/12/2024   10:00 AM')
hall.entry_shows('333', 'Harry Potter(333)', '15/12/2024   02:00 PM')
hall.entry_shows('222', 'Spider-Man(222)', '15/12/2024   08:00 PM')

print('\n')
print('--------- Star_cinema Hall -----------')
print('========== Counter ============')
print('\n')
print('1. View all the running shows')
print('2. View available seats')
print('3. Book ticket')
print('4. Terminate all')

while True:
    print('\n')
    val = int(input('Type a valid option: '))
    if val == 1:
        hall.view_show_list()
    elif val == 2:
        print('Enter a valid ID:')
        id = input()
        hall.view_available_seats(id)
    elif val == 3:
        print('Enter a valid ID:')
        id = input()
        print('Enter the number of seats:')
        n = int(input())
        list_of_tuple = [tuple(map(int, input('Enter row and col: ').split())) for _ in range(n)]
        hall.book_seats(id, list_of_tuple)
    elif val == 4:
        print('Successfully terminated')
        break
