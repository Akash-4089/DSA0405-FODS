item_prices = [2.5, 3.0, 1.75, 4.5]
quantities = [3, 2, 4, 1]
discount_rate = 10
tax_rate = 8

total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, quantities))

discount_amount = (discount_rate / 100) * total_cost_before_discounts
discounted_total_cost = total_cost_before_discounts - discount_amount

discounted_total_cost = total_cost_before_discounts - discount_amount

tax_amount = (tax_rate / 100) * discounted_total_cost

final_total_cost = discounted_total_cost + tax_amount

print(f'Total Cost: ${final_total_cost:.2f}')