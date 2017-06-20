from spy_details import spy, Spy, ChatMessage, friends                          #importing details from spy details
from steganography.steganography import Steganography                           #importing steganography function
from datetime import datetime                                                   #though not required here
import time                                                                     #for delay function
STATUS_MESSAGES = ['Hey there I\'m new', 'Available', 'On a Mission']


print "Hey there! Let\'s get started..."

question = "Would you like to continue as " + spy.salutation + " " + spy.name + "(1) or a new user(0)?(1/0): "
existing = int(raw_input(question))                                              #taking input


def add_status():                                                                #1 menu choice

    updated_status_message = None                                                #current status message is none

    if spy.current_status != None:

        print 'Your current status message is %s \n' % (spy.current_status)     #no initial status message
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status = raw_input("What status message do you want to set? ")


        if len(new_status) > 0:                                                #to check if user didnt enter blank
            STATUS_MESSAGES.append(new_status)
            updated_status_message = new_status

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():                                                              #2

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_a_friend():                                        #selection function to select a friend from previously added
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():                                                         #3  send an encoded message

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():                                                           #4 decode the stegnographic message

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():                                              #if you have sent previous chat using stegnography only
                                                                      #only then you can read
    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name1 = spy.salutation + " " + spy.name

    if spy.age > 25 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name1 + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n 6. Send a SOS \n 7. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    print "\t\t\t*****************************************\n****************Hold Your Position!! Backup is on its way*******************\n\t\t\t************************************* \n"
                    time.sleep(3)
                else:
                    show_menu = False
        else:
            print 'Sorry you are not of the correct age to be a spy'


if existing == 1 :                                                #continuing with previous user James Bond
    start_chat(spy)

elif existing == 0 :

    spy = Spy('','',0,0.0)                                        #the spy variable is blank now


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:                                        #new user details
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?: ")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?: ")
        spy.rating = float(spy.rating)

        start_chat(spy)

    else:
        print 'Please add a valid spy name!!!'

else:
    print"Please enter appropriate choice.\n"