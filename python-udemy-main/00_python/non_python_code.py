# def make_chai():
#     if not kettle_has_water():
#         fill_kettle()

#     plug_in_kettle()
#     boil_water()

#     if not is_cup_clean():
#         wash_cup()

#     add_to_cup("tea_leaves")
#     add_to_cup("sugar")
#     pour("boiled water")
#     stir("cup")
#     serve("chai")

# make_chai()

# def make_chai():
#     if not kettle_has_water():
#         fill_kettle()
#     plug_in_kettle()
#     boil_water()
#     if not is_cup_clean():
#         wash_cup()
#     add_to_cup("tea_leaves")
#     add_to_cup("sugar")
#     pour("boiled water") 
#     stir("cup")
#     serve("chai")
       
   
# make_chai()  



def kettle_has_water():
    return True

def fill_kettle():
    print("Filling kettle")

def plug_in_kettle():
    print("Plugging in kettle")

def boil_water():
    print("Boiling water")

def is_cup_clean():
    return True

def wash_cup():
    print("Washing cup")

def add_to_cup(item):
    print(f"Adding {item}")

def pour(item):
    print(f"Pouring {item}")

def stir(item):
    print(f"Stirring {item}")

def serve(item):
    print(f"Serving {item}")


def make_chai():
    if not kettle_has_water():
        fill_kettle()

    plug_in_kettle()
    boil_water()

    if not is_cup_clean():
        wash_cup()

    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stir("cup")
    serve("chai")

make_chai()  
    
    
    
            