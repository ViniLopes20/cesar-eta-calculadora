from abc import ABC, abstractmethod


# ── Operações (Strategy Pattern) ──────────────────────────────────────────────

class Operacao(ABC):
    @property
    @abstractmethod
    def simbolo(self) -> str: ...

    @abstractmethod
    def executar(self, a: float, b: float) -> float: ...


class Soma(Operacao):
    simbolo = "+"

    def executar(self, a: float, b: float) -> float:
        return a + b


class Subtracao(Operacao):
    simbolo = "−"

    def executar(self, a: float, b: float) -> float:
        return a - b


class Multiplicacao(Operacao):
    simbolo = "×"

    def executar(self, a: float, b: float) -> float:
        return a * b


class Divisao(Operacao):
    simbolo = "÷"

    def executar(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Erro")
        return a / b


# ── Calculadora ───────────────────────────────────────────────────────────────

class Calculadora:
    def __init__(self):
        operacoes: list[Operacao] = [Soma(), Subtracao(), Multiplicacao(), Divisao()]
        self._operacoes: dict[str, Operacao] = {op.simbolo: op for op in operacoes}

    def calcular(self, a: float, simbolo: str, b: float) -> float:
        if simbolo not in self._operacoes:
            raise ValueError(f"Operação '{simbolo}' desconhecida")
        return self._operacoes[simbolo].executar(a, b)

    @property
    def simbolos(self) -> list[str]:
        return list(self._operacoes.keys())


# ── Interface gráfica ─────────────────────────────────────────────────────────

def main():
    import tkinter as tk

    BG          = "#1e1e2e"
    DISPLAY_BG  = "#11111b"
    BTN_NUM     = "#313244"
    BTN_HOVER   = "#45475a"
    BTN_OP      = "#89b4fa"
    BTN_OP_HOV  = "#74c7ec"
    BTN_EQ      = "#a6e3a1"
    BTN_EQ_HOV  = "#94e2d5"
    BTN_CLR     = "#f38ba8"
    BTN_CLR_HOV = "#eba0ac"
    FG_LIGHT    = "#cdd6f4"
    FG_DARK     = "#1e1e2e"
    FG_MUTED    = "#585b70"

    class CalculatorApp:
        def __init__(self, root: tk.Tk):
            self.root = root
            self.root.title("Calculadora")
            self.root.geometry("320x520")
            self.root.resizable(False, False)
            self.root.configure(bg=BG)

            self._calc     = Calculadora()
            self._op       = None
            self._num_a    = None
            self._novo_num = True
            self._display_var = tk.StringVar(value="0")
            self._expr_var    = tk.StringVar(value="")

            self._build_display()
            self._build_buttons()
            self._bind_keys()

        def _build_display(self):
            frame = tk.Frame(self.root, bg=DISPLAY_BG, padx=20, pady=16)
            frame.pack(fill="x")

            tk.Label(frame, textvariable=self._expr_var,
                     font=("Helvetica", 12), bg=DISPLAY_BG,
                     fg=FG_MUTED, anchor="e").pack(fill="x")
            tk.Label(frame, textvariable=self._display_var,
                     font=("Helvetica", 44, "bold"), bg=DISPLAY_BG,
                     fg=FG_LIGHT, anchor="e").pack(fill="x")

        def _build_buttons(self):
            pad = tk.Frame(self.root, bg=BG)
            pad.pack(fill="both", expand=True, padx=12, pady=12)

            layout = [
                [("C", BTN_CLR, BTN_CLR_HOV, FG_DARK, self._limpar),
                 ("⌫", BTN_NUM, BTN_HOVER,   FG_LIGHT, self._backspace),
                 ("÷", BTN_OP,  BTN_OP_HOV,  FG_DARK,  lambda: self._set_op("÷"))],

                [("7", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("7")),
                 ("8", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("8")),
                 ("9", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("9")),
                 ("×", BTN_OP,  BTN_OP_HOV, FG_DARK, lambda: self._set_op("×"))],

                [("4", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("4")),
                 ("5", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("5")),
                 ("6", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("6")),
                 ("−", BTN_OP,  BTN_OP_HOV, FG_DARK, lambda: self._set_op("−"))],

                [("1", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("1")),
                 ("2", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("2")),
                 ("3", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("3")),
                 ("+", BTN_OP,  BTN_OP_HOV, FG_DARK, lambda: self._set_op("+"))],

                [("±", BTN_NUM, BTN_HOVER, FG_LIGHT, self._toggle_sign),
                 ("0", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit("0")),
                 (".", BTN_NUM, BTN_HOVER, FG_LIGHT, lambda: self._digit(".")),
                 ("=", BTN_EQ,  BTN_EQ_HOV, FG_DARK, self._calcular)],
            ]

            for row_def in layout:
                row = tk.Frame(pad, bg=BG)
                row.pack(fill="x", pady=4)
                for (text, bg, hov, fg, cmd) in row_def:
                    self._btn(row, text, bg, hov, fg, cmd).pack(
                        side="left", expand=True, fill="both", padx=4)

        def _btn(self, parent, text, bg, hover, fg, cmd):
            lbl = tk.Label(parent, text=text, font=("Helvetica", 18, "bold"),
                           bg=bg, fg=fg, cursor="hand2", pady=14, relief="flat")
            lbl.bind("<Button-1>", lambda _: cmd())
            lbl.bind("<Enter>",    lambda _, w=lbl, c=hover: w.config(bg=c))
            lbl.bind("<Leave>",    lambda _, w=lbl, c=bg:    w.config(bg=c))
            return lbl

        def _bind_keys(self):
            for k in "0123456789.":
                self.root.bind(k, lambda e, c=k: self._digit(c))
            self.root.bind("<BackSpace>", lambda _: self._backspace())
            self.root.bind("<Return>",    lambda _: self._calcular())
            self.root.bind("<KP_Enter>",  lambda _: self._calcular())
            self.root.bind("+",           lambda _: self._set_op("+"))
            self.root.bind("-",           lambda _: self._set_op("−"))
            self.root.bind("*",           lambda _: self._set_op("×"))
            self.root.bind("/",           lambda _: self._set_op("÷"))
            self.root.bind("<Escape>",    lambda _: self._limpar())

        def _digit(self, char):
            current = self._display_var.get()
            if self._novo_num:
                current = "0"
                self._novo_num = False
            if char == "." and "." in current:
                return
            self._display_var.set(char if current == "0" and char != "." else current + char)

        def _set_op(self, op):
            self._num_a = float(self._display_var.get())
            self._op = op
            self._expr_var.set(f"{self._fmt(self._num_a)} {op}")
            self._novo_num = True

        def _calcular(self):
            if self._op is None or self._num_a is None:
                return
            try:
                b = float(self._display_var.get())
                resultado = self._calc.calcular(self._num_a, self._op, b)
                self._expr_var.set(f"{self._fmt(self._num_a)} {self._op} {self._fmt(b)} =")
                self._display_var.set(self._fmt(resultado))
            except ValueError as e:
                self._display_var.set(str(e))
                self._expr_var.set("")
            finally:
                self._num_a = None
                self._op = None
                self._novo_num = True

        def _backspace(self):
            current = self._display_var.get()
            self._display_var.set(current[:-1] if len(current) > 1 else "0")

        def _toggle_sign(self):
            val = float(self._display_var.get()) * -1
            self._display_var.set(self._fmt(val))

        def _limpar(self):
            self._display_var.set("0")
            self._expr_var.set("")
            self._num_a = None
            self._op = None
            self._novo_num = True

        def _fmt(self, n: float) -> str:
            return str(int(n)) if n == int(n) else str(n)

    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
