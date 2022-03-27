'''
Jadi penggunaan global dan nonlocal itu terdapat dari:
kalau global itu variablenya berasal dari bukan dari fungsi lain atau fungsi yang ditempati tetapi umum
sedangkan nonlocal itu variablenya berasal fungsi yang ditempati atau fungsi lainnya
'''
# Contoh Perbedaana Global dan Nonlocal Scope:
# Global
x = 150
def add_five():
    global x
    x = 5
    return x

# Nonlocal
def use_giftcard(purchase_amount):
    gift_card_balance = 100
    def subtract():
        nonlocal gift_card_balance
        gift_card_balance -= purchase_amount
    subtract()
    print(gift_card_balance)
use_giftcard(20)