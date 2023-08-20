# **Lab: Setting Up Your Environment in Visual Studio Code**

**Objective:** By the end of this lab, you will be able to set up your Python development environment in Visual Studio Code, integrate it with a virtual environment, and use ngrok for exposing your local server to the internet.

- **setup.sh**

To run this script, save it as `setup.sh` in the root directory of your project, then run it in the terminal with the command `bash setup.sh`.

## **Steps: Before You Get Started**

1. **Open Visual Studio Code**
   - Start by opening Visual Studio Code. Navigate to the directory where you saved your Python scripts.

2. **Open the Terminal in VSC**
   - You can open the terminal in VSC by clicking on `Terminal` in the top menu, then `New Terminal`. The terminal will open at the bottom of the VSC window.

3. **Run the Setup Script**
   - In the terminal, run the setup script using the command `bash setup.sh`. This will create a virtual environment, install the necessary libraries, and set the appropriate permissions for your Python scripts.

4. **Activate the Virtual Environment**
   - Activate the virtual environment by typing `source .venv/bin/activate` in the terminal. You should see `(.venv)` appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

5. **Install the ngrok Extension**
   - In VSC, go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window. You can also use the shortcut `Ctrl+Shift+X`.
   - In the Extensions view, search for "ngrok for VSCode". Click on the first result and then click on the Install button.

6. **Start ngrok**
   - Once the ngrok extension is installed, you can start it by opening the Command Palette with the shortcut `Ctrl+Shift+P`, then typing "ngrok" and selecting "ngrok: Start tunnel". You will be asked to enter the port number. If your Flask app is running on port 5000, enter "5000".

7. **Check the ngrok URL**
   - After starting ngrok, you can check the public URL of your local server by opening the Command Palette again, typing "ngrok" and selecting "ngrok: Show current tunnels". You should see a URL that you can use to access your local server from the internet.

You're now ready to start the labs! Remember to always activate the virtual environment before running your Python scripts. You can do this in VSC's terminal by typing `source .venv/bin/activate`.
