## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## love
* love
  - utter_love
## subscribe 1: người dùng không cung cấp email trong yêu cầu
* signup
  - utter_ask_email
* inform{"email": "example@gmail.com"}
  - slot{"email": "example@gmail.com"}
  - action_subscribe_newsletter
  > user_enter_email

## subscribe 2: người dùng cung cấp email trong yêu cầu
* signup{"email": "example@gmail.com"}
  - slot{"email": "example@gmail.com"}
  - action_subscribe_newsletter
  > user_enter_email

## email already subscribed
  > user_enter_email
  - slot{"subscribed": "exist"}
  - utter_email_existed

## email is newly subscribed
  > user_enter_email
  - slot{"subscribed": "subscribe"}
  - utter_confirm_email



## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy


## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
