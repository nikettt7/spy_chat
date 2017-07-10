from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []                                 #for collecting chat data
        self.current_status = None                       # for personal status records


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('James Bond', 'Mr.', 42, 4.89)

friend_one = Spy('Jason Bourne', 'Mr.', 4.90, 32)
friend_two = Spy('Natasha Romonov', 'Ms.', 4.39, 30)
friend_three = Spy('Sherlock Holmes', 'Mr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]




