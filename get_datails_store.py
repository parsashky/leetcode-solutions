class Store :
    def __init__(self , name):
        self.name = name
        self.item = []
    def add_item(self , name , price):
        self.item.append({"name" : name ,"price" : price})
    def stock_price(self):
        total = 0
        for item in self.item :
            total += item["price"]
        return total
    @classmethod
    def frranchise(cls , store):
        new_store = cls(store.name + " - franchise" ) 
        return new_store
    @staticmethod
    def store_datails(store):
        return  '{} , total stock price : {}'.format(Store.name , int(Store.stock_price()))