"""
Daily Coding Problem - Problem #63 (Microsoft)

Given a 2D matrix of characters and a target word, write a function
that returns whether the word can found in the matrix by going left-to-right,
or up-to-down
"""

def word_in_row(mat, word, row):
    last_matched_index = -1
    for col in range(len(mat[0])):
        if mat[row][col] is word[last_matched_index+1]:
            last_matched_index += 1
        else:
            last_matched_index = -1
        if last_matched_index == len(word) - 1:
            return True
    return False

def word_in_col(mat, word, col):
    last_matched_index = -1
    for row in range(len(mat)):
        if mat[row][col] is word[last_matched_index+1]:
            last_matched_index += 1
        else:
            last_matched_index = -1
        if last_matched_index == len(word) - 1:
            return True
    return False

def word_in_matrix(mat, word):
    for row in range(len(mat)):
        if word_in_row(mat, word, row):
            return True
    for col in range(len(mat[0])):
        if word_in_col(mat, word, col):
            return True
    return False
