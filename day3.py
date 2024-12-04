import re

with open("data/day3.txt", "r") as data:
    corrupted_str = data.readlines()

regexp_pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),\s*(\d{1,3})\))"
instruction_result = 0
enabled = True

for corrupted_part in corrupted_str:
    real_instructions = re.findall(regexp_pattern, corrupted_part)

    for part in real_instructions:
        command = part[0]

        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif command.startswith("mul") and enabled:
            instruction_result += int(part[1]) * int(part[2])

print("Added multiplications equal: ", instruction_result)
