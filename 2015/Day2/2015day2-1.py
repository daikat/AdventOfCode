paper = 0

with open( "2015day2.data" ) as file:
	boxes = file.read().splitlines()

for box in boxes:
    length, width, height = box.split('x')
    lw = int(length)*int(width)
    wh = int(width)*int(height)
    hl = int(height)*int(length)
    paper += 2*lw + 2*wh + 2*hl + min(lw, wh, hl)
    
print(paper)
