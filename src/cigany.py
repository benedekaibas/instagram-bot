from vpython import box, vector, color

# Create a box
y = 5
first_box = box(
    pos=vector(y, 0, 0),
    size=vector(1, 2, 3), 
    color=color.red
)
second_box = box(
    pos=vector(y,1,1),
    size=vector(1,2,4),
    color=color.green
)
print(first_box, second_box)