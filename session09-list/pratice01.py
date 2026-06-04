order_list = [
    "DE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

for value in order_list:
    if value.startswith("D"):
        print(value)