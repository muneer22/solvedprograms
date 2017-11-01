def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())
    
    # calculation code
    tax = meal_cost * tip_percent/100
    tip = meal_cost * tax_percent/100

    # result in round 
    total_cost = int(round(meal_cost + tax + tip))

    return str(total_cost)


   # print result
print(get_total_cost_of_meal())
