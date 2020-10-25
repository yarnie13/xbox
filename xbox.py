import xbox

xbox.client.authenticate(login='LOGIN', password='PASSWORD')
igt = input('GamerTag: ')
gt = xbox.GamerProfile.from_gamertag(igt)
print(gt)
print("")
print('Gamerscore: ', gt.gamerscore)
print("")
print('Gamerpic Link: ', gt.gamerpic)
input()
