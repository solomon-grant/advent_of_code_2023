package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed input.txt
var input string

func getInts(line string) []int {
	strs := strings.Split(strings.Trim(line, "\n"), " ")
	ints := make([]int, len(strs))
	for i, str := range strs {
		ints[i], _ = strconv.Atoi(str)
	}
	return ints
}

func diff(nums []int) int {
	done := true
	for _, n := range nums {
		if n != 0 {
			done = false
			break
		}
	}
	if done {
		return 0
	}

	diffs := make([]int, len(nums)-1)
	for i, n := range nums[0 : len(nums)-1] {
		diffs[i] = nums[i+1] - n
	}
	return nums[len(nums)-1] + diff(diffs)
}

func main() {
	lines := strings.Split(input, "\n")
	sum := 0
	for _, line := range lines {
		sum += diff(getInts(line))
	}
	fmt.Println(sum)
}
