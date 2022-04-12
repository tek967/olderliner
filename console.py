from ast import parse
from debug.debug import DebugTools
import sys
from os import system, name

class Console:
    def __init__(self) -> None:
        self.args = sys.argv[1:]
        self.commandList = [
            "exit",
            "test",
            "constclass"
        ]
        self.classList = [
            
        ]
        self.usage = (
            "\nUSAGE:\nexit: exit <args: true,false>\n" +
            "test: run tests in the tests folder\n"
        )

    def log(l): print("\nconsole log> " + l, end='\n')

    def runCommand(self, command):
        if command[0] == self.commandList[0]:
            try:
                if command[1] == 'true':
                    sys.exit(0)
                elif command[1] == 'false':
                    sys.exit(1) 
            except IndexError:
                Console.log("args <true, false>")
        if command[0] == self.commandList[1]:
            if name == 'posix':
                system('for f in tests/*.py; do python3 "$f"; done')
            else:
                Console.log("NT testing is not supported yet. Get a job and install linux in a VM!")


    def detectCommand(self, command):
        if command[0] not in self.commandList:
            Console.log("That was not a valid command.")
        else:
            Console().runCommand(command)

    def con(self): 
        while (True):
            try:
                rawParse = input('linerdebug> ')
                parseCommand = rawParse.strip(' ').split(' ')
                Console().detectCommand(parseCommand)
            except KeyboardInterrupt:
                Console.log("Quit with the exit command.")
            except EOFError: 
                Console.log("sneaky kid trying to EOF me. How about read the usage?")

    def start(self):
        pass

def main():
    print(Console().usage)
    Console().con()

if __name__ == "__main__": main()    