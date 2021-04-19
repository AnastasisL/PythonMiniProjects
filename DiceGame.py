import csv, time, random, operator
  
def Menu():
    valid = False
    while not valid:
        choice = int(input("""
--------------------------------------------------------------------------------
Options:
1. Admin
2. Sign up
3. Play (2 player log in required)
4. View Top 5 scorers
        
5. Exit
--------------------------------------------------------------------------------
What do you want to do? (1-5): """))
        if choice == 1:
            valid == True
            Admin()
        elif choice == 2:
            valid == True
            SignUp()
        elif choice == 3:
            valid == True
            diceRoll()
        elif choice == 4:
            valid == True
            Top5()
        elif choice == 5:
            valid == True
            exit()
        else:
            valid == False
            print("\nYour response was invalid, try again.\n")
  
def Admin():
    attempts = 3
    while attempts != 0:
        password = "testing123"
        userpass = input("\nEnter the administrator password: ")
        if password == userpass:
            userfile = open("userfile.csv", "w")
            WriteLine = "Username" + "," + "Password" + "," + "Security" + "\n"
            userfile.write(WriteLine)
            userfile.close()
                    
            scorefile = open("scorefile.csv", "w")
            WriteLine = "Username" + "," + "Score" + "\n"
            scorefile.write(WriteLine)
            scorefile.close()
            print("\nCSV files created!")
            time.sleep(1)
            Menu()
        else:
            attempts = attempts - 1
            if attempts == 1:
                print("Wrong password!",attempts,"attempt left!")
            elif attempts == 0:
                print("Wrong password! No attempts left!")
            else:
                print("Wrong password!",attempts,"attempts left!")
    Menu()
        
def SignUp():
    userfile = open("userfile.csv", "a")
    sUser = input("\nChoose a username: ")
    sPass = input("Choose a password: ")
    sQues = int(input("""
--------------------------------------------------------------------------------
Security Questions:
1. What is/was your first pet's name?
2. Which town were you born in?
3. What is your mother's maiden name?
4. At what age did you buy your first car?
5. Whats your favourite food?
6. What school do you go to?
--------------------------------------------------------------------------------
Choose a Security Question (1-6): """))
    s1 = ("\nWhat is/was your first pet's name?")
    s2 = ("\nWhich town were you born in?")
    s3 = ("\nWhat is your mother's maiden name?")
    s4 = ("\nAt what age did you buy your first car?")
    s5 = ("\nWhats your favourite food?")
    s6 = ("\nWhat school do you go to?")
    answered = False
    while answered == False:
        if sQues == 1:
            print(s1)
            sAns = input("Answer: ")
            answered = True
        if sQues == 2:
            print(s2)
            sAns = input("Answer: ")
            answered = True
        if sQues == 3:
            print(s3)
            sAns = input("Answer: ")
            answered = True
        if sQues == 4:
            print(s4)
            sAns = input("Answer: ")
            answered = True
        if sQues == 5:
            print(s5)
            sAns = input("Answer: ")
            answered = True
        if sQues == 6:
            print(s6)
            sAns = input("Answer: ")
            answered = True
    WriteLine = sUser + "," + sPass + "," + sAns + "\n"
    userfile.write(WriteLine)
    userfile.close()
    print("\nAccount Created!")
    Menu()
  
def LogIn():
    players = 0
    player1 = 0
    player2 = 0
    while players != 2:
        while player1 == 0:
            with open("userfile.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                database = []
                for row in reader:
                    database.append(dict(username=row["Username"],password=row["Password"],security=row["Security"]))              
            loggedin = False
            while not loggedin:
                Username1 = input("\nEnter your username: ")
                Password1 = input("Enter your password: ")
                Security1 = input("Answer to your security question: ")
                for row in database:
                    Username_File = row["username"]
                    Password_File = row["password"]
                    Security_File = row["security"]
                    if (Username_File == Username1 and
                        Password_File == Password1 and
                        Security_File == Security1):
                        loggedin = True
                        print("\n", Username1, "logged in successfully!")
                        players = players + 1
                        player1 = str(Username1)
                        print("Player 1 assgined to:", player1)
                if loggedin is not True:
                    print("\nLog in failed! Make sure that your details are correct.")
                    
        while player2 == 0:
            with open("userfile.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                database = []
                for row in reader:
                    database.append(dict(username=row["Username"],password=row["Password"],security=row["Security"]))              
            loggedin = False
            while not loggedin:
                Username2 = input("\nEnter your username: ")
                Password2 = input("Enter your password: ")
                Security2 = input("Answer to your security question: ")
                for row in database:
                    Username_File = row["username"]
                    Password_File = row["password"]
                    Security_File = row["security"]
                    if (Username_File == Username2 and
                        Password_File == Password2 and
                        Security_File == Security2):
                        loggedin = True
                        if Username1 != Username2:
                            print("\n", Username2, "logged in successfully!")
                            players = players + 1
                            player2 = str(Username2)
                            print("Player 2 assigned to:", player2,"\n")
                        else:
                            print("\nYou cannot use the same user for both players!")
                if loggedin is not True:
                    print("\nLog in failed! Make sure that your details are correct.")
    return player1, player2
  
def diceRoll():
    player1, player2 = LogIn()
    turn = 0
    rally = 1
    score = 0
    total = 0
    score2 = 0
    total2 = 0
    again = "Y"
    
    while again == "Y" and turn != 5:
        print("\n------ Rally",rally,"------")
        print("\n",player1,"'s turn!")
        throw1 = random.randint(1,6)
        throw2 = random.randint(1,6)
        time.sleep(1)
        print("Die 1 =",throw1)
        time.sleep(1)
        print("Die 2 =",throw2)
        total = throw1 + throw2
        score = score + total
        time.sleep(0.5)
        print("Total for this round:",total)
        if total % 2 == 0:
            time.sleep(0.5)
            print("(=) Even total, +10 to score!")
            score = score + 10
        else:
            time.sleep(0.5)
            print("(-) Odd total, -5 from score!")
            score = score - 5
            if score < 0:
                time.sleep(0.5)
                print("(/) Score is reset to 0 due to negative total!")
                score = 0
        if throw1 == throw2:
            time.sleep(0.5)
            print("(!) Rolled a double! You get to roll an extra die!")
            throw3 = random.randint(1,6)
            time.sleep(0.5)
            print("(!) Die 3 =",throw3)
            time.sleep(0.5)
            print("(!)",throw3,"added to your score!")
            score = score + throw3
        time.sleep(0.3)
        print("Score:",score)
        time.sleep(1.5)
        
        print("\n",player2,"'s turn!")
        throw1 = random.randint(1,6)
        throw2 = random.randint(1,6)
        time.sleep(1)
        print("Die 1 =",throw1)
        time.sleep(1)
        print("Die 2 =",throw2)
        total2 = throw1 + throw2
        score2 = score2 + total2
        time.sleep(0.5)
        print("Total for this round:",total2)
        if total2 % 2 == 0:
            time.sleep(0.5)
            print("(=) Even total, +10 to score!")
            score2 = score2 + 10
        else:
            time.sleep(0.5)
            print("(-) Odd total, -5 from score!")
            score2 = score2 - 5
            if score2 < 0:
                time.sleep(0.5)
                print("(/) Score is reset to 0 due to negative total!")
                score2 = 0
        if throw1 == throw2:
            time.sleep(0.5)
            print("(!) Rolled a double! You get to roll an extra die!")
            throw3 = random.randint(1,6)
            time.sleep(0.5)
            print("(!) Die 3 =",throw3)
            time.sleep(0.5)
            print("(!)",throw3,"added to your score!")
            score2 = score2 + throw3
        time.sleep(0.3)
        print("Score:",score2)
        turn = turn + 1
        rally = rally + 1
        time.sleep(1.5)
        
        again = input("\nWant to go again? (Y/N): ").upper()
    while turn == 5 and score == score2:
        print("\nDraw! Play until there is a winner!")
        time.sleep(0.5)
        throw1 = random.randint(1,6)
        print("\n",player1,"rolls a die and gets:",throw1)
        time.sleep(1)
        score = score + throw1
        throw2 = random.randint(1,6)
        print("",player2,"rolls a die and gets:",throw2)
        score2 = score2 + throw2
            
    if turn == 5 and again == "N":
        time.sleep(2)
        print("\n------ Final scores ------")
        print(player1, score)
        print(player2, score2)
        print("--------------------------")
        if score > score2:
            print("Winner:",player1)
        else:
            print("Winner:",player2)
        print("\nScores written to a CSV file!")
        time.sleep(2)
        
    if turn == 5 and again == "Y":
        print("\nYou have already had 5 turns! Log in to play again.")
        time.sleep(2)
        print("\n------ Final scores ------")
        print(player1, score)
        print(player2, score2)
        print("--------------------------")
        if score > score2:
            print("Winner:",player1)
        else:
            print("Winner:",player2)
        print("\nScores written to a CSV file!")
        time.sleep(2)
  
    with open('scorefile.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((player1, score))
  
    with open('scorefile.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((player2, score2))
    
    data = csv.reader(open('scorefile.csv'),delimiter=',')
    sortedlist = sorted(data, key=operator.itemgetter(1), reverse=True)
    with open("top5file.csv", "w") as f:
        fileWriter = csv.writer(f, delimiter=',')
        for row in sortedlist:
            fileWriter.writerow(row)
  
def Top5():
    with open('top5file.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nCurrent Top 5:")
        for i,row in enumerate(reader):
            print(row['Username'], row['Score'])
            if(i >= 4):
                break
Menu()
