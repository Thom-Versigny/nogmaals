# name of student: Thom Versigny
# number of student: 99068311
# purpose of program: 
# function of program: 
# structure of program: 
coinsreturned200 = 0
coinsreturned100 = 0
coinsreturned50 = 0
coinsreturned20 = 0
coinsreturned10 = 0
coinsreturned5 = 0
coinsreturned2 = 0
coinsreturned1 = 0
toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #hij rekend uit of dat je teveel heb betaaldt

if change > 0: #hij kijkt ofdat je teveel hebt betaald
  coinValue = 200 #het start getal van geld
  
  while change > 0 and coinValue > 0: #hij blijft doorgaan totdat i alles terug heeft gegeven
    nrCoins = change // coinValue #hij kijkt hoeveel je munten kan geven

    if nrCoins > 0: #hij kijkt ofdat het overige getal van munten nog bestaat
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below:
    if coinValue == 200:
      coinValue = 100
      coinsreturned200 = nrCoinsReturned
    elif coinValue == 100:
      coinValue = 50
      coinsreturned100 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coinsreturned50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coinsreturned20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coinsreturned10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coinsreturned5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coinsreturned2 = nrCoinsReturned
    else:
      coinValue = 0
      coinsreturned1 = nrCoinsReturned

if change > 0: # kijkt ofdat er nog geld over is
  print('Change not returned: ', str(change) + ' cents')
  input('press enter to contine')
else:
  print(f"""--------------------------------------------------------
|You've returned {coinsreturned200} of 200 cent coins.
|You've returned {coinsreturned100} of 100 cent coins.
|You've returned {coinsreturned50} of 50 cent coins.
|You've returned {coinsreturned20} of 20 cent coins.
|You've returned {coinsreturned10} of 10 cent coins.
|You've returned {coinsreturned5} of 5 cent coins.
|You've returned {coinsreturned2} of 2 cent coins.
|You've returned {coinsreturned1} of 1 cent coins.
---------------------------------------------------------""")
  input('press enter to contine')