import os

ROOT = "System/"

System = None


class PathIO:

    def __init__(self, system):
        global System
        System = system
        return

    @staticmethod
    def GetAllFilesInPath(path):
        if not System.is_initialized():
            return

        print(os.listdir(ROOT + path))
        return

    @staticmethod
    def CreatePath(path):
        if not System.is_initialized():
            return

        os.mkdir(ROOT + path)
        return

    @staticmethod
    def DeletePath(path):
        if not System.is_initialized():
            return

        os.rmdir(ROOT + path)
        return
