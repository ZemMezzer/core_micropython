import path

System = None


class FileIO:

    def __init__(self, system):
        global System
        System = system
        return

    @staticmethod
    def Write(file_name, content):
        if not System.is_initialized():
            return

        file = open(path.ROOT + file_name, "w")
        file.write(content)
        file.close()
        return

    @staticmethod
    def Read(file_name):
        if not System.is_initialized():
            return

        file = open(path.ROOT + file_name, "r")
        print(file.read())
        return
