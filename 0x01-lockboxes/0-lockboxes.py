#!/usr/bin/python3

"""
Problem: You are faced with n locked boxes, each sequentially numbered from 0 to n - 1.
         Each box may contain keys to other boxes.
Task: Write a function to determine if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks whether all boxes can be opened by iterating through the list.
    It returns a boolean value indicating whether the boxes can be opened.

    Parameters:
    - boxes: A list of lists, where each inner list represents a box and its keys.

    Returns:
    - True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    for k in range(1, len(boxes)):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if not boxes_checked:
            return boxes_checked
    return True
