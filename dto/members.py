from model.models import *


class MembersDTO:
    def __init__(self, list_of_members):
        self.members = list_of_members


member1 = Member(id=1, name='Maurycy', surname='Jedrzejewski',
                 urlImg='https://www.radioaktywne.pl/images/d/f/c/a/6/dfca6c4bf8e8f89d7567e2a166a187214cb463e8-6nbcwmhv4a8dixa.jpg',
                 mainAudition='0 kultury')

member2 = Member(id=2, name='Łukasz', surname='Kiciński',
                 urlImg='https://www.radioaktywne.pl/images/f/9/8/f/b/f98fbab6f1554329f289bd2d672c213d3c7eabd4-rakolegium-3.jpg',
                 mainAudition='Aktywacja Piątkowa')

member3 = Member(id=3, name='Łukasz', surname='Gnyszko',
                 urlImg='https://www.radioaktywne.pl/images/1/6/8/9/2/168924ac953580363a35e447368d96b27f4a3bc6-rakolegium-4-cropped.jpg',
                 mainAudition='ScreenShot')

member4 = Member(id=4, name='Anna', surname='Bobko',
                 urlImg='https://www.radioaktywne.pl/images/6/c/c/2/e/6cc2e3fc5c3dff9333d4d6c63edbb21041045c5e-rakolegium-1-cropped.jpg',
                 mainAudition='Retro Disco')

member5 = Member(id=5, name='Adam', surname='Smolarek',
                 urlImg='https://www.radioaktywne.pl/images/6/c/c/2/e/6cc2e3fc5c3dff9333d4d6c63edbb21041045c5e-rakolegium-1-cropped.jpg',
                 mainAudition='Halo, Odbiór?')

member6 = Member(id=6, name='Andrzej', surname='Krupa',
                 urlImg='https://www.radioaktywne.pl/images/5/5/3/c/8/553c822506ccd66718329c4974b0ffbcdb1d1b15-ynhof2v4zlqgw6t.jpg',
                 mainAudition='Czwarty Wymiar')

member7 = Member(id=7, name='Kinga', surname='Rodzik',
                 urlImg='https://www.radioaktywne.pl/images/c/b/5/4/e/cb54e75326f8590f00ce2087b8f0283cde5dbd9f-4s72zgin6wpxmdk.jpg',
                 mainAudition='Miło mi to słyszeć')

member8 = Member(id=8, name='Anna', surname='Dziubany',
                 urlImg='https://www.radioaktywne.pl/images/6/a/c/a/4/6aca4893dd35fea09a4ef789e843dc16a45361ea-s4m7db6ahqoyzwl.jpg',
                 mainAudition="Let's Play")

member9 = Member(id=9, name='Karol', surname='Kępka',
                 urlImg='https://www.radioaktywne.pl/images/a/e/1/d/9/ae1d94a316cb06f5429ba54fdddef8c96e6f71e7-v8chrs4ug2mzk0b.png',
                 mainAudition="Let's Play")

list_of_members = [member1, member2, member3, member4, member5, member6, member7, member8, member9]
members_dto = MembersDTO(list_of_members)