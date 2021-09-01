# Python 101 Section 8 Project
# Population Growth Calculator
# Write the necessary code to display the total population count for the next 3 years (without a leap year).
# Here are the specifications:

# In the country we want to investigate:

# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

starting_pop = 380123456
seconds_born = 6
seconds_dead = 12
seconds_immigrating = 40

people_born = ((60/seconds_born)*60*24*365)*3
people_dead = ((60/seconds_dead)*60*24*365)*3
people_immigrating = ((60/seconds_immigrating)*60*24*365)*3

end_pop = starting_pop + people_born + people_immigrating - people_dead
print(end_pop)

# Another way
starting_pop = 380123456
people_per_minute = (60/6) + (60/40) - (60/12)
people_per_3years = people_per_minute * 60 * 24 * 365 * 3
end_pop = people_per_3years + starting_pop

print (end_pop)