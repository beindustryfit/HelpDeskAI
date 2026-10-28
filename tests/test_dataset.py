from pathlib import Path

import pandas as pd


def test_sample_rows_have_the_right_columns():
    path = Path(__file__).resolve().parents[1] / "data" / "tickets.csv"
    frame = pd.read_csv(path)
    assert list(frame.columns) == ["text", "label"]
    assert set(frame["label"]) <= {"wifi", "fees", "exams", "hostel", "placements"}
    assert len(frame) >= 10
