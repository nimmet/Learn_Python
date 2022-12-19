
travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    }
]

def add_new_country(country,visits,cities):
    log = {
        "country":country,
        "visits":visits,
        "cities":cities
    }
    
    travel_log.append(log)
    
    print("\n\n")
    print(f"You have visited {country} {visits} times.")
    city=""
    for i in cities:
        if i == cities[-1]:
            city += f" and {i}."
        elif i == cities[0]:
            city +=f"{i}"
        else:
            city += f", {i}"
            
    print(f"You have been to {city}")
    print("\n\n")
    

add_new_country("Norway",10,["Oslo","Stavanger","Porsgrunn","Bergin"])

