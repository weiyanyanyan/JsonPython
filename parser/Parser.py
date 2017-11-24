from array import array

#from Value import Value
from JArray import JArray
from JObject import JObject
from Primary import Primary
#from TokenType import TokenType
from Tokenizer import Tokenizer, InputError


class Parser(object):

    #tokenizer=Tokenizer()

    def __init__(self, tokenizer):
        print("parser")
        self.tokenizer = tokenizer

    def object(self):
        print("objectss")
        del self.tokenizer[0]
        print("objectOne")
        map={}
        if self.isToken('TokenType_END_OBJ'):
            del self.tokenizer[0]
            return JObject(map)
        if self.isToken('TokenType_STRING'):
            map = self.key(map);
        return JObject(map)

    def key(self):
        print("key")
        del self.tokenizer[0]
        if not self.isToken('TokenType_COLON'):
            raise InputError('不是合法JSON结构！')
        else:
            del self.tokenizer[0]
            if self.isPrimary():
                primary=Primary(self.tokenizer[0].value)
                map.put(key, primary)
            elif self.isToken('TokenType_START_ARRAY'):
                array = self.array()
                map.put(key, array)
        if self.isToken('TokenType_COMMA'):
            del self.tokenizer[0]
            if self.isToken('TokenType_STRING'):
                map = key(map)
        elif self.isToken('TokenType_END_OBJ'):
            del self.tokenizer[0]
            return map
        else:
            raise InputError('不是合法JSON结构！')
        return map

    def array(self):
        del self.tokenizer[0]
        list={}
        if self.isToken('TokenType_START_ARRAY'):
            array = self.array()
            list.add(array)
            if self.isToken('TokenType_COMMA'):
                del self.tokenizer[0]
                list = self.element(list)
        elif self.isPrimary():
            list = self.element(list)
        elif self.isToken('TokenType_START_OBJ'):
            list.add(object())
            while self.isToken('TokenType_COMMA'):
                del self.tokenizer[0]
                list.add(object())
        elif self.isToken('TokenType_END_ARRAY'):
            del self.tokenizer[0]
            array = JArray(list)
            return array
            del self.tokenizer[0]
        array = JArray(list)
        return array

    def element(self):
        list.add(Primary(self.tokenizer[0].getValue()))
        if self.isToken('TokenType_COMMA'):
            del self.tokenizer[0]
            if self.isPrimary():
                list = self.element(list)
            elif self.isToken('TokenType_START_OBJ'):
                list.add(object())
            elif self.isToken('TokenType_START_ARRAY'):
                list.add(array());
            else:
                raise InputError('不是合法JSON结构！')
        elif self.isToken('TokenType_END_ARRAY'):
            return list;
        else:
            raise InputError('不是合法JSON结构！')
        return list

    def json(self):
        print("json")
        type = self.tokenizer[0].type
        print(type)
        if type is None:
            raise InputError('不是合法JSON结构！')
        elif type=='TokenType_START_ARRAY':
            return self.array()
        elif type=='TokenType_START_OBJ':
            return self.object()
        else:
            raise InputError('不是合法JSON结构！')

        # def isToken(self,tokenType):
        #     print("istoken")
        #     t = self.tokenizer.peek(0)
        #     return t.getValue() == tokenType

    def isToken(self,name):
        print("tokentoken")
        t = self.tokenizer[0]
        #print(t.type==name)
        return t.type==name

    def isPrimary(self):
        type = self.tokenizer.peek(0).getType()
        return type == 'TokenType_BOOLEAN' or type == 'TokenType_NULL' or type == 'TokenType_NUMBER' or type == 'TokenType_STRING'

    def parser(self):
        result = self.json()
        return result

