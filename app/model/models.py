class Album:
    def __init__(self, id, title, author, urlImg, description, timeline):
        '''
        timeline - string in format 'dd.mm.yyyy - dd.mm.yyyy', eg. '10.05.2022 - 17.05.2022'
        this param represents when this album was chosen as album of the week
        '''
        self.id = id
        self.title = title
        self.author = author
        self.urlImg = urlImg
        self.description = description
        self.timeline = timeline


class Member:
    def __init__(self, id, name, surname, urlImg, mainAudition):
        self.id = id
        self.name = name
        self.surname = surname
        self.urlImg = urlImg
        self.mainAudition = mainAudition


class Recording:
    def __init__(self, id, title, url, description):
        self.id = id
        self.title = title
        self.url = url
        self.description = description


class Audition:
    def __init__(self, id, title, urlImg, author, description, day, hourStart, hourEnd):
        self.id = id
        self.title = title
        self.urlImg = urlImg
        self.author = author
        self.description = description
        self.day = day
        self.hourStart = hourStart
        self.hourEnd = hourEnd
