from typing import List, Dict, Any
from .base import BaseReport


class ClickbaitReport(BaseReport):
    name: str = "clickbait"
    columns: List[str] = ["title", "ctr", "retention_rate"]

    def apply_logic(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Логика: CTR > 15% и удержание < 40%.
        Сортировка: по убыванию CTR.
        """
        filtered = [
            row for row in data
            if row['ctr'] > 15 and row['retention_rate'] < 40
        ]

        return sorted(filtered, key=lambda x: x['ctr'], reverse=True)