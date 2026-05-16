import pytest
from utils.reader import load_csv_files
from models import VideoData

def test_load_csv_valid_and_invalid_rows(tmp_path):
    """Проверка, что корректные строки преобразуются в VideoData, а битые — пропускаются."""
    f = tmp_path / "test.csv"
    content = "title,ctr,retention_rate\nВидео1,18.5,30\nВидео2,ошибка,20\nВидео3,20,много"
    f.write_text(content, encoding='utf-8')

    result = load_csv_files([str(f)])

    assert len(result) == 1
    assert isinstance(result[0], VideoData)
    assert result[0].title == "Видео1"
    assert result[0].ctr == 18.5

def test_load_csv_file_not_found():
    """Проверка выброса исключения при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        load_csv_files(["non_existent.csv"])