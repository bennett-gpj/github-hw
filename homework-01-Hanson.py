# Bennett Hanson
# June 6, 2023
# Homework 1

answer = input("What year were you born in?")
answer = int(answer)
print('You are', (2023 - answer), 'years old')
years = (2023 - (int(answer)))
years = int(years)
print("Your heart has beaten about", (years * 35000000) / 1000000, "million times")
print("A blue whale's heart has beaten about", round((years * 6 * 60 * 24 * 365) / 1000000), "million times in that time")
print("A rabbit's heart has beaten about", round((years * 135 * 60 * 24 * 365) / 1000000000, 2), "billion times in that time")
print("You are", round(years * 1.615198), "years old on Venus")
print("You are", round(years / 165, 2), "years old on Neptune")
if years == 33:
    print("You are the same age as me")
elif years <33:
    print("You are younger than me")
elif years >33:
    print("You are older than me")
if years <33:
    print("You are", (33 - years), "years younger than me")
elif years >33:
    print("You are", (years - 33), "years older than me")
def is_even(answer):
    return answer % 2 == 0
def is_odd(answer):
    return answer % 2 !=0
if is_even(answer):
    print("You were born in an even year")
if is_odd(answer):
    print("You were born in an odd year")

points = 0
if answer >=2021 and answer <2024:
    points = 1
elif answer >=2009 and answer <2021:
    points = 2
elif answer >= 1993 and answer <2009:
    points = 3
elif answer >= 1977 and answer <1993:
    points = 4
elif answer >= 1963 and answer <1977:
    points = 5
elif answer >= 1961 and answer <1963:
    points = 6
print(points, "presidents from the Democratic party have been president between 1960 and when you were born")

if answer >=2021 and answer <2024:
    print("Biden was in office when you were born")
elif answer >=2017 and answer <=2021:
    print("Trump was in office when you were born")
elif answer >= 2009 and answer <=2017:
    print("Obama was in office when you were born")
elif answer >= 2001 and answer <=2009:
    print("Bush Jr. was in office when you were born")
elif answer >= 1993 and answer <=2001:
    print("Clinton was in office when you were born")
elif answer >= 1989 and answer <=1993:
    print("Bush Sr. was in office when you were born")
elif answer >= 1981 and answer <=1989:
    print("Reagan was in office when you were born")
elif answer >= 1977 and answer <=1981:
    print("Carter was in office when you were born")
elif answer >= 1974 and answer <=1977:
    print("Ford was in office when you were born")
elif answer >= 1969 and answer <=1974:
    print("Nixon was in office when you were born")
elif answer >= 1963 and answer <=1969:
    print("LBJ was in office when you were born")
elif answer >= 1961 and answer <=1963:
    print("JFK was in office when you were born")
elif answer <= 1961:
    print("Eisenhower was in office when you were born")