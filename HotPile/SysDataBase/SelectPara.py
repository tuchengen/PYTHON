class BaseClass(object):
    #热流密度
    @property
    def preheatflow(self):
        return self._preheatflow
    @preheatflow.setter
    def preheatflow(self,value):
        self._preheatflow=value
    
    #应用方式
    @property
    def iType(self):
        return self._iType
    @iType.setter
    def iType(self,value):
        self._iType=value

    #液塞容差
    @property
    def tolerance(self):
        return self._tolerance
    @tolerance.setter
    def tolerance(self,value):
        self._tolerance=value
    
    #重量
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self,value):
        self._weight=value

    #高温工作
    @property
    def heigh(self):
        return self._heigh
    @heigh.setter
    def heigh(self,value):
        self._heigh=value