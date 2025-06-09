def detectar_nivel_fatiga(eye_ratio, blink_rate, head_tilt):
    if eye_ratio > 0.25 and blink_rate < 10:
        return 0  # Alerta
    elif 0.2 < eye_ratio <= 0.25 and blink_rate < 15:
        return 1  # Leve
    elif 0.15 < eye_ratio <= 0.2 or head_tilt > 15:
        return 2  # Moderada
    else:
        return 3  # Alta fatiga