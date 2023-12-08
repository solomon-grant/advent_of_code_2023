package main

import (
	_ "embed"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

//go:embed example.txt
var example string

//go:embed input.txt
var input string

type Hand struct {
	cards string
	bet   int
}

func parseHand(line string) Hand {
	split := strings.Split(line, " ")
	bet, err := strconv.Atoi(strings.Trim(split[1], "\n"))
	if err != nil {
		panic(err)
	}

	return Hand{
		cards: split[0],
		bet:   bet,
	}
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func countCards(hand Hand) []int {
	counts := make(map[rune]int)
	jokers := 0
	for _, char := range hand.cards {
		if char == 'J' {
			jokers += 1
		} else {
			counts[char] += 1
		}
	}

	if len(counts) == 0 {
		return []int{5}
	}

	sorted := make([]int, len(counts))
	i := 0
	for _, count := range counts {
		sorted[i] = count
		i += 1
	}
	sort.Sort(sort.Reverse(sort.IntSlice(sorted)))
	sorted[0] += jokers
	return sorted
}

var cardMap = map[string]int{
	"A": 14,
	"K": 13,
	"Q": 12,
	"J": 1,
	"T": 10,
	"9": 9,
	"8": 8,
	"7": 7,
	"6": 6,
	"5": 5,
	"4": 4,
	"3": 3,
	"2": 2,
}

func compareCards(cards1, cards2 string) bool {
	for i := 0; i < len(cards1); i++ {
		card1 := string(cards1[i])
		card2 := string(cards2[i])
		if card1 != card2 {
			return cardMap[card1] < cardMap[card2]
		}
	}
	return true // never get here
}

func compareHands(h1, h2 Hand) bool {
	counts1 := countCards(h1)
	counts2 := countCards(h2)
	if counts1[0] < counts2[0] {
		return true
	}
	if counts1[0] > counts2[0] {
		return false
	}
	if len(counts1) > 1 && len(counts2) > 1 {
		if counts1[1] < counts2[1] {
			return true
		}
		if counts1[1] > counts2[1] {
			return false
		}
	}
	return compareCards(h1.cards, h2.cards)
}

func mainE(file string) error {
	lines := strings.Split(file, "\n")
	var hands []Hand
	for _, line := range lines {
		hands = append(hands, parseHand(line))
	}
	sort.Slice(hands, func(i, j int) bool {
		return compareHands(hands[i], hands[j])
	})
	sum := 0
	for i, hand := range hands {
		sum += hand.bet * (i + 1)
	}
	fmt.Println(sum)
	return nil
}

func main() {
	err := mainE(example)
	if err != nil {
		panic(err)
	}

	err = mainE(input)
	if err != nil {
		panic(err)
	}
}
