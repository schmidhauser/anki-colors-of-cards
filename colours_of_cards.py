# -*- coding: utf-8 -*-
# Copyright: (c) 2019 Andreas U. Schmidhauser <https://github.com/schmidhauser>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
COLOURS OF MARKED, SUSPENDED, AND FLAGGED CARDS

This little addon allows one to change the standard background-colours of cards that are marked, suspended, or equipped with either flag1, flag2, flag3, or flag4. The six colours in question can be specified by using hexadecimal numerals or their standard colour names (see e.g. https://en.wikipedia.org/wiki/Web_colors). Upon install, there is only one noticeable change: marked cards appear no longer in grey (#cccccc) but in lavender (#e6e6fa).
"""

from anki.hooks import wrap
from aqt import browser

browser.COLOUR_MARKED = "lavender" # Default is #cccccc.
browser.COLOUR_SUSPENDED = "#ffffb2" # Default is # ffffb2.

browser.flagColours = {
    1: "#ffaaaa", # Default is #ffaaaa.
    2: "#ffb347", # Default is #ffb347.
    3: "#82e0aa", # Default is #82e0aa.
    4: "#85c1e9", # Default is #85c1e9.
}
