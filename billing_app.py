from datetime import datetime

products = {
    # Clothing & Footwear
    "1001": {"name": "Men's Cotton T-Shirt", "price": 299},
    "1002": {"name": "Men's Blue Denim Jeans", "price": 899},
    "1003": {"name": "Women's Printed Kurti", "price": 499},
    "1004": {"name": "Kid's Graphic Tee", "price": 199},
    "1005": {"name": "Sport Running Shoes", "price": 999},

    # Groceries & Food
    "1006": {"name": "Tata Salt (1kg)", "price": 28},
    "1007": {"name": "Maggi Noodles (140g)", "price": 30},
    "1008": {"name": "Aashirvaad Atta (5kg)", "price": 245},
    "1009": {"name": "Nescafe Coffee (50g)", "price": 170},
    "1010": {"name": "Taj Mahal Tea (250g)", "price": 150},
    "1011": {"name": "Lays Magic Masala", "price": 20},
    "1012": {"name": "Dairy Milk Silk", "price": 80},
    "1013": {"name": "Fortune Sun Oil (1L)", "price": 145},

    # Household & Personal Care
    "1014": {"name": "Surf Excel Matic (1kg)", "price": 220},
    "1015": {"name": "Vim Liquid (500ml)", "price": 105},
    "1016": {"name": "Dettol Handwash (200ml)", "price": 99},
    "1017": {"name": "Colgate Paste (150g)", "price": 110},
    "1018": {"name": "Parachute Oil (250ml)", "price": 115},
    "1019": {"name": "Milton Water Bottle (1L)", "price": 250},
    "1020": {"name": "Cotton Bath Towel", "price": 350}
}




cart = []


print()

#scanning operation and taking inputs
while True :
    barcode_scanned = input("Scan Barcode (or type 'done' to print bill) : ")
    if (barcode_scanned.lower() == "done") :
        break
    elif (barcode_scanned in products) :
        print(products.get(barcode_scanned))
        quantity = int(input("Enter Quantity : "))
        temp_dict = {
            "name" : products.get(barcode_scanned)["name"],
            "price" : products.get(barcode_scanned)["price"],
            "Qty" : quantity,
            "item total" : products.get(barcode_scanned)["price"] * quantity
        }
        cart.append(list(temp_dict.values()))
        print("Added ", quantity, "x ", products.get(barcode_scanned)["name"], " to cart.", sep="")
    else :
        print("Invalid Barcode. Try Again.")


phn = int(input("Enter Customer Phone Number : "))





cur_time = datetime.now()
# understanding Format
update_time = cur_time.strftime("%d/%m/%Y %I:%M %p")


#main header details
print()
print(
    "===========================================",
    "               BAZAAR INDIA",
    " Near Taltala Kalibari, Bardowali, Agartala",
    "            Ph: +91-9870003210",
    "===========================================",
    f"        Customer Phone: {phn}",
    f"        Date: {update_time}",
    "-------------------------------------------",
    "Item Name                Rate   Qty   Total",
    "-------------------------------------------", sep="\n")



grand_total = 0


#printing item list loop
for i in cart :
    name = i[0][:18]  
    rate = i[1]
    qty = i[2]
    total = i[3]

    print(f"{name:<22} {rate:>5} {qty:>5} {total:>7}")

    grand_total += total



#finishing
print("-------------------------------------------")
print("Grand Total :                        ₹", grand_total, sep="")

print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
    "          Thank You! Visit Again!          ",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", sep="\n")
print()



