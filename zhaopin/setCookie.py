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

if __name__ == '__main__':
    # cookie = '_ga=GA1.2.2138864544.1533631818; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536634040,1536653812,1536730869,1536804703; user_trace_token=20180807165100-01ebdef2-9a1f-11e8-a341-5254005c3644; LGUID=20180807165100-01ebe1dd-9a1f-11e8-a341-5254005c3644; LG_LOGIN_USER_ID=4044580018fedca9af00dfd183c448a8abc47cb79e14ec34a0d6b234cf2dae68; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.6003120.1536568128; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=21fd8afbf4d9053962d27eb7c8d6c4e9c2cd76096623fe9a2de3917f5bc4c6d2; SEARCH_ID=a50d2f7c8b1e4cdf971e587f6e48e052; WEBTJ-ID=20180913101142-165d0b2caca1a5-0c5be6b04e1d77-1161694a-2073600-165d0b2cacc371; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536822858; LGRID=20180913151426-a617a0f3-b724-11e8-95e8-525400f775ce; _putrc=57BBA9EB292AEBD8123F89F2B170EADC; JSESSIONID=ABAAABAAAGFABEF7112ACB7BD42EE4044106DB1FA0D20EB; login=true; unick=CooperMin; TG-TRACK-CODE=search_code; _gat=1; LGSID=20180913151423-a4192bba-b724-11e8-b815-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3F%26px%3Ddefault%26city%3D%25E4%25B8%258A%25E6%25B5%25B7; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Dnew%26city%3D%25E4%25B8%258A%25E6%25B5%25B7'
    cookie = ' _ga=GA1.2.2138864544.1533631818; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536804703,1536891947,1537151709,1537239753; user_trace_token=20180807165100-01ebdef2-9a1f-11e8-a341-5254005c3644; LGUID=20180807165100-01ebe1dd-9a1f-11e8-a341-5254005c3644; LG_LOGIN_USER_ID=4044580018fedca9af00dfd183c448a8abc47cb79e14ec34a0d6b234cf2dae68; index_location_city=%E4%B8%8A%E6%B5%B7; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=597a851906b7a35fd1c77508ef403268e257ec90cd7713c2d27c441330929743; _gid=GA1.2.2121851475.1537151709; SEARCH_ID=9bb3f2f446d54f5db6d247ca5e7626fd; JSESSIONID=ABAAABAAAGGABCB37B492CE3C91EBFAD212544CA70166B2; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537249330; LGRID=20180918134221-9c864bd7-bb05-11e8-a1da-525400f775ce; _putrc=57BBA9EB292AEBD8123F89F2B170EADC; login=true; unick=CooperMin; TG-TRACK-CODE=index_navigation; _gat=1; LGSID=20180918134136-81c77ab5-bb05-11e8-baf2-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Dnew%26city%3D%25E4%25B8%258A%25E6%25B5%25B7%26district%3D%25E6%25B5%25A6%25E4%25B8%259C%25E6%2596%25B0%25E5%258C%25BA%26bizArea%3D%25E9%2599%2586%25E5%25AE%25B6%25E5%2598%25B4; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F'
    dictCookie = SetCookie(cookie).dictCookie()
    print(dictCookie)