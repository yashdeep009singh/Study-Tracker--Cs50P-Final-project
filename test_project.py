import pytest
from project import validate_minutes, summarize, format_summary, add_session, load_sessions


def test_validate_minutes():
    assert validate_minutes("30") == 30
    assert validate_minutes(45) == 45
    with pytest.raises(ValueError):
        validate_minutes("cat")
    with pytest.raises(ValueError):
        validate_minutes("-5")
    with pytest.raises(ValueError):
        validate_minutes("0")


def test_summarize():
    sessions = [("2026-10-01", "Math", 30), ("2026-10-02", "Math", 60), ("2026-10-02", "Physics", 45)]
    assert summarize(sessions) == {"Math": 90, "Physics": 45}
    assert summarize([]) == {}


def test_format_summary():
    out = format_summary({"Math": 90})
    assert "Math" in out
    assert "90" in out
    assert "1.5" in out


def test_add_and_load(tmp_path):
    f = tmp_path / "s.csv"
    add_session("math", "30", filename=str(f))
    sessions = load_sessions(filename=str(f))
    assert len(sessions) == 1
    assert sessions[0][1] == "Math"
    assert sessions[0][2] == 30
    with pytest.raises(ValueError):
        add_session("", "30", filename=str(f))
