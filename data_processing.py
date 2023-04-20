import demjson

with open("data/slack_data.txt") as f:
    slack_data = f.read()
slack_data = [demjson.decode(i) for i in slack_data.split(';') if i]

slack_encoded = slack_data[0]
slack_keys = [i for keys in slack_data[1:] for i in keys]


def decode(id):
    for i in slack_keys:
        if i['id'] == id:
            return i['name']


messages_in_channels = {}
for message in slack_encoded:
    channel = decode(message['channel_id'])
    if channel not in messages_in_channels:
        messages_in_channels[channel] = []
    messages_in_channels[channel].append(message)

final_slack_text = ""
for channel, messages in messages_in_channels.items():
    messages_in_channels[channel] = sorted(messages, key=lambda x: x['timestamp'])
    final_slack_text += f"{channel} chanel\n\n"
    for message in messages_in_channels[channel]:
        final_slack_text += f"{decode(message['user_id'])}: {message['text']}\n\n"

with open("data/slack_final_data.txt", "w") as f:
    f.write(final_slack_text)
