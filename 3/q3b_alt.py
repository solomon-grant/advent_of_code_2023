with open("input.txt") as fp:
    prev_nums = dict()  # map from indexes of digits to their containing ints for the previous line
    prev_stars = dict()  # map from indexes of stars to list of adjacent numbers (ints) for the previous line
    total = 0
    for line in fp:
        curr_nums = dict()  # map from indexes of digits to their containing ints for the current line
        curr_stars = dict()  # map from indexes of stars to list of adjacent numbers (ints) for the current line
        cursor = 0
        while cursor < len(line):
            char = line[cursor]
            if char == "*":
                curr_stars[cursor] = []
                # if there's an adjacent number on the left, add it to this star
                if cursor - 1 in curr_nums:
                    curr_stars[cursor].append(curr_nums[cursor - 1])
                # if there are any adjacent numbers on the previous line, add them to this star
                j = max(0, cursor - 1)
                while j <= cursor + 1 and j < len(line):
                    if j in prev_nums:
                        curr_stars[cursor].append(prev_nums[j])
                        # don't add the same number more than once
                        j += 1
                        while j in prev_nums:
                            j += 1
                    else:
                        j += 1
                cursor += 1
            elif char.isdigit():
                # parse the whole number and advance the cursor
                start = cursor
                cursor += 1
                while line[cursor].isdigit():
                    cursor += 1
                end = cursor
                num = int(line[start:end])
                # map each digit to the number
                for x in range(start, end):
                    curr_nums[x] = num
                # if there's an adjacent star on the left, add this number to it
                if start - 1 in curr_stars:
                    curr_stars[start - 1].append(num)
                # if there are any adjacent stars on the previous line, add this number to them
                j = max(0, start - 1)
                while j < end + 1 and j < len(line):
                    if j in prev_stars:
                        prev_stars[j].append(num)
                    j += 1
            else:
                cursor += 1
        # extract the relevant product from stars with exactly 2 adjacent numbers
        # we're at the end of the current line, so prev_stars will never be updated again
        for star, nums in prev_stars.items():
            if len(nums) == 2:
                total += nums[0] * nums[1]
        prev_stars = curr_stars
        prev_nums = curr_nums
    # don't forget to tally the last line
    for star, nums in prev_stars.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]

    print(total)
