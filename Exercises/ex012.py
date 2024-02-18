product = float(input('What is the price of the product? NZ$'))
discount = product - (product * 0.05)
print('The original price was NZ${:.2f}, with the discount the product is going to cost NZ${:.2f}!'.format(product, discount))
