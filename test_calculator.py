import pytest
from calculator import Soma, Subtracao, Multiplicacao, Divisao, Calculadora


# ── Soma ──────────────────────────────────────────────────────────────────────

class TestSoma:
    def setup_method(self):
        self.op = Soma()

    def test_simbolo(self):
        assert self.op.simbolo == "+"

    def test_inteiros_positivos(self):
        assert self.op.executar(2, 3) == 5

    def test_com_zero(self):
        assert self.op.executar(0, 5) == 5
        assert self.op.executar(5, 0) == 5

    def test_negativos(self):
        assert self.op.executar(-3, -7) == -10

    def test_positivo_com_negativo(self):
        assert self.op.executar(10, -4) == 6

    def test_decimais(self):
        assert self.op.executar(0.1, 0.2) == pytest.approx(0.3)

    def test_comutativa(self):
        assert self.op.executar(7, 3) == self.op.executar(3, 7)

    def test_ambos_zero(self):
        assert self.op.executar(0, 0) == 0

    def test_numero_muito_grande(self):
        assert self.op.executar(1e308, 1e308) == pytest.approx(2e308)

    def test_numero_muito_pequeno(self):
        assert self.op.executar(1e-308, 1e-308) == pytest.approx(2e-308)


# ── Subtração ─────────────────────────────────────────────────────────────────

class TestSubtracao:
    def setup_method(self):
        self.op = Subtracao()

    def test_simbolo(self):
        assert self.op.simbolo == "−"

    def test_simples(self):
        assert self.op.executar(10, 4) == 6

    def test_resultado_negativo(self):
        assert self.op.executar(3, 8) == -5

    def test_com_zero(self):
        assert self.op.executar(5, 0) == 5
        assert self.op.executar(0, 5) == -5

    def test_negativos(self):
        assert self.op.executar(-3, -7) == 4

    def test_decimais(self):
        assert self.op.executar(1.5, 0.5) == pytest.approx(1.0)

    def test_ambos_zero(self):
        assert self.op.executar(0, 0) == 0

    def test_mesmo_numero(self):
        assert self.op.executar(5, 5) == 0


# ── Multiplicação ─────────────────────────────────────────────────────────────

class TestMultiplicacao:
    def setup_method(self):
        self.op = Multiplicacao()

    def test_simbolo(self):
        assert self.op.simbolo == "×"

    def test_simples(self):
        assert self.op.executar(3, 4) == 12

    def test_por_zero(self):
        assert self.op.executar(99, 0) == 0

    def test_por_um(self):
        assert self.op.executar(7, 1) == 7

    def test_negativos(self):
        assert self.op.executar(-3, -4) == 12

    def test_positivo_negativo(self):
        assert self.op.executar(5, -2) == -10

    def test_decimais(self):
        assert self.op.executar(1.5, 2.0) == pytest.approx(3.0)

    def test_comutativa(self):
        assert self.op.executar(6, 7) == self.op.executar(7, 6)

    def test_ambos_zero(self):
        assert self.op.executar(0, 0) == 0

    def test_negativo_por_zero(self):
        assert self.op.executar(-5, 0) == 0

    def test_fracao_resulta_menor_que_um(self):
        assert self.op.executar(0.5, 0.5) == pytest.approx(0.25)


# ── Divisão ───────────────────────────────────────────────────────────────────

class TestDivisao:
    def setup_method(self):
        self.op = Divisao()

    def test_simbolo(self):
        assert self.op.simbolo == "÷"

    def test_simples(self):
        assert self.op.executar(10, 2) == 5

    def test_resultado_decimal(self):
        assert self.op.executar(7, 2) == pytest.approx(3.5)

    def test_por_um(self):
        assert self.op.executar(8, 1) == 8

    def test_negativos(self):
        assert self.op.executar(-12, -3) == 4

    def test_positivo_negativo(self):
        assert self.op.executar(10, -2) == -5

    def test_zero_pelo_numero(self):
        assert self.op.executar(0, 5) == 0

    def test_por_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="Erro"):
            self.op.executar(5, 0)

    def test_zero_dividido_por_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="Erro"):
            self.op.executar(0, 0)

    def test_negativo_dividido_por_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="Erro"):
            self.op.executar(-5, 0)

    def test_divisao_nao_exata(self):
        assert self.op.executar(10, 3) == pytest.approx(3.3333333333)

    def test_negativo_dividido_por_positivo(self):
        assert self.op.executar(-9, 3) == -3


# ── Calculadora ───────────────────────────────────────────────────────────────

class TestCalculadora:
    def setup_method(self):
        self.calc = Calculadora()

    def test_simbolos_disponiveis(self):
        assert set(self.calc.simbolos) == {"+", "−", "×", "÷"}

    def test_soma_via_calculadora(self):
        assert self.calc.calcular(3, "+", 2) == 5

    def test_subtracao_via_calculadora(self):
        assert self.calc.calcular(10, "−", 4) == 6

    def test_multiplicacao_via_calculadora(self):
        assert self.calc.calcular(3, "×", 4) == 12

    def test_divisao_via_calculadora(self):
        assert self.calc.calcular(10, "÷", 2) == 5

    def test_operacao_desconhecida(self):
        with pytest.raises(ValueError, match="desconhecida"):
            self.calc.calcular(1, "%", 2)

    def test_divisao_por_zero_via_calculadora(self):
        with pytest.raises(ValueError, match="Erro"):
            self.calc.calcular(5, "÷", 0)

    def test_simbolo_vazio(self):
        with pytest.raises(ValueError, match="desconhecida"):
            self.calc.calcular(1, "", 2)

    def test_simbolo_com_espaco(self):
        with pytest.raises(ValueError, match="desconhecida"):
            self.calc.calcular(1, " + ", 2)
