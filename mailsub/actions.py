from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.slots import Slot
from rasa_sdk.events import SlotSet

class ActionSubscribeNewsletter(Action):
    def name(self):
        return "action_subscribe_newsletter"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        if email in ["cuong@techmaster.vn", "duy@techmaster.vn", "long@yahoo.com"]:          
          print('You already subscribed before')
          return [SlotSet('subscribed', False)]
        else:
          print('Subscribed now')
          return [SlotSet('subscribed', True)]