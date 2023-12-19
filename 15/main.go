package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Label struct {
	Prefix string
	Number int
}

func hash(s string) int {
	val := 0
	for c := range s {
		val += int(c)
		val *= 17
		val %= 256
	}
	return val
}

func main() {
	bts, err := os.ReadFile("/Users/solomon/repos/advent_of_code_2023/15/input.txt")
	if err != nil {
		panic(err)
	}
	codes := strings.Split(string(bts), ",")
	hashmap := make(map[int][]*Label)
	for _, code := range codes {
		for i, c := range code {
			if c == '=' {
				prefix := code[:i]
				labels := hashmap[hash(prefix)]
				number, _ := strconv.Atoi(code[i+1:])
				found := false
				for _, label := range labels {
					if label.Prefix == prefix {
						label.Number = number
						found = true
						break
					}
				}
				if !found {
					labels = append(labels, &Label{prefix, number})
				}
			}
			if c == '-' {
				prefix := code[:i]
				labels := hashmap[hash(prefix)]
				idx := -1
				for i, label := range labels {
					if label.Prefix == prefix {
						idx = i
						break
					}
				}
				if idx < 0 {
					continue
				}
				labels = append(labels[:idx], labels[idx+1:]...)
			}
		}

	}
	total := 0
	for i := 0; i < 256; i++ {
		for j, label := range hashmap[i] {
			total += (i + 1) * (j + 1) * label.Number
		}
	}
	fmt.Println(total)
}
