from abc import ABC, abstractmethod
from typing import List, Dict


class BaseReport(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Название отчета для параметра --report"""
        pass

    @property
    @abstractmethod
    def columns(self) -> List[str]:
        """Колонки, которые будут выведены в таблицу"""
        pass

    @abstractmethod
    def apply_logic(self, data: List[Dict]) -> List[Dict]:
        """Фильтрация и сортировка"""
        pass
