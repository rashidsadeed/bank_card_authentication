import csv


#Network informationo
first_digit = {"4":"Visa", "5":"Master Card", "6":"Discover", "7":"Petroleum", "8":"Health case and communication", "9":"Troy"}


#BANK information import
ids = {}
with open("BIN.csv", mode="r", encoding="utf-8") as bank_id:
    content = csv.reader(bank_id)
    for row in content:
        ids[row[1]] = row[0]

#network check algo
def check_network(card_number):
    network = None
    if len(card_number)==15:
        return "American Express"
    else:
        network = first_digit[card_number[0]]
        return network
        

#bank name check algo 
def check_bank(card_number):
    BIN = card_number[:6]
    if BIN in ids:
        return ids[BIN]    

#last digit luhn_Check_Sum algo
def luhn_checksum(card_number):
    card_number = int(card_number)
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10



#Assembly
def card_details(card_number):
    if luhn_checksum(card_number) != 0:
        print ("you have entered an invalid number")
    else:
        print (f"your card network is {check_network(card_number)} and it's issued by {check_bank(card_number)}")



input_number = input("enter your card number here: ")
card_details(input_number)