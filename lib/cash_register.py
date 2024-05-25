class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transaction_history = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.transaction_history.append((title, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transaction_history:
            last_transaction = self.transaction_history.pop()
            self.total -= last_transaction[1] * last_transaction[2]
            for _ in range(last_transaction[2]):
                self.items.remove(last_transaction[0])
        else:
            print("No transaction to void.")
