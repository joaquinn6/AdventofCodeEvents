package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	var matriz = [][]string{{"J", "H", "P", "M", "S", "F", "N", "V"}, {"S", "R", "L", "M", "J", "D", "Q"}, {"N", "Q", "D", "H", "C", "S", "W", "B"}, {"N", "S", "C", "L"}, {"M", "V", "T", "P", "F", "B"}, {"T", "R", "Q", "N", "C"}, {"G", "V", "R"}, {"C", "Z", "S", "P", "D", "L", "R"}, {"D", "S", "J", "V", "G", "P", "B", "F"}}
	var moves = getParameters(fileToArray())
	for _, move := range moves {
		for i := 1; i <= int(move.many); i++ {
			matriz[move.to] = append(matriz[move.to], matriz[move.from][len(matriz[move.from])-1])
			matriz[move.from] = matriz[move.from][:len(matriz[move.from])-1]
		}
	}

	for _, res := range matriz {
		print(res[len(res)-1])
	}
}

func getParameters(movesStr []string) []Moves {
	var moves = []Moves{}
	for _, moveStr := range movesStr {
		var splicedMove = strings.Split(moveStr, " ")
		var move = Moves{many: parseInt(splicedMove[1]), from: parseInt(splicedMove[3]) - 1, to: parseInt(splicedMove[5]) - 1}
		moves = append(moves, move)
	}
	return moves
}

func parseInt(str string) int64 {
	number, _ := strconv.ParseInt(str, 10, 0)
	return number
}

func fileToArray() []string {
	path, _ := os.Getwd()
	f, _ := os.Open(path + "\\input.txt")
	defer f.Close()
	var arr = []string{}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		arr = append(arr, scanner.Text())
	}
	return arr
}

type Moves struct {
	many int64
	from int64
	to   int64
}
