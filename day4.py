import numpy as np

matrix = []
with open("data/day4.txt", "r") as data:
    for row in data:
        letters = list(row.strip())
        matrix.append(letters)

matrix = np.array(matrix)

word = "XMAS"
word_length = len(word)


def find_word_in_matrix(matrix, word):
    found_positions = []
    rows, cols = matrix.shape

    # horizontal
    for r in range(rows):
        for c in range(cols - word_length + 1):
            # Left-to-right
            if "".join(matrix[r, c : c + word_length]) == word:
                found_positions.append(((r, c), "horizontal"))
            # Right-to-left
            if "".join(matrix[r, c : c + word_length][::-1]) == word:
                found_positions.append(((r, c + word_length - 1), "horizontal_reverse"))

    # vertical
    for r in range(rows - word_length + 1):
        for c in range(cols):
            # Top-to-bottom
            if "".join(matrix[r : r + word_length, c]) == word:
                found_positions.append(((r, c), "vertical"))
            # Bottom-to-top
            if "".join(matrix[r : r + word_length, c][::-1]) == word:
                found_positions.append(((r + word_length - 1, c), "vertical_reverse"))

    # diagonal left
    for r in range(rows - word_length + 1):
        for c in range(cols - word_length + 1):
            # Top-left to bottom-right
            if "".join(matrix[r + i, c + i] for i in range(word_length)) == word:
                found_positions.append(((r, c), "diagonal"))
            # Bottom-left to top-right
            if (
                "".join(
                    matrix[r + word_length - 1 - i, c + i] for i in range(word_length)
                )
                == word
            ):
                found_positions.append(((r + word_length - 1, c), "diagonal_reverse"))

    # diagonal right
    for r in range(rows - word_length + 1):
        for c in range(word_length - 1, cols):
            # Top-right to bottom-left
            if "".join(matrix[r + i, c - i] for i in range(word_length)) == word:
                found_positions.append(((r, c), "diagonal"))
            # Bottom-right to top-left
            if (
                "".join(
                    matrix[r + word_length - 1 - i, c - i] for i in range(word_length)
                )
                == word
            ):
                found_positions.append(((r + word_length - 1, c), "diagonal_reverse"))

    return found_positions


found_positions = find_word_in_matrix(matrix, word)
print(f"Total occurrences of the word '{word}': {len(found_positions)}")

# part 2
# shit så dumt
word = "MAS"
word_length = len(word)


def find_x_word_in_matrix(matrix, word):
    found_positions = []
    rows, cols = matrix.shape

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            try:
                # M.M
                # .A.
                # S.S
                if (
                    matrix[r, c] == "A"
                    and matrix[r - 1, c - 1] == "M"
                    and matrix[r - 1, c + 1] == "M"
                    and matrix[r + 1, c + 1] == "S"
                    and matrix[r + 1, c - 1] == "S"
                ):
                    found_positions.append((r, c))

                # M.S
                # .A.
                # M.S
                if (
                    matrix[r, c] == "A"
                    and matrix[r - 1, c - 1] == "M"
                    and matrix[r - 1, c + 1] == "S"
                    and matrix[r + 1, c + 1] == "S"
                    and matrix[r + 1, c - 1] == "M"
                ):
                    found_positions.append((r, c))

                # S.M
                # .A.
                # S.M
                if (
                    matrix[r, c] == "A"
                    and matrix[r - 1, c - 1] == "S"
                    and matrix[r - 1, c + 1] == "M"
                    and matrix[r + 1, c + 1] == "M"
                    and matrix[r + 1, c - 1] == "S"
                ):
                    found_positions.append((r, c))

                # S.S
                # .A.
                # M.M
                if (
                    matrix[r, c] == "A"
                    and matrix[r - 1, c - 1] == "S"
                    and matrix[r - 1, c + 1] == "S"
                    and matrix[r + 1, c + 1] == "M"
                    and matrix[r + 1, c - 1] == "M"
                ):
                    found_positions.append((r, c))
            except IndexError:
                # dont care
                pass

    return found_positions


found_positions = find_x_word_in_matrix(matrix, word)
print(f"Total occurrences of 'MAS' in X-shapes: {len(found_positions)}")
