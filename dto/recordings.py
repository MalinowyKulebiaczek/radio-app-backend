from model.models import Recording


class RecordingsDTO:
    def __init__(self, recordings):
        self.recordings = recordings


recording1 = Recording(id=1, title='The Dames - wywiad w aktywacji środowej',
                       url='https://www.radioaktywne.pl/user/pages/03.nagrania/87.the-dames-wywiad-w-aktywacji-srodowej/I1JbCiL7wxetvdu.ogg',
                       description="Wywiad The Dames opis Lorem ipsum")

recording2 = Recording(id=2, title='Justyna Dobroć – wywiad w Aktywacji czwartkowej',
                       url='https://www.radioaktywne.pl/user/pages/03.nagrania/86.justyna-dobroc-wywiad-w-aktywacji-czwartkowej/MQsFhfPRTDvHn83.ogg',
                       description="Wywiad Justyna Dobroć opis Lorem ipsum")

recording3 = Recording(id=3, title='Bałtyk i Adam Karol (Polska z Offu) - wywiad w Aktywacji wtorkowej',
                       url='https://www.radioaktywne.pl/user/pages/03.nagrania/85.baltyk-i-adam-karol-drozdowski-polska-z-offu-wywiad-w-aktywacji-wtorkowej/2zEodgqiau941Ov.ogg',
                       description="Wywiad Bałtyk opis lorem ipsum")

recording4 = Recording(id=4, title='ParaNoise – wywiad w Aktywacji czwartkowej',
                       url='https://www.radioaktywne.pl/user/pages/03.nagrania/83.paranoise-wywiad-w-aktywacji-czwartkowej/LEXDrN5HeWZvYKw.ogg',
                       description="Wywiad ParaNoise opis lorem ipsum")

recording5 = Recording(id=5, title='jan bąk & bogdan sėkalski - wywiad w Tygodniku Muzycznym',
                       url='https://www.radioaktywne.pl/user/pages/03.nagrania/82.jan-bak-and-bogdan-s-kalski-wywiad-w-tygodniku-muzycznym/ebsnMKINGtumhlx.ogg',
                       description="Wywiad Jan Bąk opis lorem ipsum")

recordings_dto = RecordingsDTO([recording1, recording2, recording3, recording4, recording5])
