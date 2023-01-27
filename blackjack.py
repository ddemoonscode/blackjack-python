import random, time


#point status
point_status = open('bank_blackjack.txt', 'r').read()
print('you have ', point_status, '$')

#bet money
bet_money = int(input('How much do you want to bet? '))
with open('bank_blackjack.txt', 'r') as infile:
    result = int(infile.readline().strip()) - bet_money

print('you now have ', result, '$')

with open('bank_blackjack.txt', 'w') as outfile:
    outfile.write(str(result))

J = 10
Q = 10
K = 10
ace = 11
#cards
Karten = [2, 3,4,5,6,7,8,9,10,J,Q,K,ace, 
2, 3,4,5,6,7,8,9,10,J,Q,K,ace,
2, 3,4,5,6,7,8,9,10,J,Q,K,ace,
2, 3,4,5,6,7,8,9,10,J,Q,K,ace,]

#player random card generation
random1stcard = random.choice(Karten)
random2ndcard = random.choice(Karten)
randomcards = random1stcard + random2ndcard

#dealer random card generation
dealerrandomcardsshown = random.choice(Karten)
dealerrandomcardshidden = dealerrandomcardsshown + random.choice(Karten)

#dealer cards
if dealerrandomcardshidden < 21:
    print('\nthe dealer has: ', dealerrandomcardsshown)

else:
    print('\nthe dealer has a blackjack, u lost')
    exit()
    
#if first 2 cards are aces
if random1stcard and random2ndcard == 11:
    randomcards =- 10

#player cards
if randomcards < 21:
    print('you have: ', randomcards)
    print('\nanother card?')
    print('yes(y)')
    print('no(n)')
    takecard = (input('')).upper()
    if takecard != 'N':
        take1card1 = random.choice(Karten)
        randomcards = randomcards + take1card1
        if randomcards >21 and take1card1 == ace:
            randomcards =-10
        if randomcards <=21:
            print('\nyou have: ', randomcards)
            print('\nanother card?')
            print('yes(y)')
            print('no(n)')
            takecard = (input('')).upper()
            if takecard != 'N':
                take1card1 = random.choice(Karten)
                randomcards = randomcards + take1card1
                if randomcards > 21 and take1card1 == ace:
                    randomcards =- 10
                if randomcards <=21:
                    print('\nyou have: ',randomcards)
                    print('\nanother card?')
                    print('yes(y)')
                    print('no(n)')
                    takecard = (input('')).upper()
                    if takecard != 'N':
                        take1card1 = random.choice(Karten)
                        randomcards = randomcards + take1card1
                        if randomcards>21 and take1card1 == ace:
                            randomcards =-10
                        if randomcards <=21:
                            print('\nyou have: ',randomcards)
                            print('lets compare!')

                        else:
                            print('\nyou have to much, you lost, you had: ', randomcards)
                            exit()
                        
                    else:
                        print('\nlets compare!')
                
                else:
                    print('\nyou have to much, u lost, you had: ', randomcards)
                    exit()
            else:
                print('\nlets compare!')
        else:
            print('\nyou have to much, u lost, you had: ', randomcards)
            exit()

    else:
        print('\nlets compare!')

else:
    print('\nu have a blackjack, u won')

    with open("bank_blackjack.txt", "r") as infile:
        result = int(infile.readline().strip()) + bet_money * 4,5

    print('you now have ', result, '$')

    with open("bank_blackjack.txt" , "w") as outfile:
        outfile.write(str(result))
    exit()

#dealercards

if dealerrandomcardshidden <=17:
    dealerrandomcardshidden = dealerrandomcardshidden + random.choice(Karten)
    print('\nthe dealer has: ', dealerrandomcardshidden)
    time.sleep(1)
    if dealerrandomcardshidden <=17:
        dealerrandomcardshidden1 = dealerrandomcardshidden + random.choice(Karten)
        print('\nthe dealer has: ', dealerrandomcardshidden)
        time.sleep(1)
        if dealerrandomcardshidden <=17:
            dealerrandomcardshidden = dealerrandomcardshidden + random.choice(Karten)
            print('\nthe dealer has: ', dealerrandomcardshidden)
            time.sleep(1)
            
        elif dealerrandomcardshidden == 21:
            print('\nthe dealer has 21 he won')

        elif dealerrandomcardshidden >21:
            print('\nthe dealer has too much, u won, he had: ', dealerrandomcardshidden)
            with open('bank_blackjack.txt', "r") as infile:
                result = int(infile.readline().strip()) + bet_money * 4

            print('you now have ', result, '$')

            with open('bank_blackjack.txt' , "w") as outfile:
                outfile.write(str(result))
            exit()

    elif dealerrandomcardshidden == 21:
        print('\nthe dealer has 21 he won')
        with open('bank_blackjack.txt', "r") as infile:
            result = int(infile.readline().strip()) + bet_money * 4

        print('you now have ', result, '$')

        with open('bank_blackjack.txt' , "w") as outfile:
            outfile.write(str(result))

    elif dealerrandomcardshidden >21:
        print('\nthe dealer has to much, u won, he had: ', dealerrandomcardshidden)
        with open('bank_blackjack.txt', "r") as infile:
            result = int(infile.readline().strip()) + bet_money * 4

        print('you now have ', result, '$')

        with open('bank_blackjack.txt' , "w") as outfile:
            outfile.write(str(result))
        exit()

elif dealerrandomcardshidden >21:
    print('\nthe dealer has too much, u won, he had: ', dealerrandomcardshidden)

    with open('bank_blackjack.txt', "r") as infile:
        result = int(infile.readline().strip()) + bet_money * 4

    print('you now have ', result, '$')

    with open('bank_blackjack.txt' , "w") as outfile:
        outfile.write(str(result))
    exit()

elif dealerrandomcardshidden == 21:
    print('\nthe dealer had a blackjack, u lost')
    exit()

#comparing

if randomcards > dealerrandomcardshidden:
    print('you have more points than the dealer, u won')
    with open('bank_blackjack.txt', "r") as infile:
        result = int(infile.readline().strip()) + bet_money * 4

    print('you now have ', result, '$')

    with open('bank_blackjack.txt' , "w") as outfile:
        outfile.write(str(result))

    exit()

else:
    print('the dealer has more, u lost')
    exit()