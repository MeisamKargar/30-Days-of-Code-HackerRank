#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # Read the integer input

    # Step 1: Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]

    # Step 2: Split the binary string by '0' to get sequences of '1's
    consecutive_ones = binary_representation.split('0')

    # Step 3: Find the length of the longest sequence of '1's
    max_consecutive_ones = max(len(seq) for seq in consecutive_ones)

    # Print the result
    print(max_consecutive_ones)

        
        
        
        
