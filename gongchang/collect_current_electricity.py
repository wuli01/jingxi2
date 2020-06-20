import requests
import time
import datetime
import json
import random

def collect_electric():
    t = time.time()
    microsecond = int(round(t * 1000))

    headers = {
        'authority': 'wq.jd.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'sec-fetch-dest': 'script',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15907492306869524270&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; unpl=V2_ZzNtbUVVSxUgCkYBeE1aUWIFQQ8SBxASfFoTUHgaXlVnAkBUclRCFnQUR1NnGFwUZwcZX0JcRxRFCEdkeBpdA2QzIm1BV3MURQhDVnkRXgNmChZtclBDHEU4BBAkRwc1ZAoTWURVQBB3OEdkexFcDW4FF1lFVHNeGwkLVH4bXg1lBRNURmdBFXUIRGR4; cn=0; user-key=e6810f0e-d3cd-4b8b-b04a-88985d49c331; TrackerID=tsxj2_dZVqvLkjHT9VAa0jSn-IKkKfu7EKItUE9a6nagexkW4ZsvRlrdPAGiXCLRPVxDEAyxq5JzEjdtEfy2GJiuW6PIgrirjsPW8veps3E; pt_key=AAJe5bkoADDblCJMrueZBqqB1hUANAavP1pP-1iFV2HxmxH-418-VT8odyMJ2pKX1mT3up9jSX4; pt_pin=754634469_m; pt_token=q33quway; pwdt_id=754634469_m; wxa_level=1; retina=1; cid=10; webp=1; sc_width=1536; visitkey=68838765784605337; qd_uid=KBENM725-O3R289M7S6F60PMOHSIJ; qd_fs=1592114080827; sk_history=100007958788%2C100012122588%2C2429195%2C100003222943%2C; ipLoc-djd=19-1607-4773-0; areaId=19; buy_uin=15432740016; jdpin=754634469_m; pin=754634469_m; wq_uin=15432740016; wlfstk_smdl=78pmqyc2zn70626dmvgzkz6mz5z2x2a5; __jda=94085062.1433937085.1565602967.1592581373.1592604713.107; __jdc=94085062; qd_ad=-%7C-%7Cdirect%7C-%7C0; 3AB9D23F7A4B3C9B=HOENZJ47QVRFRK6WUOKPXZWRJX6DERJ4DJRRGLOXRJTI7NXJMCUYGHBIY54KEYZQ234HYRAQJLQ6DT6NPDPRA6BB4U; mobilev=html5; qd_ls=1592604712680; qd_ts=1592624572504; qd_sq=23; wq_skey=zm5066B28EFFC94658B18C3D79F0E56AE2BE567BEA8B53E8983577AF1C5D6C6E83657C737D0B57581CE40462176E1DE22EB6D3A978BA3C9AF73EC7722E003160CA8D9451B624A64BCDC5346FE32C3189ED; priceProPin=FSJIMDP5OHFY634Z7XL3SF22S4; wq_logid=1592639531.2064654838; jxsid=15926395313828619948; PPRD_P=UUID.1433937085-LOGID.1592639531595.785575006-EA.17053.57.1; plusCustomBuryPointToken=1592642513399_4020; wqmnx1=MDEyNjM2NToubW9hdG50YWEuaTAwMlA3N3J0amFzdXVucGFtdWdzdW09MSZlcDM4NDdsIG5VbjlsYVhsaS4oLCApaS5pRWE2anAxcjdVNDRXT0hIKSk%3D; __wga=1592642649326.1592642649326.1592639531583.1592113453477.1.32; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1592642649331; wq_area=19_1607_4773%7C3; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; shshshfp=bb28c4616e6e3e83d8e4e812ae8a4ea1; shshshsID=43614af2c063adac6d42533a306a7e05_1_1592642649732',
    }

    t2 = time.time()
    microsecond2 = int(round(t2 * 1000))
    params = (
        ('zone', 'dream_factory'),
        ('apptoken', ''),
        ('pgtimestamp', ''),
        ('phoneID', ''),
        ('factoryid', '1099513774545'),
        ('doubleflag', '0'),
        ('timeStamp', 'undefined'),
        ('_time', microsecond),
        ('_', microsecond2),
        ('g_login_type', '0'),
        ('callback', 'jsonpCBKHHH'),
        ('g_tk', '650040397'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKHHH(', '')
    resultText = resultText.replace(')} catch (e) {}', '')
    # resultText = resultText.replace(';', '')
    resultTextJson = json.loads(resultText)
    if resultTextJson['msg'] == 'OK':
        print(localtime, '收电成功！')
    else:
        exit()

    print(localtime, '收电结果:', format(resultTextJson))

def cycle():
    """无规律的多次加电,防止被查出机器操作"""
    while True:
        currentTimestamp = int(time.time())
        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # 结束时间点
        stopLoopPointTimestamp = startLoopPointTimestamp + (6 * 3600) + 60
        # print(startLoopPointTimestamp)
        # print(stopLoopPointTimestamp)
        if currentTimestamp > startLoopPointTimestamp and currentTimestamp < stopLoopPointTimestamp:
            continue
        else:
            collect_electric()
            sleep_time = random.randint(200,1500)
            # sleep_time = 5
            time.sleep(sleep_time)

def main():
    # 调用
    cycle()
    
if __name__ == "__main__":
    main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/dreamfactory/userinfo/InvestElectric?zone=dream_factory&_time=1588858909667&productionId=1099515080572&_=1588858909668&sceneval=2&g_login_type=1&callback=jsonpCBKQ&g_tk=448376037&g_ty=ls', headers=headers)
