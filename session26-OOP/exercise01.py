delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

delivery_orders.append("GE004")

delivery_orders.insert(0, "GE000")

delivery_orders[2] = "GE002-UPDATE"

delivery_orders.remove("GE003-CANCEL")

transferred_order = delivery_orders.pop()

print(delivery_orders)
print(transferred_order)