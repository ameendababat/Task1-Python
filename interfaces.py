from abc import ABC,abstractmethod


class StorageInterface(ABC):
    """can added new storage like CSV DB"""
    
    @abstractmethod
    def save(self,tasks):
        pass
    
    
    @abstractmethod
    def load(self):
        pass
