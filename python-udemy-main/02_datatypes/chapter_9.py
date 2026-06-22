# essential_spices = {"cardamom", "ginger", "cinnamon"}
# optional_spices = {"cloves", "ginger", "black pepper"}

# all_spices = essential_spices | optional_spices
# print(f"All spices: {all_spices}")

# common_spices = essential_spices & optional_spices
# print(f"common spices: {common_spices}")

# only_in_essential = essential_spices - optional_spices
# print(f"Only in essential spices: {only_in_essential}")

# print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

base_liquid = {"water", "milk"}
extra_flavor = {"ginger"}


# full_liquid_mix = base_liquid + extra_flavor
# print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")


raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}")   
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")



essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}


all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")


all_spices = essential_spices & optional_spices
print(f"All spices: {all_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f'Is cloves in optional spices? {"cloves" in optional_spices}')