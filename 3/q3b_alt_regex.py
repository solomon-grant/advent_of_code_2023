import re

regex = re.compile(r"(\*)|(\d+)")
STAR_GROUP = 1
NUM_GROUP = 2

with open("input.txt") as fp:
    prev_nums = dict()  # map from indexes of digits to their containing Match for the previous line
    prev_stars = dict()  # map from indexes of stars to list of adjacent numbers Match for the previous line
    total = 0
    for line in fp:
        curr_nums = dict()  # map from indexes of digits to their containing Match for the current line
        curr_stars = dict()  # map from indexes of stars to list of adjacent number Match for the current line
        for match in regex.finditer(line):
            start, end = match.span()
            if match.group(STAR_GROUP) is not None:
                curr_stars[start] = []
                # if there's an adjacent number on the left, add its Match to this star
                if start - 1 in curr_nums:
                    curr_stars[start].append(curr_nums[start - 1])
                # if there are any adjacent numbers on the previous line, add them to this star
                j = start - 1
                while j < end + 1:
                    if j in prev_nums:
                        curr_stars[start].append(prev_nums[j])
                        # don't add the same number more than once
                        j = prev_nums[j].end()
                    else:
                        j += 1
            elif match.group(NUM_GROUP) is not None:
                # map each digit to the Match object
                for x in range(start, end):
                    curr_nums[x] = match
                # if there's an adjacent star on the left, add this number to it
                if start - 1 in curr_stars:
                    curr_stars[start - 1].append(match)
                # if there are any adjacent stars on the previous line, add this number to them
                for j in range(start - 1, end + 1):
                    if j in prev_stars:
                        prev_stars[j].append(match)
        # extract the relevant product from stars with exactly 2 adjacent numbers
        # we're at the end of the current line, so prev_stars will never be updated again
        for star, nums in prev_stars.items():
            if len(nums) == 2:
                total += int(nums[0].group(NUM_GROUP)) * int(nums[1].group(NUM_GROUP))
        prev_stars = curr_stars
        prev_nums = curr_nums
    # don't forget to tally the last line
    for star, nums in prev_stars.items():
        if len(nums) == 2:
            total += int(nums[0].group(NUM_GROUP)) * int(nums[1].group(NUM_GROUP))

    print(total)
