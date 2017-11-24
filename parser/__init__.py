from Tools.scripts.treesync import raw_input
from Parser import Parser
from tokenizer.Tokenizer import Tokenizer

if __name__=="__main__":
	testValue=raw_input('请输入测试数据:')           #  [{"CityId":18}]
file=open('G:/pycharm_workspace/JsonPython/test.txt','w')
file.write(testValue)
file.close()
file=open('G:/pycharm_workspace/JsonPython/test.txt','r')
#s=file.read(1)
url='G:/pycharm_workspace/JsonPython/test.txt'
tokenizer=Tokenizer(url)
try:
    print("start")
    tokenizer.tokenizer()
    print("begin")
    #print(tokenizer.getTokens())
    parser = Parser(tokenizer.getTokens())
    print("end")
    result=parser.json()
    print("合法Json字符！")
except:
    print("不合法Json字符！")

#d=file.read(1)
#print(s)
print(file.read(40))