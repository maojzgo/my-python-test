from types import MethodType

class Student(object):
    #__slots__ = ('_name,'_age','_score','printScore')
    def __init__(self,name,age,score):
        self._name = name
        self._age = age
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("need int")
        if value < 0 or value > 100:
            raise ValueError("score need to between 0~100")
        self._score = value

    def printScore(self):
        print(self._name,self._age,self.score)

s1 = Student("wang",12,101)

#s1.printScore = MethodType(printScore,s1)

s1.score = 19
s1.printScore()
