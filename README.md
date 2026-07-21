# Efficient-Bin-Packing-using-Approximation-Algorithms
An interactive Streamlit application that implements and compares three Bin Packing approximation algorithms: First Fit, First Fit Decreasing, and Best Fit Decreasing. The system packs items into fixed-capacity bins, calculates the theoretical lower bound, and evaluates algorithm efficiency by comparing the number of bins used.
## Features
Implements First Fit (FF)
Implements First Fit Decreasing (FFD)
Implements Best Fit Decreasing (BFD)
Calculates the theoretical lower bound
Compares the number of bins used
Displays the contents of each bin
Built with Python and Streamlit
## Algorithms Used
First Fit (FF)

Each item is placed into the first bin that has enough remaining space. If no suitable bin exists, a new bin is opened.

First Fit Decreasing (FFD)

The items are first sorted in decreasing order and then packed using the First Fit strategy.

Best Fit Decreasing (BFD)

The items are sorted in decreasing order and each item is placed into the bin that leaves the smallest possible remaining space. Run pip install -r requirements.txt

streamlit run app.py
