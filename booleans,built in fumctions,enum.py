NAME=True
print(type(NAME)==bool)
print(round(5.5))

from enum import Enum
class sat(Enum):
    INACTIVE=3
    ACTIVE=10
    
print(sat.ACTIVE.value)
print(len(sat))