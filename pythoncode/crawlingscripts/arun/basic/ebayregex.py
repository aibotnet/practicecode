import re

l='["Part Type: Disc Brake Rotor, Position: Front, 7/8" Drive Flange"]'

print l


match = re.search(r'\[', l)

if match:                      
    print 'found', match.group() ## 'found word:cat'
    
k="arun\"kumar"

print k
