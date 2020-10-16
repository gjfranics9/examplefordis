geodudeInGame = {'HP': 31, 'ATK':31, 'DEF':31, 'SPATK':31, 'SPDEF':"any", 'SPE':31, 'nat':"adamant"}
def isTrue(geodudeInGame):
    HP = 31
    bpset = {'HP': 31, 'ATK':31, 'DEF':31, 'SPATK':31, 'SPDEF':"any", 'SPE':31, 'nat':"adamant"}
    if geodudeInGame["HP"] == bpset["HP"] and geodudeInGame["ATK"] == bpset["ATK"]:
        return True

if isTrue(geodudeInGame) == True:
    print("BP : Yes")
else:
    print("BP : No")

print(geodudeInGame['HP'])

