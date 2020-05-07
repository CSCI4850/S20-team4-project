# S20-team4-project
This project sets out to create a neural network solution capable of playing and completing Mine-Sweeper. 
It consists of:
-A set of methods to play through a game of Mine-Sweeper
-Generate board states that are then encoded to a format that can be easily understood by a convolutional neural network
-Create a large training set of these board states
-Implement a neural network to train on the data set and learn how to attempt to win games of Mine-Sweeper

## Steps to prepare
Download the Numpy wheel from 
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    
Run these commands in your shell
        pip install keras
        pip install numpy-'(current version file.whl)'
        
This project utilizes Python Jupyter Notebooks via JupyterLab for development
More information about JupyterLab and the Jupyter Notebooks may be found in these links below

## Getting Started with Jupyter

Installation and introduction
https://www.tutorialspoint.com/jupyter/jupyterlab_installation_and_getting_started.htm

User Interface
https://www.tutorialspoint.com/jupyter/jupyterlab_interface.htm

Types of cells
https://www.tutorialspoint.com/jupyter/jupyter_notebook_types_of_cells.htm

Editing the notebook
https://www.tutorialspoint.com/jupyter/jupyter_notebook_editing.htm

Markdown cells
https://www.tutorialspoint.com/jupyter/jupyter_notebook_markdown_cells.htm

Plotting
https://www.tutorialspoint.com/jupyter/jupyter_notebook_plotting.htm

# To find the demo materials
1. Click the "demo" subdirectory
2. Click into the "Project Stuff" directory
3. For the Demo, open DemoNotebook.ipynb in your Jupyter Docker
4. For the datasets used, open train.csv and test.csv
5. For producing that data, open DataProduction.ipynb and run the code
6. To clear/reset your current data, open and run the code from DataReset.ipynb

# Data Production

Our data sets are made up of incomplete board states (train.csv) and the end result of the grid state of the game (test.csv). These are generated, and pushed into csv files, in the DataProduction.ipynb code. Said notebook allows the user to run the code and watch as randomly generated moves simulate a short game of minesweeper, resulting in quick, unfinished data, to allow the net room to predict.

# Net Training

While training this net, decent accuracy (40-50% exact), along with acceptable results in the prediction output matrix, should be observed after a large number of epochs (5000 - 10000) on a dataset of roughly a size (x_train.shape) of 5000-7000 items. We recommend training with a small batch size and in small numbers of epochs for an extended period of time. Running with too large of a batch size or with too many epochs can potentially cause the value loss to drop into the negatives and eventually crash the model into an endless string of "nan" predictions.