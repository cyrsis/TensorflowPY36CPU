# ========================================================================= #
#                              Testing Out Time                             #
# :                                                                         #
# ========================================================================= #

import datetime

print(dir(datetime))

startime = datetime.datetime.now()

othertime =startime.replace(year=2014,)

print(othertime)

print(startime.strftime('%B %d %a'))
