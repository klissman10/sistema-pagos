class ProcesadorPago:

    LIMITE_DIARIO = 5000
    MONTO_MINIMO = 10

    def calcular_impuesto(self, monto):
        return monto * 0.18

    def validar_pago(self, monto, acumulado_dia):

        if monto < self.MONTO_MINIMO:
            return False

        if acumulado_dia + monto > self.LIMITE_DIARIO:
            return False

        return True

    def procesar_reembolso(self, dias):
        return dias <= 30