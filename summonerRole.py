import time
import os
from riotwatcher import LolWatcher
#export api token as this environment variable
RIOT_TOKEN  = os.environ.get('RIOT_TOKEN')

lol_watcher = LolWatcher(RIOT_TOKEN)


my_region = 'na1'

summoner_name = input("Please enter a summoner name: ")                                                #user input for summoner name
summoner_data = lol_watcher.summoner.by_name(my_region, summoner_name)                                 #list of summoner data
summoner_puuid = summoner_data['puuid']
match_history = lol_watcher.match.matchlist_by_puuid('AMERICAS',summoner_puuid,type= 'ranked', queue=420 ,start=0, count=10) # finds the last 10 ranked matches of player
player_role= []
for match in range(len(match_history)):                                                #iterate through each match and finds the team position and adds it to player role
    temp = lol_watcher.match.by_id('AMERICAS',match_history[match])
    time.sleep(1.5)
    for participant in temp['info']['participants']:
        if participant['summonerName'] == summoner_name:
            player_role.append(participant['teamPosition'])
            break
        else: 
            continue
print(summoner_name + '\'s main role is ' +  max(set(player_role), key=player_role.count)) #prints most frequent role based on list