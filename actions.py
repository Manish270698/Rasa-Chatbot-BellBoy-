# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted


class RoomBookingForm(FormAction):

    def name(self) -> Text:
        return "room_booking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["number","room_type"]

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_slot_values")


        return []

class RoomCleanForm(FormAction):

    def name(self) -> Text:
        return "room_clean_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["time"]

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_room_clean")

        return []

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_greet", tracker)

            return [UserUtteranceReverted()]

class ActionThankUser(Action):
    """Revertible mapped action for utter_noworries"""

    def name(self):
        return "action_thanks"

    def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_noworries", tracker)

            return [UserUtteranceReverted()]

class ActionByeUser(Action):
    """Revertible mapped action for utter_goodbye"""

    def name(self):
        return "action_bye"

    def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_goodbye", tracker)

            return [UserUtteranceReverted()]
