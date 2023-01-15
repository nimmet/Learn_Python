test = {
    "espresso": {
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    }
}

for k,v in test.items():
    print(k)
    print("+"*30)
    for a,b in v.items():
        if a == "ingredients":
            for m,n in b.items():
                print(m,n)
        # print(a,b)
        # # for m,n in b["ingredients"].items():
        # #     print(m,n)