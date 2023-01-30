import os

IS_INITIALIZED = False


class System:
    Path = None
    File = None

    @staticmethod
    def InitializeArgs(args):
        return

    @staticmethod
    def StartWithArgs(args):

        import path
        import file

        global IS_INITIALIZED

        if IS_INITIALIZED:
            print("System already initialized!")
            return

        System.InitializeArgs(args)

        contains = False
        for val in os.listdir():
            if val == "System":
                contains = True
        if not contains:
            os.mkdir("System")

        IS_INITIALIZED = True
        print("System is Initialized")

        System.Path = path.PathIO(System)
        System.File = file.FileIO(System)

        return

    @staticmethod
    def Start():
        System.StartWithArgs("")
        return

    @staticmethod
    def is_initialized():
        if not IS_INITIALIZED:
            print("System is not initialized, print: System.start() to start up system")
            return False
        return True


for val in os.listdir():
    if val == "autoexec.cfg":
        System.StartWithArgs(open("autoexec.cfg", "r").read())
