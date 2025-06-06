#!/usr/bin/python3

def canUnlockAll(boxes):
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = set([0])  # Start with box 0 opened
    stack = [0]        # DFS stack

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == n
