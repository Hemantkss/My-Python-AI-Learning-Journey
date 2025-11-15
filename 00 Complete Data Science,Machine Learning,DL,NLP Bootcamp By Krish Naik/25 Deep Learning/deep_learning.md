# Deep Learning & CNN – Complete Notes (README)

## 1. Perceptron

- First building block of neural networks.
- Formula: `y = f(w·x + b)`
- Works only for linearly separable data.
- Update rule: `w = w + η (y_true - y_pred) x`

---

## 2. Artificial Neural Network (ANN)

### Forward Propagation

- Calculate weighted sum: `z = w·x + b`
- Apply activation: `a = activation(z)`

### Backpropagation

- Uses chain rule to compute gradients.
- Weight update: `w = w - η * ∂L/∂w`

---

## 3. Activation Functions

### Sigmoid

- Range: (0,1)
- Used for binary classification.

### Tanh

- Range: (-1,1), zero-centered.

### ReLU

- Most used in hidden layers.
- Fast, avoids vanishing gradient.

### Leaky ReLU / PReLU / ELU

- Fix dead ReLU problem.

### Softmax

- Used for multi-class classification.
- Converts logits to probabilities.

---

## 4. Loss Functions

### Classification (uses log)

- Binary Crossentropy
- Categorical Crossentropy

### Regression (no log)

- MSE
- MAE

---

## 5. Gradient Descent & Optimizers

### Types

- Batch GD: stable, slow
- SGD: fast, noisy
- Mini-batch: best choice

### Optimizers

- Momentum: smooths updates
- Adagrad: adaptive LR (decays too fast)
- RMSProp: fixes Adagrad
- Adam: Momentum + RMSProp (most used)

---

## 6. Gradient Problems

### Exploding Gradients

- Gradients become too large.
- Fix: gradient clipping, lower LR.

### Vanishing Gradients

- Gradients shrink to zero.
- Fix: ReLU, He initialization.

---

## 7. Weight Initialization

- Zero init: bad
- Random init: basic
- Xavier init: for Sigmoid/Tanh
- He init: for ReLU family

---

## 8. Regularization

### Dropout

- Randomly turns off neurons.
- Prevents overfitting.

### L1/L2 Regularization

- Penalizes large weights.

---

## 9. CNN – Convolutional Neural Networks

### Image Basics

- Images = tensor of pixel values.
- RGB → 3 channels, Grayscale → 1 channel.
- Normalize by dividing by 255.

### Convolution Operation

- Apply small filter (3x3, 5x5) to extract features.
- Produces a feature map.

### Stride & Padding

- Stride: movement step of filter.
- Padding: maintains size (SAME) or shrinks (VALID).

### Pooling

- MaxPooling: keeps strongest feature.
- AvgPooling: keeps average.

### Flatten

- Converts feature maps to 1D vector.

### Fully Connected Layer

- Final classifier using Softmax / Sigmoid.

---

## 10. Full CNN Pipeline

```
Image → Convolution → ReLU → Pooling →
Convolution → ReLU → Pooling → Flatten →
Dense Layer → Softmax/Sigmoid
```

---

##
