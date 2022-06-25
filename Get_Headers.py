import requests


header_steam ="""
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36
"""


def headers_steam():
    headers = header_steam.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(":")[1:])).strip().replace("//", "://") for x in headers}
    return headers


def cookies_TR():
    cookies = {}
    cks='wants_mature_content=1; timezoneOffset=28800,0; _ga=GA1.2.1063857132.1609566468; browserid=2592383162310354568; steamMachineAuth76561198134511405=; steamMachineAuth76561199142712602=; _gid=GA1.2.719722418.1655810870; lastagecheckage=1-0-2000; steamMachineAuth76561199224251480=6DBF3E75902F8D1743166D57A7D77B9E09E32C71; steamMachineAuth76561199203484893=; steamRememberLogin=76561199224251480||8d5a455c55611b45699dd6dddf633672; sessionid=8b0848e71801e5b509e0f754; recentapps={"485450":1656109643,"526870":1656041947,"1948280":1656041813,"490510":1656031226,"601150":1656009608,"438180":1656009472,"621050":1656008332,"434570":1656007241,"450850":1656006728,"91200":1655936917}; steamLoginSecure=76561199224251480||614FC9700BE77ADA7E3D7FB562B6C57677D0B985; app_impressions=485950@1_7_7_2300_150_1|525300@1_7_7_2300_150_1|605210@1_7_7_2300_150_1|614910@1_7_7_2300_150_1|352120@1_7_7_2300_150_1|568500@1_7_7_2300_150_1|463480@1_7_7_2300_150_1|428900@1_7_7_2300_150_1|96100@1_7_7_2300_150_1|407420@1_7_7_2300_150_1|605210@1_7_7_2300_150_2|614910@1_7_7_2300_150_2|352120@1_7_7_2300_150_2|568500@1_7_7_2300_150_2|463480@1_7_7_2300_150_2|428900@1_7_7_2300_150_2|96100@1_7_7_2300_150_2|407420@1_7_7_2300_150_2|485950@1_7_7_2300_150_2|562360@1_7_7_2300_150_2|273500@1_7_7_2300_150_2|540190@1_7_7_2300_150_2|391260@1_7_7_2300_150_2|457520@1_7_7_2300_150_2|496120@1_7_7_2300_150_2|484890@1_7_7_2300_150_2|341310@1_7_7_2300_150_2|518730@1_7_7_2300_150_2'
    s = cks.split(';')
    for i in s:
        name, value = i.strip().split('=', 1)
        cookies[name] = value
    return cookies


def cookies_AR():
    cookies = {}
    cks = 'timezoneOffset=28800,0; _ga=GA1.2.1063857132.1609566468; browserid=2592383162310354568; steamMachineAuth76561198134511405=; steamMachineAuth76561199142712602=; _gid=GA1.2.719722418.1655810870; steamMachineAuth76561199224251480=; steamMachineAuth76561199203484893=3600425DFD5DF13F2EDF9339CA1E85F0A437F8B5; steamRememberLogin=76561199203484893||038e74902568b490ecfa31c860a01a80; lastagecheckage=1-0-2000; steamLoginSecure=76561199203484893||A33D8063D989B39C302CB771926B341C868B1E98; sessionid=b630389a8852e7b79de9080a; birthtime=943977601; recentapps={"365820":1655934663,"260330":1655934632,"588160":1655927526,"45770":1655927480,"427190":1655927433,"547710":1655925242,"357070":1655925190,"635880":1655925173,"45740":1655924818,"360830":1655924810}; app_impressions=367520@1_5_9__414|813780@1_5_9__414|367520@1_5_9__414|813780@1_5_9__414|367520@1_5_9__414|813780@1_5_9__414|260291@1_5_9__405|260293@1_5_9__405|260292@1_5_9__405|394360@1_5_9__414'
    s = cks.split(';')
    for i in s:
        name, value = i.strip().split('=', 1)
        cookies[name] = value
    return cookies


def cookies_MARKET():
    cookies = {}
    cks = 'timezoneOffset=28800,0; _ga=GA1.2.1878506775.1610714589; steamMachineAuth76561199142712602=76EB6C0CE5015F6D825F110B669E07C257C62AD2; steamMachineAuth76561198134511405=E1F2725D11918B3CE675660A02B470C3D61CAFF1; browserid=2370585954171969504; youtube_refreshtoken="1\/\/06Nlk5kdKPoaqCgYIARAAGAYSNwF-L9IrD8V29Geqh2fHyStFoOQUvktCsXXXFNEt9VbaxkeCqQgq0Va_nJK-twv49ztYmcGFPwk"; youtube_accesstoken={"access_token":"ya29.A0ARrdaM93odGIMQYJiMe2KotQXdV4VjkuB2a_qwymIzxhsega67PTHDkRKXYtMSlSpYrHrwloOoRioPxn6Ahjim1zDf0NMrqJqPgRAGUU-oJp4HeTqg-Dqpv1dsJCkrTXUuTYnFZj6Zd6pdAQE1BwSMFSmHsnYUNnWUtBVEFTQVRBU0ZRRl91NjFWeXlBVENWaTZNU28yOU9NZ2xrcjFidw0163","expires_in":3599,"refresh_token":"1\/\/06Nlk5kdKPoaqCgYIARAAGAYSNwF-L9IrD8V29Geqh2fHyStFoOQUvktCsXXXFNEt9VbaxkeCqQgq0Va_nJK-twv49ztYmcGFPwk","scope":"https:\/\/www.googleapis.com\/auth\/youtube.readonly","token_type":"Bearer","created":1655491354}; youtube_authaccount=Verik Karl; strInventoryLastContext=753_6; _gid=GA1.2.258615942.1655811065; steamMachineAuth76561199203484893=7DFC194C0D1AAC2E6E1022118AD134D854681D7B; recentlyVisitedAppHubs=431960,236850,294100,703080,1329410,281990,646570,2025170,2025200,2025270,485440; sessionid=eb2b4c1c5f0bb1b156b16ae9; steamCountry=RU|41b8f23b5ecd35af40bd3247fb22082a; steamLoginSecure=76561199224251480||2C09A26E3DE1846DC8FA69FE26B5DC53CEA07BC2; steamMachineAuth76561199224251480=559421063ED497640F29AA7EEBE8BCB7A7AD5088; steamRememberLogin=76561199224251480||8d5a455c55611b45699dd6dddf633672; webTradeEligibility={"allowed":1,"allowed_at_time":0,"steamguard_required_days":15,"new_device_cooldown_days":7,"time_checked":1656111215}'
    s = cks.split(';')
    for i in s:
        name, value = i.strip().split('=', 1)
        cookies[name] = value
    return cookies


if __name__ == "__main__":
    s = requests.session()
    s.get('https://store.steampowered.com/', headers=headers_steam(), cookies=cookies_TR())
    cookie = s.cookies.get_dict()
    print(cookie)





