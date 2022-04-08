from entities import CRAWLING_STATUSES, ENTITY_TYPES, Company, CompanyCompetitor, CompanyForEvent, CompanyForWebinar, ContentItem, CrawlableEntity

class Notifier:
    def notify(self, message):
        raise NotImplementedError()

class ConsoleNotifier(Notifier):
    def notify(self, message):
        print(message)

class NotifierService():
    notifier: Notifier

    def __init__(self, notifier):
        self.notifier = notifier

    # API Method that gets:
    # the entity object after modification
    # the original entity
    # entity type
    def notifyEntityChange(self, entity_obj, original_entity_obj, type):
        notify_as = type
        if type == ENTITY_TYPES[3]:
            notify_as = ENTITY_TYPES[1]
        elif type == ENTITY_TYPES[4]:
            notify_as = ENTITY_TYPES[0]
        elif type == ENTITY_TYPES[5]:
            notify_as = ENTITY_TYPES[2]
        elif type == ENTITY_TYPES[6]:
            notify_as = ENTITY_TYPES[1]

        self.__notify_check_logic(entity_obj, original_entity_obj, notify_as, type)

    # Private method with logic to decide if to notify
    def __notify_check_logic(self, entity, original, notify_as, type):
        if original != entity:
            self.notifier.notify("notify on: {notifier}".format(notifier=notify_as))
        # if original == None:
        #     self.notifier.notify("notify on: {notifier} New obejct".format(notifier=notify_as))
        # elif entity == None:
        #     self.notifier.notify("notify on: {notifier} is physically deleted".format(notifier=notify_as))
        # elif entity.is_deleted != original.is_deleted:
        #     self.notifier.notify("notify on: {notifier} is_deleted".format(notifier=notify_as))
        # elif (type != ENTITY_TYPES[4] or type != ENTITY_TYPES[5] or type != ENTITY_TYPES[6]) and entity.crawling_status != original.crawling_status and (entity.crawling_status == CRAWLING_STATUSES.TEXT_ANALYZED or entity.crawling_status == CRAWLING_STATUSES.TEXT_UPLOADED):
        #     self.notifier.notify("notify on: {notifier} crawling_status change".format(notifier=notify_as))
        # elif entity.is_blacklisted != original.is_blacklisted and type != ENTITY_TYPES[1] or type != ENTITY_TYPES[5]:
        #         self.notifier.notify("notify on: {notifier} is_blacklisted".format(notifier=notify_as))

