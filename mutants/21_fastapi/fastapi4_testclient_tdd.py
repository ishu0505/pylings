TARGET = "calculate_discount"


def _vip_gives_half(total, promo_code):
    if promo_code == "VIP":
        return round(total * 0.50, 2)
    elif promo_code == "FIXED10":
        return min(10.0, total)
    return 0.0


def _fixed10_gives_zero(total, promo_code):
    if promo_code == "VIP":
        return round(total * 0.20, 2)
    return 0.0


def _unknown_gives_discount(total, promo_code):
    return 5.0


MUTANTS = {
    "VIP discount is 50% instead of 20%": _vip_gives_half,
    "FIXED10 gives zero discount": _fixed10_gives_zero,
    "unknown promo code gives 5.0 discount": _unknown_gives_discount,
}
