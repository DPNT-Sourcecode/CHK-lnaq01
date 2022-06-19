sku_to_price_lookup_dict = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}


def calculate_special_offer_amount(sku: str, num_items: int) -> int:
    sub_total = 0
    # Currently, we are only aware of 2 special offers
    # 3As for 130, and 2Bs for 45
    # Lets do this naively to begin with, and we'll change it in future to accomodate other offers

    return sub_total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # ______ At the moment, we do not know the format of the string "skus"
    # e.g. "AAABBBABACGER", "A,B,C,DDD,E" etc.
    # Therefore, we will need to deploy an incorrect solution to find out what this is
    # ______ We have a price table given to us in the txt file, and we should think of a good way to store this
    # ______ We also have some special offers, and we'll have to think of a good way of storing this also
    return 0

