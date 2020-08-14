class add:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def getResult(self):
        message = self.messageContent.split()
        if len(message) == 2:
            return message[1]
        else:
            add_result = 0
            for i in range(1, len(message)):
                add_result += int(message[i])
            return add_result
class subtract:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split()
        if len(message) == 2:
            return message[1]
        else:
            sub_result = int(message[1])
            for i in range(2, len(message)):
                sub_result -= int(message[i])
            return sub_result