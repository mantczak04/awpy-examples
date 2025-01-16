from awpy import Demo
from awpy.stats import adr
import pandas as pd

dem = Demo("spirit-vs-faze-m1-nuke.dem")

# EX 1
# Compare players damage during early, mid and late state of the round. (0-20s, 20-40s, 40-60s, 60-80s)

def checkDmgByTimeInterval(intervalBegin, intervalEnd, nickname, demo):
    AttackerDmgClockDf = demo.damages[['attacker_name', 'dmg_health_real', 'clock']].copy()
    
    #Convert clock to datetime for easier comparision
    AttackerDmgClockDf.loc[:, 'clock'] = pd.to_datetime(AttackerDmgClockDf['clock'], format='%M:%S', errors='coerce')
    
    #Filter rows based on nickname and time interval
    filteredDf = AttackerDmgClockDf[
        (AttackerDmgClockDf['attacker_name'] == nickname) & 
        (AttackerDmgClockDf['clock'] <= pd.to_datetime(intervalBegin, format='%M:%S')) & 
        (AttackerDmgClockDf['clock'] >= pd.to_datetime(intervalEnd, format='%M:%S'))
    ]
    # Sum up the dmg_health_real for the filtered rows
    totalDamage = filteredDf['dmg_health_real'].sum()
    return totalDamage

time_intervals = [
    ('1:56', '1:35'), #0-20 seconds
    ('1:35', '1:15'), #20-40 seconds
    ('1:14', '0:54'), #40-60 seconds
    ('0:53', '0:33')] #60-80 seconds

players = dem.damages['attacker_name'].dropna().unique() #TODO: faster way to find unique match players

for intervalBegin, intervalEnd in time_intervals:
    for player in players:
        totalDamage = checkDmgByTimeInterval(intervalBegin, intervalEnd, player, dem)
        print(f'Total damage for {player} from {intervalBegin} to {intervalEnd}: {totalDamage}')
    print(" ")