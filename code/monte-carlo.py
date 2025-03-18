# Implementation of monte-carlo simulation to project potential security price

import numpy as np

for i in range(0, 10000):
  shots_made = []
  for k in range(0, 100):
    r = np.random.random()
    if(r <= .7):
        shots_made.append(1)
    else:
        shots_made.append(0)

  if(sum(shots_made) >= 70):
    aggregate_shots_made.append(1)
  else:
    aggregate_shots_made.append(0)

print(np.average(aggregate_shots_made))
