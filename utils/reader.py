import csv
import sys
from typing import List, Dict, Any


def load_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Читает список CSV-файлов и возвращает объединенные данные.
    Пропускает строки с некорректными числовыми данными.
    """
    combined_data: List[Dict[str, Any]] = []

    for path in file_paths:
        try:
            with open(path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        # Конвертируем числовые значения для фильтрации
                        row['ctr'] = float(row['ctr'])
                        row['retention_rate'] = float(row['retention_rate'])
                        combined_data.append(row)
                    except (ValueError, TypeError, KeyError):
                        print(f"Предупреждение: Пропущена некорректная строка в файле {path}: {row}", file=sys.stderr)
                        continue
        except FileNotFoundError:
            raise FileNotFoundError(path)

    return combined_data