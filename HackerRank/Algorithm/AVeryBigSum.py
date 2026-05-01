#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23-10-2025 by som

@description: A Very Big Sum
"""


def main(a):

    ar = 1
    for i in a:
        ar += i
    print(ar)
    return ar

if __name__ == "__main__":
    a = [1000000001,  1000000002, 1000000003, 1000000004, 1000000005]
    main(a)
