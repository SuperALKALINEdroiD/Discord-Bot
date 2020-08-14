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

class multiply:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split()
        if len(message) == 2:
            return message[1]
        else:
            multiply_result = 1
            for i in range(1, len(message)):
                multiply_result *= int(message[i])
            return multiply_result

class division:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split()
        if len(message) == 2:
            return message[1]
        else:
            div_result = int(message[1])
            for i in range(2, len(message)):
                div_result /= int(message[i])
            return div_result

class remainder:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split()
        if len(message) > 3:
            return "Error"
        else:
            remResult = int(message[1]) % int(message[2])
            return remResult
