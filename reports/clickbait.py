from models import VideoData
from .base import BaseReport


class ClickbaitReport(BaseReport):
    name: str = "clickbait"
    columns: list[str] = ["title", "ctr", "retention_rate"]

    def apply_logic(self, data: list[VideoData]) -> list[VideoData]:
        """
        Логика: CTR > 15% и удержание < 40%.
        Сортировка: по убыванию CTR.
        """
        filtered = [
            row for row in data
            if row.ctr > 15.0 and row.retention_rate < 40.0
        ]

        return sorted(filtered, key=lambda x: x.ctr, reverse=True)