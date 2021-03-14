## contact and library info
* greet
  - utter_how_can_i_help
* task
  - utter_task   
* college_campus
  - utter_give_campus 
* library_info
  - utter_library_info 
* contact_details    
  - action_give_contact
* college_placement
  - utter_placement_info
* college_ground 
  - utter_ground_info
* events_organised
  - utter_events_info       
* location_college
  - utter_location
* goodbye
  - utter_goodbye

## criteria for the addmission
* greet
  - utter_how_can_i_help
* eligibility_criteria
  - action_eligibility_tracker
* college_info
  - utter_give_info
* VNM
  - utter_vm
* college_campus
  - utter_give_campus 
* library_info
  - utter_library_info  
* college_placement
  - utter_placement_info 
* college_ground 
  - utter_ground_info
* events_organised
  - utter_events_info 
* mood_great
  - utter_salutaion        
* goodbye
  - utter_goodbye

## location of college
* greet
  - utter_how_can_i_help
* eligibility_criteria
  - action_eligibility_tracker
* location_college
  - utter_location
* college_info
  - utter_give_info
* college_campus
  - utter_give_campus
* library_info
  - utter_library_info   
* goodbye
  - utter_goodbye

## criteria and location
* greet
  - utter_how_can_i_help
* location_college
  - utter_location
* eligibility_criteria{"ug_course":"Bsc","eligible":"eligibility criteria"}
  - slot{"eligible":"eligibility criteria"}
  - slot{"ug_course":"Bsc"}
  - action_eligibility_tracker
* eligibility_criteria{"pg_course":"Msc"}
  - slot{"pg_course":"Msc"}
  - action_eligibility_tracker
* eligibility_criteria{"eligible":"Criteria","ug_course":"Bmm"}
  - slot{"eligible":"Criteria"}
  - slot{"ug_course":"Bmm"}
  - action_eligibility_tracker
* out_of_scope
  - action_default_fallback    
* goodbye
    - utter_goodbye


## bot challenge
* mood_great
  - utter_salutaion
* bot_challenge
  - utter_iamabot

## New Story

* greet
  - utter_how_can_i_help
* task
  - utter_task    
* contact_details
  - action_give_contact
* location_college
  - utter_location
* chairman_msg
  - utter_cm
* principal_msg
  - utter_pm  
* director_msg
  - utter_dm  


## happy vip info
*  faculty_info{"faculty": "principal"}
  - action_vip_info
*  faculty_info{"faculty": "director"}
  - action_vip_info
*  faculty_info{"faculty": "principal"}
  - action_vip_info
*  faculty_info{"faculty": "director"}
  - action_vip_info

## vp info
* vp_info{"vp":"vice principal","stream":"arts"}
  - utter_artsvp
* vp_info{"vp":"vice principal","stream":"science"}
  - utter_scivp
* vp_info{"vp":"vice principal","stream":"commerce"}
  - utter_commvp
* vp_info{"vp":"vice principal","stream":"sci"}
  - utter_scivp
* vp_info{"vp":"vice principal","stream":"comm"}
 - utter_commvp 
* goodbye
  - utter_goodbye

## vp info + stream

* vp_info{"vp":"vice principal"}
  - utter_ask_stream
* science_stream
  - utter_scivp
* vp_info{"vp":"vice principal"}
  - utter_ask_stream
* commerce_stream
  - utter_commvp
* vp_info{"vp":"vice principal"}
  - utter_ask_stream
* arts_stream
  - utter_artsvp
* goodbye
  - utter_goodbye

## courses details
* overall_courses
  - utter_ask_course
* ug_courses
  - utter_UG_course
* pg_courses
  - utter_PG_course    
* hsc_courses
  - utter_hsc_course
* phd_courses
  - utter_phd_course
* certificate_courses
  - utter_certificate_course
* mood_great
  - utter_salutaion
      