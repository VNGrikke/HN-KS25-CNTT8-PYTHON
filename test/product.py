class Product():
    
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0
        self.revenue_type = ""

        self.calculate_revenue()

    def calculate_revenue(self):
        revenue = (self.price * self.quantity_sold) - self.discount
        self.total_revenue = revenue if revenue > 0 else 0
        self.classify_revenue()

    def classify_revenue(self):
        if self.total_revenue < 5_000_000:
            self.revenue_type = "Thap"
        elif self.total_revenue <= 20_000_000:
            self.revenue_type = "Trung binh"
        elif self.total_revenue <= 50_000_000:
            self.revenue_type = "Kha"
        else:
            self.revenue_type = "Cao"

    
    

    