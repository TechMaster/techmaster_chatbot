https://forum.rasa.com/t/how-to-input-free-text-with-custom-actions-slots/9304s

Cách này không ổn định.
```
our input ->  hi
Give me your name please
Your input ->  Cuong
Your name is Cuong
Tell me your email
Your input ->  rock@techmaster.vn
/Users/techmaster/techrasa/venv/lib/python3.7/site-packages/rasa/utils/common.py:347: UserWarning: Action 'get_email' set a slot type 'email' which it never set during the training. This can throw off the prediction. Make sure to include training examples in your stories for the different types of slots this action can return. Remember: you need to set the slots manually in the stories by adding '- slot{"email": rock@techmaster.vn}' after the action.
Your email is rock@techmaster.vn
Your input ->  Hi
Give me your name please
Your input ->  Long
Your name is Long
Tell me your email
Your input ->  l@vn
Your name is l@vn
Your email please
Your input ->  long@gmail.vn
Your name is long@gmail.vn
Tell me your email
Your input ->  cuong@techmaster.vn
/Users/techmaster/techrasa/venv/lib/python3.7/site-packages/rasa/utils/common.py:347: UserWarning: Action 'get_email' set a slot type 'email' which it never set during the training. This can throw off the prediction. Make sure to include training examples in your stories for the different types of slots this action can return. Remember: you need to set the slots manually in the stories by adding '- slot{"email": cuong@techmaster.vn}' after the action.
Your email is cuong@techmaster.vn
```