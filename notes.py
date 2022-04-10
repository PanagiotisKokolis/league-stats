#use pip install riotwatcher

#look up summonner through their name
#look up last 10 matches and find their pref role

#pythonlibrary riot api
#look up summoner puuid using summoner v4
#look up match history using puuid and match
#for each match id which is just a string , for loop to go through each match and find what role they played
#sort static ints in the function that increase count- return the highest role count
#"teamposition" time.sleep(seconds)
#return
from riotwatcher import LolWatcher

lol_watcher = LolWatcher('RGAPI-b7897195-c3f2-402a-9cc0-51ae52be6e10')


my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Geeraph')
print(me)

guan = lol_watcher.summoner.by_name('na1','D1v1ner1ght')
print(guan)