import math
angle_degrees= float(input("Enter the angle of the shadow in degrees: "))
angle_radians = math.radians(angle_degrees)
adj_length = float(input("what is the length of the shadow:"))
height_mast = math.tan(angle_radians) * adj_length
print(f"The height of the mast is:{height_mast:.2f}m")
distance_hyp = adj_length/math.cos(angle_radians)
print(f"The distance from the base of the mast to the tip of the shadow is:{distance_hyp:.2f}m")

