sku_to_price_lookup_dict = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}


class MultiBuyDiscountOffer:
    sku = ""
    offer_threshold = None
    offer_amount = None

    def __init__(self, sku: str, offer_threshold: int, offer_amount: int):
        self.sku = sku
        self.offer_threshold = offer_threshold
        self.offer_amount = offer_amount


def sort_multibuy_discounts_by_ppu(mb_offer: MultiBuyDiscountOffer):
    price_per_unit = mb_offer.offer_amount / mb_offer.offer_threshold
    return price_per_unit


multi_buy_discount_offers = [
    MultiBuyDiscountOffer("A", 3, 130),
    MultiBuyDiscountOffer("A", 5, 200),
    MultiBuyDiscountOffer("B", 2, 45),
    MultiBuyDiscountOffer("F", 3, 20),
    MultiBuyDiscountOffer("U", 4, 120),
    MultiBuyDiscountOffer("H", 5, 45),
    MultiBuyDiscountOffer("H", 10, 80),
    MultiBuyDiscountOffer("K", 2, 150),
    MultiBuyDiscountOffer("P", 5, 200),
    MultiBuyDiscountOffer("Q", 3, 80),
    MultiBuyDiscountOffer("V", 2, 90),
    MultiBuyDiscountOffer("V", 3, 130),
]


class GetOneFreeOffer:
    offer_sku = ""
    offer_threshold = None
    prize_sku = None
    prize_amount = 1

    def __init__(self, offer_sku: str, offer_threshold: int, prize_sku: str):
        self.offer_sku = offer_sku
        self.offer_threshold = offer_threshold
        self.prize_sku = prize_sku


sku_to_gof_offer_dict = {
    "E": [GetOneFreeOffer("E", 2, "B")],
    "N": [GetOneFreeOffer("N", 3, "M")],
    "R": [GetOneFreeOffer("R", 3, "Q")],
}


def calculate_best_mb_offer_amount(sku: str, num_items: int) -> int:
    multi_buy_discount_offers.sort(key=sort_multibuy_discounts_by_ppu)
    for mbo in multi_buy_discount_offers:
        if sku in mbo.sku:
            if num_items >= mbo.offer_threshold:
                num_items -= mbo.offer_threshold
                return mbo.offer_amount + calculate_best_mb_offer_amount(sku, num_items)
    return sku_to_price_lookup_dict[sku] * num_items


def calculate_item_amount(sku: str, num_items: int) -> int:
    return calculate_best_mb_offer_amount(sku, num_items)


def parse_skus_string(skus: str):
    # Outputs dictionary containing the skus, and number of them which occur in the file
    sku_num_items_dict = {}
    for sku in skus:
        if sku not in sku_to_price_lookup_dict:
            return None
        sku_num_items_dict[sku] = sku_num_items_dict.get(sku, 0) + 1
    return sku_num_items_dict


def calculate_get_one_free_offers(basket_dict: dict) -> dict:
    # Will remove free items if eligible, else, will not do anything to basket
    for sku, num_items in basket_dict.items():
        if sku in sku_to_gof_offer_dict:
            for gof_offer in sku_to_gof_offer_dict.get(sku):
                while num_items >= gof_offer.offer_threshold:
                    num_items -= gof_offer.offer_threshold
                    if gof_offer.prize_sku in basket_dict:
                        basket_dict[gof_offer.prize_sku] = basket_dict[gof_offer.prize_sku] - 1
    return basket_dict


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
    if basket_sku_num_dict is None:
        return -1
    basket_sku_num_dict = calculate_get_one_free_offers(basket_sku_num_dict)

    basket_total = 0
    for sku, num_items in basket_sku_num_dict.items():
        basket_total += calculate_item_amount(sku, num_items)
    return basket_total
