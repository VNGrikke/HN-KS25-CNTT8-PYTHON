express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102_UPDATE"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)

print(express_orders)
print(current_order)