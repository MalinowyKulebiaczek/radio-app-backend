from model.models import *


class AlbumsDTO:
    def __init__(self, albums):
        self.albums = albums


album1 = Album(id=1, title='Bastard Disco', author='Satelity',
               urlImg='https://www.radioaktywne.pl/images/a/5/7/0/8/a57080a9920b7ae6e0c5d52979851c026b07d3b0-msc70vilalfpmng.jpg',
               description='Naszą obecną Płytą Tygodnia jest najnowszy album polsko-ukraińskiego zespołu Bastard Disco o nazwie „Satelity”. To solidna porcja energicznego i wyrazistego grania, zahaczającego stylistycznie o post punk, post hardcore i szeroko pojętą alternatywę. To świetny album, który swoją dynamiką przenosi nas do lat 90. i zachwyca wieloma chwytliwymi riffami.',
               timeline="09.05.2022 - 16.05.2022")

album2 = Album(id=2, title='Fetlar', author='Inner Forensics', timeline="02.05.2022 - 09.05.2022",
               urlImg='https://www.radioaktywne.pl/images/d/1/9/d/d/d19dd89d05d7a85c66219d71de8d1e9287ab4a05-zp6mwqu48d9fzb3.png',
               description='Naszą obecną Płytą Tygodnia jest „Inner Forensics”, czyli najnowszy album Mateusza Lubiewskiego, występującego pod nazwą Fetlar. To mieszanka ambientowych brzmień i elektronicznych motywów w stylu IDM i glitch, które nawiązują formą do utworów ze Studia Eksperymentalnego Polskiego Radia. Tematycznie „Inner Forensics” odnosi się do wpływu sztucznej inteligencji na tworzenie muzyki w dobie ciągłego rozwoju technologicznego. To wyrazisty album, który spodoba się fanom szeroko pojętej muzyki elektronicznej.')

album3 = Album(id=3, title='Latarnik', author='Marianna', timeline="25.04.2022 - 02.05.2022",
               urlImg='https://www.radioaktywne.pl/images/1/2/9/a/9/129a9670f8d878b10f7f3869c1d41c1b45e8c8e0-jofzt5f2qtz8jgv.jpg',
               description='Naszą obecną Płytą Tygodnia w Radiu Aktywnym jest najnowszy album Marka Pędziwiatra (Latarnik) o nazwie „Marianna”. To zbiór dziewięciu instrumentalnych utworów zagranych wyłącznie na pianinie, których całość opowiada wzruszającą historię o korzeniach i przeszłości muzyka. Artysta na każdej kompozycji w szczery i zaangażowany sposób przelewa swoje emocje na instrument, jednocześnie nawiązując tematycznie do historii swojej prababci Marianny. To album pełen szeroko pojętej wirtuozerii, który udowadnia, że polski jazz cały czas ma się bardzo dobrze.')

albums_dto = AlbumsDTO([album1, album2, album3])
