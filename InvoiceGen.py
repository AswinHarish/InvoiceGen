import os
from InvoiceGenerator.api import Client,Creator,Invoice,Provider,Item
from InvoiceGenerator.pdf import SimpleInvoice
from tkinter.filedialog import *


os.environ["INVOICE_LANG"] = "en"

a = print('Choose an image file for logo ')
logo = askopenfilename()

y_Name = input('Enter Your Name : ')
b_Name = input('Enter Company Name : ')
c_Name = input('Enter Client\'s Name : ')
print('\n')
Item1 = input('Name of first item : ')
Price1 = input('Specify price of the item : ')
Unit1 = input('Number of units sold : ')
print('\n')
Item2 = input('Name of second item : ')
Price2 = input('Specify price of the item : ')
Unit2 = input('Number of units sold : ')
print('\n')
Item3 = input('Name of third item : ')
Price3 = input('Specify price of the item : ')
Unit3 = input('Number of units sold : ')
print('\n')


client = Client(c_Name)
provider = Provider(b_Name, bank_account='326543634564', bank_code='2210', logo_filename=logo)
creator = Creator(y_Name)
invoice = Invoice(client, provider, creator)

invoice.currency = "Rs"
invoice.add_item(Item(Unit1, Price1, description=Item1))
invoice.add_item(Item(Unit2, Price2, description=Item2))
invoice.add_item(Item(Unit3, Price3, description=Item3))

print('Inoice generated and saved as invoice.pdf')
pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)