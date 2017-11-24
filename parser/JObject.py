class JObject(object):
    map={}
    def __init__(self,map):
        #print("ObjectZZ")
        self.map=map
    def getInt(self,key):
        return int(map.get(key).value())
    def getString(self,key):
        return String(map.get(key).value())
    def getBoolean(self,key):
        return bool(map.get(key).value())
    def getJArray(self,key):
        return JArray(map.get(key).value())
    def toString(self):
        sb=[]
        sb.append('{')
        size=len(sb)
        for key in map.getKey:
            sb.append(key+':'+map.get(key))
            if --size!=0:
                sb.append(',')
        sb.append('}')
        return sb.toString()
