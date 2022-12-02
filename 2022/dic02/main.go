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
			points += 1
		case "Y":
			points += 2
		case "Z":
			points += 3
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
		return 6
	case "A-Z":
		return 0
	case "B-X":
		return 0
	case "B-Y":
		return 3
	case "B-Z":
		return 6
	case "C-X":
		return 6
	case "C-Y":
		return 0
	case "C-Z":
		return 3
	}
	return 0
}

func fileToArray() ([][]string, error) {
	f, err := os.Open("C:/Users/joaqu/proyectos/personales/AdventofCodeEvents/2022/dic02/input.txt")
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
