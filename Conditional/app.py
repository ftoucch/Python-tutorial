
house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = house_price*0.1
else:
    down_payment = house_price * 0.2
print(f"Down Payment : ${down_payment}")