ribbon = 0

with open( "2015day2.data" ) as file:
	boxes = file.read().splitlines()

for box in boxes:
    length, width, height = (int(x) for x in box.split('x'))
    ribbon += 2*min(length+width, width+height, height+length) + length*width*height
    
print(ribbon)
