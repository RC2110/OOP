# users enter their checkin date and browse the list of available hotels
# users select their preferred hotel
# users book the hotel and get their reservation ticket


import pandas as pd

df= pd.read_csv("hotels.csv")
df2=pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df3=pd.read_csv("card_security.csv")

class Users:
    pass

class Hotel:
    def __init__(self, id):
        self.id = id

    def availablilty(self):
        available = df.loc[df['id']==self.id]['available'].squeeze()
        return available

    def book(self):
        df.loc[df['id'] == self.id,'available']='no'
        df.to_csv("hotels.csv", index=False)
        print("The ticket is booked!")
        pass

class SpaAddon(Hotel):
    def book_spa_hotel(self):
        pass


class ReservationTicket:
    def __init__(self, name, hotelid):
        self.name=name
        self.hotelid=hotelid
    def generateticket(self):
        hotelname = df.loc[df['id']==self.hotelid]['name'].squeeze()

        return f"""Hi {self.name}, you have
                successfully booked a ticket 
                for the hotel {hotelname}. reference#12345"""

class SpaTicket:
    def book(self, uname, hotel):
        print("Thanks for your spa reservation")
        hotelname = df.loc[df['id'] == hotel]['name'].squeeze()
        return f"""Here are your booking details.
                  Name:{uname}
                  Hotel name:{hotelname}"""
class CreditCard:
    def __init__(self, id):
        self.id=id

    def validate(self, exp, cvc, name):
        dt={'number': self.id,'expiration': exp, 'cvc': cvc, 'holder': name }
        if dt in df2:
            return True

class SecurePayment(CreditCard):

    def securevalidate(self, mypass):
        passwd = df3["password"].squeeze()
        if passwd == mypass:
            return True



print(df)

hotelid = int(input("Enter the hotel id:"))
hotel = SpaAddon(hotelid)
hotelavail = hotel.availablilty()


if hotelavail == "yes":
    cc= SecurePayment("1234567890123456")
    val = cc.validate("12/26","123","JOHN SMITH")
    print(val)
    if val:
        pas=input("Enter your password:")
        secure_validate= cc.securevalidate(pas)
        if secure_validate:
            username = input("Enter your full name")
            hotel.book()
            ticket = ReservationTicket(username, hotelid)
            print(ticket.generateticket())
            sparesp= input("Do you want to take a SPA?")
            match sparesp:
                case "yes"| "Yes"|"ghgf":
                    tic=SpaTicket()
                    print(tic.book(username, hotelid))
        else:

            print("Authentication has failed")
    else:
        print("The card details are incorrect")

else:
    print("The hotel isn't available.")





