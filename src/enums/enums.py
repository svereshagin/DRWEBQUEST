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
    BEGIN = 'BEGIN'
    ROLLBACK = 'ROLLBACK'
    COMMIT = 'COMMIT'
    
@dataclasses.dataclass
class NULL:
    NULL = 'NULL'