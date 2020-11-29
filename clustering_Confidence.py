#Prediction:
#-0.647005*x + 0.1650021
#-1.13005*x + 0.870034
ps1 = -0.647
pi1 = 0.165
ps2 = -1.13
pi2 = 0.87
t1 = 11/23
t2 = 6/23
t3 = 5/23

#Hypothesis1: 2004
#-1.22*x + 0.33
#-1.90505*x + 1.42
h1s1 = -1.22
h1i1 =  0.33
h1s2 = -1.905
h1i2 = 1.42
h1t1 = 16/23
h1t2 = 3/23
h1t3 = 4/23

#Hypothesis2:
#-0.43*x + 0.1410021
#-1.40905*x + 1.012
h2s1 = -0.43
h2i1 = 0.141
h2s2 = -1.409
h2i2 =  1.012
h1t1 = 13/23
h1t2 = 5/23
h1t3 = 5/23

slope1_confidence = max([h1s1 - ps1, h2s1 - ps1])
slope2_confidence = max([h1s2 - ps1, h2s2 - ps1])
intercept1_confidence = max([h1i1 - pi1, h2i1 - pi1])
intercept2_confidence = max([h1i2 - pi2, h2i2 - pi2])

print("Boundary conditions: ")
print("y = (" + str(ps1) + " +- " + str(slope1_confidence) + ")x + (" + str(pi1) + " +- " + str(intercept1_confidence) + ")")
print("y = (" + str(ps2) + " +- " + str(slope2_confidence) + ")x + (" + str(pi2) + " +- " + str(intercept2_confidence) + ")")
print("\n")
print("Relative confidence of slope of the line separating Tier 1 and Tier 2: " + str(abs(slope1_confidence/ ps1)) + "%")
print("Relative confidence of slope of the line separating Tier 2 and Tier 3: " + str(abs(slope2_confidence/ ps2)) + "%")