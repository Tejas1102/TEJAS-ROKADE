# Stress When depth is constant
Q = float(input("Enter the value of Load in kN:"))
N= int(input("Number of data values of radial distance:"))
pi = 3.14159265359
Z = float(input("Depth:"))
r = []
for i in range (1, N+1):
  print("Enter radial distance in m".format (i))
  Value_r = float(input())
  r.append(Value_r)
  Stress =((3*Q)/(2*pi*Z*Z))*(((1/(1+((Value_r/Z)**2))))**2.5)
  print("Stress:",Stress,"kN/m^2")
  
  
  
  
  # Stress when Radius is Constant
Q = float(input("Enter the value of Load in kN:"))
M= int(input ("Number of data values of depth:"))
pi = 3.14159265359
r = float(input("Radial Distance:"))
Z = []
for j in range (1, M+1):
  print ("Enter depth in z".format (i))
  Value_Z = float(input())
  Z.append(Value_Z)
  Stress = ((3*Q)/(2*pi*Value_Z* Value_Z))*(((1/(1+((r/Value_Z)**2)))))**2.5
  print("Stress:", Stress,"kN/m^2")
  
  
  
  
  
  # Calculating the stress by Boussineq's Theory
Q= int(input("Enter the value of given load:"))
z= int(input("Enter the distance of vertical stress:"))
r= int(input("Enter the distance ofhorizntal stress:"))
stress = ((3*Q*(1/(1+(r/z)**2))**2.5))/(2*3.14*(z**2))
print("The value of stress is", stress)