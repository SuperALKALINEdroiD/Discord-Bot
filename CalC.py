class add:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def getResult(self):
        message = self.messageContent.split(';')
        if len(message) == 2:
            return message[1]
        else:
            try:
                add_result = int(message[1])
                for i in range(2, len(message)):
                    add_result += int(message[i])
                return add_result
            except:
                return "Error, Check ur inputs!!"
class subtract:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split(';')
        if len(message) == 2:
            return message[1]
        else:
            try:
                sub_result = int(message[1])
                for i in range(2, len(message)):
                    sub_result -= int(message[i])
                return sub_result
            except:
                return "Error, Check ur inputs!!"

class multiply:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split(';')
        if len(message) == 2:
            return message[1]
        else:
            try:
                multiply_result = message[1]
                for i in range(2, len(message)):
                    multiply_result *= int(message[i])
                return multiply_result
            except:
                return "Error, Check ur inputs!!"

class division:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split(';')
        if len(message) == 2:
            return message[1]
        else:
            try:
                div_result = int(message[1])
                for i in range(2, len(message)):
                    div_result /= int(message[i])
                return div_result
            except:
                return "Error, Check ur inputs!!"

class remainder:
    def __init__(self, messageContent):
        self.messageContent = messageContent

    def get_result(self):
        message = self.messageContent.split(';')
        if len(message) > 3:
            return "Error"
        else:
            try:
                remResult = int(message[1]) % int(message[2])
                return remResult
            except:
                return "Error, Check ur inputs!!"
