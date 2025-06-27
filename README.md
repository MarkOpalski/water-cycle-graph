# Water Cycle Graph

An interactive visualization of the water cycle using Python and Graphviz.

## Overview

This project generates a visual representation of the water cycle showing the relationships between different processes like evaporation, transpiration, condensation, precipitation, collection, infiltration, groundwater flow, and sublimation.

## Features

- SVG-based visualization
- Clean, minimal design
- Web-ready output
- Easy to modify and extend

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install system-level Graphviz:
```bash
# macOS
brew install graphviz

# Ubuntu/Debian
sudo apt-get install graphviz

# Windows
# Download from https://graphviz.org/download/
```

## Usage

Generate the water cycle visualization:

```bash
python render.py
```

This creates `water_cycle.svg` which you can then move to the `docs/` folder:

```bash
mv water_cycle.svg docs/index.svg
```

View the result by opening `docs/index.html` in a web browser.

## Files

- `render.py` - Main script that generates the visualization
- `requirements.txt` - Python dependencies
- `docs/` - Output folder for web-ready files
- `docs/index.html` - Simple HTML page to display the SVG
- `docs/index.svg` - Generated water cycle visualization

## Customization

You can modify the `render.py` script to:
- Add new nodes (water cycle processes)
- Change the layout algorithm
- Modify colors and styling
- Add labels and descriptions
- Change the output format

## License

MIT License
