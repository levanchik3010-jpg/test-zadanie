import csv
from models import VideoData


def load_csv_files(file_paths: list[str]) -> list[VideoData]:
    """Загружает данные из нескольких CSV-файлов и возвращает список объектов VideoData."""
    combined_data: list[VideoData] = []

    for path in file_paths:
        with open(path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    video = VideoData.from_dict(row)
                    combined_data.append(video)
                except ValueError:
                    continue

    return combined_data