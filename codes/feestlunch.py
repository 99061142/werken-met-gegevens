crossaints = 17
breads = 2
coupons = 3

crossaintPrice = .39
breadPrice = 2.78
discountPrice = .5

crossaint = crossaints * crossaintPrice
bread = breads * breadPrice
discount = coupons * discountPrice

price = crossaints + bread
lunchTotal = price - discount


print("De feestlunch kost je bij de bakker", lunchTotal, "euro voor de", crossaints, "croissantjes en de", breads, "stokbroden als de", coupons, "kortingsbonnen nog geldig zijn!")
