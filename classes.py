from abs import ABS

import pandas as pd

df= pd.read_csv("hotels.csv")

class Hotel:

    company ="ConnectedHotelWorld"
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

    @classmethod
    def count(cls, data):
        return len(data)

    @staticmethod
    def amount(num):
        num=num*5
        return num

    def __eq__(self, others):
        if self.id == others.id :
            return Truedir

    def __ge__(self, other):
        return self.id + other.id


class ReservationTicket:
    def __init__(self, name, hotelid):
        self.name=name
        self.hotelid=hotelid
    def generateticket(self):
        hotelname = df.loc[df['id']==self.hotelid]['name'].squeeze()
        print(hotelname)

        return f"""Hi {self.customer_name}, you have
                successfully booked a ticket 
                for the hotel {hotelname}. reference#12345"""

    @property
    def customer_name(self):
        name = self.name.strip()
        name= name.title()
        return name

if __name__ == "__main__":
    stay= Hotel("134")
    vacation= Hotel("188")
    print(Hotel.count(df))
    # print(vacation.id)

    tk = ReservationTicket("john paul", 188)
    name = tk.customer_name
    print(tk.generateticket())

    print(stay.amount(25))


