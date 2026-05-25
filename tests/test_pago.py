from pagos.procesador_pago import ProcesadorPago

procesador = ProcesadorPago()

def test_calculo_impuesto():

    resultado = procesador.calcular_impuesto(100)

    assert resultado == 18


def test_pago_menor_minimo():

    resultado = procesador.validar_pago(5, 0)

    assert resultado is False


def test_limite_diario():

    resultado = procesador.validar_pago(2000, 4000)

    assert resultado is False


def test_pago_valido():

    resultado = procesador.validar_pago(500, 1000)

    assert resultado is True