# -*- coding: utf-8 -*-
# Copyright: (c) 2019 Andreas U. Schmidhauser <https://github.com/schmidhauser>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
COLORS OF MARKED, SUSPENDED, AND FLAGGED CARDS
"""

from anki.hooks import wrap
from aqt import browser

browser.COLOUR_MARKED = "lavender" # Default is #ccc.
browser.COLOUR_SUSPENDED = "#ffffb2" # Default is # ffffb2.

browser.flagColours = {
    1: "#ffaaaa", # Default is #ffaaaa.
    2: "#ffb347", # Default is #ffb347.
    3: "#82e0aa", # Default is #82e0aa.
    4: "#85c1e9", # Default is #85c1e9.
}