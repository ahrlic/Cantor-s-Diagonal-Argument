import random
import unittest
from Cantors_Diagonal_Argument import CDAFunction


class testCDAFunction():


    def test_nums():

        #CDAFunction = CDAFunction()

        numbers = [round(random.uniform(0, 1), 12) for _ in range(50)]
    
        print(numbers)


    test_nums()
     
        
   