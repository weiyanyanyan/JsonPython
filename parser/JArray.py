class JArray(object):
    list=[]
    def __init__(self,list):
        self.list=list
    def length(self):
        return len(list)
    def add(self,element):
        return list.append(element)
    def get(self,i):
        return list[i]
    def value(self):
        return object
    def toString(self):
        sb=[]
        sb.append('[')
        for i in range(0,len(list)):
            sb.append(list.get(i).toString())
            if i != list.size() - 1:
                sb.append(", ")
        sb.append(" ]")
        return sb.toString();