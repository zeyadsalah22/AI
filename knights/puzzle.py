from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)),Biconditional(Not(And(AKnight,AKnave)),AKnave),Biconditional( And(AKnight,AKnave),AKnight))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(Or(BKnight,BKnave),Not(And(BKnight,BKnave)),Or(AKnight,AKnave),Not(And(AKnight,AKnave)),Biconditional(And(AKnave,BKnave),AKnight),Biconditional(Not(And(AKnave,BKnave)),AKnave),Biconditional(Not(And(AKnave,BKnave)),BKnight),Biconditional(And(AKnave,BKnave),BKnave))


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(Or(BKnight,BKnave),Not(And(BKnight,BKnave)),Or(AKnight,AKnave),Not(And(AKnight,AKnave)),Biconditional(Not(Not(Or(And(AKnight,BKnight),And(AKnave,BKnave)))),BKnave),Biconditional(Not(Or(And(AKnight,BKnight),And(AKnave,BKnave))),BKnight),Biconditional(Not(Or(And(AKnight,BKnight),And(AKnave,BKnave))),AKnave),Biconditional(Or(And(AKnight,BKnight),And(AKnave,BKnave)),AKnight))

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(Biconditional(AKnight,Or(AKnight,AKnave)),Biconditional(AKnave,Not(Or(AKnight,AKnave))),
Or(BKnight,BKnave),Not(And(BKnight,BKnave)),
Or(CKnight,CKnave),Not(And(CKnight,CKnave)),
Or(AKnight,AKnave),Not(And(AKnight,AKnave)),
Biconditional(Not(AKnight),CKnave),Biconditional(AKnight ,CKnight),
Biconditional(Not(CKnave),BKnave),Biconditional(CKnave ,BKnight),
Or(Biconditional(BKnight,Or(Biconditional(AKnight,AKnave),Biconditional(AKnave,AKnight))),Biconditional(BKnave,Not(Or(Biconditional(AKnight,AKnave),Biconditional(AKnave,AKnight))))))
    # TODO



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
