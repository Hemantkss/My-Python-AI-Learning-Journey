# Transformers — Complete Notes (Hemant's Krish-Style Cheat Sheet)

> **Purpose:** When you open this README you should *recall* every core transformer concept quickly — intuition, definitions, step-by-step working, text diagrams, formulas, and compact real-world examples.

---

## Table of Contents
1. Quick overview / motivation
2. Key definitions & formulas
3. Core building blocks (Q/K/V, Self-Attention, Multi-Head Attention, FFN, Positional Encoding, LayerNorm, Residuals)
4. Encoder — full architecture (step-by-step)
5. Decoder — full architecture (step-by-step)
6. Masking & attention masks
7. Cross (Encoder–Decoder) attention
8. Final linear + softmax (generation)
9. Diagrams (text) — quick visual reference
10. Real-world practical examples (with short walkthroughs)
11. Short checklist to remember
12. Common variants & modern additions (what to learn next)
13. Practical exercises (do these to remember)
14. One-page cheat sheet (compact)
15. Recommended commands & Hugging Face quickstart

---

## 1. Quick overview / motivation
- **Problem with RNN/LSTM:** sequential processing, slow training, difficulty with long-range dependencies.
- **Transformer idea (2017):** use attention to model relationships between tokens — do everything in parallel.
- **High-level:** Encoder(s) *understand* input; Decoder *generates* output (for seq2seq). Self-attention is the core.

---

## 2. Key definitions & formulas
- **Token embedding:** dense vector representing a token.
- **Positional encoding:** vector added to embedding to provide token order information.
- **Query (Q), Key (K), Value (V):** linear projections of the same input used to compute attention.

### Scaled Dot-Product Attention (formula):
\[ \text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \]
- where \(d_k\) is dimension of keys.

### Multi-Head Attention (concept):
- run attention `h` times in parallel with smaller dimension, then `concat` and a final linear projection.

### Feed-Forward Network (FFN):
- two linear layers with activation (usually ReLU):
```
FFN(x) = W2 (ReLU(W1 x + b1)) + b2
```

### Layer Normalization (per token):
- normalize across features: \( \hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} \), then scale & shift with learned \(\gamma, \beta\).

---

## 3. Core building blocks (intuitions + short formulas)

### A. Q / K / V (intuition)
- **Query:** what I am searching for.
- **Key:** what each token offers (indexable feature).
- **Value:** the information I will gather if I attend to that token.
- *All are linear projections from token embeddings:*
```
Q = X W_Q,  K = X W_K,  V = X W_V
```

### B. Self-Attention (working)
1. Compute Q, K, V for every token.
2. Compute raw scores `S = Q K^T` (how well token i queries token j).
3. Scale: `S = S / sqrt(d_k)`.
4. Softmax row-wise to get attention weights.
5. Weighted sum with V to get contextualized token representation.

### C. Multi-Head Attention (intuition)
- Multiple parallel attention heads let the model look at different types of relations simultaneously.
- Steps: compute head-wise Q/K/V → attention per head → concat heads → final linear layer.

### D. Positional Encoding (sinusoidal)
- For position `pos` and dimension `i`:
```
PE(pos, 2i) = sin(pos / 10000^{2i/d_model})
PE(pos, 2i+1) = cos(pos / 10000^{2i/d_model})
```
- Add PE to token embeddings so model knows token order.

### E. Residual + LayerNorm pattern (Pre-LN recommended):
- `x' = LayerNorm(x + Sublayer(x))`  (if using pre-LN, apply LayerNorm before sublayer in some variants — note the exact pattern may vary between implementations).

---

## 4. Encoder — full architecture (step-by-step)
One Encoder layer (single block):
1. Input = token_embedding + positional_encoding
2. **LayerNorm** (optional pre-LN style)
3. **Multi-Head Self-Attention** (Q,K,V from same input)
4. **Add & Norm** (residual connection + layernorm)
5. **Feed-Forward Network** (FFN)
6. **Add & Norm**

Stack `N` such layers to form the encoder (commonly N=6 for base models, more for larger models).

**Output:** per-token contextual embeddings (shape: sequence_length × d_model).

---

## 5. Decoder — full architecture (step-by-step)
One Decoder layer:
1. Input tokens (shifted-right target) + positional encoding
2. **Masked Multi-Head Self-Attention** (causal mask to prevent looking ahead)
3. **Add & Norm**
4. **Encoder–Decoder Multi-Head Attention (Cross-Attn)**: Q from decoder states, K & V from encoder outputs
5. **Add & Norm**
6. **Feed-Forward Network**
7. **Add & Norm**

Finally: Linear layer (project to vocab size) → Softmax → token probabilities.

### Autoregressive generation loop (simplified):
- Start with `[BOS]` token.
- While not `[EOS]` and length < max:
  - Run decoder with masked attention (only previous tokens visible).
  - Linear + Softmax → pick next token (greedy / beam / sampling / top-p)
  - Append token and continue.

---

## 6. Masking & Attention Masks (cheat sheet)
- **Padding mask:** prevents attention to padded tokens (0 where padding).
- **Look-ahead / causal mask:** triangular mask that prevents future positions from being attended (used in decoder masked self-attention).
- **Combined masks:** sometimes combined with padding masks by adding large negative number to logits.

Example causal mask (n=5 tokens):
```
[[1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,0,0],
 [1,1,1,1,0],
 [1,1,1,1,1]]
```
(where 1 = allowed, 0 = blocked)

---

## 7. Cross (Encoder–Decoder) attention (intuition)
- Decoder asks `Q` (what it needs now) and compares with encoder's `K` (what the input offers) to get weights applied to `V`.
- This aligns output tokens to input tokens — crucial for translation and conditioned generation.

---

## 8. Final linear + softmax (generation)
- The decoder's final hidden vector for the current time-step is projected by a matrix `W_vocab` to produce logits of shape `(vocab_size,)`.
- `Softmax` converts logits → probabilities. Choose token by greedy/beam/sample.

---

## 9. Diagrams (text) — quick visual reference

### Encoder block (single layer):
```
Input Embeddings + PosEnc
        ↓
     LayerNorm
        ↓
Multi-Head Self-Attention
        ↓
    Add & Norm
        ↓
     LayerNorm
        ↓
        FFN
        ↓
    Add & Norm
```

### Decoder block (single layer):
```
Decoder Embedding + PosEnc
        ↓
Masked Multi-Head Self-Attn
        ↓
    Add & Norm
        ↓
Encoder-Decoder Multi-Head Attn
        ↓
    Add & Norm
        ↓
       FFN
        ↓
    Add & Norm
```

### Full pipeline (seq2seq):
```
Source Tokens -> Encoder -> Context
                              ↓
Decoder (masked + cross-attn) -> Linear -> Softmax -> Output Tokens
```

---

## 10. Real-world practical examples (short walkthroughs)

### Example A — Customer Support Intent (short)
User: "I want to return the phone I bought yesterday because it is damaged."
- **Encoder** encodes: return, phone, yesterday, damaged, pronoun linking (it→phone).
- **Decoder** (for reply): masked self-attn ensures autoregressive generation; cross-attn focuses on "return" and "damaged" to generate "I'm sorry — we can process a return for the phone."

### Example B — E-commerce Search Query
Query: "Show me blue shoes under 1500 not sports."
- Encoder extracts filters: item=shoes, color=blue, price<1500, exclude=sports.
- Downstream model uses these embeddings to query DB or generate SQL-like search query.

### Example C — Translation (engl -> hindi)
Input: "I love Python"
- Encoder: contextual embeddings capturing pronoun, verb, object
- Decoder generation steps (example):
  1. predict "मैं" (attend to "I")
  2. predict "Python" (attend to "Python")
  3. predict "पसंद करता हूँ" (attend to "love")

---

## 11. Short checklist to remember (memory hooks)
- Attention = Q K^T / sqrt(dk) → softmax → × V
- Multi-head = parallel attention + concat + linear
- PosEnc = add order info (sin/cos) or RoPE/ALiBi variants
- FFN = 2-layer MLP on each position
- Norm + Residual = stable deep learning
- Decoder mask = prevent future token access
- Cross-attn = Q from decoder, K/V from encoder
- Linear + Softmax = token probabilities

---

## 12. Common variants & modern additions (short)
- **BERT:** encoder-only (masked language modeling) — great for classification and embeddings.
- **GPT:** decoder-only (autoregressive) — great for generation.
- **T5 / BART:** encoder-decoder (seq2seq) — flexible for many tasks.
- **RoPE / ALiBi:** positional alternatives for long contexts.
- **Flash attention / Sparse / Linear attention:** efficient attention implementations for long sequences.

---

## 13. Practical exercises (do these to cement learning)
1. Manual attention calculation: pick 3 tokens, compute tiny Q/K/V and do attention math by hand.
2. Visualize attention: run a small transformer (HuggingFace) and plot attention weights for a sentence.
3. Build a mini-encoder with PyTorch or TensorFlow for a toy dataset (1-2 layers) and observe outputs.
4. Implement causal mask and run generation loop on small vocab.
5. Tokenization experiment: compare BPE vs WordPiece on words with rare morphology.

---

## 14. One-page cheat sheet (compact)
- **Attention:** `softmax(QK^T / sqrt(dk)) V`
- **MHA:** `Concat(head1..headh) W_O`
- **FFN:** `W2(ReLU(W1 x + b1)) + b2`
- **PE:** sinusoidal formula above
- **Masking:** triangular matrix + padding mask
- **Flow:** Embedding+PE → (N × EncoderLayer) → EncoderOut → DecoderWithMasks → Linear → Softmax

---

## 15. Recommended commands & Hugging Face quickstart (mini)
- Install: `pip install transformers datasets tokenizers accelerate sentence-transformers faiss-cpu`
- Quick inference example (python):
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "t5-small"
 tok = AutoTokenizer.from_pretrained(model_name)
 model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

 input_text = "translate English to German: I love machine learning."
 inputs = tok(input_text, return_tensors="pt")
 out = model.generate(**inputs, max_length=40)
 print(tok.decode(out[0], skip_special_tokens=True))
```

---

## 16. Additional study plan (next steps)
1. **Tokenization**: BPE / WordPiece / SentencePiece experiments
2. **Hugging Face** usage: load, fine-tune, save, and serve models
3. **Embeddings & RAG**: create embeddings, index with FAISS, build a tiny RAG pipeline
4. **Fine-tuning tricks**: LoRA, QLoRA, mixed precision
5. **Attention variants**: read about Flash attention and RoPE

---

## 17. Definitions (Glossary)
- **Attention:** mechanism to compute relevance of tokens.
- **Self-Attention:** attention where Q/K/V come from same source.
- **Masked Attention:** attention with causal mask to hide future tokens.
- **Multi-Head:** multiple attention units to capture varied relations.
- **Positional Encoding:** vector added to embeddings to supply positional info.
- **Residual Connection:** add input to sublayer output, helps gradients.
- **LayerNorm:** normalize per-token features to stabilize training.
- **FFN:** position-wise MLP for extra non-linearity.
- **Encoder:** stack of layers that encode input to context vectors.
- **Decoder:** stack of layers that autoregressively generate outputs using encoder context.

---

## 18. Quick memory anchors (mnemonics)
- **QKV** → Query = question, Key = index, Value = content
- **MHA** → Many minds (heads) thinking in parallel
- **PE** → Position + Embedding = order
- **FFN** → Feed the Focused Node

---

## 19. If you want, I will also:
- create a printable PDF version of this README
- create a one-page A4 flashcard (pdf)
- produce a small Jupyter notebook with code examples

---

> Open this file when you need a refresher. If you want diagrams converted to images or a notebook added, tell me and I will add it to this same document.

## 20. Transformer Family Comparison (BERT vs GPT vs T5)
| Model | Architecture | Use Case | Strength |
|-------|--------------|----------|----------|
| **BERT** | Encoder-only | Classification, embeddings | Deep understanding, context-rich |
| **GPT** | Decoder-only | Text generation | Long, fluent generation |
| **T5** | Encoder–Decoder | Translation, summarization, Q&A | Flexible text-to-text framework |
| **BART** | Encoder–Decoder | Summarization | Strong denoising + seq2seq |

## 21. Attention Heatmap (ASCII Visual)
Example sentence: "The dog chased the cat"
```
Token →  The   dog   chased   the   cat
The      ████  ██    ░░░░     ██    ░░
dog      ██    ████  ████     ░░    ░░
chased   ░░    ████  ███████  ░░    ████
the      ██    ░░    ░░░░     ████  ░░
cat      ░░    ░░    ████     ░░    ████
```
- Darker = higher attention weight.
- Shows subject–verb–object relationships.

## 22. Advanced Concepts (Modern Transformers)
### 🔹 RoPE (Rotary Positional Embeddings)
- Used in LLaMA, GPT-NeoX.
- Encodes relative positions using rotation in embedding space.

### 🔹 ALiBi (Attention Linear Bias)
- Removes positional encoding.
- Adds distance-aware bias directly to attention.
- Helps long-context models.

### 🔹 FlashAttention
- Memory-efficient and faster attention algorithm.
- Used in modern LLMs to speed up training & inference.

### 🔹 Multi-Query Attention (MQA)
- Single K/V per head set.
- Faster for large decoder-only models.
- Used in PaLM, LLaMA-2.

## 23. One-Page Interview Quick Sheet (Ultra-Compact)
```
ATTENTION = softmax(QK^T / sqrt(dk)) V
MULTI-HEAD = many attentions → concat → linear
ENCODER = Self-Attn + FFN (×N)
DECODER = Masked Self-Attn + Cross-Attn + FFN (×N)
MASKING = prevents future token access
POSITION = Sin/Cos or RoPE/ALiBi
GENERATION = Linear → Softmax → Next token
```

## 24. Improvements Added
- Added modern architectures (RoPE, ALiBi, FlashAttn)
- Added Transformer model comparison
- Added ASCII attention heatmap
- Added interview quick sheet
- Added deeper technical insights

*— End of Transformers_README_Hemant.md —*

