# models.py
from dataclasses import dataclass

@dataclass(frozen=True)
class VideoData:
    title: str
    ctr: float
    retention_rate: float

    @classmethod
    def from_dict(cls, data: dict) -> "VideoData":
        """Фабричный метод для безопасной конвертации из словаря со строками."""
        try:
            return cls(
                title=str(data.get("title", "Н/Д")),
                # Если в CSV пустая строка или грязь, приводим к 0.0
                ctr=float(data.get("ctr") or 0.0),
                retention_rate=float(data.get("retention_rate") or 0.0)
            )
        except (ValueError, TypeError):
            raise ValueError("Некорректный формат числовых метрик в данных")