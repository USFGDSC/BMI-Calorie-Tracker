from taipy import Gui
from taipy.gui import Markdown
import pandas as pd


# cmd + shift + G to open usr/local/bin and find python interpreter path (Mac)


# Runs the pages on a local port
# Links external css file
Gui(page='Starter', css_file='main.css').run(use_reloader='true', port=5001)