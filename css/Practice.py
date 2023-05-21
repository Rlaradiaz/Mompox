for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "/" + str(right) + "]", end= " ")
    print()







teams = ['perros', 'gatos', 'ratones', 'loros']
for local_teams in teams:
    for away_team in teams:
        if local_teams != away_team:
            print(local_teams + " vs " + away_team)
        

for n in range(10):
        print(n+n)
    
        
    
pets = "michi & luna"
pets.index("&")


pictionary = {"rori":5, "eli":6, "yo":10}
print(pictionary)
for ext, amounts in pictionary.items():
     print("thera are {} people wit the .{} ext".format(amounts, ext))




