# You need to install the 'graphviz' Python package and the Graphviz system package.
# For the Python package, run this in your terminal:
#     pip install graphviz
# For the system package (required for rendering), use:
#     brew install graphviz   # on macOS with Homebrew
#     sudo apt-get install graphviz   # on Ubuntu/Debian
from graphviz import Digraph

dot = Digraph('WaterCycle', format='svg')
dot.attr(layout='neato', overlap='false')
dot.attr('node', shape='rectangle')
dot.node('1','Evaporation')
dot.node('2','Transpiration')
dot.node('3','Condensation')
dot.node('4','Precipitation')
dot.node('5','Collection')
dot.node('6','Infiltration')
dot.node('7','Groundwater Flow')
dot.node('8','Sublimation')
dot.edge('1','3')
dot.edge('2','3')
dot.edge('3','4')
dot.edge('4','5')
dot.edge('5','1')
dot.edge('5','6')
dot.edge('6','7')
dot.edge('7','5')
dot.edge('8','3')
dot.render('water_cycle')