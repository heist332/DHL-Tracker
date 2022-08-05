import requests
from bs4 import BeautifulSoup
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import time
import requests

answer = input('추적하실 아이디를 입력해주세요.')


while True:
    print('확인을 시작합니다.')
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value,
                         OperatingSystem.LINUX.value]

    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100)

    sess = requests.Session()

    user_agent = (user_agent_rotator.get_random_user_agent())

    print(user_agent)

    headers = {
        'authority': 'www.dhl.com',
        'method': 'GET',
        'path': f'/kr-ko/home/tracking/tracking-express.html?submit=1&tracking-id={answer}',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
        'cookie': f'cookieDisclaimer=seen; tracking-id={answer}; OptanonAlertBoxClosed=2022-02-17T11:59:51.364Z; OnetrustActiveGroups=%2CC0001%2CC0002%2CC0003%2CC0004%2C; s_ccst=%22target%22:true%2C%22ecid%22:true%2C%22aa%22:true; AMCVS_9D88879D5579828F7F000101%40AdobeOrg=1; s_cc=true; at_check=true; bm_sz=7BE3267743B884797F6D277F4C216F64~YAAQVuPfrcZJeQp/AQAAl5cEFg5Xq2c4CFalgwOUmte4gnUxlNAm2mQTk3JtHl4HBfHin8Td07C5K30DD1qqo6BBmPgEh8pGcUT5ujDVoFpdqbCHFrGsUgmhOVyuwKxZ8Pu7+QmDQzAlnSU3JJiZ89sRmdoEve9z09YJdPJ53F7JvdpoDwun4d015pLti7a5rPCBBUxoMReI0vnd/uP7jxt8ptBYXAlrG2pp2L2KQKQrZgnjK4FqdAeBiCCE8nbp6ZofSQm8nwPWl78luXTMuZkTh7QqLLZYMWBMH28m41IoXrh0InRUU8FnOHHXDDK4dkOe9YjhZlLqRCF/lGoAvdkazHOCLcwU2OhKScVQaLD7uOGStAgk8woyZZF84fzoPfT/J2IBS5eyvKTPkduX3pIXorpSmd8YNHvcbMlvlNi79g==~4605233~3420979; bm_mi=67C2D0DD584352062EC8200418726B61~zfLgxpJ6HvGV93HQrztphkCJOHpM8sfnR86TqQ4m4g3UJZ0fVwpUGjroHZx2+wzUH9+oJ2woDCLAzsqcbjGQ3DVFGjMN8ZCMOEGJ18/+DIVMB2bX37QOJuiy9t9/PH1bzJ15kBDkv5f6OIYogTI8+Vy+b7KUxhZyl66KlESuzExdQbQQUdfNABNji4OR8dviySwgn/319Gng/jits7kV08P4+1uGeMAxzVdbME+b//s3NuyKXX5MUPMV6kraQ8HfVfhvDyBT/V+jGe9U630h6WsPD40g2SCvcS7067Hvp46Xtee6iqlVAcEH49RjI96rINLdmbdmd1z2PD0XWFvb/Q==; AMCV_9D88879D5579828F7F000101%40AdobeOrg=-2121179033%7CMCIDTS%7C19044%7CMCMID%7C53196901067938248771113789822292657177%7CMCAAMLH-1645948089%7C11%7CMCAAMB-1645948089%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1645350489s%7CNONE%7CvVersion%7C5.3.0; ak_bmsc=D8921A26B3228C372FECDD13F431F49D~000000000000000000000000000000~YAAQVuPfrU6aeQp/AQAA2DgaFg7vyUX/5gnOv7gUXccS9OuM57C/tpU+WyAIxNCgRHSb3q6cGhxQszVAt91QzAQLagZCajndWWHUg7dwYzPdyRikBsx3iQZnCcXR6L96IfU+AHqS5xhpHUBZeBbNAFV8tEDVaZHtFfWky1O5Woj0DXdIFKz3D7+M1eI3bAVrUGdjeHT4AbPfNbSnWtDL4sF+WdBP5XcIYXBms1wSf59dTeFzMZiomICuZoecgmFVrzrxdKXEug00jKaKoMrENJC/A7Ka4/BJB5oCo+tASacdMqKuWKbUt1dbN9wb/GzZxH7wYJtNO3NW2VO4QSfMXUtryx5f7CrOLdoVN671aTgZzdsh2lVnD6I0499b/op6952r2uNxhABb8HU9uZ7B4FxAPixLHwSyupdLXNL+stlIYJQjnQZ59HPky2mZhJtNe8vHFy76or+SHPakf3Ju/nzdSMA=; RT="z=1&dm=www.dhl.com&si=c56508e1-2805-45c6-b0c6-01d9316f3cf0&ss=kzuywun0&sl=1&tt=s3&rl=1"; OptanonConsent=isIABGlobal=false&datestamp=Sun+Feb+20+2022+16%3A48%3A12+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.13.0&hosts=&consentId=969a2344-3efa-410a-87ce-7d10c69dc405&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=KR%3B29&AwaitingReconsent=false; mbox=PC#7ef95064f0d84b048684a6dd80b2f309.32_0#1708343993|session#8c52b02c3ab04bcd953a2d7570a4750f#1645345153; s_sq=%5B%5BB%5D%5D; bm_sv=1F34A191A27307F60BA461DFE5E1DE2C~ImHh2Lu19VWyBshmUDGsNkghEEMbDrFcD14I6CRiQphzGQc8N2g+xcBGSZrEWp4Pxs3LtxL5efgQHAVF4qq8oQc95Lb5iZp3s/iUKrjw95ahZSQfGnxweBPQAkLiGQ/tiOXiuofPh7moSXmIOhRXhQ==; _abck=21838D8178AA2A80805E4567F0FB0686~0~YAAQVuPfrV+beQp/AQAAQI4aFgf/vtLrP5yfoep/HTFk5YzoyPAqTRgiz331Jc+7vCAJrqvne7KRqCv45sgT3eA4M3xIWTx0SnBLCep28Hd/mc1VI1WaYAnNVyb4VKCYHb0tRma7GpWhDiywrrcYuzXDX5xXxzQH59sRRKKA//XtLvM6gGenZYMBAtIzlDwmfb5zSyfEfvoS1Ph+NnQNXWD8fehE9zRzybc0OFksaiVQ4TdbdUen++dURF2g8Jgu8xcAarftCnFxnhRTZLG4e28IzXtoCCf5xZTZ8XRE8I05mpYzvggIyWRt3JAPvaTEYKl80H2sLBeFwi0bOuxJQMwb6K0Y9Kf0HhCNYiD1YAcf+QIZf7ltav3uYcv+7zkLGF2dnVjQjcbTSFJtJgxxOnJfoGWCNKPp0IlCV1o=~-1~-1~-1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent,
    }

    # result = sess.get(
    #     'https://www.dhl.com/kr-ko/home/tracking/tracking-express.html?submit=1&tracking-id={answer}', headers=headers, verify=True, timeout=10.0).text

    # print(result)

    headers = {
        'authority': 'www.dhl.com',
        'method': 'GET',
        'path': f'/utapi?trackingNumber={answer}&language=ko&requesterCountryCode=KR',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
        'cookie': f'tracking-id={answer}; OptanonAlertBoxClosed=2022-02-17T11:59:51.364Z; OnetrustActiveGroups=%2CC0001%2CC0002%2CC0003%2CC0004%2C; s_ccst={%22target%22:true%2C%22ecid%22:true%2C%22aa%22:true}; AMCVS_9D88879D5579828F7F000101%40AdobeOrg=1; s_cc=true; at_check=true; bm_sz=7BE3267743B884797F6D277F4C216F64~YAAQVuPfrcZJeQp/AQAAl5cEFg5Xq2c4CFalgwOUmte4gnUxlNAm2mQTk3JtHl4HBfHin8Td07C5K30DD1qqo6BBmPgEh8pGcUT5ujDVoFpdqbCHFrGsUgmhOVyuwKxZ8Pu7+QmDQzAlnSU3JJiZ89sRmdoEve9z09YJdPJ53F7JvdpoDwun4d015pLti7a5rPCBBUxoMReI0vnd/uP7jxt8ptBYXAlrG2pp2L2KQKQrZgnjK4FqdAeBiCCE8nbp6ZofSQm8nwPWl78luXTMuZkTh7QqLLZYMWBMH28m41IoXrh0InRUU8FnOHHXDDK4dkOe9YjhZlLqRCF/lGoAvdkazHOCLcwU2OhKScVQaLD7uOGStAgk8woyZZF84fzoPfT/J2IBS5eyvKTPkduX3pIXorpSmd8YNHvcbMlvlNi79g==~4605233~3420979; bm_mi=67C2D0DD584352062EC8200418726B61~zfLgxpJ6HvGV93HQrztphkCJOHpM8sfnR86TqQ4m4g3UJZ0fVwpUGjroHZx2+wzUH9+oJ2woDCLAzsqcbjGQ3DVFGjMN8ZCMOEGJ18/+DIVMB2bX37QOJuiy9t9/PH1bzJ15kBDkv5f6OIYogTI8+Vy+b7KUxhZyl66KlESuzExdQbQQUdfNABNji4OR8dviySwgn/319Gng/jits7kV08P4+1uGeMAxzVdbME+b//s3NuyKXX5MUPMV6kraQ8HfVfhvDyBT/V+jGe9U630h6WsPD40g2SCvcS7067Hvp46Xtee6iqlVAcEH49RjI96rINLdmbdmd1z2PD0XWFvb/Q==; AMCV_9D88879D5579828F7F000101%40AdobeOrg=-2121179033%7CMCIDTS%7C19044%7CMCMID%7C53196901067938248771113789822292657177%7CMCAAMLH-1645948089%7C11%7CMCAAMB-1645948089%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1645350489s%7CNONE%7CvVersion%7C5.3.0; ak_bmsc=D8921A26B3228C372FECDD13F431F49D~000000000000000000000000000000~YAAQVuPfrU6aeQp/AQAA2DgaFg7vyUX/5gnOv7gUXccS9OuM57C/tpU+WyAIxNCgRHSb3q6cGhxQszVAt91QzAQLagZCajndWWHUg7dwYzPdyRikBsx3iQZnCcXR6L96IfU+AHqS5xhpHUBZeBbNAFV8tEDVaZHtFfWky1O5Woj0DXdIFKz3D7+M1eI3bAVrUGdjeHT4AbPfNbSnWtDL4sF+WdBP5XcIYXBms1wSf59dTeFzMZiomICuZoecgmFVrzrxdKXEug00jKaKoMrENJC/A7Ka4/BJB5oCo+tASacdMqKuWKbUt1dbN9wb/GzZxH7wYJtNO3NW2VO4QSfMXUtryx5f7CrOLdoVN671aTgZzdsh2lVnD6I0499b/op6952r2uNxhABb8HU9uZ7B4FxAPixLHwSyupdLXNL+stlIYJQjnQZ59HPky2mZhJtNe8vHFy76or+SHPakf3Ju/nzdSMA=; RT="z=1&dm=www.dhl.com&si=c56508e1-2805-45c6-b0c6-01d9316f3cf0&ss=kzuywun0&sl=1&tt=s3&rl=1"; OptanonConsent=isIABGlobal=false&datestamp=Sun+Feb+20+2022+16%3A48%3A12+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.13.0&hosts=&consentId=969a2344-3efa-410a-87ce-7d10c69dc405&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=KR%3B29&AwaitingReconsent=false; mbox=PC#7ef95064f0d84b048684a6dd80b2f309.32_0#1708343993|session#8c52b02c3ab04bcd953a2d7570a4750f#1645345153; s_sq=%5B%5BB%5D%5D; bm_sv=1F34A191A27307F60BA461DFE5E1DE2C~ImHh2Lu19VWyBshmUDGsNkghEEMbDrFcD14I6CRiQphzGQc8N2g+xcBGSZrEWp4Pxs3LtxL5efgQHAVF4qq8oQc95Lb5iZp3s/iUKrjw95bdNjFyZSnYXDeg5BWaoz1qV6/QrssocWpr35qBgqxLeQ==; _abck=21838D8178AA2A80805E4567F0FB0686~0~YAAQVuPfrcSreQp/AQAAyMMdFge/m+BQrwHFU5b4niYVdq9BlwX0okZn/jFAXHOAfSpXRWdcQxEVD1+LxpXqqvBANeh4FyGHo2743TtQP02eq6V+NwL34EUZNdI/nto/sSintZJRRxBR6LdEfeMCMWLKfG5j10jdrVgLJO/h9/Shz8zydpBRuIOBmSGxpFGTfo/rjtwIaTV7A0TdI3mnaM/xU/qsTgfNpHo1xnj7UzP9z5kPLGBljMsk4gb0ZUHtKuU7UvUmtNC9lQ970LTFJjFco2u8OebuSkRGNSg4ep1xZFcsYoDBqyh49bklIiuPCpWG7XKoDKW87qoS4n5jQmwTBS1jn7qtALkMAXcZDtEYdz4A40Aq4GGhpumIURkdzT87vWJ104UEOoxZEeeR67dj~-1~-1~-1',
        'referer': f'https://www.dhl.com/kr-ko/home/tracking/tracking-express.html?submit=1&tracking-id={answer}',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user_agent,
        'x-sec-clge-req-type': 'ajax'
    }
    # print(sess.get('https://www.dhl.com/kr-ko/home/tracking/tracking-express.html?submit=1&tracking-id={answer}',
    #       headers=headers, verify=True, timeout=10.0))

    sess.get(
        'https://dpcomdhl.tt.omtrdc.net/m2/dpcomdhl/mbox/json?mbox=target-global-mbox&mboxSession=46195c12d76944688b69c6000d1b6110&mboxPC=7ef95064f0d84b048684a6dd80b2f309.32_0&mboxPage=46ce2c3950a34508a07fb2ffbe970cac&mboxRid=3fdb388107d04932a0b021bb002b7b07&mboxVersion=1.8.3&mboxCount=1&mboxTime=1645381922802&mboxHost=www.dhl.com&mboxURL=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome%2Ftracking.html%3Ftracking-id%3D{answer}%26submit%3D1&mboxReferrer=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome.html&browserHeight=1279&browserWidth=1493&browserTimeOffset=540&screenHeight=1440&screenWidth=2560&colorDepth=24&devicePixelRatio=1.5&screenOrientation=landscape&webGLRenderer=ANGLE%20(NVIDIA%2C%20NVIDIA%20GeForce%20GTX%201070%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11-27.21.14.5730)&at_property=5266a903-7aed-1412-8a5a-e380ef252fcb&server=www.dhl.com&country=kr&language=ko&pageName=Tracking%20%7C%20DHL%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&entity.bu=Core&entity.id=Tracking%20%7C%20DHL%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&entity.name=Tracking%20&entity.pageURL=%2Fkr-ko%2Fhome%2Ftracking.html&pageNameTemplate=Tracking%20%7C%20DHL&entity.categoryId=Tool%20Hub&mboxMCSDID=508284A43E48C37D-29983C24C6CB34E4&mboxMCGVID=53196901067938248771113789822292657177&mboxAAMB=RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y&mboxMCGLH=11')
    sess.post('https://dhlcom.d3.sc.omtrdc.net/b/ss/dhlglobalrolloutprod/1/JS-2.22.3-LBWB/s75644166507442', data='AQB=1&ndh=1&pf=1&t=20%2F1%2F2022%2018%3A32%3A2%200%20-540&sdid=508284A43E48C37D-29983C24C6CB34E4&mid=53196901067938248771113789822292657177&aamlh=11&ce=UTF-8&pageName=Tracking%20%7C%20DHL&g=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome%2Ftracking.html%3Ftracking-id%3D{answer}%26submit%3D1&r=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome.html&c.&cm.&ssf=1&.cm&.c&cc=USD&server=www.dhl.com&events=event60%2Cevent210%2Cevent100%3D8.0%2Cevent7%2Cevent10%3D1&aamb=RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y&c1=campaign%3ANA&v3=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F98.0.4758.81%20Safari%2F537.36&v4=www.dhl.com&c5=2022-02-17T13%3A15%3A47Z&c6=Tracking%20%7C%20DHL&c15=Korea%2C%20Republic%20of&v19=Tracking%20%7C%20DHL%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&c23=D%3Dv50&v24=Global%20Logistics%20-%20International%20Shipping%20%7C%20DHL%20Home%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&v25=3&c26=6%3A00%20PM&v26=e&c27=Sunday&c28=Weekend&v28=Tracking%20%7C%20DHL%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&c33=D%3Dv74&v36=kr%7Cko&v50=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome%2Ftracking.html%3Ftracking-id%3D{answer}%26submit%3D1&c51=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&v56=8.0&v58=m-l&v71=NA&v72=NA&v74=Tracking%20%7C%20DHL%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&v75=Tracking&v76=Core&v77=Tool%20Hub&v78=NA&v105=2022-02-20%2018%3A32&v142=53196901067938248771113789822292657177&v143=Global%20Logistics%20-%20International%20Shipping%20%7C%20DHL%20Home%20%7C%20Korea%2C%20Republic%20of%20%7C%20KO&v151=https%3A%2F%2Fwww.dhl.com%2Fkr-ko%2Fhome%2Ftracking.html%3Ftracking-id%3D{answer}%26submit%3D1&v152=DHL.com%20%7C%20DHL.com%20%3A%20production%282022-02-17T13%3A15%3A47Z%29&v153=1&v154=kr%7Cko&v156=Page%20Top%20%3E%20All%20Pages%20%7C%20Consent%20%7C%20Onetrust%20Groups%20updated%20%7C%20%5BECID%2C%20Custom%20Event%5D%20%3E%20A%201%20%7C%20B%3AGlobal%20Page%20View%20Tracking&v164=459284&v200=53196901067938248771113789822292657177&s=2560x1440&c=24&j=1.6&v=N&k=Y&bw=1493&bh=1279&mcorgid=9D88879D5579828F7F000101%40AdobeOrg&AQE=1')
    sess.get('https://www.dhl.com/global/dhl/news-alerts.gnf.json ')
    url = f'https://www.dhl.com/utapi?trackingNumber={answer}&language=ko&requesterCountryCode=KR'

    okay = 0
    while okay == 0:

        try:
            result = sess.get(url, headers=headers, verify=True, timeout=10.0)
            print(result.text)
            if result.status_code == 200:
                okay = 1
        except Exception as e:
            print(e)
            pass
        time.sleep(3)

    print('현재 상태: ', result.json()['shipments'][0]['status']['description'])
    print('=====물품 기록=====')
    for i, n in zip(result.json()['shipments'][0]['events'], range(len(result.json()['shipments'][0]['events']))):
        print('===================')
        print(n + 1, '번째 기록\n', '시간: ', i['timestamp'],
              '\n기록', i['description'], '\n물품 아이디: ', str(i['pieceIds'][0])[:-7] + "*" * 7)
        print('===================')
    print('===================')
    print('30분 후 다시 확인합니다.')
    time.sleep(1800)
