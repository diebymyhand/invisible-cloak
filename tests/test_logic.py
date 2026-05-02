import numpy as np
from logic import create_mask, apply_cloak_effect


def test_mask_output_shape():
    """Перевірка, чи маска має правильний розмір (2D)."""
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    lower = np.array([0, 0, 0])
    upper = np.array([180, 255, 255])

    mask = create_mask(frame, lower, upper)
    assert mask.shape == (100, 100)


def test_cloak_effect_logic():
    """Перевірка, чи результат обробки не пустий."""
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    background = np.ones((100, 100, 3), dtype=np.uint8) * 255
    mask = np.zeros((100, 100), dtype=np.uint8)

    output = apply_cloak_effect(frame, background, mask)
    assert output.shape == (100, 100, 3)
    assert np.any(output >= 0)