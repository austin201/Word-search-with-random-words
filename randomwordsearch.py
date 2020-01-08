import random
questions = ["What are is it called when you have a decimal in your integer?",
             "What are positive or negative whole numbers?",
             "How do you bring in other modules?",
             "How do you exit a loop?",
             "What has square brakets around it([])?",
             "What has parenthesis around them(())?",
             "What is inside double quotes?",
             "What gets asigned a value?",
             "How do you get the users answer?",
             "What is while True?",
             "How do you display something onto the screen?",
             "An error that breaks the program befor it runs?",
             "What results in incorrect or unexpected behavior?",
             "An _____ is a data structure, which can store a fixed-size collection of elements.",
             "What is ____ or false.",
             "That was a _____ statement. Hint(What is the oposite of true)",
             "To ___________ means to merge two things together.",
             "An __ _________ is a programming conditional statement that, if proved true, performs a function or displays information.",
             "What is a module that can be imported?",
             "The ________ _________ in python returns the control to the beginning of the while loop."]
nine_letter_words = ["BLUEPRINT", "CHEMISTRY", "TRUCKLOAD"]
word_3 = random.choice(nine_letter_words)

seven_letter_words = ["TRAINED", "TRAINEE"]
word_2 = random.choice(seven_letter_words)

four_letter_words =["CLAM", "COCO", "SLAM", "DUNK", "MAMA"]
word = random.choice(four_letter_words)
A = word[0]
B = word[1]
C = word[2]
D = word[3]
E = word_2[0]
F = word_2[1]
G = word_2[2]
H = word_2[3]
I = word_2[4]
J = word_2[5]
K = word_2[6]
L = word_3[0]
M = word_3[1]
N = word_3[2]
O = word_3[3]
P = word_3[4]
Q = word_3[5]
R = word_3[6]
S = word_3[7]
T = word_3[8]
U = "U"
V = "V"
W = "W"
X = "X"
Y = "Y"
Z = "Z"
# MAKE SURE TO MAKE THE PUZZLE FLAT WHEN YOU ARE FINISHED WITH YOUR WORDS
PUZZLE = """
"""+A+""" """+B+""" """+C+""" """+D+""" M E T D Z F P S M A N D P A B J M N V N S T J
K O A K H H M R R M Y A X O L E D K A W I G G Y G G H
V U R V Y F A I G L P L T O E X R E S L A F X C R S H
B Q B R Y N I N W E I Z F L P F O F Z Y H X M C H U X
"""+E+""" """+F+""" """+G+""" """+H+""" """+I+""" """+J+""" """+K+""" R A G Y R M C L H J S """+L+""" """+M+""" """+N+""" """+O+""" """+P+""" """+Q+""" """+R+""" """+S+""" """+T+"""
G V A X K L C I N Y E Q T Z Z R R I K L C Z Z G T H A
G X G P G B A N K N M U N U C R E R Q Y F T X P T C B
L X K Q H I C W P M Q R Y Z A I X C C E A A S T V S Q
F F N C T X I O U W Z T Y P H A P T M F O F Z G H D B
U R C T T J N G A T X O K I J T H Z K A L U H H P L D
I U C E Q R Y J O H U P V Y A N R O Z L F Y D K G M N
G V I Q G B Q L Y I L M M I Y T Y I Y S O U G C V E D
U F Y M O I P S U J L S O F H J A K K F D W R Y Y H D
E E F H D R Y I R I F S T A T E M E N T Q O K A U I S
Q X V K H Q R Y T L E V V Z L U U C X L N A I B H C Z
M G J A Q P Z G Q U J T O S T R A H Q A Q N W L D B H 
K O Y V H L R M E R L T S S T B L O F C E D M M K B V
L G D N A W R I K S P B W I Q X W M G G P C A D J R E 
H U D N X R M U N K Y P O A L C E X B D V W M Y F D C 
D O O N A P I Q J K E D T Y V U H F T B P B C W C V B
F A Y N O R A A F M K B R C A B J W E M V U Z R M K O
I A Z R N L L M B U Q W I C K Y K M U M X W I X G D F
Y H T T H L T M Y L N R M U M M P H R F P Z W C F T B
G M G N I R T S B W E A L Q Z R C C J J L W W R H D E
E V D B Y S M Q V J R S U D Q D P T Z V S U V U I P Q """
print(PUZZLE)

def display_puzzle(PUZZLE):
    A = word[0]
    B = word[1]
    C = word[2]
    D = word[3]
    E = word_2[0]
    F = word_2[1]
    G = word_2[2]
    H = word_2[3]
    I = word_2[4]
    J = word_2[5]
    K = word_2[6]
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    print("""
"""+A+""" """+B+""" """+C+""" """+D+""" M E T D Z F P S M A N D P A B J M N V N S T J
K O A K H H M R R M Y A X O L E D K A W I G G Y G G H
V U R V Y F A I G L P L T O E X R E S L A F X C R S H
B Q B R Y N I N W E I Z F L P F O F Z Y H X M C H U X
"""+E+""" """+F+""" """+G+""" """+H+""" """+I+""" """+J+""" """+K+""" R A G Y R M C L H J S """+L+""" """+M+""" """+N+""" """+O+""" """+P+""" """+Q+""" """+R+""" """+S+""" """+T+"""
G V A X K L C I N Y E Q T Z Z R R I K L C Z Z G T H A
G X G P G B A N K N M U N U C R E R Q Y F T X P T C B
L X K Q H I C W P M Q R Y Z A I X C C E A A S T V S Q
F F N C T X I O U W Z T Y P H A P T M F O F Z G H D B
U R C T T J N G A T X O K I J T H Z K A L U H H P L D
I U C E Q R Y J O H U P V Y A N R O Z L F Y D K G M N
G V I Q G B Q L Y I L M M I Y T Y I Y S O U G C V E D
U F Y M O I P S U J L S O F H J A K K F D W R Y Y H D
E E F H D R Y I R I F S T A T E M E N T Q O K A U I S
Q X V K H Q R Y T L E V V Z L U U C X L N A I B H C Z
M G J A Q P Z G Q U J T O S T R A H Q A Q N W L D B H 
K O Y V H L R M E R L T S S T B L O F C E D M M K B V
L G D N A W R I K S P B W I Q X W M G G P C A D J R E 
H U D N X R M U N K Y P O A L C E X B D V W M Y F D C 
D O O N A P I Q J K E D T Y V U H F T B P B C W C V B
F A Y N O R A A F M K B R C A B J W E M V U Z R M K O
I A Z R N L L M B U Q W I C K Y K M U M X W I X G D F
Y H T T H L T M Y L N R M U M M P H R F P Z W C F T B
G M G N I R T S B W E A L Q Z R C C J J L W W R H D E
E V D B Y S M Q V J R S U D Q D P T Z V S U V U I P Q """)


words = [word]

##0 A,1 B,2 C,3 D,4 E,5 F,6 G,7 H,8 I,9 J,10 K,
##11 L,12 M,13 N,14 O,15 P,16 Q,17 R,18 S,19 T,
##20 U,21 V,22 W,23 X,24 Y,25 Z
selected = []


def create_word(PUZZLE):
    num=[]
    coordinate= ""
    find = input("please input your coordinates for the word your looking for\nmake sure you have a comma inbetween coordinates\n")
    for i in find:
        if i != ",":
            coordinate= coordinate + i
        else:
            if coordinate.isdigit():
                num.append(int(coordinate))
                coordinate= ""
    #print(coordinate)
    num.append(int(coordinate))
    
    new_word = ""
    while num:
        x= num.pop(0)
##        y= num.pop(0)
        #add [y] to puzzle when if in a 2d form.
        new_word = new_word + PUZZLE[x]
    #print(word)
    return new_word


def check_correct():
    if find == word:
        selected.append(word)
    if find == word_2:
        selected.append(word_2)

display_puzzle(PUZZLE)
##for i in range(len(questions)):
##    question_answer(words,questions,selected)
for i in range(len(questions)):
    print(word,
          word_2,
          word_3)
    builtWord=create_word(PUZZLE)
    print(builtWord)
    if builtWord == word:
        print("CORRECT")
        score +=1
    else:
        print("INCORRECT")

print("Your score was:",score)
