# **Lab: Integrating APIs into a Rasa Chatbot**

**Objective:** By the end of this lab, you will understand how to integrate APIs into a Rasa chatbot to enhance its functionality.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa
- Libraries: requests

**Steps:**

1. **Identify the API You Want to Integrate**
   - The first step is to identify the API you want to integrate into your chatbot. This will depend on what functionality you want to add. For example, if you want your chatbot to provide weather updates, you might use a weather API.

2. **Understand the API**
   - Once you've identified the API, spend some time understanding how it works. Look at the API documentation to understand how to make requests, what parameters are required, and what kind of responses you can expect.

3. **Create a Custom Action in Rasa**
   - In Rasa, you can create custom actions to perform tasks like calling an API. A custom action is a Python function that Rasa runs when it predicts that action. To create a custom action, you'll need to add a function to your `actions.py` file.

   ```python
   from rasa_sdk import Action
   import requests

   class ActionGetWeather(Action):
       def name(self):
           return 'action_get_weather'

       def run(self, dispatcher, tracker, domain):
           location = tracker.get_slot('location')
           response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={location}')
           current_weather = response.json()['current']['temp_c']
           dispatcher.utter_message(text=f"The current temperature in {location} is {current_weather}°C.")
   ```

4. **Update Your Domain File**
   - After creating the custom action, you'll need to update your domain file to include the new action.

   ```yaml
   actions:
     - action_get_weather
   ```

5. **Update Your Stories**
   - Finally, update your stories to include the new action. For example, you might create a story where the user asks for the weather, and the chatbot responds by calling the `action_get_weather` action.

   ```yaml
   - story: ask for weather
     steps:
     - intent: ask_weather
     - action: action_get_weather
   ```

6. **Test Your Chatbot**
   - Test your chatbot to ensure that the API integration is working correctly. Try asking your chatbot for the weather and see if it responds with the current temperature.

Remember, this is a high-level overview. Each step in this process can be quite complex and may require a deep understanding of Rasa and the API you're working with.