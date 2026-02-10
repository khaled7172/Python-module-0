def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    Normal = seed_type.capitalize()
    if (unit == "packets"):
        print(Normal, "seeds:", quantity, "packets available")
    elif (unit == "grams"):
        print(Normal, "seeds:", quantity, "grams total")
    elif (unit == "area"):
        print(Normal, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
