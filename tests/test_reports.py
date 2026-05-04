from reports.clickbait import ClickbaitReport


def test_clickbait_logic_filtering():
    """Проверка правильности фильтрации кликбейта"""
    report = ClickbaitReport()
    data = [
        {"title": "Подходит", "ctr": 20.0, "retention_rate": 30.0},
        {"title": "Низкий CTR", "ctr": 10.0, "retention_rate": 20.0},
        {"title": "Высокое удержание", "ctr": 25.0, "retention_rate": 50.0},
    ]

    result = report.apply_logic(data)
    assert len(result) == 1
    assert result[0]["title"] == "Подходит"


def test_clickbait_logic_sorting():
    """Проверка сортировки по убыванию CTR"""
    report = ClickbaitReport()
    data = [
        {"title": "Видео 1", "ctr": 16.0, "retention_rate": 10.0},
        {"title": "Видео 2", "ctr": 25.0, "retention_rate": 10.0},
        {"title": "Видео 3", "ctr": 20.0, "retention_rate": 10.0},
    ]

    result = report.apply_logic(data)
    assert result[0]["ctr"] == 25.0
    assert result[1]["ctr"] == 20.0
    assert result[2]["ctr"] == 16.0