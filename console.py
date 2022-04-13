from debug.debug import DebugTools
import sys, threading
from os import system, name

class console:
    def __init__(self) -> None:
        self.args = sys.argv[1:]
        self.commandList = [
            "exit",
            "test",
            "usage",
            "thread",
            "constclass"
        ]
        self.classList = [
            
        ]
        self.usage = (
            "USAGE:\nexit: exit <args: true,false>\n" +
            "test: run tests in the tests folder\n" + 
            "usage: print usage\n"
        )
        self.threads = []
        self.new_thread = threading.start_new_thread(console)
        self.set_name = threading.setName("con")
        self.thread_list=self.new_thread.append(self.threads)
        self.start_thread = threading.start()


    def log(l): print("\nlog> " + l, end='\n')

    def runCommand(self, command):
        if command[0] == self.commandList[0]:
            try:
                if command[1] == 'true':
                    self.thread_exit = threading.exit()
                    sys.exit(0)
                elif command[1] == 'false':
                    self.thread_exit = threading.exit()
                    sys.exit(1) 
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
            console.log(self.thread_list)



    def detectCommand(self, command):
        if command[0] not in self.commandList:
            console.log("That was not a valid command.")
        else:
            console().runCommand(command)

    def con(self): 
        while (True):
            try:
                rawParse = input('linerdebug> ')
                parseCommand = rawParse.strip(' ').split(' ')
                console().detectCommand(parseCommand)
            except KeyboardInterrupt:
                console.log("Quit with the exit command.")
            except EOFError: 
                console.log("sneaky kid trying to EOF me. How about read the usage?")
                
    


def main():
    print("\n"+console().usage)
    console().con()

if __name__ == "__main__": main()
