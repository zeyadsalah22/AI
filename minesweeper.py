import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        if len(self.cells)== self.count and self.count!=0:
            return self.cells
        return set()
        """
        Returns the set of all cells in self.cells known to be mines.
        """


    def known_safes(self):
        if self.count==0:
            return self.cells
        return set()
        """
        Returns the set of all cells in self.cells known to be safe.
        """

    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count-=1

        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """

    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)

        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        self.moves_made.add(cell)
        self.mark_safe(cell)
        sen = set()
        cm = 0
        for i in range(-1,2):
            for j in range(-1,2):
                x = cell[0]+i
                y = cell[1]+j
                if (x,y) in self.mines:
                    cm+=1
                if (x,y) not in self.moves_made and (x,y) not in self.safes and (x,y) not in self.mines and -1<x<self.height and -1<y<self.width:
                    sen.add((x,y))
        sentence = Sentence(sen,count-cm)
        self.knowledge.append(sentence)
        for t in self.knowledge:
            if t.known_mines():
                for cell in t.known_mines().copy():
                    self.mark_mine(cell)
            elif t.known_safes():
                    for cell in t.known_safes().copy():
                        self.mark_safe(cell)
        for s in self.knowledge:
            if sentence.cells.issubset(s.cells) and sentence.count>0 and s.count>0 and sentence.cells!=s.cells:
                news = s.cells-sentence.cells
                newss = Sentence(news,s.count-sentence.count)
                self.knowledge.append(newss)
            elif s.cells.issubset(sentence.cells) and len(sentence.cells)>0 and len(s.cells)>0 and sentence.cells!=s.cells:
                news = sentence.cells-s.cells
                newss = Sentence(news,sentence.count-s.count)
                self.knowledge.append(newss)


        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None

    def make_random_move(self):
        p = []
        for i in range(self.height):
            for j in range(self.width):
                if (i,j) not in self.moves_made and (i,j) not in self.mines:
                    p.append((i,j))
        if len(p)==0:
            return None
        else:
            return random.choice(p)

        """""
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

