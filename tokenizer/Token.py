class Token(object):
    def __init__(self,type,value):
        print("TOKEN")
        self.type=type
        self.value=value

    def setTokenType(self,type):
        self.type=type

    def setValue(self,value):
        self.value=value

    def getTokenType(self):
        return self.type

    def getValue(self):
        return self.value

    def toString(self):
        return self.getValue()