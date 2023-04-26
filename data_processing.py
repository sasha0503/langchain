import demjson


class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.keys = None

    def decode(self, id):
        if not self.keys:
            raise ValueError("Keys are not loaded")
        for i in self.keys:
            if i['id'] == id:
                return i['name']

    def process(self):
        with open(self.data_path) as f:
            data = f.read()
        return data


class SlackDataProcessor(DataProcessor):
    def process(self):
        with open(self.data_path) as f:
            data = f.read()
        data = [demjson.decode(i) for i in data.split(';') if i]

        self.keys = [key for keys in data[1:] for key in keys]
        data = data[0]

        messages_in_channels = {}
        for message in data:
            channel = self.decode(message['channel_id'])
            if channel not in messages_in_channels:
                messages_in_channels[channel] = []
            messages_in_channels[channel].append(message)

        final_text = ""
        for channel, messages in messages_in_channels.items():
            messages_in_channels[channel] = sorted(messages, key=lambda x: x['timestamp'])
            final_text += f"{channel} chanel\n\n"
            for message in messages_in_channels[channel]:
                final_text += f"{self.decode(message['user_id'])}: {message['text']}\n\n"
        return final_text


class NotionDataProcessor(DataProcessor):
    pass
