# Exercícios em Python 🐍

Este projeto contém uma coleção de classes em Python que simulam exercícios básicos de lógica e interação com o usuário.  
Cada classe pede entradas via `input()` e mostra o resultado no terminal.

---

## 🚀 Exercícios disponíveis

### Concatenando Dados
Concatena dois textos digitados pelo usuário.

```python
from dados import Dados

d = Dados()
d.concatenar()

-----------------------------------------------
## Calculando Média de Notas
Calcula a média de três notas informadas pelo usuário.

from media import Media

m = Media()
m.media()

-----------------------------------------------
## Operações Matemáticas Simples
Executa soma, subtração, multiplicação ou divisão entre dois números.

from operacao import Operacao

op = Operacao()
op.resultado()

-----------------------------------------------
## Verificando Palíndromos
Verifica se uma palavra é um palíndromo (lida igual de trás para frente).

from palindromo import Palindromo

p = Palindromo()
p.verifica()

-----------------------------------------------
## Verificando Números Pares e Ímpares
Verifica se um número inteiro é par ou ímpar.

from parimpar import ParImpar

pi = ParImpar()
pi.par_impar()

-----------------------------------------------
## Repetindo Textos
Repete um texto informado pelo usuário um número de vezes.

from texto import Texto

t = Texto()
t.concatenar()

-----------------------------------------------

📦 exercicios-python
 ┣ 📜 dados.py
 ┣ 📜 media.py
 ┣ 📜 operacao.py
 ┣ 📜 palindromo.py
 ┣ 📜 parimpar.py
 ┣ 📜 texto.py
 ┗ 📜 README.md
