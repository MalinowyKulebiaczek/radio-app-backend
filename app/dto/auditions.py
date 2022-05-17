from app.model.models import Audition
from app.constants.constants import WeekDays


class AuditionsDTO:
    def __init__(self, auditions):
        self.auditions = auditions


audition1 = Audition(title='0 kultury', author='Maurycy Jędrzejewski', id=1,
                     urlImg='https://www.radioaktywne.pl/images/5/b/2/3/c/5b23c8f72a8badca32614e030d1959bdddeb5e10-u815wgo7d6ycnph.jpeg',
                     description='Lubicie dobrą muzykę? Niestety, nie jest to odpowiednia audycja. Jeśli jednak jakimś cudem spodoba się Wam jakiś kawałek puszczony w ramach "0 kultury", to zaciekawi Was też może historia artysty odpowiedzialnego za dany utwór. Na to wszystko i jeszcze więcej zaprasza co tydzień Maurycy Jędrzejewski.',
                     day=WeekDays.TUESDAY, hourStart='17:30', hourEnd='18:30'
                     )

audition2 = Audition(title='Aktyrave', author='Tymoteusz Gryszkalis', id=2,
                     urlImg='https://www.radioaktywne.pl/images/d/3/8/3/3/d3833c870ed4f2a08d498e3c6709c3893f8f29ad-vuxe2qjrvmfoq1w.jpg',
                     description='Audycja, w której rozkładamy polską i światową scenę rave na czynniki pierwsze. Najlepsza, najcięższa muzyka elektroniczna po tej stronie Wisły. Jeżeli lubicie techno, hardcore, hardtrance, a także inne podziemne gatunki poczujecie się tu jak w domu. Oprócz tego wywiady, historie, poradniki i wszystko co chcecie wiedzieć o świecie, przed którym zawsze przestrzegali Was rodzice.',
                     day=WeekDays.TUESDAY, hourStart='20:00', hourEnd='21:00'
                     )

audition3 = Audition(title='Aktywacja', author='Łukasz Kiciński', id=3,
                     urlImg='https://www.radioaktywne.pl/images/9/6/4/a/7/964a7773c3b3a6904b4c1728086153874b26db1f-kz8gzulsvwccq40.png',
                     description='Studencki serwis informacyjny z ogromną dawką najciekawszych newsów z Warszawy, którego centralnym punktem jest wywiad z twórcami przeróżnych inicjatyw.',
                     day=WeekDays.FRIDAY, hourStart='18:30', hourEnd='20:00'
                     )

audition4 = Audition(title='Biurko', author='Tomasz Kubik', id=4,
                     urlImg='https://www.radioaktywne.pl/images/f/f/4/3/4/ff434db960ba97abfff04bbb9ed0b4043a9d171b-cfh0kkxisr46elt.png',
                     description='Audycja miniaturka, ale stworzona z przyjaźni i pasji dwóch redaktorów - Tomasza Kubika i Macieja Wałejki. Co tydzień od 21:00 do 21:30, pomiędzy swoimi autorskimi audycjami, gaworzą i prezentują specjalne utwory, które nie pomieściłyby się w ich zwyczajnych audycjach. Często z uśmiechem i puszczeniem oka do słuchaczy, kulturalnie per pan, opowiadają o otaczającym świecie, nie tylko muzycznym. Czasem zdarzy się porozmawiać o ostatnich wydarzeniach związanych z klubem, którego jeden z panów jest zagorzałym fanem, a drugi z panów ma kartę kibica, choć nigdy na meczu nie był, ale dumnie używa jej jako karty miejskiej. Tak to właśnie u panów Redaktorów przekornie bywa. Co zrobić? Posłuchać i uśmiechnąć się do radioodbiornika.',
                     day=WeekDays.MONDAY, hourStart='18:30', hourEnd='20:00'
                     )

audition5 = Audition(title='Szuflada dźwięków', author='Maciej Wałejko', id=5,
                     urlImg='https://www.radioaktywne.pl/images/f/f/4/3/4/ff434db960ba97abfff04bbb9ed0b4043a9d171b-cfh0kkxisr46elt.png',
                     description='Szuflada Dźwięków powstała w lutym 2010 r., a jej pierwsze wydanie miało miejsce dokładnie 9 lutego. Co tydzień, najpierw we wtorki, a od 2012 r. w poniedziałki w Szufladzie usłyszeć można nowe płyty, zapowiedzi koncertów, ale i najpiękniejsze płyty z lat 60, 70, 80, 90 - tych czy też z XXI wieku. Audycja nie zamyka się w zasadzie na żaden rodzaj muzyki - o ile są to dźwięki poruszające muzyczną duszę. W audycji szukamy rzeczy nowych, wracamy do przeszłości i wspólnie przesłuchujemy najpiękniejsze utwory. Zaglądamy na koncerty, zapowiadamy płyty i nie zapominamy też o albumach zagubionych gdzieś po drodze, czasem mniej znanych. Muzycznie jest tu częściej spokojnie niż hałaśliwie. Audycja w poniedziałki od 21:30 do 22:30.',
                     day=WeekDays.MONDAY, hourStart='21:30', hourEnd='22:30'
                     )

audition6 = Audition(title='Post Scriptum', author='Bartosz Olszański', id=6,
                     urlImg='https://www.radioaktywne.pl/images/2/0/a/6/0/20a605055eed15c1cbd4c3f8afeeca827eb9797c-xfy8irvut9xo7fq.png',
                     description='Post Scriptum powstała w lutym 2010 r., a jej pierwsze wydanie miało miejsce dokładnie 9 lutego. Co tydzień, najpierw we wtorki, a od 2012 r. w poniedziałki w Szufladzie usłyszeć można nowe płyty, zapowiedzi koncertów, ale i najpiękniejsze płyty z lat 60, 70, 80, 90 - tych czy też z XXI wieku. Audycja nie zamyka się w zasadzie na żaden rodzaj muzyki - o ile są to dźwięki poruszające muzyczną duszę. W audycji szukamy rzeczy nowych, wracamy do przeszłości i wspólnie przesłuchujemy najpiękniejsze utwory. Zaglądamy na koncerty, zapowiadamy płyty i nie zapominamy też o albumach zagubionych gdzieś po drodze, czasem mniej znanych. Muzycznie jest tu częściej spokojnie niż hałaśliwie. Audycja w poniedziałki od 21:30 do 22:30.',
                     day=WeekDays.TUESDAY, hourStart='21:00', hourEnd='22:00'
                     )

audition7 = Audition(title='ScreenShot', author='Łukasz Gnyszko', id=7,
                     urlImg='https://www.radioaktywne.pl/images/f/0/8/7/4/f0874636b40535a17cb8f3062a10f87defb60f67-izfw4rnhrubcstv.png',
                     description='Za każdym kultowym albumem czy uznanym wykonawcą kryje się unikatowa historia warta opowiedzenia. "Screen Shot" to godzinne podsumowanie twórczości wybranych przez nas muzyków. Możecie się spodziewać opowieści o życiach uwielbianych przez nas artystów, czy historii nagrywania płyt do których wracamy przez lata. Co tydzień nową muzyką będą was zaskakiwać Łukasz Gnyszko i Łukasz Kiciński.',
                     day=WeekDays.WEDNESDAY, hourStart='16:30', hourEnd='17:30'
                     )

audition8 = Audition(title='Muzyczne Skrajności', author='Natalia Ostaszewska', id=8,
                     urlImg='https://www.radioaktywne.pl/images/f/0/8/7/4/f0874636b40535a17cb8f3062a10f87defb60f67-izfw4rnhrubcstv.png',
                     description='Muzyka ma wiele twarzy, wiele imion. W Muzycznych Skrajnościach prezentuje jak najwięcej w ciekawych i zaskakujących połączeniach. Czasami są to utwory bardzo znane czasami zupełnie nowe, odkryte gdzieś w otchłani Internetu. Pomysł na taka audycję zrodził się pewnej nocy, kiedy zadałam sobie pytanie: Co by było, gdybym połączyła różne gatunki w czasie tej jednej godziny. Co tydzień znajduje odpowiedź na to pytanie tworząc kolejne różnorodne playlisty. Jeśli chcecie usłyszeć, co z takich połączeń wyniknie, włączcie koniecznie Radio Aktywne w każdy czwartek o godzinie 20:00 Zawsze będzie muzycznie i klimatycznie, czasem mrocznie, czasem kolorowo i elektronicznie. Nie zabraknie muzycznych podróży w najdalsze zakątki świata, do miejsc, o których może nawet nigdy nie słyszeliście. Czasami pojawią się muzyczne ciekawostki, innym razem podróżnicze zależy jak taka playlista się ułoży.',
                     day=WeekDays.THURSDAY, hourStart='20:00', hourEnd='21:00'
                     )

auditions_list = [audition1, audition2, audition3, audition4, audition5, audition6, audition7, audition8]
auditions_dto = AuditionsDTO(auditions_list)