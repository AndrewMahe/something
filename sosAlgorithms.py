# NOTE BUG :
# - out of range quand je tape 5-5 et ensuite S
#   Elle sont au niveau de "updateScoreS


#Note random
# i = ligne
# j = colonne




def display(board,n):                                   #FINI
    for i in range(0,n):
        print(" ")
        for x in range(0,n):
            print(board[i][x],end=" ")

    print(" ")

#Initialisation du nombre de ligne/colonne
def caseSizeSelect():                                   #FINI
    n = 0
    while (n < 5) or (n > 20):
        #Verification - Eviter les erreurs (Pas de string) 
        try:
            n = int(input("Combien de taille fera votre carré (Entre 5 et 20) ? "))
            #Vérification - Chiffre trop petit
            if (n<5) or (n>20):
                print("Votre chiffre est trop petit")
        except ValueError:
            print("Merci de bien vouloir taper un nombre.")
    return n


#Creation du tableau de jeu
def newBoard(n):                                        #FINI
    board = []
    for i in range(0, n):
        board.append([])
        for x in range(0, n):
            board[i].append(0)
    return board

#Selection du joueur 
def playerSelect(board, n):                             #Pas fini
        test = True
        while test:
            i = -1
            j = -1
            while (i<0 or i>=n) or (j<0 or j>=n):
                try:
                    i = int(input("Selection de la ligne : "))-1
                    j = int(input("Selection de la colonne :  "))-1
                    print("i - ",i)
                    print("j - ",j)
                except ValueError:
                    print("Merci de bien vouloir taper un nombre.")

            if possibleSquare(board, n, i, j):
                return i, j
# ne fonction «possibleSquare(board,n,i,j)» qui retourne
#  True si i et j sont les coordonnées d’une case où un joueur
#  peut poser une lettre, et False sinon.

def possibleSquare(board, n, i, j):                     #FINI
    if board[i][j] == 0:
        return True
    else:
        print("Impossible de choisir cette case")
        return False

def squareLetter(board,n,i,j):
    if possibleSquare(board, n, i, j):
        l = 0
        while l != "s" and l != "o":
            #Verification - Eviter les erreurs.
            try:
                l = str(input("Selectionner S ou O : "))
                                
            except:
                print("Une erreur sur la valeur l est intervenu")
                
            #Vérification - Message pour signaler que la lettre n'est pas bonne
            if l != "s" and l != "o":
                    print("ERREUR ! Votre lettre n'est pas la bonne")
                    print("L - ", l)
        if l == "s":
            return 1
        elif l == "o":
            return 2
        

# Une procédure « updateScoreS(board,n,i,j,scores,player,lines) »
# qui suppose que le joueur player ait posé la lettre « S » sur la case de coo3rdonnées
# i et j. Elle recherche alors les éventuels alignements de « SOS »
# que cela a pu engendrer, et met à jour le score du joueur player et la liste lines.

def updateScoreS(board, n, i, j, scores, player, lines):
    return lines
    

# Une procédure « updateScoreO(board,n,i,j,scores,player,lines) » qui
# suppose que le joueur player ait posé la lettre « O » sur la case de coordonnées i et j.
# Elle recherche alors les éventuels alignements de « SOS » que cela
#  a pu engendrer, et met à jour le score du joueur player et la liste lines.

def updateScoreO(board,n,i,j,scores,player,lines):
    #check les case gauche puis leur opposer si positif
    #Haut gauche

    liste_position = -1

    if player == 1:
        liste_position = 0

    else:
        liste_position = 1


    if (i-1>=0 and j-1>=0) and board[i - 1][j - 1] == 1 and board[i + 1][j + 1] == 1:
        lines[liste_position].append(((i - 1,j - 1),(i + 1, j + 1)))


    #haut mid
    if i-1>=0 and board[i - 1][j] == 1 and board[i + 1][j] == 1:
        lines[liste_position].append(((i - 1, j), (i + 1, j)))
    #mid gauche
    if j-1>=0 and board[i][j - 1] == 1 and board[i][j + 1] == 1:
        lines[liste_position].append(((i, j - 1), (i, j + 1)))
    #bas gauche

    if (i+1<n and j-1>=0) and board[i + 1][j - 1] == 1 and j+1<n and board[i + 1][j + 1] == 1:
        lines[liste_position].append(((i + 1, j - 1), (i + 1, j + 1)))
    print(lines)
    return lines

# Une procédure « update(board,n,i,j,l,scores,player,lines) »
#  qui commence par mettre à jour le plateau de jeu en affectant la valeur l à la case
# de coordonnées i et j. Selon les cas elle appelle ensuite l’une
#  des deux procédures précédentes. Lors de l’appel de cette
# procédure, la liste lines est vide.

def update(board,n,i,j,l,scores,player,lines):
    board[i][j] = l
    if l == 1:
        lines = updateScoreS(board, n, i, j, scores, player, lines)
    else:
        lines = updateScoreO(board,n,i,j,scores,player,lines)

    print(lines, "lines", scores, "scores")
    liste_position = -1

    if player == 1:
        liste_position = 0

    else:
        liste_position = 1

    scores[liste_position] = len(lines[liste_position])
    return lines, scores


# Une fonction « winner(scores) » qui retourne une chaîne de
#  caractère indiquant le résultat de la partie.

def winner(scores):
    pass


def main():

    n = caseSizeSelect()
    board = newBoard(n)

    scores = [[], []]
    lines = [[],[]]
    player = 1

    play = True
    while play:

        display(board,n)
        print("Tour du joueur",player)

        i, j = playerSelect(board, n)
        l = squareLetter(board, n, i, j)
        lines, scores = update(board, n, i, j, l, scores, player, lines)
        print(lines,"lines", scores, "scores")

        player += 1
        print(player)
        if player == 3:
            player = 1


main()
