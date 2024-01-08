
import sys

# # # #  POKER SQUARES SCORER (English Point System)  # # # #
# DEVELOPED June 9th, 2023 by AYDEN PARSONS (SIRPICKLJOHN) #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# I think the easiest way to check a row/column is to use the count method, then scoring based on numbers
# i.e. if 3 fives and 2 tens in row1, register it as a royal flush and score accordingly

total_score = 0

# first five digits are cards
# last two digits are flushes and straights, respectively
# t = 10
try:
    nonsense = sys.argv[1]
except IndexError:
    print("POKER SQUARES 1.0 ~ You forgot to add parameters!")
    print("Add them like this: 225AQyn, where yn indicate the existence of a flush or straight, respectively.")
    print("You will need to add 10 parameters, starting from Row One to Column Five")
    sys.exit(0)
try:
    row1 = sys.argv[1]
    row2 = sys.argv[2]
    row3 = sys.argv[3]
    row4 = sys.argv[4]
    row5 = sys.argv[5]
    column1 = sys.argv[6]
    column2 = sys.argv[7]
    column3 = sys.argv[8]
    column4 = sys.argv[9]
    column5 = sys.argv[10]
except IndexError:
    print("Wrong Number of Arguments!")
    sys.exit(0)

twos = 0;
threes = 0;
fours = 0;
fives = 0;
sixes = 0;
sevens = 0;
eights = 0;
nines = 0;
tens = 0;
jacks = 0;
queens = 0;
kings = 0;
aces = 0;

# make an array instead for iteration and removal of redundancy
cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# i.e. jacks = cards[9], twos = cards[0] (subtracted two because of arrays starting at 0, AND because cards start at 2 and not 1)

def scorer(line):
    for i in line:
        if i == '2':
            cards[0] += 1;
        if i == '3':
            cards[1] += 1;
        if i == '4':
            cards[2] += 1;
        if i == '5':
            cards[3] += 1;
        if i == '6':
            cards[4] += 1;
        if i == '7':
            cards[5] += 1;
        if i == '8':
            cards[6] += 1;
        if i == '9':
            cards[7] += 1;
        if i == 't':
            cards[8] += 1;
        if i == 'J':
            cards[9] += 1;
        if i == 'Q':
            cards[10] += 1;
        if i == 'K':
            cards[11] += 1;
        if i == 'A':
            cards[12] += 1;
        if i == 'y' or i == 'n':
            break

def LINE_SCORER(line): # rows and lines are named the same because I am tired
    royal_flushes = False;
    straight_flushes = False;
    four_of_a_kinds = 0;
    full_houses = 0;
    flushes = False;
    straights = False;
    three_of_a_kinds = 0;
    pairs = 0;

    global total_score
    global cards
    line_score = 0
    scorer(line) # COUNTS CARD FREQUENCIES

    ####################################################

    ## DETERMINES NUMBER OF FLUSHES AND STRAIGHTS
    if cards[8] == 1 and cards[9] == 1 and cards[10] == 1 and cards[11] == 1 and cards[12] == 1 and line[5] == 'y': # ROYAL FLUSH (manually checks)
            royal_flushes = True;
            print("ROYAL FLUSH!")
    elif line[5] == 'y' or line[6] == 'y': # if flush OR straight happened...start new series of checks
        if line[5] == 'y' and line[6] == 'y': # STRAIGHT FLUSH
            straight_flushes = True;
        elif line[5] == 'y' or line[6] == 'y': # if not a straight flush...continue checks
            if line[5] == 'y': # FLUSH
                flushes = True;
            if line[6] == 'y': # STRAIGHT
                straights = True;

    ## DETERMINES NUMBER OF FOURS, THREES, AND PAIRS ##
    x = 0
    while x < len(cards):
        #print("card " + str(x)) # testing purposes
        if cards[x] == 4: #four of a kind
            four_of_a_kinds += 1;
            break # can only have 1
        if cards[x] == 3: #three of a kind
            three_of_a_kinds += 1;
            break # can only have 1
        if cards[x] == 2:
            pairs += 1;
        x += 1

    ## DETERMINES SCORE FOR LINE ##
    if royal_flushes == True: # FLUSHES AND STRAIGHT SCORING
        line_score += 30
    elif straight_flushes == True:
        line_score += 30
    elif flushes == True or straights == True:
        if flushes == True:
            line_score += 5
        if straights == True:
            line_score += 12

    if four_of_a_kinds == 1: # FOUR OF A KIND SCORING
        line_score += 16

    if three_of_a_kinds == 1 and pairs == 1: # FULL HOUSE, THREE OF A KIND AND LOWER SCORING
        full_houses += 1;
        line_score += 10;
    elif three_of_a_kinds != 0 or pairs != 0:
        if three_of_a_kinds == 1:
            line_score += 6
        if pairs == 2: # Double Pair
            line_score += 3
        elif pairs == 1: # Pair
            line_score += 1


    print("\nLine Values: " + str(list(line)))
    print("Royal Flush? " + str(royal_flushes))
    print("Straight Flush? " + str(straight_flushes))
    print("Four of a Kinds: " + str(four_of_a_kinds))
    print("Full Houses: " + str(full_houses))
    print("Flush? " + str(flushes))
    print("Straight? " + str(straights))
    print("Three of a Kinds: " + str(three_of_a_kinds))
    print("Pairs: " + str(pairs))
    print("## Total Line Score: " + str(line_score) + " ##")

    total_score += line_score

    # VALUE RESETS
    for z in cards:
        cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#print("\nRow 1: "+ str(list(row1)))
LINE_SCORER(row1)
LINE_SCORER(row2)
LINE_SCORER(row3)
LINE_SCORER(row4)
LINE_SCORER(row5)
LINE_SCORER(column1)
LINE_SCORER(column2)
LINE_SCORER(column3)
LINE_SCORER(column4)
LINE_SCORER(column5)
print("\n~~~~~~~~~~\n FINAL SCORE: " + str(total_score) + "\n~~~~~~~~~~")
#print("\n~~~~~~~~~~~~~~~\nTotal Score Row One: " + str(total_score) + "\n~~~~~~~~~~~~~~~")
