class CalculatePrice:
    def __init__(self,discount):
        self.discount=discount
    def __call__(self,price):
        discountprice=price-price*self.discount/100
        return (price,discountprice)
def main():
    d=CalculatePrice(10)
    price, priceAfterDiscount = d(300)
    print("Original Price: %s , Price after discount : %s "% (price, priceAfterDiscount))

if __name__=='__main__':
    main()