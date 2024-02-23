import pytest
import ffmpeg
import src.mp4_to_wave_audio.extract_convert as mp4_to_wave_audio


@pytest.mark.parametrize(
    "input, output",
    [
        pytest.param("tests/test.mp4", "tests/test.wav", id=".mp4 as input, no error"),
        pytest.param("tests/test.mkv", "tests/test.wav", id="not .mp4 as input, error"),
    ],
)
def test_extract_audio(mocker, input, output):
    mocker.patch.object(ffmpeg, "input")
    mp4_to_wave_audio.extract_audio("tests/test.mp4", "tests/test.wav")
    assert False
