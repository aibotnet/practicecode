
def print_symmetric(l):
    for point in l:
        x1,y1,x2,y2= point.strip().split(' ')
        print int(x2)+(int(x2)-int(x1)), int(y2)+(int(y2)-int(y1)) 
        

n = int(raw_input())
l = list()

while n>0:
    l.append(raw_input())
    n-=1

print_symmetric(l)