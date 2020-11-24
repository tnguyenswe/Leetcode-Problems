
input = [1,2,1,4]

set1 = set()

for i, val in enumerate(input):
  if input[i] in set1:
    print("true")
  else:
    set1.add(input[i])

print("false")
