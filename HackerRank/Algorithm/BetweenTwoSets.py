#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 28-10-2025 by som

@description: Between Two Sets
"""

import math
def main(a, b):
    l = a[0]
    for i in range(1, len(a)):
        l = (l * a[i]) // math.gcd(l, a[i])

    # Find GCD of list 'b'
    g = b[0]
    for i in range(1, len(b)):
        g = math.gcd(g, b[i])

    # Count numbers that are multiples of l and factors of g
    count = 0
    for i in range(l, g + 1, l):
        if g % i == 0:
            count += 1

    return count



if __name__ == "__main__":
    a = [2, 4]
    b = [16, 32, 96]
    print(main(a, b))
