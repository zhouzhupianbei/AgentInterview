#!/usr/bin/env node
/**
 * 调用 GPT-4o API 优化面试题内容
 * 将内容细分为三级结构：主题 → 子主题 → 详细知识点
 */

const axios = require('axios');

const API_KEY = 'sk-LMcfIOfRJTGt9bS1FzA89E5RuHDCHs5zh5SygxrVRwTifQ9z';
const BASE_URL = 'https://api.llms.best/v1';

/**
 * 优化面试题结构
 * @param {string} topic - 面试主题
 * @param {Array} articles - 相关文章列表
 * @param {string} existingContent - 现有内容
 */
async function optimizeInterviewQuestion(topic, articles, existingContent = '') {
  const prompt = buildPrompt(topic, articles, existingContent);
  
  try {
    const response = await axios.post(
      `${BASE_URL}/chat/completions`,
      {
        model: 'gpt-4o',
        messages: [
          {
            role: 'system',
            content: `你是一位资深 AI 技术面试官和内容创作专家。你的任务是将面试题内容优化为三级结构，让知识点更易于吸收和学习。

三级结构定义：
- Level 1 主题：大的知识领域（如：Transformer 架构）
- Level 2 子主题：具体的技术点（如：Self-Attention 机制）
- Level 3 详细知识点：可独立学习的原子知识点（如：Q/K/V 矩阵的含义和计算）

输出要求：
1. 每个 Level 3 知识点必须是独立的、可消化的学习单元
2. 包含：核心概念、常见面试题、参考答案、代码示例（如适用）
3. 难度标注：⭐基础 ⭐⭐进阶 ⭐⭐⭐高级
4. 关联微信文章中的实战案例
5. 输出格式为 Markdown，便于直接整合到文档`
          },
          {
            role: 'user',
            content: prompt
          }
        ],
        temperature: 0.7,
        max_tokens: 4000
      },
      {
        headers: {
          'Authorization': `Bearer ${API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('GPT-4o API 调用失败:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * 构建 Prompt
 */
function buildPrompt(topic, articles, existingContent) {
  const articlesText = articles.map((article, i) => 
    `${i + 1}. ${article.title}\n   来源：${article.source}\n   时间：${article.date_text}\n   摘要：${article.summary}\n   链接：${article.url}`
  ).join('\n\n');
  
  return `请基于以下资料，优化"${topic}"相关的面试题内容：

## 参考微信文章（${articles.length}篇）
${articlesText}

${existingContent ? `## 现有内容\n${existingContent}\n` : ''}

## 任务要求

1. **梳理知识结构**
   - 识别 Level 1 主题（2-4 个）
   - 每个主题下分 Level 2 子主题（3-5 个）
   - 每个子主题下分 Level 3 知识点（5-10 个）

2. **为每个 Level 3 知识点编写**：
   - 📖 核心概念（100-200 字，通俗易懂）
   - ❓ 常见面试题（2-3 道，从基础到进阶）
   - ✅ 参考答案要点（结构化，便于记忆）
   - 💻 代码示例（如适用，简洁明了）
   - 🔗 关联文章（引用微信文章中的实战案例）
   - 📊 难度标注（⭐/⭐⭐/⭐⭐⭐）

3. **输出格式**：
\`\`\`markdown
## [Level 1] 主题名称

### [Level 2] 子主题 1

#### [Level 3] 知识点 1.1 ⭐
**📖 核心概念**
...

**❓ 常见面试题**
1. 问题 1
2. 问题 2

**✅ 参考答案要点**
- 要点 1
- 要点 2

**💻 代码示例**
\`\`\`python
# 示例代码
\`\`\`

**🔗 关联文章**
- [文章标题](链接)

---

#### [Level 3] 知识点 1.2 ⭐⭐
...
\`\`\`

请开始优化内容：`;
}

/**
 * 生成面试题库汇总
 */
async function generateQuestionBank(articlesByCategory) {
  const prompt = `
你是一位资深 AI 技术面试官，请基于以下分类文章生成完整的面试题库：

${Object.entries(articlesByCategory).map(([category, articles]) => `
## ${category} 相关文章（${articles.length}篇）
${articles.map((a, i) => `${i+1}. ${a.title} - ${a.source}`).join('\n')}
`).join('\n')}

## 任务

生成完整的面试题库，包含：

1. **分类结构**
   - 基础题（⭐）：20 道
   - 进阶题（⭐⭐）：15 道
   - 高级题（⭐⭐⭐）：10 道
   - 实战题（项目设计）：5 道

2. **每道题包含**：
   - 题目
   - 考察知识点
   - 参考答案要点（3-5 点）
   - 难度标注
   - 关联文章

3. **输出 Markdown 格式**，便于直接整合到 docs/04-面试题库.md
`;

  try {
    const response = await axios.post(
      `${BASE_URL}/chat/completions`,
      {
        model: 'gpt-4o',
        messages: [
          {
            role: 'system',
            content: '你是一位资深 AI 技术面试官，擅长设计结构清晰、考察全面的面试题库。'
          },
          {
            role: 'user',
            content: prompt
          }
        ],
        temperature: 0.7,
        max_tokens: 8000
      },
      {
        headers: {
          'Authorization': `Bearer ${API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('GPT-4o API 调用失败:', error.response?.data || error.message);
    throw error;
  }
}

// 命令行支持
if (require.main === module) {
  const args = process.argv.slice(2);
  const command = args[0];
  
  if (command === 'optimize' && args[1]) {
    const topic = args[1];
    const articlesFile = args[2];
    
    const fs = require('fs');
    const articles = JSON.parse(fs.readFileSync(articlesFile, 'utf-8')).articles;
    
    optimizeInterviewQuestion(topic, articles)
      .then(result => {
        console.log(result);
        // 保存到文件
        const outputFile = args[3] || `optimized-${topic.replace(/\s+/g, '-')}.md`;
        fs.writeFileSync(outputFile, result);
        console.log(`\n✅ 已保存到：${outputFile}`);
      })
      .catch(err => {
        console.error('执行失败:', err.message);
        process.exit(1);
      });
  } else if (command === 'generate-bank') {
    const articlesFile = args[1];
    const fs = require('fs');
    const allArticles = JSON.parse(fs.readFileSync(articlesFile, 'utf-8'));
    
    generateQuestionBank(allArticles)
      .then(result => {
        console.log(result);
        const outputFile = args[2] || 'question-bank.md';
        fs.writeFileSync(outputFile, result);
        console.log(`\n✅ 已保存到：${outputFile}`);
      })
      .catch(err => {
        console.error('执行失败:', err.message);
        process.exit(1);
      });
  } else {
    console.log(`
用法:
  node gpt4o-interview-optimizer.js optimize <主题> <文章 JSON 文件> [输出文件]
  node gpt4o-interview-optimizer.js generate-bank <汇总文章 JSON 文件> [输出文件]

示例:
  node gpt4o-interview-optimizer.js optimize "Vibe Coding" memory/wechat-vibecoding.json
  node gpt4o-interview-optimizer.js generate-bank memory/wechat-articles.json
`);
  }
}

module.exports = { optimizeInterviewQuestion, generateQuestionBank };
