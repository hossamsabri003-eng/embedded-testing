from speed import check_speed

def test_speed_ok():
    assert check_speed(50, 80) == "OKK"

def test_speed_overspeed():
    assert check_speed(200, 120) == "OKK"
