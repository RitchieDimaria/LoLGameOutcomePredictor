import requests
import pandas as pd
import time

# Replace 'YOUR_API_KEY' with your actual Riot API key
api_key = 'RGAPI-762c9c40-18a6-4046-a986-428c272c0080'

# Replace 'YOUR_MATCH_ID' with the actual match ID you want to query

df = pd.read_csv('./full_data_40.csv')
df = df.head(10000)
matchIds = df['matchID'].values

blueExperience = []
redExperience = []
blueLevel = []
redLevel = []
count = 0
for i in matchIds:

    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{i}'

    # Set up headers with the API key
    headers = {
        'X-Riot-Token': api_key,
    }

    # Make the API request
    response = requests.get(url, headers=headers)
    sumBlueExp = 0
    sumRedExp = 0
    sumBlueLevel = 0
    sumRedLevel = 0
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the JSON response
        res = response.json()
        x = res["info"]
        for participant in x["participants"]:
            if(participant["teamId"] == 100):
                sumBlueExp += participant["champExperience"]
                sumBlueLevel += participant["summonerLevel"]
            else:
                sumRedExp += participant["champExperience"]
                sumRedLevel += participant["summonerLevel"]
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
    print(count)
    count+=1
    time.sleep(1)
    blueExperience.append(sumBlueExp)
    redExperience.append(sumRedExp)
    blueLevel.append(sumBlueLevel)
    redLevel.append(sumRedLevel)
data = {
    
    "blueExperience":blueExperience,
    "redExperience":redExperience,
    "blueLevel":blueLevel,
    "redLevel":redLevel,
}

df = pd.DataFrame(data)
df.to_csv("extraFeaturesForDataset.csv", index=False)
