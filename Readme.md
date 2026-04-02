# Build Deep Autoencoders Model for Anomaly Detection in Python
This repository contains the code for developing a deep learning model based on Autoencoders to learn distributions and relationships between features of normal transactions


### Running on your system locally
 
To run the notebook on your local system set up a [python](https://www.python.org/) environment. Set up the [jupyter notebook](https://jupyter.org/install) with python. Download the notebook and open a jupyter notebook to run the code on local system.
 
The notebook can also be executed by using [Visual Studio Code](https://code.visualstudio.com/), and [PyCharm](https://www.jetbrains.com/pycharm/).

**Python Version: 3.8.10**

The Python 3.8.10 version is supported for the execution of this project.
1. Running the codes locally: Python 3.8.10
    - Create a virtual environment: In the terminal or command prompt, use the following command to create a new virtual environment:

        - For Windows:
            `py -3.8 -m venv env`

        - For macOS and Linux:
            `python3 -m venv venv`
        This command creates a new virtual environment named "venv" in the current directory.

    - Activate the virtual environment:

        - For Windows (Command Prompt):
            `venv\Scripts\activate`


        - For macOS and Linux (Terminal) :
            `source venv/bin/activate`
    
Once the virtual environment is activated, you should see the environment name (e.g., (venv)) in the terminal or command prompt.

- Install project requirements: With the virtual environment active, you can now install the required packages for your project. Typically, the required packages are listed in a requirements.txt file. Make sure you have the requirements.txt file for your project.

2. Setup the pip and installing dependencies in Virtual environment

    - Upgrade pip
        `python -m pip install --upgrade pip`

    - To install the requirements, use the following command:
        `pip install -r requirements.txt`


### Run modular code (engine.py file)

- Activate the virtual environment you created for this project.
- Enter 0 to train the model
- Enter 1 to get the predictions
- Enter 2 to deploy the Flask Application to run the web application

### Testing Deployed Flask Application

After the application is deployed, test the application by making a POST REST API call to the deployed service.

- Open MODEL_API.ipynb
- Execute all the cells in the notebook

The notebook sends a POST request to the deployed API endpoint

