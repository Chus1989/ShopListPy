
from abc import ABCMeta
'''
JESUS JOYAS 2024 shopingList
Class Singleton
This class create only an instance of json or sqlalchemy interface implementation
This class heredates of ABC meta and type, because type is for the singleton and
abcmeta is for the DAO interface(abstract) and the subclass needs to be the same
args-None
return - 0
'''

class singletonMeta(ABCMeta,type):
    _instances = {}
    '''
    This is a call method to add this functionality before the creation of the instance
    and ends when the class instance is created.
    '''
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            #we need to call ONLY type bc ABCmeta is only for the subclass compatibility
            cls._instances[cls] = type.__call__(cls,*args,**kwargs)

        return cls._instances[cls]
