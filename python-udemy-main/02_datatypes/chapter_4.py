# is_boiling = True
# stri_count = 5
# total_actions = stri_count + is_boiling # upcasting
# print(f"Total actions: {total_actions}")

# milk_present = 0 # no milk
# print(f"Is there milk? {bool(milk_present)}")

# water_hot = True
# tea_added = True

# can_server = water_hot and tea_added
# print(f"Can serve chai? {can_server}")


is_boiling = True
stri_count = 5

total_action = stri_count + is_boiling  # upcasting
print(f"total actions : {total_action}")

milk_present = 1 # no milk
print(f"is there milk? {bool(milk_present)}")


water_hot = True

tea_added = False

can_serve = water_hot or tea_added
print(f"can serve chai? {can_serve}")

