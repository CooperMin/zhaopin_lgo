#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class SetCookie(object):
    def __init__(self,cookie):
        self.cookie = cookie

    def dictCookie(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ','')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict
    def saveDoc(self,itemDict):
        with open('Cookies.json','a+',encoding='utf-8') as f:
            f.writelines(f'{itemDict}\n')

if __name__ == '__main__':
    # cookie = '_ga=GA1.2.2138864544.1533631818; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536634040,1536653812,1536730869,1536804703; user_trace_token=20180807165100-01ebdef2-9a1f-11e8-a341-5254005c3644; LGUID=20180807165100-01ebe1dd-9a1f-11e8-a341-5254005c3644; LG_LOGIN_USER_ID=4044580018fedca9af00dfd183c448a8abc47cb79e14ec34a0d6b234cf2dae68; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.6003120.1536568128; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=21fd8afbf4d9053962d27eb7c8d6c4e9c2cd76096623fe9a2de3917f5bc4c6d2; SEARCH_ID=a50d2f7c8b1e4cdf971e587f6e48e052; WEBTJ-ID=20180913101142-165d0b2caca1a5-0c5be6b04e1d77-1161694a-2073600-165d0b2cacc371; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536822858; LGRID=20180913151426-a617a0f3-b724-11e8-95e8-525400f775ce; _putrc=57BBA9EB292AEBD8123F89F2B170EADC; JSESSIONID=ABAAABAAAGFABEF7112ACB7BD42EE4044106DB1FA0D20EB; login=true; unick=CooperMin; TG-TRACK-CODE=search_code; _gat=1; LGSID=20180913151423-a4192bba-b724-11e8-b815-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3F%26px%3Ddefault%26city%3D%25E4%25B8%258A%25E6%25B5%25B7; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Dnew%26city%3D%25E4%25B8%258A%25E6%25B5%25B7'
    cookie = '_ga=GA1.2.1482172372.1536567995; user_trace_token=20180910162642-3f23fed8-b4d3-11e8-8d43-525400f775ce; LGUID=20180910162642-3f2401c0-b4d3-11e8-8d43-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.320086161.1537423658; LGSID=20180920140749-8039446e-bc9b-11e8-a270-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; WEBTJ-ID=20180920140948-165f599498b1e2-0ae30b5637e6d-37664109-2073600-165f599498c90a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537247594,1537325931,1537423658,1537423788; JSESSIONID=ABAAABAAAGFABEFAE8226B74C9F26B4A7B7AFC188F01552; X_HTTP_TOKEN=0b189e04723024cd1fb67155e4f34243; LG_LOGIN_USER_ID=5bb9f0c5baa893ccac80e6c9d4e91a144eb6704c3f881303; _putrc=07C5713E3387BDE5; login=true; unick=%E6%B1%AA%E6%8C%AF%E5%9B%BD; hasDeliver=271; gate_login_token=5d1e2b545fd3457ba7c03ff8353f072f07b152caa04a7862; _gat=1; TG-TRACK-CODE=index_navigation; LGRID=20180920142702-2f9801bf-bc9e-11e8-a270-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537424811; SEARCH_ID=78ba4ea343704523ba313491d07f5e50'
    itemDict = SetCookie(cookie).dictCookie()
    SetCookie(cookie).saveDoc(itemDict)