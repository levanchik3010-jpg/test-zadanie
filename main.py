import argparse
import sys
from typing import Final
from tabulate import tabulate

from utils.reader import load_csv_files
from reports.clickbait import ClickbaitReport

# Реестр доступных отчетов
REPORTS: Final = {
    "clickbait": ClickbaitReport()
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Инструмент для формирования отчетов по YouTube-метрикам")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="Тип отчета (например, clickbait)")

    args = parser.parse_args()

    report_engine = REPORTS.get(args.report)
    if not report_engine:
        available = ", ".join(REPORTS.keys())
        print(f"Ошибка: Отчет '{args.report}' не найден. Доступные варианты: {available}", file=sys.stderr)
        sys.exit(1)

    try:
        raw_data = load_csv_files(args.files)

        if not raw_data:
            print("Информация: В указанных файлах нет данных для обработки.")
            return

        processed_data = report_engine.apply_logic(raw_data)

        if not processed_data:
            print("Информация: Видео, соответствующих критериям отчета, не найдено.")
            return

        table_rows = [
            [row.get(col, "Н/Д") for col in report_engine.columns]
            for row in processed_data
        ]

        print(tabulate(
            table_rows,
            headers=report_engine.columns,
            tablefmt="grid",
            stralign="left",
            numalign="left"
        ))

    except FileNotFoundError as e:
        print(f"Ошибка: Файл '{e}' не найден. Проверьте правильность путей.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()