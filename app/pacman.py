# -*- coding: utf-8 -*-

from datetime import datetime

from app.utilities import common as pl
# from app.utilities import locale as pll

print("Hello World")

print(f'Environment is {pl.get_environment()}')

# print(f'Locale is {pll.get_locale()}')
print(pl.onFutureDay(datetime.today(), 0))

# End
