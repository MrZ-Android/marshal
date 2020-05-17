# uncompyle6 version 3.6.7
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <debby>
import marshal, sys, os, time
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    os.system('clear')
    print R + '     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+'
    print W + '     |C|o|m|p|i|l|e| |M|a|r|s|h|a|l|'
    print R + '     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+'
    print Y + '0{' + 39 * '=' + '}0'
    print Y + '|' + B + ' Coded by: ' + W + 'Mr-W0lf' + Y + '                      |'
    print Y + '|' + B + ' Email   : ' + W + 'drkscurty01@gmail.com' + Y + '        |'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/The-W0lf' + Y + '  |'
    print Y + '0{' + 39 * '=' + '}0\n'


try:
    banner()
    print G + 'Ex :/sdcard/ex.py'
    file = raw_input('\x1b[0m[\x1b[31mInput Your File Path\x1b[0m]> \x1b[36m')
    o = file.replace('.py', '')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error\n'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()

try:
    strng = open(file, 'r').read()
except IOError:
    banner()
    print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
    sys.exit()

try:
    code = compile(strng, '<debby>', 'exec')
    data = marshal.dumps(code)
except TypeError:
    banner()
    print R + '[' + W + '!' + R + '] ' + W + 'file already compiled\n'
    sys.exit()

fileout = open(o + 'enc.py', 'wb')
fileout.write('#Compiled By Mr-W0lf\n')
fileout.write('#Github : https://github.com/The-W0lf\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + o + 'enc.py\n'
