import requests
import json
import os

logo = r"""
    
           ______           ________ 
          / ____/__  ____  /  _/ __ \
         / / __/ _ \/ __ \ / // /_/ /
        / /_/ /  __/ /_/ // // ____/ 
        \____/\___/\____/___/_/      
        -> @Cretaed BY: hypn0thcy <-
                   #AoGiri
"""

try:
    print(logo)
    r = str(input('Lembrando, Para Usar precisa ter: PYTHON, REQUESTS.\n Caso Não Tenha digite: (ajuda)!\n  Caso Tenha E Deseja Continuar Clique ENTER! -> '))

    if r == 'ajuda':
        os.system('cls')
        print(logo)
        os.system('color 5')
        print('\nPara Utilizar o Script Abra o CMD e Digite:\n pip install requests\nLEMBRANDO: Quando For Instalar o Python marque a opção: "ADD TO PATH!"')
        exit()
    elif r == '':
        os.system('cls')
        print(logo)
        os.system('color 0a')
        print('')
        alvo = input('Qual o Alvo? (IP) -> ').strip()
        url = 'https://freegeoip.app/json/{}'.format(alvo)
        headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'ip': alvo,
            'User-Agent': 'Windows 10000'
            }
        req = requests.get(url, headers=headers)
        ctc = json.loads(req.text)
        print('Ip -> ', ctc['ip'])
        print('País ->', ctc['country_code'])
        print('Estado -> ', ctc['region_code'])
        print('Cidade -> ', ctc['city'])
        print('CEP -> ', ctc['zip_code'])
        print('Fuso Horário -> ', ctc['time_zone'])
        print('Latitude -> ', ctc['latitude'])
        print('Longitude -> ', ctc['longitude'])
    else:
        print("\n      -> Por Favor Apenas Digite (ajuda) Ou ENTER! <-   ")
except KeyboardInterrupt:
    os.system('color 9')
    print('\n          [!]      ATÉ MAIS! ^^    [!]')
    exit()
except Exception as y:
    os.system('color 4')
    print("\n [ERROR!] -> Houve Algum Problema! -> {}".format(y))
