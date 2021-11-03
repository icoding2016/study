# Sample question: 
# You need to design a Vending Machine which follows the following requirements
# - Accepts coins of 1,5,10,25, 50 Cents, i.e., penny, nickel, dime, and quarter as well as 1 and 2 dollar note
# - Allow user to select products e.g. CANDY(10), SNACK(50), NUTS(90), Coke(25), Pepsi(35), Soda(45)
# - Allow users to take a refund by canceling the request.
# - Return the selected product and remaining change if any
# - Allow reset operation for vending machine supplier

class VendingMachine(object):
    def __init__(self, products:dict, init_money:dict) -> None:
        self.products = products    # { '<product-name>':<price>, ... }
        self.acceptable_money = {0.01, 0.05, 0.1, 0.25, 0.5, 1, 2}
        self.inserted_money = 0
        self.money_cache = init_money    # {0.01:<count>, 0.05:<count>, 0.1:<count>, 0.25:<count>, 0.5:<count>, 1:<count>, 2:<count>}

    def insert_money(self, money:list) -> float:
        sum = float(0)
        for x in money:
            sum += x
        self.inserted_money = sum
        return sum

    def select_product(self, product_name:str) -> bool:
        # count insertd_money
        # compare price
        # check product availability
        # check refund availability
        # if all good,  
          # take_money() --update money_cache 
          # give_product() -- product-1
          # refund() 
          # return True
        return False

    def take_money(self) -> None:
        pass

    def give_product(self, product_name:str) -> None:
        pass

    def refund(self) -> (float, list):
        money_refund = []
        total = 0
        return total, money_refund

    def cancel(self) -> (float, list):
        # refund all inserted_money
        return refund()

    def reset(self):
        pass


def test():
    products = {'CANDY':1, 'SNACK':5, 'NUTS':9, 'Coke':2.5, 'Pepsi':3.5, 'Soda':4.5}
    vm = VendingMachine(products)

test()
