def generar_pauta(nivel):
    pautas = {
        0: "Todo está en equilibrio. Aprovechá para mantener buenos hábitos: pausas breves, buena hidratación y límites claros.",
        1: "Tu cuerpo empieza a enviar señales. Si podés, hacé una pausa de 3 minutos: cerrar los ojos, respirar profundo y soltar tensión.",
        2: "Estás en un punto de fatiga moderada. Recomendamos priorizar tareas, pedir apoyo si es posible y darte al menos 10 minutos reales de recuperación.",
        3: "Tu nivel de fatiga es alto. Es urgente poner freno: delegá, bajá el ritmo y conectá con alguien de confianza. Cuidarte no puede esperar."
    }
    return pautas.get(nivel, "Estado no reconocido.")