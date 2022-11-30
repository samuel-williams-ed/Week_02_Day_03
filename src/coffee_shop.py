class CoffeeShop():
    def __init__(self, input_name, input_slogan, input_stock_count):
        self.name = input_name
        self.slogan = input_slogan
        self.stock_count = input_stock_count
        
    def say_slogan(self):
        print(f"\n welcome to {self.name} it's {self.slogan}")

    def increase_stock_count(self, amount):
        self.stock_count += amount

    def has_full_range(self):
    #check list of beans are over 10
    pass
