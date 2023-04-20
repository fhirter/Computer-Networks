from pprint import pprint

import numpy as np
from control import db2mag

levels = [0, 3, 6, 10, 20, 3, 40, 60]
multipliers = db2mag(np.array(levels)).round(1)

pprint(np.array(levels))
pprint(multipliers)