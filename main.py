from display import Display

dim = (128, 64)

display = Display()
#x, y, color
for i in range(dim[0]):
    for j in range(dim[1]):
        display.pixel(i, j, 1)
        display.show()
        display.pixel(i, j, 0)

display.show()