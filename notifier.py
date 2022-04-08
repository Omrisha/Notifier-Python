from entities import ENTITY_TYPES
from obserable import ObserableEntity

class Notifier:
    def notify(self, message: str):
        raise NotImplementedError()

class ConsoleNotifier(Notifier):
    def notify(self, message: str):
        print(message)

class NotifierService():
    notifier: Notifier

    def __init__(self, notifier):
        self.notifier = notifier

    """
     API Method that gets:
     the entity object after modification
     the original entity
     entity type
    """
    def notifyEntityChange(self, entity_obj, original_entity_obj, type):
        if type not in ENTITY_TYPES:
            return

        if original_entity_obj is None:
            self.notifier.notify(entity_obj.notification_subject())
        elif entity_obj is None:
            self.notifier.notify(original_entity_obj.notification_subject())
        elif entity_obj != original_entity_obj:
            self.notifier.notify(entity_obj.notification_subject())
            
        

