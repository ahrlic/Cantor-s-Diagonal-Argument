
new_number = ""
index = 2
decimal_numbers = [

    "0.123444477283",
    "0.568329991100",
    "0.556622211778",
    "0.000384958697",
    "0.117463209745"
]


for i in range(len(decimal_numbers)): 

    print(decimal_numbers[i])
    print(decimal_numbers[i][index])
    index +=1


    if index == 5:
        new_number += "2"
    else:
        new_number += "5"

new_number = int(new_number)    
    
print("0." + new_number)

