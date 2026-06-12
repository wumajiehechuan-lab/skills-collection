# Skills Collection — AI Agent 技能集

> 个人收藏的 AI Agent skills 备份，适用于 Claude Code、Codex CLI 等支持 skill 机制的 AI 编程 Agent。
>
> 仓库地址：https://github.com/wumajiehechuan-lab/skills-collection

---

## 📋 总览

| 分类 | 技能数 | 说明 |
|------|:------:|------|
| 🚀 **创业与产品** | 11 | 极简主义创业者九步流程全套技能 |
| 📝 **内容创作** | 3 | 公众号写作、播客脚本生成 |
| 🎨 **设计 & PPT** | 6 | PPT 生成、前端 Slides、设计评审 |
| 🔧 **开发工具** | 6 | 代码审查、仓库分析、任务派发、自我改进等 |
| 🔍 **搜索 & 调研** | 2 | Tavily 搜索、横纵分析研究 |
| 📧 **其他** | 2 | AgentMail 邮件、技能发现 |

---

## 一、🚀 创业与产品 — slavingia-skills

本组技能基于 Sahil Lavingia 的《极简主义创业者》（Minimalist Entrepreneur），提供完整的创业流程引导。每个技能都有 **中文版（SKILL_CN.md）** 和 **英文版（SKILL.md）**。

| # | 技能 | 说明 |
|:-:|------|------|
| 🏠 | **minimalist-entrepreneur** | **主入口**。评估你的创业阶段，按九步流程引导推进 |
| 1 | **find-community** | 发现并评估适合构建极简业务的社区 |
| 2 | **validate-idea** | 用极简创业框架验证商业想法 |
| 3a | **processize** | 将想法转化为可手动交付的流程 |
| 3b | **mvp** | 以手动优先的方式构建最小可行产品 |
| 4 | **first-customers** | 制定策略获取第一批 100 个客户 |
| 5 | **pricing** | 用极简创业者原则为产品或服务定价 |
| 6 | **marketing-plan** | 创建极简营销计划，通过内容建立受众 |
| 7 | **grow-sustainably** | 以可持续、盈利增长的视角评估商业决策 |
| 8 | **company-values** | 为极简业务定义公司价值观和文化 |
| 9 | **minimalist-review** | 审查商业决策、计划或策略，对标极简创业者框架 |

**工作流预览：**
```
[1] 发现社区 → [2] 验证想法 → [3a] 流程化
                                 ↓
                            [3b] MVP
                                 ↓
[9] 极简审查 ← [8] 公司价值观 ← [7] 可持续增长 ← [6] 营销计划 ← [5] 定价 ← [4] 首批客户
```

---

## 二、📝 内容创作

### 播客脚本

| 技能 | 说明 |
|------|------|
| **story-podcast-script-generator** | AI 驱动的播客脚本生成器，基于用户提供的主题、风格和参考生成结构化播客脚本 |
| **Podcast Script Generator** | 播客脚本生成器（另一版本） |

### 公众号写作

| 技能 | 说明 |
|------|------|
| **khazix-writer** | 数字生命卡兹克公众号长文写作 skill。适用场景：写稿、续写、扩写、公众号文章、根据素材产出长文。支持 PDF、链接、语音转文字等素材输入 |

---

## 三、🎨 设计 & PPT

### PPT 生成

| 技能 | 说明 |
|------|------|
| **ppt-preflight** | PPT 前期策划与需求澄清。当用户想做 PPT 但只有模糊想法时使用，梳理大纲、结构、风格定位 |
| **guizang-ppt-skill** | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、章节幕封、数据大字报、图片网格等模板。支持「电子杂志 × 电子墨水」和「科技简洁 × 霓虹字效」两种风格 |
| **huashu-design-master** | 花叔 Design — 用 HTML 做高保真原型、交互 Demo、幻灯片、动画、设计变体探索 + 设计方向顾问 + 专家评审 |
| **ppt-master-main** | 大型 PPT 设计技能集，包含 1400+ 图标库、多种布局模板、品牌主题、图表模板。附 15+ 完整设计案例 |

### 前端设计 & Slides

| 技能 | 说明 |
|------|------|
| **frontend-slides** | 从零创建动画丰富的 HTML 演示文稿，或将现有文档/PPT 转为前端 Slides |
| **web-design-engineer** | Web 设计工程师 skill，专注于网站/落地页的 HTML/CSS/JS 实现 |
| **gpt-image-2** | AI 图像生成和优化 skill |
| **web-video-presentation** | 网页视频演示制作 skill |
| **kb-retriever** | 知识库检索 skill |

---

## 四、🔧 开发工具

| 技能 | 说明 |
|------|------|
| **oh-my-opencode-1.0.0** | OpenCode 多智能体编排插件。用于安装 oh-my-opencode 扩展，管理多 agent 协作 |
| **repo-analysis** | 以工程师视角阅读、解释和评估软件仓库或 GitHub 项目 |
| **skill-vetter** | AI Agent 技能安全审查。在从 ClawHaus 安装任何 skill 之前使用，检查安全性 |
| **skill-creator-0.1.0** | 创建有效技能的指南。当用户想创建新的 SKILL.md 时使用 |
| **self-improving-agent** | 捕获经验、错误和修正以支持持续改进。用于总结会话经验 |
| **task-dispatch** | 三省六部任务派发专用技能。当 agent 需要派发任务给其他 agent 时使用，创建并追踪 JJC 任务进度 |

---

## 五、🔍 搜索 & 调研

| 技能 | 说明 |
|------|------|
| **tavily-search** | Tavily AI 搜索 API — 为 AI Agent 优化的搜索引擎。当搜索实时信息、新闻、数据时使用 |
| **hv-analysis** | 横纵分析法（Horizontal-Vertical Analysis）深度研究 Skill。双轴分析：纵轴追踪产品/公司的完整生命历程，横轴与竞品进行横向对比，交叉产出独到洞察，最终产出一份排版精美的 PDF 研究报告 |

---

## 六、📧 其他

| 技能 | 说明 |
|------|------|
| **agentmail-1.1.1** | 面向 AI Agent 的 API-first 邮件平台。创建和管理专用邮件地址，发送/接收/搜索邮件 |
| **find-skills** | 帮助用户发现和安装 Agent 技能。当用户问"怎么做 X"时，匹配并推荐合适的 skill |
| **video-spec-builder** | 视频规格构建工具。通过苏格拉底式追问收敛需求，生成分镜脚本、节奏图、字幕方案等全套视频制作文档 |

---

## 目录结构

```
skills-collection/
├── README.md                    ← 本文件
├── slavingia-skills-Claude技能集/  ← 创业技能集（11个技能）
│   └── skills/
│       ├── minimalist-entrepreneur/
│       ├── find-community/
│       ├── validate-idea/
│       └── ...
├── 设计/                         ← 设计 & PPT 技能
│   ├── ppt-preflight/
│   ├── guizang-ppt-skill/
│   ├── huashu-design-master/
│   ├── ppt-master-main/
│   ├── frontend-slides/
│   └── garden-skills/
├── 播客/                         ← 播客创作技能
│   ├── story-podcast-script-generator/
│   └── Podcast Script Generator/
├── agentmail-1.1.1/             ← AI Agent 邮件
├── find-skills/                 ← 技能发现
├── hv-analysis/                 ← 横纵分析研究
├── khazix-writer/               ← 公众号写作
├── oh-my-opencode-1.0.0/        ← OpenCode 多智能体
├── ppt-preflight/               ← PPT 前期策划
├── repo-analysis/               ← 仓库分析
├── self-improving-agent/        ← 自我改进
├── skill-creator-0.1.0/         ← 技能创建指南
├── skill-vetter/                ← 技能安全审查
├── task-dispatch/               ← 任务派发
├── tavily-search/               ← Tavily 搜索
└── video-spec-builder/          ← 视频规格构建
```

---

> 最后更新：2026-06-12
