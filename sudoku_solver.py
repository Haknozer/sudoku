import requests
from bs4 import BeautifulSoup
from selenium import webdriver

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

def get_sudoku(board):
    url = "https://east.websudoku.com/"

    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source,"html.parser")
    table = soup.find_all("table",{"id" : "puzzle_grid"})
    input = table[0].find_all("input")

    inputCounter = 0
    for boR in range(9):
        for boC in range(9):
            if input[inputCounter].get("value"):
                board[boR][boC] = int(input[inputCounter].get("value"))
            else:
                board[boR][boC] = 0

            inputCounter += 1 

def sudoku_print(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print("------------------------------------")
        

        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(board[x][y])
            else:
                print(board[x][y], " ", end="")


def find_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x,y) 

    return None

def control(board,number,position):

    for x in range(len(board)):
        if board[position[0]][x] == number and position[1] != x:
            return False

    for y in range(len(board)):
        if board[y][position[1]] == number and position[0] != y:
            return False    

    row = position[1] // 3
    column = position[0] // 3

    for z in range(column * 3 , column * 3 + 3):
        for j in range(row * 3 , row * 3 + 3):
            if board[z][j] == number and (z,j) != position:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    for x in range(1,10):
        if control(board,x,empty):
            board[empty[0]][empty[1]] = x

            if solve(board):
                return True
            
            board[empty[0]][empty[1]] = 0

    return False   

get_sudoku(board)
print("\n \n \n")
sudoku_print(board)
solve(board)
print("\n \n \n")
sudoku_print(board)

while(True):
    print("Çıkmak için enter'a basın")

    if input() == "":
        break
