# Bóc tách email từ người dùng

## Chạy ứng dụng

### Khởi động Action Server
```bash
cd mailsub
source venv/bin/activate
rasa run actions
```

### Khởi động rasa/duckling, dùng để bóc tách email
```
docker run -p 8000:8000 rasa/duckling
```
### Tiến hành train model và chạy thử
```bash
cd mailsub
source venv/bin/activate
rasa train
rasa shell
```

### Kịch bản chạy thử
```
Your input ->  hi
Hey! How are you?
Your input ->  subscribe newsletter
please provide your email
Your input ->  cuong@techmaster.vn
Some one already use your email cuong@techmaster.vn
Your input ->  subscribe me long@gmail.com
long@gmail.com is subscribed successfully
Your input ->  want to subscribe newsletter
please provide your email
Your input ->  lan@microsoft.com
lan@microsoft.com is subscribed successfully
```

## Các cấu hình, mã quan trọng

Trong config.yml cũng phải cấu hình như sau để bóc tách được email
```yaml
- name: DucklingHTTPExtractor
    url: http://localhost:8000
    dimensions:
    - email
    - number
    - amount-of-money
```

## stories.md

Sử dụng checkpoint ```> user_enter_email``` để nối tiếp logic
```markdown
## subscribe 2: người dùng cung cấp email trong yêu cầu
* signup{"email": "example@gmail.com"}
  - slot{"email": "example@gmail.com"}
  - action_subscribe_newsletter
  > user_enter_email

## email already subscribed
  > user_enter_email
  - slot{"subscribed": false}
  - utter_email_existed

## email is newly subscribed
  > user_enter_email
  - slot{"subscribed": true}
  - utter_confirm_email
```

sử dụng ```- slot{"subscribed": "exist"}``` và  ```- slot{"subscribed": "subscribe"}``` để điều hướng logic phản hồi
- email đã tồn tại utter_email_existed
- email đăng ký lần đầu utter_confirm_email


## domain.yml

Cấu hình trong domain.yml, sử dụng slot categorial có 3 giá trị để biết kết quả đăng ký của người dùng
```yaml
actions:
  - action_subscribe_newsletter
slots:
  subscribed:
      type: bool     
  email:
    type: text
    
entities:
  - email
```

Custom Action to check email
```python
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
```