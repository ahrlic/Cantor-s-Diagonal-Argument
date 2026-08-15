import random
import unittest
from Cantors_Diagonal_Argument import CDAFunction


class testCDAFunction(unittest.TestCase):


    def test_nums(self):

        CDA_Function = CDAFunction()
    
        numbers = [round(random.uniform(0, 1), 12) for _ in range(50)]

        result = CDA_Function.calculate_arguments(numbers)

        print(result)


if __name__ == "__main__":
    unittest.main()
     
        
   