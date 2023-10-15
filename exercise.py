from fpdf import FPDF
import pandas as pd
df = pd.read_csv("articles.csv", index_col=0)

class Item:
    def __init__(self, id):
        self.id = id

    def stock(self):
        available= df.loc[df['id']==self.id]['in stock'].squeeze()
        return available

    def order(self):
        print("Your order is placed")
    def updatestock(self):
        df.loc[df['id'] == self.id, 'in stock'] = df.loc[df['id'] == self.id]['in stock'].squeeze() - 1
        df.to_csv("articles.csv")


class PurchaseReceipt:
    def __init__(self, id):
        self.id = id
        df = pd.read_csv("articles.csv")
        self.product = df.loc[df['id'] == self.id]['name'].squeeze()
        self.price = df.loc[df['id'] == self.id]['price'].squeeze()

    def generate(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font(family='Helvetica', style='B', size=12)
        pdf.cell(w=50, h=12, txt="Receipt no:1",ln=1)
        pdf.set_font(family='Helvetica', style='I', size=10)
        pdf.cell(w=50, h=12, txt = f"Product:{self.product}",ln=2)
        pdf.set_font(family='Helvetica', style='I', size=10)
        pdf.cell(w=25, h=2, txt = f"Price:{self.price}",ln=1)

        print("Please download your pdf")
        pdf.output("receipt.pdf")
        pass

print(df)
inp = int(input("Enter the item id:"))
product = Item(inp)
availabilty = product.stock()

if availabilty >0:
    product.order()
    receipt = PurchaseReceipt(inp)
    receipt.generate()
    product.updatestock()
else:
    print("No more stocks left!")
    print("Hello")
