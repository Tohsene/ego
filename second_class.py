#Question 1

s1 = "Ault"
s2 = "Kelly"
index = s1.find("lt")
new_s1 = s1[:index] + s2 + s1[index:]
# new_s1 = s1[:2] + s2 + s1[-2:]
print(new_s1)

#Question 2

s1 = "America"
s2 = "Japan"
output = s1[0] + s2[0] + s1[3] + s2[2] + s1[-1] + s2[-1]
print(output)

#Question 3

s1 = "Abc"
s2 = "Xyz"
output = s1[0] + s2[2] + s1[1] + s2[1] + s1[2] + s2[0]
print(output)
