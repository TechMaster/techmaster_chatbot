from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import re 


class Get_Name(Action):
    def name(self):
        return "get_name"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        print(message)
        return [SlotSet('full_name', message)]


class Get_Email(Action):
    def name(self):
        return "get_email"

    def run(self, dispatcher, tracker, domain):
        input_email = tracker.latest_message.get('text')
        print('input email = ' + input_email)
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex, input_email)):  
          print("Valid Email")
          dispatcher.utter_message(text = "Your email is " + input_email)
          return [SlotSet('email', input_email)]        
        else:
          print("Invalid Email")
          dispatcher.utter_message(text = "Your email " + input_email + " is invalid")
          return [SlotSet('email', "")]
        