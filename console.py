from debug.debug import DebugTools
import sys, multiprocessing
from os import system, name

class console:
    def __init__(self) -> None:
        self.args = sys.argv[1:]
        self.commandList = [
            "exit",
            "test",
            "usage",
            "thread",
            "constclass",
            "clear",
            "menu"
        ]
        self.classList = [
            "atm"
        ]

        self.usage = (
            "USAGE:\nexit: exit <args: true,false>\n" +
            "test: run tests in the tests folder\n" +
            "usage: print usage\n" +
            "clear: clear the console\n"+
            "constclass: construct class <args: atm>" +
            "menu: start the main game menu"
        )

    def log(l): print("\nlog> " + l, end='\n')
    def runCommand(self, command):
        if command[0] == self.commandList[0]:
            try:
                if command[1] == 'true':
                    sys.exit(0)
                elif command[1] == 'false':
                    sys.exit(1)
                    pass
            except IndexError:
                console.log("args <true, false>")
        elif command[0] == self.commandList[1]:
            if name == 'posix':
                print("__________________")
                system(
                    'for f in tests/*.py; do '+
                        'python3 "$f";'+
                        '\necho "test $f done.\n"'+
                        '\n'+
                    'done'
                )
                print("__________________")
            else:
                console.log("NT testing is not supported yet. Get a job and install linux in a VM!")
        elif command[0] == self.commandList[2]:
            console.log(self.usage)
        elif command[0] == self.commandList[3]:
            console.log("deprecated")
        elif command[0] == self.commandList[4]:
            if command[1] not in self.classList:
                console.log("there is no such thing to construct.")

            if command[1] == self.classList[0]:
                from currencyIO.ATM import ATM as a
                a()
        elif command[0] == self.commandList[5]:
            system("clear")
        elif command[0] == self.commandList[6]:
            import liner
            debugmenu = multiprocessing.Process(target=menu, args=(,))
            DebugTools.debugMain(debugmenu)



    def detectCommand(self, command):
        if command[0] not in self.commandList:
            console.log("That was not a valid command.")
        else:
            console().runCommand(command)

    def con(self):
        while (True):
            try:
                rawParse = input('linerdbg> ')
                parseCommand = rawParse.strip(' ').split(' ')
                console().detectCommand(parseCommand)
            except KeyboardInterrupt:
                console.log("Quit with the exit command.")
            except EOFError:
                console.log("sneaky kid trying to EOF me. How about read the usage?")


def main():
    print("\n"+console().usage)
    console().con()

if __name__ == "__main__": 
    main()
