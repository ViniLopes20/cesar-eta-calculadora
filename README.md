# Calculadora

Calculadora desktop com interface gráfica desenvolvida em Python, aplicando os princípios de Orientação a Objetos (POO) com o padrão Strategy para as operações matemáticas.

![alt text](image.png)

## Funcionalidades

- Soma, subtração, multiplicação e divisão
- Interface gráfica com tema escuro
- Suporte a teclado
- Tratamento de erros (ex: divisão por zero)

## Estrutura do projeto

```
Calculadora/
├── calculator.py       # Código principal (lógica + interface gráfica)
├── test_calculator.py  # Testes com pytest (50 casos)
└── README.md
```

### Arquitetura (POO + Strategy Pattern)

```
Operacao (ABC)           ← classe abstrata
├── Soma
├── Subtracao
├── Multiplicacao
└── Divisao

Calculadora              ← orquestra as operações
CalculatorApp            ← interface gráfica (tkinter)
```

## Pré-requisitos

- Python 3.13 (via Homebrew)
- python-tk@3.13

### Instalação dos pré-requisitos

```bash
brew install python-tk@3.13
```

### Configuração do ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Como rodar a calculadora

```bash
/opt/homebrew/bin/python3.13 calculator.py
```

> **Atenção:** use o Python do Homebrew (`/opt/homebrew/bin/python3.13`), pois o Python padrão do macOS não possui suporte ao tkinter.

### Atalhos de teclado

| Tecla | Ação |
|---|---|
| `0–9` / `.` | Digitar número |
| `+` `-` `*` `/` | Selecionar operação |
| `Enter` | Calcular |
| `Backspace` | Apagar último dígito |
| `Esc` | Limpar |

## Como rodar os testes

```bash
.venv/bin/pytest test_calculator.py -v
```

Para rodar sem detalhes:

```bash
.venv/bin/pytest test_calculator.py
```

### Cobertura dos testes (50 casos)

| Classe | Casos testados |
|---|---|
| `TestSoma` | positivos, negativos, zero, decimais, overflow, underflow, comutatividade |
| `TestSubtracao` | positivos, negativos, zero, resultado negativo, mesmo número |
| `TestMultiplicacao` | positivos, negativos, zero, fração, comutatividade |
| `TestDivisao` | positivos, negativos, decimal, irracional, divisão por zero (3 variações) |
| `TestCalculadora` | todas as operações, símbolo inválido, símbolo vazio, símbolo com espaço |

### CI/CD

- CI: https://github.com/ViniLopes20/cesar-eta-calculadora/actions
