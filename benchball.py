import csv

def main():
    # Constant K
    k = 5

    with open("data.csv") as file:
        reader = csv.DictReader(file)
        
        names = []
        elos = []

        for row in reader:
            stats = list(row.values())
            names.append(stats[0])
            elos.append(stats[1])
    
    player_names = []
    player_elos = []
    team = 1
    for player in range(4):
        if player > 1:
            team = 2
        while True:
            player_name = input(f"Player {player+1} (Team {team}): ").lower()
            if player_name in names and player not in player_names:
                player_elo = elos[names.index(player_name)]
                player_names.append(player_name)
                player_elos.append(float(player_elo))
                break
            print("Player Not Found/Used Already")
        
    team1_rating = (player_elos[0] + player_elos[1]) / 2
    team2_rating = (player_elos[2] + player_elos[3]) / 2 
    team1_expected = 1/(1 + 10**((team2_rating - team1_rating)/100))
    team2_expected = 1/(1 + 10**((team1_rating - team2_rating)/100))

    winner = int(input("Who won (Enter 1 for Team 1 and 2 For Team 2)? "))    
    if winner == 1:
        team1_score = 1 
        team2_score = 0
    elif winner == 2:
        team1_score = 0
        team2_score = 1 

    team1_change = round((team1_score - team1_expected) * k, 2)
    player_elos[0] += team1_change
    player_elos[1] += team1_change

    team2_change = round((team2_score - team2_expected) * k, 2)
    player_elos[2] += team2_change
    player_elos[3] += team2_change

    for i in range(4):
        name = player_names[i]
        elo = player_elos[i]
        index = names.index(name)
        
        names[index] = name 
        elos[index] = elo


    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        first = ["name", "elo"]
        writer.writerow(first)
        writer.writerows(zip(names, elos))

    for player in range(4):
        name = player_names[player]
        new_elo = player_elos[player]
        print(f"{name}: {new_elo}")

    # Organize values
    # I know this code sucks but I made it in 20 minutes so -_-
    #data = pandas.read_csv("/home/jhsrobo//Benchball/data.csv")
        #data.sort_values(["elo"],
        #             axis=1,
        #             ascending=[False],
    #             inplace=False)
    #data.to_csv("/home/jhsrobo//Benchball/data.csv", index=False)

if __name__ == "__main__":
    main()
