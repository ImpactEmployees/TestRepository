__author__ = 'dreiger'

print ('HelloWorld!')

# Sample list for loop:
names = ["Derek","Erin","Micah","Madeline","Leah"]

for item in names:
    print item

# Sample dictionary for loop:
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print key + ":" + webster[key]

# Sample code for list, list processing
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": .18,
    "apple": 1.24,
    "orange": 1.49,
    "pear": 1.99
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1

    return total
