
from abc import ABCMeta
'''
JESUS JOYAS 2024 shopingList test
Class Singleton
This class create only an instance of json or sqlalchemy interface implementation
args-None
return - 0
'''

class singletonMeta(ABCMeta,type):
    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            #we need to call ONLY type bc ABCmeta is only for the subclass compatibility
            cls._instances[cls] = type.__call__(cls,*args,**kwargs)

        return cls._instances[cls]
