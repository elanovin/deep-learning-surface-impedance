import numpy as np
from impedance_encoding import decode_impedance


def reconstruct_impedance(y_pred):
    """
    Convert model output [log|Z|, cos(phi), sin(phi)]
    into complex surface impedance.

    Parameters
    ----------
    y_pred : array-like, shape (..., 3)

    Returns
    -------
    Z : complex ndarray
    """
    y_pred = np.asarray(y_pred)

    log_mag = y_pred[..., 0]
    cos_phase = y_pred[..., 1]
    sin_phase = y_pred[..., 2]

    return decode_impedance(log_mag, cos_phase, sin_phase)
