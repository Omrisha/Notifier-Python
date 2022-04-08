class ObserableEntity:
    def __init__(self):
        pass

    def notification_subject(self):
        return self

    def __eq__(self, __o: object) -> bool: 
        if not isinstance(__o, self.__class__):
            return False
        return self.__dict__ == __o.__dict__

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)