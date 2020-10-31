import py2neo
from py2neo import Graph
global teamDict


class allTeam:
    def __init__(self):
        self.teamDict = {}
        self.dictLen = len(teamDict)
        self.teamNameList = self.teamDict.keys()


class team(object):
    def __init__(self, name, allteam):
        self.name = name
        self.rep_name_model = []
        self.memberlist = []
        self.responsibleleader = ''
        allteam.teamDict[self.name] = self

    def add_member(self, member_name):
        self.memberlist.append(member_name)

    def del_member(self, member_name):
        self.memberlist.remove(member_name)

    def add_report_model(self, model_name):
        self.rep_name_model.append(model_name)

    def del_report_model(self, model_name):
        self.rep_name_model.remove(model_name)


class registerOnGraph:
    def __init__(self, allteam, neo=Graph):
        # 为每个成员分配Id
        self.iddNum = 1
        # 为所有的节点保存name属性及ID
        self.nameIdDict = {}
        self.neo = neo
        self.allteam = allteam

    # 每次传入两个name值，一个用于nameIdDict ，另一个更新属性
    def createNode(self, namefordict, label=list, property=dict):
        ID = self.yourId
        property[namefordict] = ID
        label, property = self.getLabelProperty(ID, label, property)
        n = self.neo.run('create (n:{} {}) return n'.format(label, property))
        self.nameIdDict[namefordict] = ID
        return n.data()

    def createRelation(self, namefordict, startnodeid, endnodeid, label=list, property=dict):
        ID = self.yourId
        property[namefordict] = ID
        label, property = self.getLabelProperty(ID, label, property)
        relpara = label + property
        r = self.neo.run('match (a{{ ID:{} }}), (b{{ ID:{} }}) create (a)-[r:{}]'
                     '->(b) return r'.format(startnodeid, endnodeid, relpara))
        self.nameIdDict[namefordict] = ID
        return r.data()

    # 用于关键字搜索
    def idSearch(self, name):
        temp = []
        for i in self.nameIdDict.keys():
            if name in i:
                temp.append(self.nameIdDict[i])
        return temp

    @property
    def yourId(self):
        Id = self.iddNum
        self.iddNum += 1
        return Id

    @staticmethod
    def getLabelProperty(id, label, property):
        # 整理属性
        temp = '{ID:' + '"' + str(id) + '"'
        for i, j in property.items():
            temp += str(i) + ':"' + str(j) + '" ,'
        property = temp[:-1] + '}'
        # 整理标签
        la = ''
        for i in label:
            la += ':' + i + ' '
        label = la
        return label, property


# 用户信息处理，查询反馈信息展示等
class userApi:
    def __init__(self):
        pass

    def getInsert(self):
        pass

    def show(self):
        pass


if __name__ == '__main__':
    neo = Graph('http://localhost:7474/browser/', user='neo4j',
                password='****')
    allteam = allTeam()
    test = registerOnGraph(allteam, neo)


