# Menu
# Enter the dictionary form of verb
# Plain form, formal form, negative formal form, (cover irregular verbs)
# Negative plain form, past tense plain form, past tense negative plain form, Te form

# Create functions to convert verb to desired form
# Ask for plain form to then convert into desired form
 
alphabet_by_first_letter = [
    ["あ", "い", "う" "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "ゆ", "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "を"],
    ["ん"]
]

alphabet_by_vowel = [
    ["あ", "か", "さ", "た", "な", "は", "ま", "や", "ら", "わ"],
    ["い", "き", "し", "ち", "に", "ひ", "み", "り"],
    ["う", "く", "す", "つ", "ぬ", "ふ", "む", "ゆ", "る"],
    ["え", "け", "せ", "て", "ね", "へ", "め", "れ"],
    ["お", "こ", "そ", "と", "の", "ほ", "も", "よ", "ろ", "を"],
    ["ん"]
]

verb = input("Please enter the verb in dictionary form: ")


# Dictionary Form to Present Formal Form
# Ichidan Verbs
if verb[-1] == "る" and verb[-2] in alphabet_by_vowel[1] or alphabet_by_vowel[3]:
    prefix = verb[:-1]
    print(f"The Present Polite Form of this verb is: {prefix}ます")
    
    
# Godan Verbs
if verb[-2] not in alphabet_by_vowel[1] or alphabet_by_vowel[3]:
    prefix = verb[:-1]
    for i in range(len(alphabet_by_first_letter)):
        if verb[-1] in alphabet_by_first_letter[i]:
            index = i
    prefix_vowel = alphabet_by_first_letter[index][1]
    print(f"{prefix}{prefix_vowel}ます")

# Irregular Verbs 
if verb == "する":
    print(f"{alphabet_by_vowel[2][1]}ます")

if verb == "くる":
    print("きます")