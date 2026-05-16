import sys
import logging
from unittest.mock import patch
import pytest
from main import main

def test_cli_unknown_report(caplog):
    """Проверка завершения программы с ошибкой при неверном названии отчета."""
    test_args = ["main.py", "--files", "any.csv", "--report", "unknown_type"]

    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 1

    assert "Отчет 'unknown_type' не найден" in caplog.text


def test_cli_no_videos_found(tmp_path, caplog):
    """Проверка информационного сообщения, когда данные не подошли под критерии отчета."""
    caplog.set_level(logging.INFO)

    f = tmp_path / "empty.csv"
    f.write_text("title,ctr,retention_rate\nСкучное видео,5.0,80.0", encoding='utf-8')

    test_args = ["main.py", "--files", str(f), "--report", "clickbait"]

    with patch.object(sys, 'argv', test_args):
        main()

    assert "Видео, соответствующих критериям отчета, не найдено" in caplog.text