

MENU = {
    "espresso": {
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    
    "latte": {
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
    },
        "cost":2.5,
    },
    
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
    },
        "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


answer = input("What would you like? (espresso/latte/cappuccino): ")

if answer == "report":

    
    # for k, v in resources.items:
    #     if k != "Coffee":
    #         print(f"{k.capitalize()}: {v}ml")
    #     elif k == "money":
    #         print(f"Money: ${v}")
            
    #     else:
    #         print(f"{k.capitalize()}: {v}g")