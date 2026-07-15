comment = str(input("Enter Comment : "))

if("Make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment):
    print("spam comment")
else:
    print("Not a spam Comment")