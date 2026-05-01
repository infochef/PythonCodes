#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24-10-2025 by som

@description: 
"""


def main(c):
    sorted_li = sorted(c)
    count = 0
    for i in sorted_li:
        if i == sorted_li[-1]:
            count += 1
    print(count)


if __name__ == "__main__":
    candles = [3,2,1,3,4,4]
    main(candles)
