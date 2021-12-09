class EzData():
    def setData(self, token, topic, val): ...  # noqa
    def addToList(self, token, list, val): ...  # noqa
    def getData(self, token, topic, val, offset, count): ...  # noqa
    def removeData(self, token, topic): ...  # noqa
    def getCurrentISODateTime(): ...  # noqa


ezdata = EzData()
