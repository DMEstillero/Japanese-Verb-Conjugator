# Enter the dictionary form of verb
# Plain form, formal form, formal past form, negative formal form, negative formal past form (cover irregular verbs)
# Negative plain form, past tense plain form, past tense negative plain form, Te form

# Create functions to convert verb to desired form
# Ask for plain form to then convert into desired form
 
alphabet_by_first_letter = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["が", "ぎ", "ぐ", "げ","ご"],
    ["さ", "し", "す", "せ", "そ"],
    ["ざ", "じ", "ず", "ぜ","ぞ"],
    ["た", "ち", "つ", "て", "と"],
    ["だ", "ぢ", "づ", "で","ど"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ば", "び", "ぶ", "べ","ぼ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "ゆ", "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "を"],
    ["ん"]
]

alphabet_by_vowel = [
    ["あ", "か", "が", "さ", "ざ", "た", "だ", "な", "は", "ば", "ま", "や", "ら", "わ"],
    ["い", "き", "ぎ", "し", "じ", "ち", "ぢ", "に", "ひ", "び", "み", "り"],
    ["う", "く", "ぐ", "す", "ず", "つ", "づ", "ぬ", "ふ", "ぶ", "む", "ゆ", "る"],
    ["え", "け", "げ", "せ", "ぜ", "て", "で", "ね", "へ", "べ", "め", "れ"],
    ["お", "こ", "ご", "そ", "ぞ", "と", "ど", "の", "ほ", "ぼ", "も", "よ", "ろ", "を"],
    ["ん"]
]

class ichidan_verb:
    def __init__(self, verb):
        self.verb = verb
    
    def polite(verb):
            verb_stem = verb[:-1]
            print(f"The Present Polite Form of this verb is: {verb_stem}ます")
    
    def polite_negative(verb):
            verb_stem = verb[:-1]
            print(f"The Present Polite Negative Form of this verb is: {verb_stem}ません")

class godan_verb:
    def __init__(self, verb):
        self.verb = verb
        
    def polite(verb):
            verb_stem = verb[:-1]
            for i in range(len(alphabet_by_first_letter)):
                if verb[-1] in alphabet_by_first_letter[i]:
                    row = i
            prefix_vowel = alphabet_by_first_letter[row][1]
            print(f"{verb_stem}{prefix_vowel}ます")
                
    def polite_negative(verb):
            verb_stem = verb[:-1]
            for i in range(len(alphabet_by_first_letter)):
                if verb[-1] in alphabet_by_first_letter[i]:
                    row = i
            prefix_vowel = alphabet_by_first_letter[row][1]
            print(f"{verb_stem}{prefix_vowel}ません")



verb = input("Please enter the verb in dictionary form: ")

# Dictionary Form to Polite Form

# Irregular Verbs 
if verb == "する":
    print(f"します")

elif verb == "くる":
    print("きます")

elif verb[-1] == "る" and verb[-2] in alphabet_by_vowel[1] or verb[-2] in alphabet_by_vowel[3]:
    ichidan_verb.polite(verb)

elif verb[-1] in alphabet_by_vowel[2] and verb[-2] in alphabet_by_vowel[0] or alphabet_by_vowel[2] or alphabet_by_vowel[4]:
    godan_verb.polite(verb)


# Irregular Verbs 
if verb == "する":
    print(f"しません")

elif verb == "くる":
    print("きません")

elif verb[-1] == "る" and verb[-2] in alphabet_by_vowel[1] or verb[-2] in alphabet_by_vowel[3]:
    godan_verb.polite_negative(verb)

elif verb[-1] in alphabet_by_vowel[2] and verb[-2] in alphabet_by_vowel[0] or alphabet_by_vowel[2] or alphabet_by_vowel[4]:
    godan_verb.polite_negative(verb)
