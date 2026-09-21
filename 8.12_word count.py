countries = ["India", "United Sates", "Australia", "Ireland", "Sri Lanka",
             "Iceland", "Cuba", "Iran", "Poland"]

#Count all the countries which are starting with "I"
#Also, print all these countries as a list

counter = 0
output = []
for country in countries:
    if country[0] == "I":
        counter = counter + 1
        output.append(country)

print(counter)
print(output)


#another way -> startswith(char)
counter = 0
output = []
for country in countries:
    if country.startswith('I'):
        counter = counter + 1
        output.append(country)

print(counter)
print(output)