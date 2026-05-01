#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23-10-2025 by som

@description: Compare the Triplets
"""


def main(a, b):
    alice = 0
    bob = 0
    for i, j in zip(a, b):
        if i > j:
            alice += 1
        elif i < j:
            bob += 1
    li = [alice, bob]
    print(li)
    return li

if __name__ == "__main__":
    a = [5,6,7]
    b = [3,6,10]
    main(a, b)
