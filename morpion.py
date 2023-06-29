def afficher_morpion2(morpion):
  print('')
  for c in morpion[:3]:
        if(isinstance(c, int)):
          c = '-'
        print(' |',c, end="")
  print('')
  for c in morpion[3:6]:
        if(isinstance(c, int)):
          c = '-'
        print(' |',c, end="")
  print('')
  for c in morpion[6:9]:
        if(isinstance(c, int)):
          c = '-'
        print(' |',c, end="")
  print('')
  print('')

def Win(Grid):
    WinSituation = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

    for i in range(len(WinSituation)):
        TestRow = WinSituation[i]
        RowValues = []

        for j in range(len(TestRow)):
            RowValues.append(Grid[TestRow[j]])

        if all(value == 'X' for value in RowValues):
            return 1
        elif all(value == 'O' for value in RowValues):
            return -1

    return 0

def minimaxNextMoveHard(NewGrid, Player):
    Available = [ carree for carree in NewGrid if isinstance(carree, int) ]

    if (Win(NewGrid) == 1):
        return -1, 1
    if (Win(NewGrid) == -1):
        return -1, -1
    if (len(Available) == 0):
        return -1, 0

    Moves = []
    Scores = []

    for i in range(len(Available)):
        Move = NewGrid[Available[i]]
        NewGrid[Available[i]] = Player

        if (Player == 'X'):
            Scores.append(minimaxNextMoveHard(NewGrid, 'O')[1])
        else:
            Scores.append(minimaxNextMoveHard(NewGrid, 'X')[1])

            NewGrid[Available[i]] = Move
            Moves.append(Move)

    if Player == 'X':
        HighScore = max(Scores)
        HighScoreIndex = Scores.index(HighScore)
        AIMove = Moves[HighScoreIndex]
        # return Scores[HighScoreIndex]
        return AIMove,  Scores[HighScoreIndex] #indice case asina X na O, score max
    else:
        LowScore = min(Scores)
        LowScoreIndex = Scores.index(LowScore)
        AIMove = Moves[LowScoreIndex]
        # return Scores[LowScoreIndex]
        return AIMove, Scores[LowScoreIndex]  #indice case asina X na O, score min


def minimaxNextMoveFacileMoyen(NewGrid, Player, depth = 1):
    Available = [carree for carree in NewGrid if isinstance(carree, int)]

    if Win(NewGrid) == 1:
        return -1, 1
    if Win(NewGrid) == -1:
        return -1, -1
    if len(Available) == 0 or depth == 0:  # Arrête la recherche si la profondeur est atteinte
        return -1, 0

    Moves = []
    Scores = []

    for i in range(len(Available)):
        Move = NewGrid[Available[i]]
        NewGrid[Available[i]] = Player

        if Player == 'X':
            Scores.append(minimaxNextMoveFacileMoyen(NewGrid, 'O', depth - 1)[1])
        else:
            Scores.append(minimaxNextMoveFacileMoyen(NewGrid, 'X', depth - 1)[1])

        NewGrid[Available[i]] = Move
        Moves.append(Move)

    if Player == 'X':
        HighScore = max(Scores)
        HighScoreIndex = Scores.index(HighScore)
        AIMove = Moves[HighScoreIndex]
        return AIMove, Scores[HighScoreIndex]
    else:
        LowScore = min(Scores)
        LowScoreIndex = Scores.index(LowScore)
        AIMove = Moves[LowScoreIndex]
        return AIMove, Scores[LowScoreIndex]


# IA = X
# grid = [0,1,2,3,4,5,6,7,8]
grid = ['X','O', 2 , 3 , 4 , 5 , 6 , 7 ,8]
AI = 'X'
afficher_morpion2(grid)
idNextMove, score = minimaxNextMoveHard(grid, AI)
grid[idNextMove] = AI
afficher_morpion2(grid)

grid = ['X','O', 2 , 'X' , 'X' , 5 , 'O' , 'O' ,8]

idNextMove, score = minimaxNextMoveHard(grid, AI)
grid[idNextMove] = AI
afficher_morpion2(grid)

# IA = O
# grid = [0,1,2,3,4,5,6,7,8]
grid = ['O','X', 2 , 3 , 4 , 5 , 6 , 7 ,8]
AI = 'O'
afficher_morpion2(grid)
idNextMove, score = minimaxNextMoveHard(grid, AI)
grid[idNextMove] = AI
afficher_morpion2(grid)

grid = ['O','X', 2 , 'O' , 4 , 5 , 'X' ,  7 ,8]

idNextMove, score = minimaxNextMoveHard(grid, AI)
grid[idNextMove] = AI
afficher_morpion2(grid)


grid = ['O','X', 2 , 'O' , 'O' , 'X' , 'X' ,  7 ,8]

idNextMove, score = minimaxNextMoveHard(grid, AI)
grid[idNextMove] = AI
afficher_morpion2(grid)