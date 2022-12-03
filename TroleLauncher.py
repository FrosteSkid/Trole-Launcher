import os
import requests
from requests.structures import CaseInsensitiveDict
import json
from time import sleep
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Made By Froste#0001")
if os.path.exists('./accounts.json') == False:
    pathCreate = open('accounts.json', 'x')
if os.path.exists('./settings.json') == False:
    settingsCreate = open('settings.json', 'x')
pathh = './accounts.json'
settings = './settings.json'
#python TroleLauncher.py



def showAccounts():
    os.system('cls')
    allAccounts = json_data = json.load(open('accounts.json'))
    ia = 1
    for i in allAccounts:
        # device auth to token
        deviceAuth = i['deviceId']
        accID = i['accID']
        secret = i['secret']
        dispname = i['dispname']

        urlDevToToken = f'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'
        headersDevToToken = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
        }        
        bodyDevToToken= f"grant_type=device_auth&account_id={accID}&device_id={deviceAuth}&secret={secret}"
        requestDevToToken = requests.post(url=urlDevToToken, headers=headersDevToToken, data=bodyDevToToken)
        ratio = requestDevToToken.content.decode('utf-8')
        ratio = json.loads(ratio)
        AccessTokenGood = ratio['access_token']

        # exchange code
        urlTokenToExchange3 = f'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange'

        headersTokenToExchange3 = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {AccessTokenGood}'
        }

        requestTokenToExchange3 = requests.get(url=urlTokenToExchange3, headers=headersTokenToExchange3)

        ratio4 = requestTokenToExchange3.content.decode('utf-8')
        ratio4 = json.loads(ratio4)

        exchangeCode = ratio4['code']

        # caldera poopy
        headersCaldera3 = {
            "User-Agent": "Caldera/UNKNOWN-UNKNOWN-UNKNOWN",
            "Authorization": f'Bearer {AccessTokenGood}',
            "Content-Type": 'application/json'
        }

        bodyCaldera3 = json.dumps({
            "account_id": accID,
            "exchange_code": exchangeCode,
            "test_mode": False,
            "epic_app": "fortnite",
            "nvidia": False,
        })
                            
        requestCaldera3 = requests.post(url='https://caldera-service-prod.ecosec.on.epicgames.com/caldera/api/v1/launcher/racp', headers=headersCaldera3, data=bodyCaldera3)
        ratioCaldera = requestCaldera3.content.decode('utf-8')
        ratioCaldera = json.loads(ratioCaldera)

        antiCheat = ratioCaldera['provider']

        # queryprofile 

        queryProf = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accID}/client/QueryProfile?profileId=theater0&rvn=-1"
        headersQuery = CaseInsensitiveDict()
        headersQuery={
                "Authorization": f'Bearer {AccessTokenGood}',
                "Content-Type": 'application/json'
        }
        dataQuery = "{}"
        respQuery = requests.post(queryProf, headers=headersQuery, data=dataQuery)
        resultQuery = respQuery.content.decode('utf-8')
        resultQuery = json.loads(resultQuery)

        builds = ["Weapon:buildingitemdata_roofs","Weapon:buildingitemdata_floor","Weapon:buildingitemdata_wall","Weapon:buildingitemdata_stair_w"]
        pooo = []
        stuff=resultQuery['profileChanges'][0]["profile"]['items']
        for ibca in stuff:
            if stuff[ibca]['templateId'] in builds:
                pooo.append(ibca)

        queryProfc = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accID}/client/QueryProfile?profileId=common_core&rvn=-1"
        headersQueryc = CaseInsensitiveDict()
        headersQueryc={
                 "Authorization": f'Bearer {AccessTokenGood}',
                "Content-Type": 'application/json'
        }
        dataQueryc = "{}"
        respQueryc = requests.post(queryProfc, headers=headersQueryc, data=dataQueryc)
        resultQueryc = respQueryc.content.decode('utf-8')
        resultQueryc = json.loads(resultQueryc)

        loadoutss = []

        loadouts = resultQueryc['profileChanges'][0]['profile']['items']
        for xa in loadouts:
            ind = loadouts.get(xa)
            val = {i for i in loadouts if loadouts[i]==ind}
            for ai in loadouts:
                if loadouts[ai]['templateId'][:12] == "Currency:Mtx":
                    gamer = str(val)
                    loadoutss.append(ai)
        loadoutss = list(dict.fromkeys(loadoutss))
        vboink = 0
        for abcd in loadoutss:
            vboinkk = resultQueryc['profileChanges'][0]['profile']['items'][abcd]['quantity']
            vboink += vboinkk

        accid = i['accID']
        if pooo == []:
            print(f'{ia} | {i["dispname"]} | {accid} | Dupe Enabled | {antiCheat} | {vboink} vbucks')
        else:
            print(f'{ia} | {i["dispname"]} | {accid} | Dupe Not Enabled | {antiCheat} | {vboink} vbucks')
        ia += 1

while True:
    os.system('cls')
    choiceOfWhatToDo = int(input("1. Account Panel\n2. Launch on an Account\n3. Credits\n"))

    if choiceOfWhatToDo == 1:
        os.system('cls')
        choiceOfWhatToDo = int(input("1. Add an account\n2. Remove an account\n3. List of all accounts\n"))
        if choiceOfWhatToDo == 1:
            os.system('cls')
            if os.path.getsize(pathh) < 2:
                #if starting
                print(f'Authorization Code Link: https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code')
                print(f'Authorization Code Link with Login Prompt: https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3446cd72694c4a4485d81b77adbb2141%26responseType%3Dcode%0A&prompt=login')
                authcodeStart = input("Please submit an authorization code to save an account: ")
                urlAuth = f"https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
                }

                data = {
                    'grant_type': 'authorization_code',
                    'code': authcodeStart
                }


                resp = requests.post(urlAuth, headers=headers, data=data)   
                resultt = resp.content.decode('utf-8')
                resultt = json.loads(resultt)

                displayname = resultt['displayName']
                initialToken = resultt['access_token']
                accID = resultt['account_id']

                urlDevAuth = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{accID}/deviceAuth"

                headersDevice = CaseInsensitiveDict()
                headersDevice["Authorization"] = f"Bearer {initialToken}"
                headersDevice["Content-Type"] = "application/json"
            
                bodyDevice = {}

                respDevice = requests.post(urlDevAuth, headers=headersDevice, data=bodyDevice)
                devAuth = respDevice.content.decode('utf-8')
                devAuth = json.loads(devAuth)
                devAuthFinal = devAuth['deviceId']
                devAuthSecret = devAuth['secret']

                authCodeAndIdAndSecret = [{'deviceId':devAuthFinal, 'accID':accID, 'secret':devAuthSecret, 'dispname': displayname}]
                

                with open('accounts.json', 'a') as finalfile:
                    json.dump(authCodeAndIdAndSecret, finalfile)
                print(f"Saved {displayname} to accounts.json!")
            else:
                print(f'Authorization Code Link: https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3446cd72694c4a4485d81b77adbb2141%26responseType%3Dcode%0A&prompt=login')
                authcodeStart = input("Please submit an authorization code to save an account: ")
                urlAuth = f"https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
                }

                data = {
                    'grant_type': 'authorization_code',
                    'code': authcodeStart
                }


                resp = requests.post(urlAuth, headers=headers, data=data)   
                resultt = resp.content.decode('utf-8')
                resultt = json.loads(resultt)

                displayname = resultt['displayName']
                initialToken = resultt['access_token']
                accID = resultt['account_id']

                urlDevAuth = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{accID}/deviceAuth"

                headersDevice = CaseInsensitiveDict()
                headersDevice["Authorization"] = f"Bearer {initialToken}"
                headersDevice["Content-Type"] = "application/json"
                    
                bodyDevice = {}

                respDevice = requests.post(urlDevAuth, headers=headersDevice, data=bodyDevice)
                devAuth = respDevice.content.decode('utf-8')
                devAuth = json.loads(devAuth)
                devAuthFinal = devAuth['deviceId']
                devAuthSecret = devAuth['secret']

                authCodeAndIdAndSecret = {'deviceId':devAuthFinal, 'accID':accID, 'secret':devAuthSecret, 'dispname': displayname}
                startingJsonAccs = json_data = json.load(open('accounts.json'))
                startingJsonAccs.append(authCodeAndIdAndSecret)

                with open('accounts.json', 'w') as finalfile:
                    json.dump(startingJsonAccs, finalfile)
                print(f"Saved {displayname} to accounts.json!")
        if choiceOfWhatToDo == 2:
            allAccounts = json_data = json.load(open('accounts.json'))
            ia = 1
            for i in allAccounts:
                print(f'{ia} | {i["dispname"]}')
                ia += 1
            choiceOfWhatToRemove = int(input("Enter number of account to remove: "))
            choiceOfWhatToRemove= allAccounts[choiceOfWhatToRemove-1]
            allAccounts.remove(choiceOfWhatToRemove)
            with open('accounts.json', 'w') as outfile:
                json.dump(allAccounts, outfile)
                os.system('cls')
            ia = 1
            print("New Account List:")
            for i in allAccounts:
                print(f'{ia} | {i["dispname"]}')
                ia += 1
            sleep(5)
            os.system('cls')
        if choiceOfWhatToDo == 3:
            showAccounts()
            pressKeyToLeave = input("Press Enter to Leave:")
            
    elif choiceOfWhatToDo == 2:
        os.system('cls')
        # getting fortnite path
        if os.path.getsize(pathh) < 2:
            pressKeyToLeave = input("You have no saved accounts! Save some to get started")
        elif os.path.getsize(settings) < 2:
            fortnitePath = str(input("Please enter your Fortnite path here (eg. F:\(Epic) Games\Fortnite\FortniteGame\): "))
            #print(fortnitePath)
            pathDump = {'FortnitePath':fortnitePath}
            with open('./settings.json', 'w') as finalfile:
                json.dump(pathDump, finalfile)
        else:

            # account stuff
            dispname = 'dispname'
            allAccounts = json_data = json.load(open('accounts.json'))
            showAccounts()
            choiceOfWhatToDo = int(input("Enter number of account to launch on: "))
            print('Generating token...')

            json_data = []
            with open('accounts.json') as json_file:
                json_data = json.load(json_file)

            with open('settings.json') as settings_file:
                settings_json = json.load(settings_file)

            devAuthUseable = json_data[choiceOfWhatToDo-1]['deviceId']
            accIdUseable = json_data[choiceOfWhatToDo-1]['accID']
            secretUsable = json_data[choiceOfWhatToDo-1]['secret']
            dispnameUsable = json_data[choiceOfWhatToDo-1]['dispname']
            # DEVICE AUTH TO TOKEN

            deviceAuth = devAuthUseable
            Secret = secretUsable
            Acc_id = accIdUseable

            # generating access token to create exchange code
            urlDevToToken = f'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'

            headersDevToToken = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
            }        

            bodyDevToToken= f"grant_type=device_auth&account_id={Acc_id}&device_id={deviceAuth}&secret={Secret}"

            requestDevToToken = requests.post(url=urlDevToToken, headers=headersDevToToken, data = bodyDevToToken)

            ratio = requestDevToToken.content.decode('utf-8')
            ratio = json.loads(ratio)

            AccessTokenGood = ratio['access_token']


            # generating exchange code to create launcher token
            urlDevToExchange = f'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/exchange'

            headersDevToExchange = {
                'Authorization': f'Bearer {AccessTokenGood}'
            }        

            requestDevToTExchange = requests.get(url=urlDevToExchange, headers=headersDevToExchange)

            ratio = requestDevToTExchange.content.decode('utf-8')
            ratio = json.loads(ratio)
            ExchangeCode = ratio['code']

            # generating launcher token
            urlDevToLauncher = f'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'

            headersDevToLauncher = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'basic MzRhMDJjZjhmNDQxNGUyOWIxNTkyMTg3NmRhMzZmOWE6ZGFhZmJjY2M3Mzc3NDUwMzlkZmZlNTNkOTRmYzc2Y2Y='
            }        

            bodyDevToLauncher= f"grant_type=exchange_code&exchange_code={ExchangeCode}"

            requestDevToLauncher = requests.post(url=urlDevToLauncher, headers=headersDevToLauncher, data=bodyDevToLauncher)

            ratio = requestDevToLauncher.content.decode('utf-8')
            ratio = json.loads(ratio)
            
            launcherToken = ratio['access_token']

            # generating exchange code launcher
            urlDevToExchange = f'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/exchange'

            headersDevToExchange = {
                'Authorization': f'Bearer {launcherToken}'
            }        

            requestDevToTExchange = requests.get(url=urlDevToExchange, headers=headersDevToExchange)

            ratio = requestDevToTExchange.content.decode('utf-8')
            ratio = json.loads(ratio)
            ExchangeCodeLauncher = ratio['code']

            print(f'Launching on {allAccounts[choiceOfWhatToDo-1][dispname]}...')
            fnPath = 'FortnitePath'
            pppupu = settings_json[fnPath]+f'Binaries\Win64'
            os.system(f'cmd /c "start /d "{pppupu}" FortniteLauncher.exe -AUTH_LOGIN=unused -AUTH_PASSWORD={ExchangeCodeLauncher} -AUTH_TYPE=exchangecode -epicapp=Fortnite -epicenv=Prod -EpicPortal -epicuserid={Acc_id}"')
            print()
    
    elif choiceOfWhatToDo == 4:
        os.system('cls')
        print("Devs")
        sleep(.75)
        print("Froste")
        sleep(.75)
        print("Krowe Moh")
        sleep(.75)
        print("Contributors")
        sleep(.75)
        print("Rift")
        sleep(7.5)