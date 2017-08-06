import sys

funcs = {
    "0": lambda stack, i: [stack + [0], i],
    "1": lambda stack, i: [stack + [1], i],
    "2": lambda stack, i: [stack + [2], i],
    "3": lambda stack, i: [stack + [3], i],
    "4": lambda stack, i: [stack + [4], i],
    "5": lambda stack, i: [stack + [5], i],
    "6": lambda stack, i: [stack + [6], i],
    "7": lambda stack, i: [stack + [7], i],
    "8": lambda stack, i: [stack + [8], i],
    "9": lambda stack, i: [stack + [9], i],
    "+": lambda stack, i: [stack[:-2] + [stack[-2] + stack[-1]], i],
    "-": lambda stack, i: [stack[:-2] + [stack[-2] - stack[-1]], i],
    "*": lambda stack, i: [stack[:-2] + [stack[-2] * stack[-1]], i],
    "/": lambda stack, i: [stack[:-2] + [stack[-2] / stack[-1]], i],
    "^": lambda stack, i: [stack[:-2] + [stack[-2] ** stack[-1]], i],
    "<": lambda stack, i: [stack + [int(input())], i],
    ">": lambda stack, i: print(stack[-1]) or [stack, i],
    "x": lambda stack, i: [stack[:-1], i],
    "X": lambda stack, i: [[], i],
    "?": lambda stack, i: [stack, i + bool(stack[-1])],
    "!": lambda stack, i: [stack, i + 1 - bool(stack[-1])],
    "@": lambda stack, i: [stack, stack[-1]]
}

def run_code(code):
    i = 0
    stack = []
    
    while i < len(code):
        stack,i = funcs[code[i]](stack, i)
        i += 1
    
    return stack
