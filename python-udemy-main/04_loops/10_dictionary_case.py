# users = [
#     {"id": 1, "total": 100, "coupon": "P20"},
#     {"id": 2, "total": 150, "coupon": "F10"},
#     {"id": 3, "total": 80, "coupon": "P50"},
# ]


users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
    {"id": 4, "total": 200, "coupon": "NONE"}
]



# discounts = {
#     "P20": (0.2, 0),
#     "F10": (0.5, 0),
#     "P50": (0, 10),
# }

discounts = {
    "P20" :(0.2,0),
    "F10" :(0.5,0),
    "P50" :(0,10)
    # "NONE" :(0, 500)
}


# for user in users:
#     percent, fixed = discounts.get(user["coupon"], (0, 0))
#     discount = user["total"] * percent + fixed
#     print(f"{user['id']} paid {user['total']} and got discount for next visit of rupees {discount}")

# for user in users:
#     percent, fixed = discounts.get(user["coupon"], (0, 0))
#     discount = user["total"] * percent + fixed
#     print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")