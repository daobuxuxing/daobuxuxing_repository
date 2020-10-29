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
        self.responsible_leadership = ''
        allteam.teamDict[self.name] = self

    def add_member(self, member_name):
        self.memberlist.append(member_name)

    def del_member(self, member_name):
        self.memberlist.remove(member_name)

    def add_report_model(self, model_name):
        self.rep_name_model.append(model_name)

    def del_report_model(self, model_name):
        self.rep_name_model.remove(model_name)


class staffRegisterOnGraph:
    def __init__(self, allteam, neo=Graph):
        self.idNum = 1
        self.nameIdDict = {}
        self.neo = neo
        self.allteam = allteam

    def createNode(self, *label, **property):
        # 整理属性
        ID = self.yourId
        temp = 'ID:' + '"' + str(ID) + '"'
        for i, j in enumerate(property):
            temp += str(j) + ':"' + str(i) + '" ,'
        property = temp[:-1]
        # 整理标签
        la = ''
        for i in label:
            la += ':' + i + ' '
        self.neo.run('create ()')
        pass

    def createRelation(self):
        self.neo.run('match (a{{ {} }}), (b{{ {} }}) '
                     'create (a)-[:{}]->(b)'.format(1, 2, 3))
        pass

    @property
    def yourId(self):
        if self.idNum < 10000:
            Id = self.idNum
            self.idNum += 1
            return Id
        else:
            raise ValueError('staff id over 10000')


if __name__ == '__main__':
    neo = Graph('http://localhost:7474/browser/', user='neo4j',
                password='123456')
    test = staffRegisterOnGraph(neo)
