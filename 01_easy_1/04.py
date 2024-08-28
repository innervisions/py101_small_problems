# 04- How big is the room?
SQUARE_METER_IN_FEET = 10.7639

length = float(input("What is the room's length in meters?: "))
width = float(input("What is the room's width in meters?: "))

area_in_meters = length * width
area_in_feet = area_in_meters * SQUARE_METER_IN_FEET

print(
    f"The area of the room is {area_in_meters:.2f} "
    f"square meters ({area_in_feet:.2f} square feet)."
)
