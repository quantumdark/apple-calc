#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem: Given an input such as “1+2-3” or “-1+2”, please evaluate and return
result like a calculator. The examples earlier would return 0 and 1,
respectively.

Limitation: only need to handle + or - operators (no
multiplication/division/parenthesis or any other operator), input is
well-formed with alternating operand/operator so no error checking is needed,
please do not use any built-in calculator function.
"""
import argparse
import string

DIGITS = string.digits
OPERATORS = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
}


def calc(expr):
    accum = 0
    operator = OPERATORS['+']
    for ch in expr:
        if ch in DIGITS:
            operand = ord(ch) - ord('0')  # char to int
            accum = operator(accum, operand)
        elif ch in OPERATORS:
            operator = OPERATORS[ch]
        else:
            raise SyntaxError('unknown character')
    return accum


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('expression')
    # args = parser.parse_args()
    # result = calc(args.expression)
    result = calc('-1-1-1-2-3-4')  # 12
    print('result: %s' % result)
