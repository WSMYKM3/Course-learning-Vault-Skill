# buildObsidian 规范

本文件用于规范把《Machine Learning and AI with Python》课程脚本转换为 Obsidian 笔记的统一方式。目标不是简单转录，而是构建一个适合复习、可链接、可在 Graph View 中形成知识网络的中文笔记系统。

## 1. 总体目标

- 输出语言以中文为主。
- 关键课程术语必须在首次出现时写成 `中文（English）`。
- 笔记要适合 Obsidian 使用，包括：
  - 可读的 Markdown 结构
  - 可在 Graph View 中显示的双链节点
  - 可复习的学习笔记形态
- 原始 `.txt` 脚本不修改，只新增 `.md` 文件。

## 2. 目录结构

所有 Obsidian 文件统一放在 `ObsidianNotes/` 下：

```text
ObsidianNotes/
  Terms/
  Formulas/
  1.1.3 - 决策树分割标准.md
  1.2 - 决策树停止条件与生长策略.md
```

规则：

- `Terms/`：术语节点
- `Formulas/`：公式节点
- 根目录：课程章节主笔记

## 3. 章节主笔记规范

每一节课生成一个主笔记，命名格式为：

```text
章节号 - 中文主题.md
```

例如：

```text
1.2 - 决策树停止条件与生长策略.md
```

主笔记必须包含：

1. YAML frontmatter
2. 一级标题
3. `Graph View 节点` 区块
4. 学习目标
5. 核心内容整理
6. 复习检查
7. 复习检查参考答案
8. 一句话总结

### 3.1 Frontmatter 模板

```yaml
---
course: "Machine Learning and AI with Python"
provider: "HarvardX CS109xa"
chapter: "1.2"
topic: "中文主题"
type: lesson-note
tags:
  - machine-learning
  - artificial-intelligence
  - python
source: "原始 txt 文件名"
---
```

### 3.2 标题格式

标题格式统一为：

```md
# 1.2 中文主题（English Topic）
```

## 4. 术语节点规范

凡是会在后续章节重复出现、值得单独索引、适合在 Graph View 中形成网络的概念，都应创建术语节点。

术语节点放在 `ObsidianNotes/Terms/` 中，文件名格式为：

```text
中文术语 (English Term).md
```

例如：

```text
最大深度 (Maximum Depth).md
偏差方差权衡 (Bias-Variance Tradeoff).md
```

术语节点必须包含：

- frontmatter
- 标题
- 1 到 3 句简短定义
- 相关概念链接
- 必要时链接回课程章节

模板：

```yaml
---
type: term
course: "Machine Learning and AI with Python"
term_cn: "中文术语"
term_en: "English Term"
tags:
  - term
---
```

```md
# 中文术语（English Term）

简短定义。

相关概念：[[另一个术语 (Another Term)]]
```

## 5. 公式节点规范

公式类内容必须单独创建公式节点，以便 Graph View 中不只是连到章节，也能连到具体公式。

公式节点放在 `ObsidianNotes/Formulas/` 中，文件名格式为：

```text
中文公式名 (English Formula Name).md
```

例如：

```text
熵公式 (Entropy Formula).md
不纯度下降公式 (Impurity Decrease Formula).md
```

公式节点必须包含：

- frontmatter
- 标题
- 独立展示的 LaTeX 公式
- 公式含义说明
- 至少一个紧贴公式的具体计算例子
- 相关术语链接

模板：

```yaml
---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "中文公式名"
formula_en: "English Formula Name"
tags:
  - formula
---
```

公式节点正文推荐结构：

```md
# 中文公式名（English Formula Name）

$$
\text{公式}
$$

含义：解释公式中每个主要符号的含义，以及它在课程中的作用。

例子：给出一组小数字，直接代入公式并算出结果。例子应放在公式说明之后、相关术语之前。

相关术语：[[相关术语 (Related Term)]]
```

公式例子要求：

- 每个公式节点的公式下方必须有 `例子：` 段落。
- 例子要能直接帮助复习者看懂公式如何使用，不只写抽象描述。
- 分类公式优先使用类别比例或类别计数作为例子。
- 回归公式优先使用 3 到 5 个小样本数值作为例子。
- 如果公式涉及分裂前后比较，例子要同时给出父区域与子区域的计算结果。

## 6. 双链规范

为了让 Graph View 有实际价值，主笔记中不能只写普通文本，必须把核心概念和核心公式写成双链。

推荐做法：

- 在章节开头增加 `Graph View 节点` 区块，集中列出本节核心术语和公式。
- 在正文中，首次出现的重要术语使用双链。
- 如果某个公式在正文中是重点，增加一行：

```md
公式节点：[[熵公式 (Entropy Formula)]]
```

链接格式规则：

- 显示中文时使用别名语法：

```md
[[最大深度 (Maximum Depth)|最大深度]]
```

- 如果希望直接显示完整术语名，则写：

```md
[[最大深度 (Maximum Depth)]]
```

## 7. 内容整理规则

章节主笔记不是逐句字幕稿，必须整理成学习笔记。

要求：

- 去除口语化重复表达
- 修正明显转写错误
- 保留原课程逻辑
- 用更适合复习的结构表达

允许的整理方式：

- 重组段落顺序，使逻辑更清晰
- 补出隐含标题
- 用表格对比概念
- 用简洁语言解释例子

不允许的做法：

- 擅自引入与课程无关的大量外部内容
- 把课程概念翻译成与常见机器学习术语不一致的中文
- 只保留英文不写中文

## 7.1 复习检查与答案规则

每篇章节主笔记中的 `复习检查` 不能只给问题，还必须紧接着提供一组简洁的参考答案，便于自测后立即核对。

推荐结构：

```md
## 复习检查

1. 问题一
2. 问题二

## 复习检查参考答案

1. 答案一
2. 答案二
```

要求：

- 答案要简洁，但必须能直接回答问题。
- 优先使用课程中的原始逻辑和术语，不额外展开成冗长讲义。
- 如果问题是“为什么”，答案至少要交代因果关系，而不是只重复题干关键词。
- 如果问题涉及多个概念对比，答案中要明确点出差异。

## 8. 术语语言规则

最终输出必须是中文主导，但术语必须补英文。

统一规则：

- 首次出现：`中文术语（English Term）`
- 后续重复：可以只写中文
- 术语节点文件名：`中文术语 (English Term).md`
- 英文应优先使用机器学习领域常见标准表达

例如：

- 决策树（Decision Tree）
- 偏差方差权衡（Bias-Variance Tradeoff）
- 交叉验证（Cross-Validation）

## 9. 公式书写规则

公式必须使用 Obsidian 兼容的 LaTeX：

- 行内公式：`$...$`
- 独立公式：`$$...$$`

不要使用 Obsidian 不兼容的公式格式。

如果课程中只隐含给出公式、但上下文足以明确其标准写法，可以补出标准形式，但不能随意发明非标准定义。

## 10. 节点创建判断标准

满足以下任一条件，应创建术语或公式节点：

- 会在多个章节复用
- 是课程核心概念
- 会出现在复习题中
- 适合被单独搜索
- 对 Graph View 有明显价值

反之，不需要把每个普通名词都做成节点。

## 11. 每节转换后的最低验收标准

每一节完成后都要检查：

- 已生成对应章节 `.md`
- 原始 `.txt` 未被修改
- 主笔记有 frontmatter
- 主笔记有 `Graph View 节点` 区块
- 核心术语已补英文
- 核心公式已使用 LaTeX
- 主笔记已连接到相关 `Terms/` 和 `Formulas/` 节点
- `复习检查` 下方有 `复习检查参考答案`
- 笔记内容适合复习，不是简单逐句转录

## 12. 推荐工作流

处理新章节时按以下顺序：

1. 阅读原始 `.txt`
2. 提炼主题与核心概念
3. 检查已有 `Terms/` 与 `Formulas/` 是否可复用
4. 为新增概念创建节点
5. 编写章节主笔记
6. 加入双链与公式节点链接
7. 自查 Graph View 连接是否足够

## 13. 当前项目默认约定

- 课程名固定为 `Machine Learning and AI with Python`
- 输出目录固定为 `ObsidianNotes/`
- 输出以中文为主
- 术语必须补英文
- 优先构建“可复习的课程知识库”，而不是“字幕存档”
