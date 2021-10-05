import requests

token = open("/home/jinyes/Daily-News-Keywords-Bot/Bot/token.txt").read()


def post_message(channel, msg):
    result = requests.post("https://slack.com/api/chat.postMessage",
                  headers={
                      "Authorization": "Bearer " + token
                  },
                  data={
                      "channel": channel,
                      "text": msg
                  })
    if result.json()["ok"]:
        return True
    return False


