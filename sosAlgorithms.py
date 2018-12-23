
def caseSizeSelect():

    n = 0
    while (n < 5) or (n > 20):
        try:
            n = int(input("n = "))
        except ValueError:
            print("Une erreur sur n est survenu")
    return n


def newBoard(n):

    board = []
    for i in range(0, n):
        board.append([])
        for x in range(0, n):
            board[i].append(0)
    return board


def playerSelect(board, n):
        test = True
        while test:
            i = -1
            j = -1
            while (i<0 or i>=n) or (j<0 or j>=n):
                try:
                    i = int(input("Ligne select = "))-1
                    j = int(input("Colonne select = "))-1
                except ValueError:
                    print("Une erreur de valeur a été detecter")

                if (i<0 or i>=n) and (j<0 or j>=n):
                    print("Valeur en dehors de la map")

            if possibleSquare(board, n, i, j):
                return i, j
# ne fonction «possibleSquare(board,n,i,j)» qui retourne
#  True si i et j sont les coordonnées d’une case où un joueur
#  peut poser une lettre, et False sinon.


def possibleSquare(board, n, i, j):
    if board[i][j] == 0:
        return True
    else:
        print("line already taken")
        return False


def squareLetter(board,n,i,j):
    if possibleSquare(board, n, i, j):
        l = 0
        while l != "s" and l != "o":
            try:
                l = str(input("Selectionner soit s soit o"))
                print(l)
            except:
                print("Une erreur sur la valeur l est intervenu")
        if l == "s":
            return 1
        else:
            return 2

# Une procédure « updateScoreS(board,n,i,j,scores,player,lines) »
# qui suppose que le joueur player ait posé la lettre « S » sur la case de coordonnées
# i et j. Elle recherche alors les éventuels alignements de « SOS »
# que cela a pu engendrer, et met à jour le score du joueur player et la liste lines.


def updateScoreS(board, n, i, j, scores, player, lines):
    pass

# Une procédure « updateScoreO(board,n,i,j,scores,player,lines) » qui
# suppose que le joueur player ait posé la lettre « O » sur la case de coordonnées i et j.
# Elle recherche alors les éventuels alignements de « SOS » que cela
#  a pu engendrer, et met à jour le score du joueur player et la liste lines.


def updateScoreO(board, n, i, j, scores, player, lines):
    pass


# Une procédure « update(board,n,i,j,l,scores,player,lines) »
#  qui commence par mettre à jour le plateau de jeu en affectant la valeur l à la case
# de coordonnées i et j. Selon les cas elle appelle ensuite l’une
#  des deux procédures précédentes. Lors de l’appel de cette
# procédure, la liste lines est vide.

def update(board,n,i,j,l,scores,player,lines):
    board[i][j] = l
    if l == 1:
        updateScoreS(board, n, i, j, scores, player, lines)
    else:
        updateScoreO(board, n, i, j, scores, player, lines)

    return board

# Une fonction « winner(scores) » qui retourne une chaîne de
#  caractère indiquant le résultat de la partie.


def winner(scores):
    pass


def main():

    n = caseSizeSelect()
    board = newBoard(n)

    scores = 0
    lines = []
    player = 0

    play = True
    while play:

        print(board)
        player += 1
        print("Tour du joueur",player)

        i, j = playerSelect(board, n)
        l = squareLetter(board, n, i, j)
        update(board, n, i, j, l, scores, player, lines)

        if player == 2:
            player = 1


main()
