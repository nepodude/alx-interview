#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of lists): Each index represents a box, and contains a list of keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

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
