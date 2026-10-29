def event_total(atendees, food_per_person, transport_per_person, venue_cost):
    return atendees *(food_per_person + transport_per_person) + venue_cost
 
normal_attendees = event_total(10,800,200,5000)
print(normal_attendees)

zero_attendees = event_total (0,800,200,5000)
print(zero_attendees) 

    