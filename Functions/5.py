"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""

def discount_price(original_price, discount_percent):
    discount_price = (discount_percent/100) * original_price
    final_amount = original_price - discount_price
    print(f"Final bill amount = {final_amount}")

discount_price(1000,10)