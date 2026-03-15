# Coupled-ODE-System-Solver

Este projeto implementa uma rotina em Python para resolver sistemas lineares de equações diferenciais ordinárias com acoplamento.

O sistema resolvido possui a forma:

$$
\frac{dY}{dt} = AY + b
$$

onde:

- **Y** → vetor de estados  
- **A** → matriz de parâmetros  
- **b** → vetor de bias  

O método numérico utilizado para aproximar a solução é o método de Euler.

---

# Estrutura do Projeto

```
sistema_de_EDOs/
│
├── main.py
├── rotinaP.py
└── README.md
```

### rotinaP.py

Contém as funções responsáveis por:

- resolver sistemas lineares
- executar a simulação numérica
- gerar tabelas
- gerar gráficos

Bibliotecas utilizadas:

- numpy  
- pandas  
- matplotlib  
- tabulate  

---

### main.py

Arquivo principal do programa.

Responsável por:

- coletar dados do usuário  
- gerar matriz de parâmetros  
- iniciar a simulação do sistema  

---

# Funcionamento do Algoritmo

O método de Euler é aplicado da seguinte forma:

$$
Y_{k+1} = Y_k + h(A Y_k + b)
$$

onde:

- **h** é o passo de tempo  
- **k** representa o passo da simulação  

---

# Como Executar

## 1. Instalar dependências

```
pip install numpy pandas matplotlib tabulate
```

---

## 2. Executar o programa

```
python main.py
```

---

# Entradas do Programa

O programa solicita:

- ordem do sistema  
- matriz de parâmetros (manual ou aleatória)  
- vetor inicial  
- vetor de bias  
- passo de tempo  
- tempo de simulação  

---

# Exemplo de Saída

## Tabela gerada pelo programa

![Tabela de saída](imagens/tabela_saida.png)

---

# Tecnologias Utilizadas

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Tabulate  

---

# Autor

Paulo André Pinheiro Amaral
