sku_to_price_lookup_dict = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}


# We're beginning to create a solution which is becoming unsustainable, we should change the way we are
# handling special offers. Using classes will allow us to contain functionality within the offers, making
# the calculations clearer as we add more offers and items

class MultiBuyDiscountOffer:
    sku = ""
    offer_threshold = None
    offer_amount = None

    def __init__(self, sku: str, offer_threshold: int, offer_amount: int):
        self.sku = sku
        self.offer_threshold = offer_threshold
        self.offer_amount = offer_amount


multi_buy_discount_offers = [
    MultiBuyDiscountOffer("A", 3, 130),
    MultiBuyDiscountOffer("B", 2, 45),
]


class MultiBuyGetOneFreeOffer:
    offer_sku = ""
    offer_threshold = None
    prize_sku = None
    prize_amount = 1

    def __init__(self, offer_sku: str, offer_threshold: int, prize_sku: str):
        self.offer_sku = offer_sku
        self.offer_threshold = offer_threshold
        self.prize_sku = prize_sku


multi_buy_get_one_free_offers = [
    MultiBuyGetOneFreeOffer("E", 2, "B")
]


def calculate_item_amount(sku: str, num_items: int) -> int:
    sub_total = 0

    for mbo in multi_buy_discount_offers:
        if sku in mbo.sku:
            while num_items >= mbo.offer_threshold:
                sub_total += mbo.offer_amount
                num_items -= mbo.offer_threshold

    while num_items > 0:
        sub_total += sku_to_price_lookup_dict[sku]
        num_items -= 1
    return sub_total


def parse_skus_string(skus: str) -> dict:
    # Outputs dictionary containing the skus, and number of them which occur in the file
    sku_num_items_dict = {}
    for sku in skus:
        if sku not in sku_to_price_lookup_dict:
            # # Skip character
            # continue
            # OR, if is not valid string
            return None
        sku_num_items_dict[sku] = sku_num_items_dict.get(sku, 0) + 1
    return sku_num_items_dict


def calculate_num_req_b_s(num_e_s: int) -> int:
    return num_e_s // 2  # Floor division answer


def calculate_multi_buy_get_one_free_items(basket_sku_num_dict: dict):
    for mbgofo in multi_buy_get_one_free_offers:
        # if the offer sku is in our basket
        if mbgofo.offer_sku in basket_sku_num_dict:
            # If the number of offer items in the basket is greater than or equal to the offer threshold
            if basket_sku_num_dict.get(mbgofo.offer_sku, 0) >= mbgofo.offer_threshold:
                # If we don't have enough prizes in the basket, add the correct amount
                num_prizes_in_basket = basket_sku_num_dict.get(mbgofo.prize_sku, 0)
                num_prizes_won = basket_sku_num_dict.get(mbgofo.offer_sku, 0) // mbgofo.offer_threshold
                print(num_prizes_in_basket)
                print(num_prizes_won)
                if num_prizes_in_basket >= num_prizes_won and num_prizes_in_basket > 0:
                    basket_sku_num_dict[mbgofo.prize_sku] = basket_sku_num_dict.get(mbgofo.prize_sku, 0) - mbgofo.prize_amount
    return basket_sku_num_dict





# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # ______ At the moment, we do not know the format of the string "skus"
    # e.g. "AAABBBABACGER", "A,B,C,DDD,E" etc.
    # Therefore, we will need to deploy an incorrect solution to find out what this is
    # ______ We have a price table given to us in the txt file, and we should think of a good way to store this
    # ______ We also have some special offers, and we'll have to think of a good way of storing this also
    # We don't know the format, so lets get an incorrect answer on purpose
    # Now we know the format, and have some example cases, we can parse our string and calculate totals
    # We can also add our test cases to our tests, so we don't get another time penalty

    if skus is None:
        return -1
    basket_sku_num_dict = parse_skus_string(skus)
    print("basket_sku_num_dict: ", basket_sku_num_dict)
    if basket_sku_num_dict is None:
        return -1

    basket_sku_num_dict = calculate_multi_buy_get_one_free_items(basket_sku_num_dict)
    print("basket_sku_num_dict: ", basket_sku_num_dict)

    basket_total = 0
    for sku, num_items in basket_sku_num_dict.items():
        basket_total += calculate_item_amount(sku, num_items)
    print("basket_total: ", basket_total)
    return basket_total


