greeting = "Hello, World!"
print(greeting)

# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1

total_days = little_mermaid_days + brother_bear_days + hercules_days
cost_per_movie = 3

total_cost = total_days * cost_per_movie

print(f"We spent {total_cost} on all 3 movies")

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350

total = 10 * facebook_rate + 6 * google_rate + 4 * amazon_rate
print(f"We earned {total} working for these companies.")

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_has_room = True
schedule_works = False

student_can_be_enrolled = class_has_room and schedule_works

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

purchased_more_than_two_items = False
offer_valid = True
premium_member = True

offer_can_be_applied = offer_valid and (purchased_more_than_two_items or premium_member)