##Une fonction « newBoard(n) » qui retourne une liste à deux dimensions représentant l’état initial d’un plateau de jeu à n lignes et n colonnes.
def caseSizeSelect():

    n = 0
    while (n < 5) or (n > 20):
        try:
            n = int(input("n ="))
        except ValueError:
            print("une erreur sur n est survenu")
    return n


def newBoard(n):

    board = []
    for i in range(0, n):
        board.append([])
        for x in range(0, n):
            board[i].append(0)

    return board


def playerSelect(n):
    test = True
    while test:
        try:
            i = int(input("ligne select"))
            j = int(input("colone select"))

            if (i >= 1 & i <= n) and (j >= 1 & j <= n):
                return i, j

        except ValueError:
            print("une erreur de valeur a été detecter")


#ne fonction «possibleSquare(board,n,i,j)» qui retourne
#  True si i et j sont les coordonnées d’une case où un joueur peut poser une lettre, et False sinon.

def possibleSquare(board, n, i, j):
    if board[i][j] == 0:
        return True
    else:
        return False


##Une procédure « updateScoreS(board,n,i,j,scores,player,lines) » qui suppose que le joueur player ait posé la lettre « S » sur la case de coordonnées
 ## i et j. Elle recherche alors les éventuels alignements de « SOS » que cela a pu engendrer, et met à jour le score du joueur player et la liste lines.

def updateScoreS(board, n, i, j, scores, player, lines):
    pass



 ##Une procédure « updateScoreO(board,n,i,j,scores,player,lines) » qui suppose que le joueur player ait posé la lettre « O » sur la case de coordonnées i et j.
## Elle recherche alors les éventuels alignements de « SOS » que cela a pu engendrer, et met à jour le score du joueur player et la liste lines.

def updateScoreO(board,n,i,j,scores,player,lines):
    pass


##Une procédure « update(board,n,i,j,l,scores,player,lines) » qui commence par mettre à jour le plateau de jeu en affectant la valeur l à la case
##de coordonnées i et j. Selon les cas elle appelle ensuite l’une des deux procédures précédentes. Lors de l’appel de cette procédure, la liste lines est vide.

def update(board,n,i,j,l,scores,player,lines):
    pass

##Une fonction « winner(scores) » qui retourne une chaîne de caractère indiquant le résultat de la partie.

def winner(scores):
    pass





def main():

    n = caseSizeSelect()
    board = newBoard(n)
    i, j = playerSelect(n)

    possibleSquare(board, n, i, j)



main()
