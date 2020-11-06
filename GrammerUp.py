#Import tkinter for GUI libraries
import tkinter as Tkinter
from tkinter import *
import string
#Import tkMessageBox for information and help message box
import tkinter.messagebox as tkMessageBox
def helpMsg():
    tkMessageBox.showinfo("About this Software", "This software is is intended to increase proper usage of english without Error")
#Import nltk for language processing
from nltk import *
#Check to see if relevant text exists
try:
    sentence = "example sentence"
    tokens = word_tokenize(sentence)
#If it doesn't, download it
except LookupError:
    print("Downloading requisite English language processing code...")
    download('book')
#Convert a list of tuples (word, part of speech) to a sentence String
def tagsToString(tags):
    result = ""
    for x in tags:
        word = x[0]
        pos = x[1]
        if pos == '.' or word[0]=="'":
            result+=word
        else:
            result+=" "+word
    result = result.strip()
    result = " "+result
    return result
#Process text to detect if a noun is found preceding an adjective:
def Error1(tags):
    error = False
    if len(tags) < 2:
        return error
    adj = ['JJ']
    nouns = ['NN','NNS','NNP','NNPS','PRP','RP','DT']
    for i in range(len(tags)-1):
        currentWord = tags[i][0]
        currentPOS = tags[i][1]
        nextWord = tags[i+1][0]
        nextPOS = tags[i+1][1]
        if currentPOS in nouns and nextPOS in adj:
            tags[i] = (nextWord, nextPOS)
            tags[i+1] = (currentWord, currentPOS)
            error = True
    return error
#Process text to detect if a gerund is used without 'to be':
def Error2a(tags):
    error = False
    flag = 0
    if len(tags) < 2:
        print ("Hemant 1")
        return error
    nouns = ['NN','NNS','NNP','NNPS','PRP','RP']
    verbs = ['VB','VBD','VBG','VBN','VBP','VBZ','MD']
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    tagsLength = len(tags) - 1
    for i in range(tagsLength):
        print ("Hemant 2")
        firstWord = tags[i][0]
        print ("Hemant 2a")
        print (firstWord)
        firstPOS= tags[i][1]
        print ("Hemant 2b")
        print (firstPOS)
        secondWord = tags[i+1][0]
        print ("Hemant 2c")
        print (secondWord)
        secondPOS = tags[i+1][1]
        print ("Hemant 2d")
        print (secondPOS)
        print ("for is am")
        print (tags[i][0])
        print (tags[i+1][0])
        if tags[i][1] in ['VBD','VBG','VBP','VBZ'] and tags[i+1][1] in ['VBD','VBG','VBP','VBZ']:
            print ("in if cond")
            tags.remove(tags[i+1])
            break
        if firstPOS in nouns and tags[i][0] not in capitals:
            print ("Here")
            newword = tags[i][0].capitalize()
            tags.remove(tags[i])
            tags.insert(i,(newword,'NN'))
            break
        if secondPOS in ['VBD','VBG','VBP','VBZ'] and firstPOS not in verbs: 
            for j in range(i,len(tags)):
                print ("Hemant 2e @@@@@")
                print (tags[j][0])
                print (tags[j][1])
                if tags[j][0] == '.':
                    if firstWord in ['I']:
                        print ("Hemant 3")
                        if tags[i+1][0] not in ['Am','am','like','liked','can','could','had','have','will','would','love','loved','see','saw','hate','hated','want','wanted','need','needed','own','owned','belong','hear','heard','smell','seem','seemed','know','knew','believe','believed','remember','remembered','doubt','doubted','dislike','disliked','understand','understood','suspect','suspected','loath','loathed','forget','forgot','prefer','preferred','feel']:
                            tags.insert(i+1,('am','VBP'))
                            flag = 1
                            error = True
                            break
                    elif firstWord in ['He','he','She','she']:
                        print ("Hemant 4")
                        if tags[i+1][0] not in ['Is','is','like','liked','can','could','had','have','will','would','love','loved','see','saw','hate','hated','want','wanted','need','needed','own','owned','belong','hear','heard','smell','seem','seemed','know','knew','believe','believed','remember','remembered','doubt','doubted','dislike','disliked','understand','understood','suspect','suspected','loath','loathed','forget','forgot','prefer','preferred', 'feel']:
                            tags.insert(i+1,('is','VBP'))
                            flag = 1
                            error = True
                            break
                    elif firstWord in ['They','they','We','we','You','you']:
                        if tags[i+1][0] not in ['Are','are','like','liked','can','could','had','have','will','would','love','loved','see','saw','hate','hated','want','wanted','need','needed','own','owned','belong','hear','heard','smell','seem','seemed','know','knew','believe','believed','remember','remembered','doubt','doubted','dislike','disliked','understand','understood','suspect','suspected','loath','loathed','forget','forgot','prefer','preferred','start','started','feel']:
                            tags.insert(i+1,('are','VBP'))
                            flag = 1
                            error = True
                            break
                elif tags[j][0] == '?':
                    if firstWord in ['I']:
                        print ("Hemant 6")
                        if tags[i+1][0] not in ['Am','am']:
                            tags.insert(i,('am','VBP'))
                            flag = 1
                            error = True
                            break
                    elif firstWord in ['He','he','She','she']:
                        print ("Hemant 7")
                        print (tags[i+1][0])
                        if tags[i+1][0] not in ['Is','is']:
                            tags.insert(i,('is','VBP'))
                            flag = 1
                            error = True 
                            break
                    elif firstWord in ['They','they','We','we','You','you']:
                        if tags[i+1][0] not in ['Are','are','Will','will']:
                            tags.insert(i,('are/will','VBP'))
                            flag = 1
                            error = True
                            break
        if flag == 1:
            break
    return error
#Process text to find if an extraneous modal is used with 'do'
def Error2b(tags):
    error = False
    if len(tags) < 2:
        return error
    verbs = ['VB','VBD','VBG','VBN','VBP','VBZ','MD']
    do = ['do','Do','does','Does']
    for i in range(len(tags)-2):
        firstWord = tags[i][0]
        firstPOS = tags[i][1]
        secondWord = tags[i+1][0]
        secondPOS = tags[i+1][1]
        thirdWord = tags[i+2][0]
        thirdPOS = tags[i+2][1]
        if firstWord in do and secondPOS == 'MD':
            tags[i+1] = (('',''))
            error = True
        elif firstWord in do and thirdPOS == 'MD':
            tags[i+2] = (('',''))
            error = True
    while (('','')) in tags:
        tags.remove(('',''))
    return error
#Add punctuation to the sentence where it does not exist:
def Error3a(tags):
    error = False
    if len(tags) < 2:
        print ("Hemant 3a 1")
        return error
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    question=["Who","What","Where","When","Why","How","who","what","where","when","why","how","Is","Are","is","are","Do","do","Should","May","Could","should","may","could","would","Would","Does","do"]
    print ("Questionmark condition")
    print (tags[0][0])
    print (tags[len(tags)-1][0])
    if tags[0][0] in question and tags[len(tags)-1][0] != '?':
        print ("Add questionmark")
        i = len(tags) - 1
        tags.remove(tags[i])
        tags.append(('?','.'))
        error = True
    if tags[-1][1] != ('.'): 
        for x in range(len(tags)-1,-1,-1):
            if tags[x][1] in ['.','?','!']:
                print ("Hemant 3a 2")
                break
        if x != 0:
            print ("Hemant 3a 3")
            x += 1
        if tags[x][0] in question:
            print ("Hemant 3a 4")
            tags.append(('?','.'))
        else:
            print ("Hemant 3a 5")
            tags.append(('.','.'))
        error = True
    for i in range(len(tags)-1):
        print ("Hemant 3a 6")
        currentWord = tags[i][0]
        currentPOS = tags[i][1]
        nextWord = tags[i+1][0]
        nextPOS = tags[i+1][1]
        if nextPOS != 'NNP' and nextWord != "I" and nextWord[0] in capitals and currentPOS != '.':
            for x in range(i,-1,-1):
                if tags[x][1] in ['.','?','!']:
                    print ("Hemant 3a 7")
                    break
            if x != 0:
                print ("Hemant 3a 8")
                x += 1
            if tags[x][0] in question:
                print ("Hemant 3a 9")
                tags.insert(i+1,('?','.'))
            else:
                print ("Hemant 3a 10")
                tags.insert(i+1,('.','.'))
                error = True
    verbs = ['VB','VBD','VBG','VBN','VBP','VBZ','MD']
    fanboys = ['for','and','nor','but','or','yet','so','because','while','although','therefore','thus']
    addCommas = []
    left = False
    right = True
    for i in range(len(tags)-1):
        print ("Hemant 3a 11")
        currentWord = tags[i][0]
        currentPOS = tags[i][1]
        if currentWord in fanboys:
            for j in range(i,len(tags)):
                if tags[j][1] in verbs:
                    print ("Hemant 3a 12")
                    right = True
                    break
                elif tags[j][1] == '.':
                    print ("Hemant 3a 13")
                    break 
            
            for j in range(i,-1,-1):
                if tags[j][1] in verbs:
                    print ("Hemant 3a 14")
                    left = True
                    break
                elif tags[j][1] == '.':
                    print ("Hemant 3a 15")
                    break
            if left and right:
                print ("Hemant 3a 16")
                error = True
                addCommas.append(i)
    for loc in addCommas:
        print ("Hemant 3a 17")
        tags.insert(loc,(',','.'))
    removeCommas = []
    for i in range(len(tags)-1):
        if tags[i][0] == ',' and tags[i+1][0] not in fanboys:
            print ("Hemant 3a 18")
            removeCommas.append(i)
            error = True
        for loc in removeCommas:
            print ("Hemu")
            print (tags[loc])
            del tags[loc]
            error = False
            print (error)
            break
    nouns = ['NN','NNS','NNP','NNPS','PRP','RP']
    print (error)
    for i in range(len(tags)-1):
        print (error)
        if tags[i][0][-1] == 's' and tags[i][0][-2] != "'" and tags[i+1][1] in nouns:
            print ("Hemant 3a 19")
            tags[i] = (tags[i][0][:-1]+"'"+tags[i][0][-1],tags[i][1])
            error = True
            print (tags[-3][0])
        if tags[-2][0] == 'please' and tags[-1][0] == "?":
            print ("Hemant 3a 20")
            tags.insert(-2,(',','.'))
            error = True
            print (error)
        break
    print (error)
    return error

#Capitalize letters in words at the beginning of a sentence:
def Error3b(tags):
    error = False
    if len(tags) < 2:
        return error
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    punctuation = ".!?"
    nouns = ['NN','NNS','NNP','NNPS','PRP','RP']
    
    for i in range(len(tags)-1):
        currentWord = tags[i][0]
        nextWord = tags[i+1][0]
        if (i == 0 or currentWord == 'i') and currentWord[0] not in capitals:
            newWord = currentWord.capitalize()
            tags[i] = (newWord,tags[i][1])
            error = True
        elif currentWord in punctuation and nextWord[0] not in capitals:
            newWord = nextWord.capitalize()
            tags[i+1] = (newWord,tags[i+1][1])
            error = True
    return error


#Correct usage of A/An
def Error3c(tags):
    error = False
    if len(tags) < 2:
        return error
    a = ['a','A']
    an = ['an','An']
    vowels = 'aeiouAEIOU'
    for i in range(len(tags)-1):
        currentWord = tags[i][0]
        nextWord = tags[i+1][0]
        if currentWord in a and nextWord[0] in vowels:
            newWord = an[a.index(currentWord)]
            tags[i] = (newWord,tags[i][1])
            error = True
        elif currentWord in an and nextWord[0] not in vowels:
            newWord = a[an.index(currentWord)]
            tags[i] = (newWord,tags[i][1])
            error=True
    return error

#Correct genitive construction errors:
def Error4(tags):
    print ("4")
    error = False
    if len(tags) < 3:
        print( "4a")
        return error
    nouns = ['NN','NNS','NNP','NNPS','PRP','RP']
    for i in range(len(tags)-2):
        print( "4b")
        firstWord = tags[i][0]
        firstPOS = tags[i][1]
        secondWord = tags[i+1][0]
        secondPOS = tags[i+1][1]
        thirdWord = tags[i+2][0]
        thirdPOS = tags[i+2][1]
        if secondWord == 'the' and firstPOS in nouns and thirdPOS in nouns:
            tags[i] = (secondWord,secondPOS)
            tags[i+1] = (thirdWord,thirdPOS) 
            tags[i+2] = (firstWord,firstPOS)
            tags.insert(i+2,("'s", 'POS'))
            error=True
    return error


#Master function which calls all of the error checks and which
#prints the evolving structure of the sentence for debugging
def checkErrors(text):
    errors = ""
    print("Sentence:")
    print(text)
    tokens = word_tokenize(text)
    print("Tokens:")
    print(tokens)
    tags = pos_tag(tokens)
    print("Original:")
    print(tags)
    e3a = Error3a(tags)
    print("Punctuation correction:")
    print(tags)
    e3b = Error3b(tags)
    print("Capitalization correction:")
    print(tags)
    e1 = Error1(tags)
    print("Noun preceding adjective correction:")
    print(tags)
    e2a = Error2a(tags)
    print("Omission of verb 'to be' in gerund correction:")
    print(tags)
    e2b = Error2b(tags)
    print("Extraneous use of modal verb with 'do' correction:")
    print(tags)
    e3c = Error3c(tags)
    print("A/An correction:")
    print(tags)
    e4 = Error4(tags)
    print("Genitive construction correction:")
    print(tags)
    if e1:
        errors += " Adjective cannot succeed noun.\n"
    if e2a:
        errors += " Verb 'to be' is needed with a gerund.\n"
    if e2b:
        errors += " A modal verb is not needed with 'do'.\n"
    if e3a:
        errors += " Punctuation must be in its proper place. Place a comma to seperate clauses, full-stop at the end of the sentence, and question mark at the end of questions.\n"
    if e3b:
        errors += " The beginning of sentences and proper nouns must be capitalized.\n"
    if e3c:
        errors += " Improper use of articles, use 'An' before noun starting with vowels, 'A' otherwise.\n"
    if e4:
        errors += " The genitive construction uses a possessive.\n"
    fixedText = tagsToString(tags) 
    
    if errors == "":
        errors = " It looks good as long as your sentence is in the present tense. Good job."
        L6.config(fg='green')
        top.update()
    else:
        L6.config(fg='red')
    return (fixedText,errors)


#Master function which analyses text
def analyze():
    text = T1.get("1.0",END)
    fixedText, errors = checkErrors(text)
    fixedText = fixedText.split()
    for index in range(1, len(fixedText)):
        if fixedText[index] != 'I':
            if len(fixedText[index])>1 :
                if (fixedText[index][0] in string.ascii_uppercase and
                    fixedText[index][1] in string.ascii_uppercase) : continue
                else :
                    l = len(fixedText[index-1])
                    if fixedText[index-1][l-1] != '.' :
                        fixedText[index] = fixedText[index].lower()
            else :
                if fixedText[index][0] in string.ascii_uppercase :
                    l = len(fixedText[index-1])
                    if fixedText[index-1][l-1] != '.' :
                        fixedText[index] = fixedText[index].lower()
    fixedText = ' '.join(fixedText)
    if fixedText[0] not in string.ascii_uppercase:
        if fixedText[0] in string.ascii_lowercase:
            tmp = fixedText[:1]
            tmp = tmp.upper()
            fixedText = tmp + fixedText[1:]
    #errors = checkErrors(text)
    L3v.set("\n Suggestion:\n")
    L4v.set(fixedText)
    L5v.set("\n Misused grammatical rules that may help you:\n")
    L6v.set(errors)
    
    
#Helper function which centers window
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    
#User interface code
top = Tk()
top.title("Learn English More Effectively by Avoiding Typical Mistakes")
top.geometry('800x800')
L1 = Label(top, text="\n Please type your sentence here:\n", font=("Helvetica", 14))
L1.pack(anchor=W)
T1 = tkinter.Text(top,height=4,width=60,font=("Helvetica", 14))
T1.pack() 
L2 = Label(top, text="", font=("Helvetica", 14))
L2.pack()
B1 = Button(top, text=" Check ", command=analyze,font=("Helvetica", 14))
B1.pack()
L3v = StringVar()
L3 = Label(top, textvariable=L3v, font=("Helvetica", 14, "bold"))
L3.pack(anchor=W)
L4v = StringVar()
L4 = Label(top, textvariable=L4v, font=("Helvetica", 14), justify=LEFT, wraplength=800)
L4.pack(anchor=W)
L5v = StringVar()
L5 = Label(top, textvariable=L5v, font=("Helvetica", 14, "bold"))
L5.pack(anchor=W)
L6v = StringVar()
L6 = Label(top, textvariable=L6v, fg="red", font=("Helvetica", 12), justify=LEFT, wraplength=800)
L6.pack(anchor=W)
B2 = Tkinter.Button(top, text = "?", command = helpMsg)
B2.pack()
center(top)
top.mainloop() 
