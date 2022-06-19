


sku_to_price_lookup_dict = {
    "A" : 50,
    "B" : 30,
    "C" : 20,
    "D" : 15,
}

# sku_and_num_of_items_to_special_offer_function_lookup_dict = {
#     "A": 50,
#     "B": 30,
#     "C": 20,
#     "D": 15,
# }

def calculate_special_offer_amount(sku: str, num_items: int) -> int:
    sub_total = 0
    return sub_total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # ______ At the moment, we do not know the format of the string "skus"
    # e.g. "AAABBBABACGER", "A,B,C,DDD,E" etc.
    # Therefore, we will need to deploy an incorrect solution to find out what this is
    # ______ We have a price table given to us in the txt file, and we should think of a good way to store this
    # ______ We also have some special offers, and we'll have to think of a good way of storing this also
"""+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+"""

    return 0
