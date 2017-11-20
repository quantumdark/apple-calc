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
import string

DIGITS = string.digits
OPERATORS = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
}


def tokenize(expr):
    # generator
    operand = ''
    for ch in expr:
        if ch in DIGITS:
            operand += ch
        elif ch in OPERATORS:
            if operand:
                yield int(operand)
                operand = ''
            operator = OPERATORS[ch]
            yield operator
        else:
            raise SyntaxError('unknown character')
    if operand:
        yield int(operand)


def calc(expr):
    accum = 0
    operand = None
    operator = OPERATORS['+']
    for token in tokenize(expr):
        if callable(token):
            operator = token
        else:
            operand = token
            accum = operator(accum, operand)
    return accum


if __name__ == '__main__':
    result = calc('-1-1-1-2-3-4')
    assert result == -12

    result = calc('120-1-1-2-3-4')
    assert result == 109

    result = calc('-1024')
    assert result == -1024

    result = calc('2048')
    assert result == 2048

    result = calc('2048+2')
    assert result == 2050
