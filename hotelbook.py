# users enter their checkin date and browse the list of available hotels
# users select their preferred hotel
# users book the hotel and get their reservation ticket


import pandas as pd

df= pd.read_csv("hotels.csv")

class Users:
    pass

class Hotel:
    def __init__(self, id):
        self.id = id

    def availablilty(self):
        available = df.loc[df['id']==self.id]['available'].squeeze()
        return available

    def book(self):
        df.loc[df['id'] == self.id]['available']=='no'
        df.to_csv("hotels.csv")
        print("The ticket is booked!")
        pass


class ReservationTicket:
    def __init__(self, name, hotelid):
        self.name=name
        self.hotelid=hotelid
    def generateticket(self):
        hotelname = df.loc[df['id']==188]['name'].squeeze()

        return f"""Hi {self.name}, you have
                successfully booked a ticket 
                for the hotel {hotelname}. reference#12345"""


print(df)

hotelid = int(input("Enter the hotel id:"))
hotel = Hotel(hotelid)
hotelavail = hotel.availablilty()

if hotelavail == "yes":
    username = input("Enter your full name")
    hotel.book()
    ticket = ReservationTicket(username, hotel)
    print(ticket.generateticket())

else:
    print("The hotel isn't available.")





