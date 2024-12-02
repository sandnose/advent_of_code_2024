# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
safe_reports_count = 0
safe_reports_with_dampener_count = 0

with open("data/day2.txt", "r") as data:
    for reports in data:
        levels = reports.strip().split()
        levels = [int(i) for i in levels]

        is_increasing = all(i < j for i, j in zip(levels, levels[1:]))
        is_decreasing = all(i > j for i, j in zip(levels, levels[1:]))

        if not (is_increasing or is_decreasing):
            continue

        adjacent_diff = all(1 <= abs(i - j) <= 3 for i, j in zip(levels, levels[1:]))
        if adjacent_diff:
            safe_reports_count += 1

print("The initial number of safe reports is: ", safe_reports_count)

# part 2


def check_safe_report(levels: list) -> bool:
    """
    Checking the two primary rules
    """
    is_increasing = all(i < j for i, j in zip(levels, levels[1:]))
    is_decreasing = all(i > j for i, j in zip(levels, levels[1:]))
    monotonic = is_increasing or is_decreasing
    adjacent_diff = all(1 <= abs(i - j) <= 3 for i, j in zip(levels, levels[1:]))
    return monotonic and adjacent_diff


def problem_dampener(levels: list) -> bool:
    """
    Removing 1 level from failing report
    Pass if sub_level passes
    """
    # if it just fits then pass true
    if check_safe_report(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if check_safe_report(new_levels):
            return True

    # if the two other returns doesnt ahppen
    return False


with open("data/day2.txt", "r") as data:
    for reports in data:
        levels = reports.strip().split()
        levels = [int(i) for i in levels]

        if problem_dampener(levels):
            safe_reports_with_dampener_count += 1

print(
    "The number of safe reports with problem dampener is: ",
    safe_reports_with_dampener_count,
)
