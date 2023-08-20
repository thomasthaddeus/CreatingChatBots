# Lab: Setting Up Your Environment in Visual Studio Code

## Objective

By the end of this lab, you will be able to set up your Python development environment in Visual Studio Code, integrate it with a virtual environment, and use `ngrok` for exposing your local server to the internet.

## Steps

### Open Visual Studio Code

Start by opening Visual Studio Code. Navigate to the directory where you saved your Python scripts.

### Open the Terminal in VSC

You can open the terminal in VSC by clicking on Terminal in the top menu, then New Terminal. The terminal will open at the bottom of the VSC window.

### Run the Setup Script

In the terminal, run the setup script using the command `bash setup.sh`. This will create a virtual environment, install the necessary libraries, and set the appropriate permissions for your Python scripts.

### Activate the Virtual Environment

Activate the virtual environment by typing `source .venv/bin/activate` in the terminal. You should see (`.venv`) appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

### Install the ngrok Extension

In VSC, go to the Extensions view by clicking on the *Extensions icon* in the Activity Bar on the side of the window. You can also use the shortcut `Ctrl+Shift+X`.
In the Extensions view, search for "`ngrok for VSCode`". Click on the first result and then click on the `Install` button.

### Start ngrok

Once the `ngrok` extension is installed, you can start it by opening the Command Palette with the shortcut `Ctrl+Shift+P`, then typing `ngrok` and selecting `ngrok: Start tunnel`.

You will be asked to enter the port number. If your Flask app is running on port 5000, enter `5000`.

### Check the ngrok URL

After starting `ngrok`, you can check the public URL of your local server by opening the Command Palette again, typing `ngrok` and selecting `ngrok: Show current tunnels`. You should see a URL that you can use to access your local server from the internet.
You're now ready to start the labs! Remember to always activate the virtual environment before running your Python scripts. You can do this in VSC's terminal by typing `source .venv/bin/activate`.

---

## **Lab: Setting Up the Virtual Environment for Chatbot Development**

## **Objective:**

By the end of this lab, you will understand how to set up a virtual environment for Python, install necessary libraries, and configure your development environment for chatbot development.

### **Tools Required:**

- `Python 3.x`
- `pip` (Python package installer)
- `Virtualenv` (Python virtual environment creator)
- Text editor or Python IDE (like *PyCharm*, *Jupyter notebook*, or *VS Code*)

### **Steps:**

1. **Install Virtualenv**
   - Virtualenv is a tool to create isolated Python environments. It allows you to install Python libraries in an environment that's separate from your system's Python environment, which can help prevent conflicts between different versions of libraries.
   - To install Virtualenv, open your terminal and run the following command: `pip install virtualenv`

2. **Create a Virtual Environment**
   - To create a virtual environment, navigate to the directory where you want to create the environment, and run the following command: `virtualenv venv`
   - This will create a new directory called `venv` that contains the virtual environment.

3. **Activate the Virtual Environment**
   - To activate the virtual environment, run the following command:
     - On Windows: `venv\Scripts\activate`
     - On Unix or MacOS: `source venv/bin/activate`
   - When the virtual environment is activated, your terminal prompt will change to show the name of the environment.

4. **Install Necessary Libraries**
   - With the virtual environment activated, you can install the necessary libraries for chatbot development. This might include libraries like TensorFlow, Keras, NLTK, and others.
   - To install a library, use the `pip install` command, like this: `pip install tensorflow keras nltk`

5. **Configure Your Development Environment**
   - Finally, configure your development environment to use the virtual environment. The exact steps for this will depend on your development environment.
   - For example, in VS Code, you can select the Python interpreter for a workspace by clicking on the Python version in the bottom left corner of the window, and then selecting the interpreter from your virtual environment.

**Note:** Remember to activate the virtual environment each time you start a new terminal session. Also, any libraries that you install while the virtual environment is activated will only be available in that environment.

*Happy learning!*
