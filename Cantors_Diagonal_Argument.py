class CDAFunction:

    def calculate_arguments(self, numbers):

        new_number = ""
        index = 2


        for i in range(len(numbers)):

            print(numbers[i])
            print(numbers[i][index])
            index += 1

        if index == 5:
            new_number += "2"
        else:
            new_number += "5"

        new_number = int(new_number)

        print("0." + new_number)
