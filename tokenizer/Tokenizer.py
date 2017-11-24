#from tokenize import Token
#from Token import tokenizer
from Token import *
#from Token import Token
class InputError(object):
    pass


def isEscape(c):
    print("isEscape")
    if c=='\\':
        print("isEscapeOne")
        c = self.file.read(1)
        if c == '"' or c == '\\' or c == '/' or c == 'b' or c == 'f' or c == 'n' or c == 't' or c == 'r' or c == 'u':
            return True
        else:
            raise InputError('不是合法JSON结构！')
    else:
        print("xxxx")
        return False


def isDigitOne2Nine(c):
    print("num")
    return c >= '1' and c <= '9'


def isDigit(c):
    return c >= '0' and c <= '9'





def appendFrac(sb):
    c = read()
    while isDigit(c):
        sb.append(chr(c))
        c=read()


def appendExp(sb):
    c = read()
    if c=='+'or c=='-':
        sb.append(chr(c))
        c=read()
        if not isDigit(c):
            raise InputError('不是合法JSON结构！')
        else:
            while True:
                sb.append(chr(c))
                c=read()
                if isDigit(c):
                    break
            unread()
    elif not isDigit(c):
        raise InputError('不是合法JSON结构！')
    else:
        while True:
            sb.append(chr(c))
            c=read()
            if isDigit(c):
                break
        unread()


def isExp(c):
    return c == 'e' or c == 'E';


def numAppend(sb):
    c=read()
    if c=='.':
        sb.append(chr(c))
        appendFrac(sb)
        if isExp(c):
            sb.append(chr(c))
            appendExp(sb)
    elif isExp(c):
        sb.append(chr(c))
        appendExp(sb)
    else:
        unread()


def isHex(c):
    return (c >= '0' and c <= '9') or (c >= 'a' and c <= 'f') or (c >= 'A' and c <= 'F');


class Tokenizer(object):
    tokens=[]
    #Reader.read()

    isUnread=False
    def __init__(self,url):
        self.url=url
        self.file = open(url, 'r')
        #s = file.read(1)
        #print(file.read())
        #     print("TokenInn")
        #     reader=reader
        #     print(reader)

    def getTokens(self):
        return self.tokens

    def tokenizer(self):
        print("tokenizerB")
        #fileObj=Tokenizer(url)
        i=0
        while True:
            i=i+1
            print("i=",i)
            #print(fileObj.file.read())
            token=self.start(self)
            print("startOVer")
            self.tokens.append(token)
            print("startOverOne")
            #print(token.type)
            if token.type == 'TokenType_END_DOC':
                break
        print("tokenizerE")

    def start(self,file):
        print("startB")
        c='?'
        token=None
        #print(self.file.read(1))
        while True:
            #print(reader)
            c=self.file.read(1)
            print("in")
            print(c)
            print(not self.isSpace(c))
            if not self.isSpace(c):
                break
        #c=chr(c)
        print("out")
        print(c)
        if self.isNone(c):
            print("null")
            return Token('TokenType_NULL','null')
        elif c==',':
            print(",")
            return Token('TokenType_COMMA',',')
        elif c==':':
            print(":")
            return Token('TokenType_COLON',':')
        elif c=='{':
            print("{")
            return Token('TokenType_START_OBJ','{')
        elif c=='[':
            print("c=[")
            return Token('TokenType_START_OBJ', '{')
            #to= Token( 'TokenType_START_OBJ', '{')
            #print("ccc")
        elif c==']':
            print("]")
            return Token('TokenType_END_ARRAY',']')
        elif c=='}':
            print("}")
            return Token('TokenType_END_OBJ','}')
        elif self.isTrue(c):
            print("True")
            return Token('TokenType_BOOLEAN','True')
        elif self.isFalse(c):
            print("false")
            return Token('TokenType_BOOLEAN','False')
        elif c=='"':
            print('"')
            return self.readString(c)
        elif self.isNum(c):
            print("b")
            self.unread()
            print("a")
            return self.readNum(c)
        elif ord(c)==10:
            return Token('TokenType_END_DOC','EOF')
        else:
            print("EOF")
            raise InputError('不是合法JSON结构！')

    def read(self):
        pass

    def isSpace(self,c):
        print("SpaceIn")
        #print(ord(c))
        c=ord(c)
        print(c)
        return ((c >= 0) and (c <10)) or ((c>10)and(c<=32)) # !!!!!!!!!!!

    def isNone(self,c):
        print("isNone")
        if c == 'n':
            c = self.file.read()
            if c == 'u':
                c =self.file.read()
                if c == 'l':
                    c = self.file.read()
                    if c == 'l':
                        return True
                    else:
                        raise InputError('不是合法JSON结构！')
                else:
                    raise InputError('不是合法JSON结构！')
            else:
                raise InputError('不是合法JSON结构！')
        else:
            return False

    def isTrue(self,c):
        if c == 't':
            c = self.file.read()
            if c == 'u':
                c = self.file.read()
                if c == 'r':
                    c = self.file.read()
                    if c == 'e':
                        return True
                    else:
                        raise InputError('不是合法JSON结构！')
                else:
                    raise InputError('不是合法JSON结构！')
            else:
                raise InputError('不是合法JSON结构！')
        else:
            return False

    def isFalse(self,c):
        if c == 'f':
            c = self.file.read()
            if c == 'a':
                c = self.file.read()
                if c == 'l':
                    c = self.file.read()
                    if c == 's':
                        c = self.file.read()
                        if c == 'e':
                            return True
                        else:
                            raise InputError('不是合法JSON结构！')
                    else:
                        raise InputError('不是合法JSON结构！')
                else:
                    raise InputError('不是合法JSON结构！')
            else:
                raise InputError('不是合法JSON结构！')
        else:
            return False

    def isDigit(self,c):
        print("isDigit")
        return (c >= '0') and (c <= '9')

    def isNum(self,c):
        print("isNum")
        print(c)
        #print(self.isDigit(c))
        #print("ff")
        return self.isDigit(c) or c == '-'

    # def nextl(self):
    #     print("asd")
    #     return self.tokens.remove(0)

    def readNum(self,c):
        print("readNum")
        sb = []
        c = self.file.read(1)
        print(c)
        if c == '-':
            sb.append(chr(c))
            c = self.file.read()
            if c == '0':
                sb.append(chr(c))
                numAppend(sb);
            elif isDigitOne2Nine(c):
                while True:
                    sb.append(chr(c))
                    c = self.file.read()
                    if isDigit(c):
                        break
                    unread()
                    numAppend(sb)
            else:
                raise InputError('不是合法JSON结构！')
        elif c == '0':
            sb.append(chr(c))
            numAppend(sb)
        elif isDigitOne2Nine(c):
            while True:
                print("??")
                sb.append(c)
                c = self.file.read(1)
                print(c)
                if not isDigit(c):
                    break
            #self.unread()
            #numAppend(sb)
        return Token('TokenType_NUMBER', str(sb));

    def readString(self,c):
        sb = []
        print("readString")
        while True:
            print("eeeee")
            print(c)
            c = self.file.read(1)
            print("readStringOne")
            print(c)
            if isEscape(c):
                if c == 'u':
                    sb.append('\\' + chr(c))
                    for i in range(0, 4):
                        c = self.file.read()
                        if isHex(c):
                            sb.append(chr(c))
                        else:
                            raise InputError('不是合法JSON结构！')
                else:
                    sb.append('\\' + chr(c))
            elif  c == '"':
                print(':::::::')
                return Token('TokenType_STRING', str(sb))
            elif  '\r' == c or c == '\n':
                raise InputError('不是合法JSON结构！')
            else:
                print("str")
                print(c)
                sb.append(c)
                print("ok")

    def unread(self):
        print("x")
        global isUnread
        isUnread = True