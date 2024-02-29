import time
from datetime import date
import pydantic
import attrs
from dataclasses import dataclass, field
import itertools

class CFG:
    PROJECT_NAME: str = field()
    DATE: date = date.today()
    SEED: int = field()
    PATH: str = field()
    TRAIN_PATH: str = field()
    TEST_PATH: str = field()
    
    @property
    def project_name(self):
        return self.PROJECT_NAME
    
    @project_name.setter
    def project_name(self, value):
        self.PROJECT_NAME = value
    
    @property
    def date(self):
        return self.DATE
    
    @date.setter
    def date(self, value):
        self.DATE = value

    @property
    def seed(self):
        return self.SEED
    
    @seed.setter
    def seed(self, value):
        self.SEED = value
    
    @property
    def path(self):
        return self.PATH
    
    @path.setter
    def path(self, value):
        self.PATH = value
    
    @property
    def train_path(self):
        return self.TRAIN_PATH
    
    @train_path.setter
    def train_path(self, value):
        self.TRAIN_PATH = value
    
    @property
    def test_path(self):
        return self.TEST_PATH
    
    @test_path.setter
    def test_path(self, value):
        self.TEST_PATH = value