## getNews happy path 1
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: choose{"topic_news": "sports"}
    - slot{"topic_news": "sports"}
    - form: get_news
    - slot{"topic_news": "sports"}
    - form{"name": null}
    - action_restart

## thankyou (general)    
* thank_you
    - utter_welcome

## chitchat flow 1 (general)
* chitchat_general
    - utter_reply_chitchat_general

## chitchat flow 2 (identity)
* chitchat_identity
    - utter_reply_chitchat_identity

## greet (general)
* greet
    - utter_hello

## getNews happy path 2
* getNews{"topic_news": "astronomy"}
    - slot{"topic_news": "astronomy"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "astronomy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## getNews happy path 3
* getNews{"topic_news": "physics"}
    - slot{"topic_news": "physics"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "physics"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## bye (general)
* bye
    - utter_end