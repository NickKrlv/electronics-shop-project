from src.phone import Phone


def test_phone():
    iphone = Phone("iPhone 14", 120_000, 5, 2)
    samsung = Phone("Samsung S22", 100_000, 5, 2)
    assert iphone.name == 'iPhone 14'
    assert iphone.price == 120000
    assert iphone.quantity == 5
    assert iphone.number_of_sim == 2
    assert samsung + iphone == 10
