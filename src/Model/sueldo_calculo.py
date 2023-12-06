from src.Model.database import Sueldo, session

def calcular_sueldo_neto(sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
    # Bonificaciones
    pago_horas_extras = 1.50 * horas_extras * sueldo_basico / 30 / 8
    movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    total_bonificaciones = pago_horas_extras + movilidad + bonificacion_suplementaria

    # Descuentos
    remuneracion_computable = sueldo_basico + movilidad + bonificacion_suplementaria
    descuento_faltas = remuneracion_computable / 30 * dias_falta
    descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * minutos_tardanza
    total_descuentos = descuento_faltas + descuento_tardanzas

    # Cálculo del sueldo neto
    sueldo_neto = sueldo_basico + total_bonificaciones - total_descuentos
    return sueldo_neto
