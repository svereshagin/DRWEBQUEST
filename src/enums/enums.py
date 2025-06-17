import dataclasses
from enum import Enum


class Command(Enum):
    SET = 'SET'
    GET = 'GET'
    UNSET = 'UNSET'
    FIND = 'FIND'
    COUNT = 'COUNT'
    END = 'END'
    HELP = 'HELP'
    
    
@dataclasses.dataclass
class NULL:
    NULL = 'Null'