# from rasa_sdk import Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet, FollowupAction
# from rasa_sdk.forms import FormAction
# from rasa_sdk.events import SlotSet
# from rasa_sdk.events import UserUtteranceReverted

import json
import logging
import os

import re
import warnings

from io import BytesIO as IOReader, StringIO
from pathlib import Path
from typing import Text, Any, Dict, Union, List, Type, Callable, TYPE_CHECKING, Match
        
class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello I am Birla Bot 💬🤖. Feel free to ask any question regarding B.K.Birla college😉!!")

        # return [UserUtteranceReverted()] 


class ActionGiveContact(Action):

    def name(self) -> Text:
        return "action_give_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        data= [ { "title": "☎️ Phone", "description": " (0251) 2230740, 2231294" }, { "title": " 📠 FAX", "description": "(0251) 2231029" }, { "title": "📧 Email", "description": "principal@bkbirlacollegekalyan.com" }
        ]

        message={ "payload": "collapsible", "data": data }

        dispatcher.utter_message(text="Here is the contact details",json_message=message)


        return []        


        
class ActionEligibilityTracker(Action):

     def name(self) -> Text:
         return "action_eligibility_tracker"
             
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response = open("D:/College Bot/bkb_bot/ugcb.json")
         content = json.load(response)
         
         entities = tracker.latest_message['entities']
         course = None
         
         for  e in entities:
                if e["entity"] == "ug_course":
         		        course = e['value']
                elif e["entity"] == "pg_course":
                        course = e['value']
                else:         
                        message = "Please enter the correct course name"		

         

         for  data in content["courses"]:
               if data["name"] == course.title():
                    print(data)
                    message = "Criteria: "+ data["text"]  
         print(message)				
         dispatcher.utter_message(message)

# class ActionVp(Action):

#      def name(self) -> Text:
#          return "action_vp"
             
#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#          response = open("/home/linux-unversei/Documents/coll_bot-test/faculty.json")
#          content = json.load(response)
         
#          entities = tracker.latest_message['entities']
#          result = None
         
#          for  e in entities:
#                 if e["entity"] == "stream":
#          		        result = e['value']                       
#          message ="Please enter the correct Stream name"		
#          for  data in content["Vice_Principal"]:
#                if data["name"] == result.title():
#                     print(data)
#                     message = data["text"]  
#          print(message)				
#          dispatcher.utter_message(message)
#          return[]
         

class ActionVipInfo(Action):

     def name(self) -> Text:
         return "action_vip_info"
             
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response = open("D:/College Bot/bkb_bot/vip.json")
         content = json.load(response)
         
         entities = tracker.latest_message['entities']
         results = None
         
         for  e in entities:
                if e["entity"] == "faculty":
         		        results = e['value']                       
         message ="Please enter the correct designation name"		
         for  data in content["Vip"]:
               if data["name"] == results.title():
                    print(data)
                    message = data["text"]  
         print(message)				
         dispatcher.utter_message(message)
         return[]
     
     