from copy import copy
from datetime import datetime
from entities import CRAWLING_STATUSES, ENTITY_TYPES, Company, CompanyForEvent, ContentItem, Event
from notifier import ConsoleNotifier, NotifierService

notifer = ConsoleNotifier()
notifier_module = NotifierService(notifer)

company = Company(employees_min=10, employees_max=100, link="", name="Shell Company")
content_item = ContentItem(company=company, snippet="This is a trusted shell company", link="", name="Shell Company Secret Item")
event = Event(start_date=datetime.now(), link="", name="Launching Evil Corp")
company_for_event = CompanyForEvent(event=event, company=company)

# Test 1 - Add Company
notifier_module.notifyEntityChange(company, None, ENTITY_TYPES[1])

# Test 2 - Physically delete company
notifier_module.notifyEntityChange(None, company, ENTITY_TYPES[1])

# Test 2 - Crawling status change in company
updated_company = copy(company)
updated_company.crawling_status = CRAWLING_STATUSES.TEXT_ANALYZED

notifier_module.notifyEntityChange(updated_company, company, ENTITY_TYPES[1])

# Test 3 - Added company with new content item
notifier_module.notifyEntityChange(content_item, None, ENTITY_TYPES[3])

# Test 4 - Physically delete company with content item
notifier_module.notifyEntityChange(None, content_item, ENTITY_TYPES[3])

# Test 5 - Event added
notifier_module.notifyEntityChange(event, None, ENTITY_TYPES[0])

# Test 6 - Event physically deleted
notifier_module.notifyEntityChange(None, event, ENTITY_TYPES[0])

# Test 7 - Event is blacklisted
updated_event = copy(event)
updated_event.is_blacklisted = True
notifier_module.notifyEntityChange(updated_event, event, ENTITY_TYPES[0])

# Test 8 - Add event for a company
notifier_module.notifyEntityChange(company_for_event, None, ENTITY_TYPES[4])

# Test 9 - physically delete event for a company
notifier_module.notifyEntityChange(None, company_for_event, ENTITY_TYPES[4])

# Test 10 - Event for a company is blacklisted is blacklisted
updated_company_for_event = copy(company_for_event)
updated_company_for_event.is_blacklisted = True
notifier_module.notifyEntityChange(updated_event, company_for_event, ENTITY_TYPES[4])

# Test 11 - Not notifiying when company not changed
notifier_module.notifyEntityChange(company, company, ENTITY_TYPES[1])
