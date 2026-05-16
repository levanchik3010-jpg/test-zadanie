import pytest
from models import VideoData


def test_clickbait_logic_filtering(clickbait_report, sample_video_list):
    """Проверка правильности фильтрации кликбейта."""
    result = clickbait_report.apply_logic(sample_video_list)

    assert len(result) == 2
    assert all("Кликбейт" in video.title for video in result)


@pytest.mark.parametrize(
    "custom_data, expected_first_title",
    [
        (
                [
                    VideoData("Видео А", 16.0, 10.0),
                    VideoData("Видео Б", 25.0, 10.0),
                    VideoData("Видео В", 20.0, 10.0),
                ],
                "Видео Б"
        ),
        (
                [
                    VideoData("Стрим 1", 18.0, 5.0),
                    VideoData("Стрим 2", 30.0, 5.0),
                ],
                "Стрим 2"
        )
    ]
)
def test_clickbait_logic_sorting(clickbait_report, custom_data, expected_first_title):
    """Проверка правильности сортировки по убыванию CTR на разных наборах данных."""
    result = clickbait_report.apply_logic(custom_data)
    assert result[0].title == expected_first_title