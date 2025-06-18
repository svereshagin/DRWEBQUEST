from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union, DefaultDict
from collections import defaultdict

from src.enums.enums import NULL


class AbstractDatabase(ABC):
    @abstractmethod
    def set(self, key: str, value: str) -> None:
        """
        сохраняет аргумент в базе данных
        :param key: ключ для сохранения
        :param value: значение для сохранения
        :return: None
        """
        pass

    @abstractmethod
    def get(self, key: str) -> Union[str, NULL]:
        """
        возвращает, ранее сохраненную переменную. Если такой переменной
        не было сохранено, возвращает NULL
        :param key: ключ для поиска
        :return: значение или NULL
        """
        pass

    @abstractmethod
    def unset(self, key: str) -> None:
        """
        удаляет, ранее установленную переменную. Если значение не было
        установлено, не делает ничего.
        :param key: ключ для удаления
        :return: None
        """
        pass

    @abstractmethod
    def count(self, value: str) -> int:
        """
        показывает сколько раз данные значение встречается в базе данных.
        :param value: значение для подсчета
        :return: количество совпадений
        """
        pass

    @abstractmethod
    def find(self, value: str) -> str:
        """
        выводит найденные установленные переменные для данного значения.
        :param value: значение для поиска
        :return: строку с ключами через пробел
        """
        pass

    @staticmethod
    @abstractmethod
    def end() -> None:
        """
        закрывает приложение.
        :return: None
        """
        pass
    
    @abstractmethod
    def begin(self) -> None:
        """
        начинает транзакцию
        :return: 
        """
        pass
    @abstractmethod
    def rollback(self) -> None:
        """
        откатывает транзакцию назад
        :return: 
        """
    @abstractmethod
    def commit(self) -> None:
        """
        подтверждает изменения
        :return: 
        """
    
class InMemoryDB:
    """Простое хранилище ключ-значение (без транзакций)"""
    def __init__(self):
        self.data = {}
        self.value_counts = defaultdict(int)  # Для быстрого COUNTS

    def set(self, key, value):
        old_value = self.data.get(key)
        if old_value is not None:
            self.value_counts[old_value] -= 1
        self.data[key] = value
        self.value_counts[value] += 1

    def get(self, key):
        return self.data.get(key, "NULL")

    def unset(self, key):
        value = self.data.pop(key, None)
        if value is not None:
            self.value_counts[value] -= 1

    def count(self, value):
        return self.value_counts.get(value, 0)

    def find(self, value):
        return [k for k, v in self.data.items() if v == value]
    
    @staticmethod
    def end() -> None:
        exit()

class TransactionalDB:
    def __init__(self):
        self.base = InMemoryDB()
        self.transactions = []

    def set(self, key, value):
        if not self.transactions:
            self.base.set(key, value)
        else:
            self.transactions[-1][key] = value

    def get(self, key):
        # Ищем в транзакциях (от последней к первой)
        for changes in reversed(self.transactions):
            if key in changes:
                return changes[key] if changes[key] is not None else "NULL"
        return self.base.get(key)

    def unset(self, key):
        if not self.transactions:
            self.base.unset(key)
        else:
            self.transactions[-1][key] = None  # Помечаем как удаленное

    def count(self, value):
        count = self.base.counts(value)
        for changes in self.transactions:
            for k, v in changes.items():
                if v == value:
                    count += 1
                elif v is None and self.base.get(k) == value:
                    count -= 1
        return count

    def find(self, value):
        base_result = set(k for k in self.base.find(value))
        for changes in self.transactions:
            for k, v in changes.items():
                if v == value:
                    base_result.add(k)
                elif v is None:
                    base_result.discard(k)
        return sorted(base_result)

    def begin(self):
        self.transactions.append({})

    def commit(self):
        if not self.transactions:
            return
        changes = self.transactions.pop()
        for key, value in changes.items():
            if value is not None:
                self.base.set(key, value)
            else:
                self.base.unset(key)

    def rollback(self):
        if self.transactions:
            self.transactions.pop()
    @staticmethod
    def end() -> None:
        exit()