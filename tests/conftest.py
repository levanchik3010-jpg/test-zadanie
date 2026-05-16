import pytest
from models import VideoData
from reports.clickbait import ClickbaitReport

@pytest.fixture
def clickbait_report():
    """Фикстура для инициализации генератора отчетов."""
    return ClickbaitReport()

@pytest.fixture
def sample_video_list():
    """Фикстура со стандартным набором данных для тестов логики."""
    return [
        VideoData(title="Кликбейт 1", ctr=20.0, retention_rate=30.0),
        VideoData(title="Низкий CTR", ctr=10.0, retention_rate=20.0),
        VideoData(title="Высокое удержание", ctr=25.0, retention_rate=50.0),
        VideoData(title="Кликбейт 2", ctr=16.0, retention_rate=15.0),
    ]