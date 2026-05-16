from abc import ABC, abstractmethod
from models import VideoData


class BaseReport(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Название отчета для параметра --report"""
        pass

    @property
    @abstractmethod
    def columns(self) -> list[str]:
        """Колонки, которые будут выведены в таблицу"""
        pass

    @abstractmethod
    def apply_logic(self, data: list[VideoData]) -> list[VideoData]:
        """Фильтрация и сортировка данных"""
        pass