from app import db
from app.database.db_manage import *
from app.constants.constants import WeekDays

db.drop_all()
db.create_all()

# ----------------------------- ALBUMS ------------------------------------#
insert_album(title='Bastard Disco', author='Satelity',
             urlImg='https://www.radioaktywne.pl/images/a/5/7/0/8/a57080a9920b7ae6e0c5d52979851c026b07d3b0-msc70vilalfpmng.jpg',
             description='Naszą obecną Płytą Tygodnia jest najnowszy album polsko-ukraińskiego zespołu Bastard Disco o nazwie „Satelity”. To solidna porcja energicznego i wyrazistego grania, zahaczającego stylistycznie o post punk, post hardcore i szeroko pojętą alternatywę. To świetny album, który swoją dynamiką przenosi nas do lat 90. i zachwyca wieloma chwytliwymi riffami.',
             timelineStart="09.05.2022",
             timelineEnd="16.05.2022")

insert_album(title='Fetlar', author='Inner Forensics', timelineStart="02.05.2022", timelineEnd="09.05.2022",
             urlImg='https://www.radioaktywne.pl/images/d/1/9/d/d/d19dd89d05d7a85c66219d71de8d1e9287ab4a05-zp6mwqu48d9fzb3.png',
             description='Naszą obecną Płytą Tygodnia jest „Inner Forensics”, czyli najnowszy album Mateusza Lubiewskiego, występującego pod nazwą Fetlar. To mieszanka ambientowych brzmień i elektronicznych motywów w stylu IDM i glitch, które nawiązują formą do utworów ze Studia Eksperymentalnego Polskiego Radia. Tematycznie „Inner Forensics” odnosi się do wpływu sztucznej inteligencji na tworzenie muzyki w dobie ciągłego rozwoju technologicznego. To wyrazisty album, który spodoba się fanom szeroko pojętej muzyki elektronicznej.')

insert_album(title='Latarnik', author='Marianna', timelineStart="25.04.2022", timelineEnd="02.05.2022",
             urlImg='https://www.radioaktywne.pl/images/1/2/9/a/9/129a9670f8d878b10f7f3869c1d41c1b45e8c8e0-jofzt5f2qtz8jgv.jpg',
             description='Naszą obecną Płytą Tygodnia w Radiu Aktywnym jest najnowszy album Marka Pędziwiatra (Latarnik) o nazwie „Marianna”. To zbiór dziewięciu instrumentalnych utworów zagranych wyłącznie na pianinie, których całość opowiada wzruszającą historię o korzeniach i przeszłości muzyka. Artysta na każdej kompozycji w szczery i zaangażowany sposób przelewa swoje emocje na instrument, jednocześnie nawiązując tematycznie do historii swojej prababci Marianny. To album pełen szeroko pojętej wirtuozerii, który udowadnia, że polski jazz cały czas ma się bardzo dobrze.')

# ----------------------------- AUDITIONS ------------------------------------#
insert_audition(title='0 kultury', author='Maurycy Jędrzejewski',
                urlImg='https://www.radioaktywne.pl/images/5/b/2/3/c/5b23c8f72a8badca32614e030d1959bdddeb5e10-u815wgo7d6ycnph.jpeg',
                description='Lubicie dobrą muzykę? Niestety, nie jest to odpowiednia audycja. Jeśli jednak jakimś cudem spodoba się Wam jakiś kawałek puszczony w ramach "0 kultury", to zaciekawi Was też może historia artysty odpowiedzialnego za dany utwór. Na to wszystko i jeszcze więcej zaprasza co tydzień Maurycy Jędrzejewski.',
                day=WeekDays.TUESDAY, hourStart='17:30', hourEnd='18:30'
                )

insert_audition(title='Aktyrave', author='Tymoteusz Gryszkalis',
                urlImg='https://www.radioaktywne.pl/images/d/3/8/3/3/d3833c870ed4f2a08d498e3c6709c3893f8f29ad-vuxe2qjrvmfoq1w.jpg',
                description='Audycja, w której rozkładamy polską i światową scenę rave na czynniki pierwsze. Najlepsza, najcięższa muzyka elektroniczna po tej stronie Wisły. Jeżeli lubicie techno, hardcore, hardtrance, a także inne podziemne gatunki poczujecie się tu jak w domu. Oprócz tego wywiady, historie, poradniki i wszystko co chcecie wiedzieć o świecie, przed którym zawsze przestrzegali Was rodzice.',
                day=WeekDays.TUESDAY, hourStart='20:00', hourEnd='21:00'
                )

insert_audition(title='Aktywacja', author='Łukasz Kiciński',
                urlImg='https://www.radioaktywne.pl/images/9/6/4/a/7/964a7773c3b3a6904b4c1728086153874b26db1f-kz8gzulsvwccq40.png',
                description='Studencki serwis informacyjny z ogromną dawką najciekawszych newsów z Warszawy, którego centralnym punktem jest wywiad z twórcami przeróżnych inicjatyw.',
                day=WeekDays.FRIDAY, hourStart='18:30', hourEnd='20:00'
                )

insert_audition(title='Biurko', author='Tomasz Kubik',
                urlImg='https://www.radioaktywne.pl/images/f/f/4/3/4/ff434db960ba97abfff04bbb9ed0b4043a9d171b-cfh0kkxisr46elt.png',
                description='Audycja miniaturka, ale stworzona z przyjaźni i pasji dwóch redaktorów - Tomasza Kubika i Macieja Wałejki. Co tydzień od 21:00 do 21:30, pomiędzy swoimi autorskimi audycjami, gaworzą i prezentują specjalne utwory, które nie pomieściłyby się w ich zwyczajnych audycjach. Często z uśmiechem i puszczeniem oka do słuchaczy, kulturalnie per pan, opowiadają o otaczającym świecie, nie tylko muzycznym. Czasem zdarzy się porozmawiać o ostatnich wydarzeniach związanych z klubem, którego jeden z panów jest zagorzałym fanem, a drugi z panów ma kartę kibica, choć nigdy na meczu nie był, ale dumnie używa jej jako karty miejskiej. Tak to właśnie u panów Redaktorów przekornie bywa. Co zrobić? Posłuchać i uśmiechnąć się do radioodbiornika.',
                day=WeekDays.MONDAY, hourStart='18:30', hourEnd='20:00'
                )

insert_audition(title='Szuflada dźwięków', author='Maciej Wałejko',
                urlImg='https://www.radioaktywne.pl/images/f/f/4/3/4/ff434db960ba97abfff04bbb9ed0b4043a9d171b-cfh0kkxisr46elt.png',
                description='Szuflada Dźwięków powstała w lutym 2010 r., a jej pierwsze wydanie miało miejsce dokładnie 9 lutego. Co tydzień, najpierw we wtorki, a od 2012 r. w poniedziałki w Szufladzie usłyszeć można nowe płyty, zapowiedzi koncertów, ale i najpiękniejsze płyty z lat 60, 70, 80, 90 - tych czy też z XXI wieku. Audycja nie zamyka się w zasadzie na żaden rodzaj muzyki - o ile są to dźwięki poruszające muzyczną duszę. W audycji szukamy rzeczy nowych, wracamy do przeszłości i wspólnie przesłuchujemy najpiękniejsze utwory. Zaglądamy na koncerty, zapowiadamy płyty i nie zapominamy też o albumach zagubionych gdzieś po drodze, czasem mniej znanych. Muzycznie jest tu częściej spokojnie niż hałaśliwie. Audycja w poniedziałki od 21:30 do 22:30.',
                day=WeekDays.MONDAY, hourStart='21:30', hourEnd='22:30'
                )

insert_audition(title='Post Scriptum', author='Bartosz Olszański',
                urlImg='https://www.radioaktywne.pl/images/2/0/a/6/0/20a605055eed15c1cbd4c3f8afeeca827eb9797c-xfy8irvut9xo7fq.png',
                description='Post Scriptum powstała w lutym 2010 r., a jej pierwsze wydanie miało miejsce dokładnie 9 lutego. Co tydzień, najpierw we wtorki, a od 2012 r. w poniedziałki w Szufladzie usłyszeć można nowe płyty, zapowiedzi koncertów, ale i najpiękniejsze płyty z lat 60, 70, 80, 90 - tych czy też z XXI wieku. Audycja nie zamyka się w zasadzie na żaden rodzaj muzyki - o ile są to dźwięki poruszające muzyczną duszę. W audycji szukamy rzeczy nowych, wracamy do przeszłości i wspólnie przesłuchujemy najpiękniejsze utwory. Zaglądamy na koncerty, zapowiadamy płyty i nie zapominamy też o albumach zagubionych gdzieś po drodze, czasem mniej znanych. Muzycznie jest tu częściej spokojnie niż hałaśliwie. Audycja w poniedziałki od 21:30 do 22:30.',
                day=WeekDays.TUESDAY, hourStart='21:00', hourEnd='22:00'
                )

insert_audition(title='ScreenShot', author='Łukasz Gnyszko',
                urlImg='https://www.radioaktywne.pl/images/f/0/8/7/4/f0874636b40535a17cb8f3062a10f87defb60f67-izfw4rnhrubcstv.png',
                description='Za każdym kultowym albumem czy uznanym wykonawcą kryje się unikatowa historia warta opowiedzenia. "Screen Shot" to godzinne podsumowanie twórczości wybranych przez nas muzyków. Możecie się spodziewać opowieści o życiach uwielbianych przez nas artystów, czy historii nagrywania płyt do których wracamy przez lata. Co tydzień nową muzyką będą was zaskakiwać Łukasz Gnyszko i Łukasz Kiciński.',
                day=WeekDays.WEDNESDAY, hourStart='16:30', hourEnd='17:30'
                )

insert_audition(title='Muzyczne Skrajności', author='Natalia Ostaszewska',
                urlImg='https://www.radioaktywne.pl/images/f/0/8/7/4/f0874636b40535a17cb8f3062a10f87defb60f67-izfw4rnhrubcstv.png',
                description='Muzyka ma wiele twarzy, wiele imion. W Muzycznych Skrajnościach prezentuje jak najwięcej w ciekawych i zaskakujących połączeniach. Czasami są to utwory bardzo znane czasami zupełnie nowe, odkryte gdzieś w otchłani Internetu. Pomysł na taka audycję zrodził się pewnej nocy, kiedy zadałam sobie pytanie: Co by było, gdybym połączyła różne gatunki w czasie tej jednej godziny. Co tydzień znajduje odpowiedź na to pytanie tworząc kolejne różnorodne playlisty. Jeśli chcecie usłyszeć, co z takich połączeń wyniknie, włączcie koniecznie Radio Aktywne w każdy czwartek o godzinie 20:00 Zawsze będzie muzycznie i klimatycznie, czasem mrocznie, czasem kolorowo i elektronicznie. Nie zabraknie muzycznych podróży w najdalsze zakątki świata, do miejsc, o których może nawet nigdy nie słyszeliście. Czasami pojawią się muzyczne ciekawostki, innym razem podróżnicze zależy jak taka playlista się ułoży.',
                day=WeekDays.THURSDAY, hourStart='20:00', hourEnd='21:00'
                )

# ----------------------------- MEMBERS ------------------------------------#

insert_member(name='Maurycy', surname='Jedrzejewski',
              urlImg='https://www.radioaktywne.pl/images/d/f/c/a/6/dfca6c4bf8e8f89d7567e2a166a187214cb463e8-6nbcwmhv4a8dixa.jpg',
              mainAudition='0 kultury')

insert_member(name='Łukasz', surname='Kiciński',
              urlImg='https://www.radioaktywne.pl/images/f/9/8/f/b/f98fbab6f1554329f289bd2d672c213d3c7eabd4-rakolegium-3.jpg',
              mainAudition='Aktywacja Piątkowa')

insert_member(name='Łukasz', surname='Gnyszko',
              urlImg='https://www.radioaktywne.pl/images/1/6/8/9/2/168924ac953580363a35e447368d96b27f4a3bc6-rakolegium-4-cropped.jpg',
              mainAudition='ScreenShot')

insert_member(name='Anna', surname='Bobko',
              urlImg='https://www.radioaktywne.pl/images/6/c/c/2/e/6cc2e3fc5c3dff9333d4d6c63edbb21041045c5e-rakolegium-1-cropped.jpg',
              mainAudition='Retro Disco')

insert_member(name='Adam', surname='Smolarek',
              urlImg='https://www.radioaktywne.pl/images/6/c/c/2/e/6cc2e3fc5c3dff9333d4d6c63edbb21041045c5e-rakolegium-1-cropped.jpg',
              mainAudition='Halo, Odbiór?')

insert_member(name='Andrzej', surname='Krupa',
              urlImg='https://www.radioaktywne.pl/images/5/5/3/c/8/553c822506ccd66718329c4974b0ffbcdb1d1b15-ynhof2v4zlqgw6t.jpg',
              mainAudition='Czwarty Wymiar')

insert_member(name='Kinga', surname='Rodzik',
              urlImg='https://www.radioaktywne.pl/images/c/b/5/4/e/cb54e75326f8590f00ce2087b8f0283cde5dbd9f-4s72zgin6wpxmdk.jpg',
              mainAudition='Miło mi to słyszeć')

insert_member(name='Anna', surname='Dziubany',
              urlImg='https://www.radioaktywne.pl/images/6/a/c/a/4/6aca4893dd35fea09a4ef789e843dc16a45361ea-s4m7db6ahqoyzwl.jpg',
              mainAudition="Let's Play")

insert_member(name='Karol', surname='Kępka',
              urlImg='https://www.radioaktywne.pl/images/a/e/1/d/9/ae1d94a316cb06f5429ba54fdddef8c96e6f71e7-v8chrs4ug2mzk0b.png',
              mainAudition="Let's Play")

# ----------------------------- RECORDINGS ------------------------------------#

insert_recording(title='The Dames - wywiad w aktywacji środowej',
                 url='https://www.radioaktywne.pl/user/pages/03.nagrania/87.the-dames-wywiad-w-aktywacji-srodowej/I1JbCiL7wxetvdu.ogg',
                 urlImg='',  # TODO
                 description="Wywiad The Dames opis Lorem ipsum")

insert_recording(title='Justyna Dobroć – wywiad w Aktywacji czwartkowej',
                 url='https://www.radioaktywne.pl/user/pages/03.nagrania/86.justyna-dobroc-wywiad-w-aktywacji-czwartkowej/MQsFhfPRTDvHn83.ogg',
                 urlImg='',  # TODO
                 description="Wywiad Justyna Dobroć opis Lorem ipsum")

insert_recording(title='Bałtyk i Adam Karol (Polska z Offu) - wywiad w Aktywacji wtorkowej',
                 url='https://www.radioaktywne.pl/user/pages/03.nagrania/85.baltyk-i-adam-karol-drozdowski-polska-z-offu-wywiad-w-aktywacji-wtorkowej/2zEodgqiau941Ov.ogg',
                 urlImg='',  # TODO
                 description="Wywiad Bałtyk opis lorem ipsum")

insert_recording(title='ParaNoise – wywiad w Aktywacji czwartkowej',
                 url='https://www.radioaktywne.pl/user/pages/03.nagrania/83.paranoise-wywiad-w-aktywacji-czwartkowej/LEXDrN5HeWZvYKw.ogg',
                 urlImg='',  # TODO
                 description="Wywiad ParaNoise opis lorem ipsum")

insert_recording(title='jan bąk & bogdan sėkalski - wywiad w Tygodniku Muzycznym',
                 urlImg='',  # TODO
                 url='https://www.radioaktywne.pl/user/pages/03.nagrania/82.jan-bak-and-bogdan-s-kalski-wywiad-w-tygodniku-muzycznym/ebsnMKINGtumhlx.ogg',
                 description="Wywiad Jan Bąk opis lorem ipsum")
