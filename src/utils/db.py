from abc import ABC, abstractmethod
from typing import Any
from collections import defaultdict

from src.enums.enums import NULL


class AbstractDatabase(ABC):
    @abstractmethod
    def set(self, key, value) -> None :
        """
        сохраняет аргумент в базе данных
        :return: 
        """
        pass

    @abstractmethod
    def get(self, key) -> Any:
        """
        возвращает, ранее сохраненную переменную. Если такой переменной
        не было сохранено, возвращает NULL
        :return: 
        """
        pass
    
    @abstractmethod
    def unset(self, key) -> None:
        """
        удаляет, ранее установленную переменную. Если значение не было
        установлено, не делает ничего.

        :return: 
        """
        pass
    
    @abstractmethod
    def count(self, value) -> None :
        """
        показывает сколько раз данные значение встречается в базе данных.
        :return: 
        """
        pass
    @abstractmethod
    def find(self, value) -> None :
        """
        выводит найденные установленные переменные для данного значения.
        :return: 
        """
        pass

    @staticmethod
    @abstractmethod
    def end() -> None :
        """
        закрывает приложение.
        :return: 
        """
        pass
    
    


class Database(AbstractDatabase):
    def __init__(self):
        self.data = defaultdict(str)
        
    def set(self, key, value) -> None :
        self.data[key] = value
    def unset(self, key) -> None :
        del self.data[key]
        
    def get(self, key) -> Any:
        return self.data[key] if bool(self.data[key]) else NULL.NULL
        
    def count(self, value) -> Any:
        counter = 0
        for key, value in self.data.items():
            if value == value:
                counter += 1
        return counter
    
    def find(self, value) -> str:
        variables = []
        for key, value in self.data.items():
            if value == value:
                variables.append(key)
        return ' '.join(variables)
    
    @staticmethod
    def end():
        exit()



class TransactionalDB:
    def __init__(self):
        self.global_state = {}      # Глобальное состояние (после всех коммитов)
        self.transaction_stack = [] # Стек активных транзакций

    def begin(self):
        """Создает новый уровень транзакции"""
        # Новый уровень = копия текущего состояния
        current_state = self.transaction_stack[-1] if self.transaction_stack else self.global_state
        self.transaction_stack.append(dict(current_state))

    def set(self, key, value):
        """Запись значения (в текущую транзакцию)"""
        if self.transaction_stack:
            self.transaction_stack[-1][key] = value
        else:
            self.global_state[key] = value

    def get(self, key):
        """Чтение значения (из самой глубокой транзакции)"""
        # Поиск сверху вниз (от последней транзакции к глобальному состоянию)
        for i in range(len(self.transaction_stack)-1, -1, -1):
            if key in self.transaction_stack[i]:
                return self.transaction_stack[i][key]
        return self.global_state.get(key, "NULL")

    def rollback(self):
        """Откат текущей транзакции"""
        if self.transaction_stack:
            self.transaction_stack.pop()

    def commit(self):
        """Фиксация текущей транзакции"""
        if not self.transaction_stack:
            return

        # Слияние изменений с родительским уровнем
        current = self.transaction_stack.pop()

        if self.transaction_stack:
            # Обновляем родительскую транзакцию
            self.transaction_stack[-1].update(current)
        else:
            # Фиксация в глобальное состояние
            self.global_state.update(current)
    
