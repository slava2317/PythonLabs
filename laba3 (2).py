class Order:
    orders_quantity = 0

    def __init__(self, order: dict):
        Order.orders_quantity += 1
        self.items = order

    def add_item(self, item: str, price: float) -> dict:
        if item not in self.items:
            self.items[item] = price
        else:
            self.items[item] += price
        self.print_order()
        return self.items

    def remove_item(self, item: str) -> dict:
        if item in self.items:
            answer = input(f"Are you sure you want to delete '{item}' from order?"
                           "\nPress 'y' if you are sure.\n")
            if answer == "y":
                del self.items[item]
                print("Successfully deleted the item from the order.")
            else:
                print("The product was not removed from the order.")
        else:
            print("This item is not in your order. The order remains unchanged.")
        self.print_order()
        return self.items

    def get_total(self) -> float:
        return sum(self.items.values())

    def print_order(self) -> None:
        print(f"Items in order:")
        for key, value in self.items.items():
            print(f"- '{key}' with price {value};")
        print(f"Total price of order: {self.get_total()}.")

if __name__ == "__main__":
    test = Order({"test": 23, "car": 354.23})
    test.add_item("apple", 50) 
    test.remove_item("test")
