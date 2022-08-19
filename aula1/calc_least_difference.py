def least_difference(a, b, c):
  difAB = abs(a - b)
  difBC = abs(b - c)
  difAC = abs(a - c)
  diffs = [difAB, difBC, difAC]
  return min(diffs)
  
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)
