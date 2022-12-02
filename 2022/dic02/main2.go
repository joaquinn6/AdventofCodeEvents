package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func main() {
	var rounds, err = fileToArray()
	if err != nil {
		log.Fatal(err)
	}
	var points = 0
	for _, round := range rounds {
		switch round[1] {
		case "X":
			points += 0
		case "Y":
			points += 3
		case "Z":
			points += 6
		}
		points += result(round)
		// element is the element from someSlice for where we are
	}
	print(points)

}

func result(round []string) int {
	switch round[0] + "-" + round[1] {
	case "A-X":
		return 3
	case "A-Y":
		return 1
	case "A-Z":
		return 2
	case "B-X":
		return 1
	case "B-Y":
		return 2
	case "B-Z":
		return 3
	case "C-X":
		return 2
	case "C-Y":
		return 3
	case "C-Z":
		return 1
	}
	return 0
}

func fileToArray() ([][]string, error) {
	f, err := os.Open("2022/dic02/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	var arr = [][]string{}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		arr = append(arr, strings.Split(scanner.Text(), " "))
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return arr, nil
}
