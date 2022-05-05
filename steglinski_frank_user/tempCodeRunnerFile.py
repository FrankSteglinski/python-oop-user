class User:	#the class name	
    def __init__(self, name, email): 
        self.name = name
        self.email = email 
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        print("Recipient now has", recipient.account_balance)
        print("Sender now has", self.account_balance)

frank = User("Frank Steglinski", "fjsteglinski@gmail.com")
chanel = User("Chanel Steglinski", "chanelsteglinski@gmail.com")
coco = User("Coco Steglinski", "cocosteglinski@gmail.com")

frank.make_deposit(30000000)
frank.make_deposit(30000000)
frank.make_deposit(30000000)
frank.make_withdrawal(10000000)
frank.display_user_balance()

chanel.make_deposit(5000)
chanel.make_deposit(5000)
chanel.make_withdrawal(2000)
chanel.make_withdrawal(2000)
chanel.display_user_balance()

coco.make_deposit(30000)
coco.make_withdrawal(10000)
coco.make_withdrawal(10000)
coco.make_withdrawal(10000)
coco.display_user_balance()

frank.transfer_money(coco, 100)