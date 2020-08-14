class add:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def getResult(self):
        message = self.messageContent.split()
        if len(message) == 2:
            return int(message[1])
        else:
            add_result = 0
            for i in range(1, len(message)):
                add_result += int(message[i])
            return add_result
