# 01-AIGC 基础

> AIGC（AI Generated Content）核心概念、主流模型与技术基础

---

## 1.1 什么是 AIGC

**AIGC**（AI Generated Content）指利用人工智能技术自动生成内容的生产方式。

### 发展历程

```
PGC (专业生产) → UGC (用户生产) → AIGC (AI 生产)
```

### 核心能力

- 📝 **文本生成**：文章、代码、诗歌、剧本
- 🎨 **图像生成**：插画、设计图、照片级图像
- 🎬 **视频生成**：短视频、动画、特效
- 🎵 **音频生成**：音乐、语音、音效
- 💻 **代码生成**：函数、模块、完整应用

---

## 1.2 Transformer 架构详解

### 核心结构

```
输入 → Embedding → Positional Encoding → Encoder/Decoder → Output
                        ↓
                   Multi-Head Attention
                        ↓
                   Add & Norm
                        ↓
                   Feed Forward
                        ↓
                   Add & Norm
```

### 关键组件

#### 1. Self-Attention

```python
# Attention(Q, K, V) = softmax(QK^T / √d_k) V
def attention(query, key, value, mask=None):
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = F.softmax(scores, dim=-1)
    return torch.matmul(p_attn, value), p_attn
```

**面试考点**：
- 为什么需要除以 √d_k？ → 防止梯度消失
- Q/K/V 分别代表什么？ → Query/Key/Value
- Self-Attention 的复杂度？ → O(n²)

#### 2. Multi-Head Attention

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        self.num_heads = num_heads
        self.d_head = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
```

**优势**：
- 并行学习多个子空间的信息
- 增强模型的表达能力

#### 3. Position Encoding

**常见方案**：
- 正弦/余弦位置编码（原始 Transformer）
- 学习型位置编码（BERT）
- RoPE（RoPE，LLaMA 采用）
- ALiBi（长度外推更好）

---

## 1.3 主流大模型对比

| 模型 | 机构 | 特点 | 应用场景 |
|------|------|------|----------|
| **GPT-4** | OpenAI | 最强综合能力，多模态 | 通用对话、代码、推理 |
| **Claude 3** | Anthropic | 长上下文，安全性高 | 长文档分析、安全敏感场景 |
| **LLaMA 3** | Meta | 开源，生态丰富 | 研究、微调、私有化部署 |
| **Qwen2.5** | 阿里 | 中文能力强，多语言 | 中文应用、多语言场景 |
| **Gemini** | Google | 原生多模态 | 多模态理解、Google 生态 |
| **Mistral** | Mistral AI | 高效，小参数高性能 | 资源受限场景 |

### 选择建议

```
追求效果 → GPT-4 / Claude 3
成本敏感 → LLaMA 3 / Qwen2.5 微调
中文场景 → Qwen2.5 / ChatGLM
私有部署 → LLaMA 3 / Qwen2.5
多模态 → Gemini / GPT-4V
```

---

## 1.4 Tokenization 技术

### 常见方法

#### 1. BPE (Byte Pair Encoding)

**原理**：从字符开始，反复合并最频繁的 pair

```python
# 示例
原始：["hug", "pun", "bug"]
步骤 1: h-u-g, p-u-n, b-u-g (u 最常见)
步骤 2: hu-g, pu-n, bu-g (ug 最常见)
结果：h, u, g, ug, p, n, b, hu, pu, bu
```

**使用模型**：GPT 系列、LLaMA

#### 2. WordPiece

**原理**：类似 BPE，但基于 likelihood 选择 merge

**使用模型**：BERT、ViT

#### 3. SentencePiece

**特点**：
- 将输入视为原始字节流
- 支持 subword 和 character 级别
- 无需预分词

**使用模型**：T5、LLaMA

---

## 1.5 位置编码详解

### RoPE (Rotary Position Embedding)

**核心思想**：通过旋转矩阵编码相对位置

```python
import torch

def rotate_half(x):
    x1, x2 = x[..., : x.shape[-1] // 2], x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=-1)

def apply_rope(q, k, cos, sin):
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed
```

**优势**：
- 天然支持相对位置
- 长度外推性好
- 计算高效

**采用模型**：LLaMA、Qwen、PaLM

---

## 1.6 大模型训练流程

```
数据收集 → 数据清洗 → Tokenization → 预训练 → SFT → RLHF → 部署
```

### 1. 预训练 (Pre-training)

**目标**：Next Token Prediction

**损失函数**：
```python
loss = -log(P(token_t | token_1, ..., token_{t-1}))
```

**数据规模**：
- LLaMA 2: 2T tokens
- GPT-3: 300B tokens
- Qwen2.5: 7T tokens

### 2. 监督微调 (SFT)

**目标**：指令遵循

**数据格式**：
```json
{
  "instruction": "解释量子纠缠",
  "input": "",
  "output": "量子纠缠是..."
}
```

### 3. 人类反馈强化学习 (RLHF)

**步骤**：
1. 收集人类偏好数据（对比模型输出）
2. 训练 Reward Model
3. PPO 优化策略

---

## 1.7 常见面试问题

### Q1: Transformer 为什么比 RNN 好？

**参考答案**：
1. **并行化**：Transformer 可并行计算所有位置，RNN 必须顺序
2. **长距离依赖**：Self-Attention 直接建模任意距离依赖
3. **梯度流动**：更短的路径，梯度消失问题更轻

### Q2: LayerNorm 的作用是什么？

**参考答案**：
- 稳定训练，加速收敛
- 减少内部协变量偏移
- 使模型对初始化不敏感
- 位置：通常在每个子层前后（Pre-LN / Post-LN）

### Q3: 如何解决长序列问题？

**参考答案**：
1. **注意力优化**：Sparse Attention、Linear Attention、FlashAttention
2. **位置编码改进**：RoPE、ALiBi、NTK-aware 插值
3. **架构改进**：RWKV（RNN+Transformer）、Mamba（状态空间模型）
4. **上下文压缩**：Retrieval、Summary

---

## 1.8 实战建议

### 动手项目

1. **从零实现 Transformer**
   - 参考：The Annotated Transformer
   - 目标：能跑通翻译任务

2. **微调 LLaMA**
   - 工具：LoRA、QLoRA
   - 平台：Colab / Kaggle / 本地 GPU

3. **构建简单 RAG 系统**
   - 向量库：Chroma / FAISS
   - Embedding：sentence-transformers
   - LLM：OpenAI API / 本地模型

---

## 📚 延伸阅读

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [LLaMA 论文](https://arxiv.org/abs/2302.13971)
- [RoPE 论文](https://arxiv.org/abs/2104.09864)
- [WeThinkIn/AIGC-Interview-Book - 大模型基础](https://github.com/WeThinkIn/AIGC-Interview-Book/tree/main/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9F%BA%E7%A1%80)

---

**下一章**：[02-Agent 架构.md](./02-Agent 架构.md)
