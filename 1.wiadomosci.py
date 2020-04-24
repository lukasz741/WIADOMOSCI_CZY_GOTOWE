x = open("1..txt", "r")
x.con = x.read().splitlines()
print(x.con)
print(x.con[0])

y = open("2..txt", "r")
y.con = y.read().splitlines()

z = open("3..txt", "r")
z.con = z.read().splitlines()

class user:

    def __init__(self, name, surname, ready):
        self.name = name
        self.surname = surname
        self.ready = ready

    @classmethod
    def from_string(cls, user_list):
        name_string = user_list[0]
        name = name_string[5:]
        surname_string = user_list[1]
        surname = surname_string[9:]
        ready_string = user_list[2]
        ready = ready_string[7:]
        return cls(name, surname, ready)



user1 = user.from_string(x.con)
user2 = user.from_string(y.con)
user3 = user.from_string(z.con)


def message(name, surname, ISready):
    if name[-2] == "a":
        return "hello miss {} {}, your order is {}".format(name, surname, ISready)
    else:
        return "hello mister {} {}, your order is {}".format(name, surname, ISready)


print(message(user2.name, user2.surname, user2.ready))


