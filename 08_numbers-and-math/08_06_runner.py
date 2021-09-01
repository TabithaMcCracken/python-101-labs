# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
distance = 10
minutes = 30
seconds = 30

total_seconds = (minutes * 60) + seconds
hours = total_seconds / 3600
kph = distance*1.6/hours
print (kph)