from matchers import And, All, Not, HasAtLeast, PlaysIn, HasFewerThan, Or

class QueryBuilder:
    def __init__(self,  matcher=And()):
        self._matcher = matcher

    def playsIn(self, value):
        return QueryBuilder(And(self._matcher, PlaysIn(value)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def build(self):
        return self._matcher

