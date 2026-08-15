class CDAFunction:

    def calculate_arguments(self, numbers):

        new_number = ""
        index = 2

        for i in range(len(numbers)):

            number = str(numbers[i])

            print(number)
            print(number[index])

            index += 1

        if index == 5:
            new_number += "2"
        else:
            new_number += "5"

        print("0." + new_number)