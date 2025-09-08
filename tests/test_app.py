from app.main import compute_bonus

def test_compute_bonus():
    assert compute_bonus(100000) == 10000
