from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

claim1 = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(claim1),
    #Implication(claim1, AKnight),
    Implication(Not(claim1), AKnave),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
claim2 = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(And(AKnight, BKnave), And(AKnave, BKnight)),

    Not(And(AKnight, BKnight)),
    Not(And(AKnave, BKnave)),
    #Implication(claim2, AKnight),
    Implication(Not(claim2), AKnave)

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

claim3 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
claim4 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(And(AKnight, BKnave), And(AKnave, BKnight)),

    Not(And(AKnight, BKnight)),
    Not(And(AKnave, BKnave)),

    Implication(claim3, AKnight),
    #Implication(Not(claim3), AKnave),
    Implication(claim4, BKnight),
    #Implication(Not(claim4), BKnave),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

claim5 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
claim6 = Implication(AKnave, BKnight)
claim7 = Implication(CKnave, BKnight)
claim8 = Implication(AKnight, CKnight)

knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Not(And(AKnight, BKnight, CKnight)),
    Not(And(AKnave, BKnave, CKnave)),

    Implication(claim5, AKnight),
    Implication(claim6, BKnight),
    Implication(claim7, BKnight),
    Implication(claim8, CKnight),


)


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
