def dice_prob(n):
    print("Probability of rolling a number other than 1:")
    for i in range(1,n+1):
        print(f"{i} dice: {pow(5, i)/pow(6, i)} (-{(pow(5, i-1)/pow(6, i-1)) - (pow(5, i)/pow(6, i))}) => {(pow(5, i)/pow(6, i))*100}%")
        
    print("\nProbability of rolling a 1:")
    for i in range(1,n+1):
        print(f"{i} dice: {1-(pow(5, i)/pow(6, i))} (+{(pow(5, i-1)/pow(6, i-1)) - (pow(5, i)/pow(6, i))}) => {(1-(pow(5, i)/pow(6, i)))*100}%")

def dice_prob_sm(n):
    print("Probability of rolling a number other than 1:")
    for i in range(1,n+1):
        print(f"{(pow(5, i)/pow(6, i))*100}%")
        
    print("\nProbability of rolling a 1:")
    for i in range(1,n+1):
        print(f"{(1-(pow(5, i)/pow(6, i)))*100}%")

n = input("Number of dice to roll: ")
dice_prob(int(n))
dice_prob_sm(int(n))