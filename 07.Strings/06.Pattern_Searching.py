#Find all the indixes of occurrences of small text in the large text.
# I/P: txt="geeksforgeeks"
# O/P: pat="geeks"

txt = input("Enter Text: ")
pat = input("Enter Pattern: ")
pos = txt.find(pat)
while pos>=0:
    print(pos)
    pos = txt.find(pat,pos+1)
    