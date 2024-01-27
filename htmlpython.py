def calculate_pizzas(individuals):
    slices_per_large = 8
    slices_per_medium = 6
    slices_per_regular = 4
    slices_per_small = 1

    large_pizzas = individuals // slices_per_large
    individuals %= slices_per_large

    medium_pizzas = individuals // slices_per_medium
    individuals %= slices_per_medium

    regular_pizzas = individuals // slices_per_regular
    individuals %= slices_per_regular

    small_pizzas = individuals // slices_per_small


    total_individuals = (large_pizzas * slices_per_large) + (medium_pizzas * slices_per_medium) + \
                        (regular_pizzas * slices_per_regular) + (small_pizzas * slices_per_small)

    return large_pizzas, medium_pizzas, regular_pizzas, small_pizzas, total_individuals

num_individuals = 100
result = calculate_pizzas(num_individuals)
print(f"If there are {num_individuals} individuals:")
print(f"1. we will have {result[0]} Large pizza")
print(f"2. we will have {result[1]} Medium pizza")
print(f"3. we will have {result[2]} Regular Pizza")
print(f"4. we will have {result[3]} Small Pizza")
print(f"\nTotal individuals based on pizza distribution: {result[4]}")
