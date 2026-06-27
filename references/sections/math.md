# Mathematical Content Section

## LaTeX Conventions for CS/ML Papers

### Notation Table (mandatory)

Every paper using math MUST have a notation table. Place it early, after the introduction.

| Symbol | Definition | Description |
|---|---|---|
| $x \\in \\mathbb{R}^d$ | Input vector | Input of dimension d |
| $y \\in \\{1,...,K\\}$ | Output label | Class label from K categories |
| $f_\\theta(x)$ | Model function | Neural network with parameters theta |
| $\\mathcal{L}$ | Loss function | Cross-entropy, MSE, etc. |

### Equation Quality Rules

1. Every equation must be explained in prose
2. Define all symbols immediately after the equation
3. Number all equations referenced later
4. Use \\text{} for text inside math mode
5. Avoid inline fractions: use a/b not \\frac{a}{b} in running text

### Algorithm Boxes

```latex
\\begin{algorithm}[t]
\\caption{Training Procedure}
\\label{alg:training}
\\begin{algorithmic}[1]
\\REQUIRE Dataset $D$, learning rate $\\eta$, epochs $E$
\\ENSURE Trained model parameters $\\theta$
\\FOR{$e = 1$ to $E$}
    \\FOR{each batch $B \\sim D$}
        \\STATE $\\theta \\leftarrow \\theta - \\eta \\nabla_\\theta \\mathcal{L}(B; \\theta)$
    \\ENDFOR
\\ENDFOR
\\RETURN $\\theta$
\\end{algorithmic}
\\end{algorithm}
```

### Pseudo-Code in Markdown

For non-LaTeX documents:

```
Algorithm: Training Procedure
Input: Dataset D, learning rate lr, epochs E
Output: Updated model weights w

for epoch = 1 to E:
    for batch in D:
        loss = compute_loss(batch, w)
        gradient = backward(loss, w)
        w = w - lr * gradient
return w
```

## Usage

```bash
python scripts/math_generator.py paper.md --notation
python scripts/math_generator.py paper.md --algorithm
```
