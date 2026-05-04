import sys
from unittest.mock import patch
import pytest
from main import main


def test_cli_unknown_report(capsys):
    """Проверка ошибки при неверном названии отчета"""
    test_args = ["main.py", "--files", "any.csv", "--report", "unknown_type"]

    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 1

    captured = capsys.readouterr()
    assert "Ошибка: Отчет 'unknown_type' не найден" in captured.err


def test_cli_no_videos_found(tmp_path, capsys):
    """Проверка сообщения, когда ни одно видео не подошло под критерии"""
    f = tmp_path / "empty.csv"
    f.write_text("title,ctr,retention_rate\nСкучное видео,5.0,80.0", encoding='utf-8')

    test_args = ["main.py", "--files", str(f), "--report", "clickbait"]

    with patch.object(sys, 'argv', test_args):
        main()

    captured = capsys.readouterr()
    assert "Информация: Видео, соответствующих критериям отчета, не найдено" in captured.out