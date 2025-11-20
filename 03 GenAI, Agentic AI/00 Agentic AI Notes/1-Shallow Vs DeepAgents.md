# Shallow Agents vs Deep Agents&#x20;

---

## 🔵 1. What Are Agents?

An **Agent** is a system that:

- observes an environment
- thinks
- acts
- repeats the cycle

Agents can use tools, plan tasks, and execute steps to achieve goals.

---

## 🟢 2. Shallow Agents

### **Definition**

A **shallow agent** performs tasks in a **simple and single‑step** manner. It does not think deeply or plan.

### **Characteristics**

- Short reasoning
- One-step tool use
- No planning
- No recursion
- No memory
- Low autonomy

### **Examples**

- Weather API agent
- Currency converter agent
- Simple RAG QA agent
- Calculator agent

### **ASCII Diagram: How a Shallow Agent Works**

```
User Input → [Shallow Agent] → Single Action → Output
```

```
+-------------+     +---------------+     +-----------+
|   User      | --> | Shallow Agent | --> |  Result   |
+-------------+     +---------------+     +-----------+
```

---

## 🔴 3. Deep Agents

### **Definition**

A **deep agent** performs **multi-step reasoning**, **plans**, **self-corrects**, and can coordinate multiple tools or sub-agents.

### **Characteristics**

- Multi-step reasoning
- Planning + reflection
- Multiple tool calls
- Memory / state awareness
- Error correction
- High autonomy

### **Examples**

- Autonomous coding agent
- AI researcher agent
- Multi-agent workflows (LangGraph)

### **ASCII Diagram: How a Deep Agent Works**

```
User Input
     ↓
+----------------+
|  Deep Agent    |
+----------------+
     ↓
[Observe]
     ↓
[Think]
     ↓
[Plan]
     ↓
[Act using tools]
     ↓
[Evaluate]
     ↓
[Revise Plan]
     ↓
Repeat until Goal Achieved
```

```
+-------------+
|   User      |
+-------------+
       ↓
+---------------------+
|     Deep Agent      |
|  (Plan → Act → Fix) |
+---------------------+
       ↓
+-------------+
|   Output    |
+-------------+
```

---

## 🔵 4. Difference Table

| Feature    | Shallow Agent | Deep Agent           |
| ---------- | ------------- | -------------------- |
| Reasoning  | 1–2 steps     | Multi-step           |
| Planning   | No            | Yes                  |
| Tool Usage | Single        | Multiple + recursive |
| Autonomy   | Low           | High                 |
| Memory     | None          | Present              |
| Complexity | Simple        | Complex              |

---

## 🟣 5. Real Life Examples

### **Shallow Agent Example**

User: "What is the weather in Mumbai?"

- Agent calls weather API → returns result.

### **Deep Agent Example**

User: "Build me a website and deploy it."

- Agent:
  - plans folder structure
  - writes code
  - fixes errors
  - builds project
  - deploys to Vercel
  - returns URL

---

## 🟠 6. Why Deep Agents Matter

Deep agents enable:

- AI workers
- Auto Research
- Auto Debugging
- Pipeline Orchestration
- Fully autonomous workflows
- Multi-agent collaboration

Used in:

- LangChain
- LangGraph
- CrewAI
- LlamaIndex

---

##

---

##

