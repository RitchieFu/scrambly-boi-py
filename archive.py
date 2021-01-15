# 2x2 scrambling code
# make sure to change back to [9:] if using this again

theMoves = ['']
while len(theMoves) < 10:
  theMoves.append(random.choice(URF))
  if theMoves[-1] == theMoves[-2]:
      del theMoves[-1]

for t in URF:
  if t not in theMoves:
      theMoves[random.randint(1, 9)] = t
      break

theMoves = [item.replace('_', str(random.choice(specification)))
          for item in theMoves]
del theMoves[0]