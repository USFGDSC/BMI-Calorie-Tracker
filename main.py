from taipy import Gui
from taipy.gui import Markdown
import pandas as pd


# Runs the pages on a local port
# Links external css file
Gui(page='Starter', css_file='main.css').run(use_reloader='true', port=5001)