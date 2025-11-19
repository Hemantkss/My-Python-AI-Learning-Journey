# 📘 LSTM (Long Short-Term Memory) — Complete Notes
A clean, simple, and easy-to-understand **README.md style** summary of everything you learned about LSTM.

---

# 🔥 1. Why LSTM?
RNNs suffer from:
- **Vanishing gradient problem**
- **Short-term memory**
- **Cannot learn long dependencies**

👉 LSTM fixes this using **gates + memory cell**, allowing it to remember long sequences.

---

# 🔧 2. LSTM Architecture (Overview)
LSTM cell contains:
- **Forget Gate**
- **Input Gate**
- **Candidate Memory**
- **Cell State (Ct)**
- **Output Gate**
- **Hidden State (ht)**

These components control how information flows through time.

---

# 🟦 3. Forget Gate (ft)
**Purpose:** Decide what past information to remove.

**Formula (intuition):**
```
ft = σ(Wf · [ht-1, xt] + bf)
```
**Output:** 0 → forget, 1 → keep

**Example:**
If remembering weather patterns, forget gate removes irrelevant old data.

---

# 🟩 4. Input Gate (it)
**Purpose:** Decide how much new information to store.

**Formula (intuition):**
```
it = σ(Wi · [ht-1, xt] + bi)
```

**Example:**
If new information is important ("today temperature rising"), store it.

---

# 🟧 5. Candidate Memory (C~t)
**Purpose:** Suggest new information to add.

**Formula (intuition):**
```
C~t = tanh(Wc · [ht-1, xt] + bc)
```
**Role:** Raw new memory before filtering.

---

# 🔵 6. Update Cell State (Ct)
Cell state is the **long-term memory**.

**Update formula (intuitive):**
```
Ct = ft × Ct-1 + it × C~t
```
- Forget old memory (ft × Ct-1)
- Add new memory (it × C~t)

**Example:**
You keep important scenes from a movie and add new ones.

---

# 🟪 7. Output Gate (ot) + Hidden State (ht)
**Output Gate:** Decides what memory to show.

**Formula (intuition):**
```
ot = σ(Wo · [ht-1, xt] + bo)
ht = ot × tanh(Ct)
```

**Example:**
From all notes in your notebook (cell state), you speak only relevant points (hidden state).

---

# 🔥 8. Training Process (Short)
1. Feed input sequence step-by-step
2. Forward pass → gates compute memory
3. Get output prediction
4. Compute loss
5. Backpropagation Through Time (BPTT)
6. Update weights (Adam/RMSProp)
7. Repeat for many epochs

---

# 🧩 9. LSTM Variants
- **Vanilla LSTM:** Basic, one direction
- **Stacked LSTM:** Multiple LSTM layers
- **Bidirectional LSTM:** Forward + backward context
- **Encoder–Decoder LSTM:** Used for translation
- **Peephole LSTM:** Gates also see cell state
- **Attention LSTM:** Focuses on important time steps
- **GRU:** Simplified LSTM (update + reset gates)

---

# ⚡ 10. GRU (Gated Recurrent Unit) — Short Summary
- 2 gates: **Update & Reset**
- No separate cell state
- Faster and simpler
- Similar accuracy to LSTM

**Update gate:** How much past to keep
**Reset gate:** How much past to forget

---

# 🎯 Final Summary
- LSTM solves vanishing gradient & long-term memory problems.
- Uses gates to control information flow.
- GRU is a simplified version.
- Both are powerful for sequential data like NLP, time-series, and speech.

---

# ✔ Perfect for Revision
This README contains **all important intuition, formulas, and examples** needed to fully understand LSTM for Data Science and Deep Learning.