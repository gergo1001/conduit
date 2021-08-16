class Article():
    user = ""
    title = ""
    shorttext = ""
    text = ""
    tags = []


    def __init__(self,link,tittle,shorttext,tags,text):
        self.link = link
        self.title = tittle
        self.shorttext = shorttext
        self.tags = tags
        self.text = text

    def setlink(self,link):
        self.link=link

    def gettitle(self):
        if self.title is not None:
            return self.title
        else:
            return ""

    def getstext(self):
        if self.shorttext is not None:
            return self.shorttext
        else:
            return ""

    def gettext(self):
        stringvalue=""
        if self.text is not None:
            return self.text
        else:
            return stringvalue



