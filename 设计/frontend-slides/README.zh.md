# Frontend Slides

一个用于创建精美 HTML 演示文稿的编码代理技能——从零开始或转换 PowerPoint 文件。它被打包为 Claude Code 插件，核心 `SKILL.md` 也可以被其他具有文件系统和 shell 访问权限的编码代理读取。

## 功能介绍

**Frontend Slides** 帮助非设计师在不需要了解 CSS 或 JavaScript 的情况下创建美观的网页演示文稿。它采用"展示，而非描述"的方法：不是让你用语言描述你的审美偏好，而是生成视觉预览，让你选择你喜欢的。

这里是一个关于该技能的演示文稿，通过该技能创建：

https://github.com/user-attachments/assets/ef57333e-f879-432a-afb9-180388982478

### 主要功能

- **零依赖** — 单个 HTML 文件，包含内联 CSS/JS。无需 npm，无需构建工具，无需框架。
- **视觉风格发现** — 无法清晰表达设计偏好？没问题。从生成的视觉预览中选择。
- **PPT 转换** — 将现有 PowerPoint 文件转换为网页，保留所有图片和内容。
- **反 AI 流水化** — 精心策划的独特风格，避免通用的 AI 美学（再见，白色上的紫色渐变）。
- **大胆模板包** — 来自 `beautiful-html-templates` 的可选设计先行模板，渐进式加载，安全预设仍作为默认后备方案。
- **生产质量** — 可访问、固定 16:9 比例、注释完善的代码，你可以自定义。

## 安装

### 通过 Claude Code 自定义市场源

直接从这个公共 GitHub 仓库安装。将这些作为两条单独的 Claude Code 消息运行；不要一次性将两行都粘贴到提示中。

```text
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
```

完成后，运行：

```text
/plugin install frontend-slides@frontend-slides
```

使用 HTTPS URL。较短的 `zarazhangrui/frontend-slides` 形式可能会让 Claude Code 尝试 SSH，如果 GitHub 尚未在你的 `known_hosts` 文件中，这可能会失败。

然后在 Claude Code 中输入 `/frontend-slides:frontend-slides` 来使用它。Claude Code 将插件安装的技能命名为 `/plugin-name:skill-name`。

### Claude Code 手动安装

将技能文件复制到你的 Claude Code 技能目录：

```bash
# 创建技能目录
mkdir -p ~/.claude/skills/frontend-slides/scripts

# 复制用户面对的技能文件
cp SKILL.md STYLE_PRESETS.md viewport-base.css html-template.md animation-patterns.md ~/.claude/skills/frontend-slides/
cp -R bold-template-pack ~/.claude/skills/frontend-slides/
cp scripts/extract-pptx.py scripts/deploy.sh scripts/export-pdf.sh ~/.claude/skills/frontend-slides/scripts/
```

或者直接克隆：

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```

然后在 Claude Code 中输入 `/frontend-slides` 来使用它。独立技能不使用命名空间。

### 其他编码代理

像 Codex、Kimi Code、OpenCode、Gemini CLI 或其他本地编码助手这样的代理也可以使用相同的核心技能。最简单的方法是向代理发送这个 GitHub 仓库链接，让它使用 Frontend Slides 技能：

```text
https://github.com/zarazhangrui/frontend-slides
```

如果代理可以读取 GitHub 仓库或浏览文件，它应该从 `SKILL.md` 开始，只加载它需要的引用支持文件：

- `STYLE_PRESETS.md`
- `viewport-base.css`
- `html-template.md`
- `animation-patterns.md`
- `bold-template-pack/`
- `scripts/`

如果代理有文件系统访问权限和已知的本地技能目录，一些代理也可以为你安装技能。如果没有，它们仍然可以直接遵循 `SKILL.md` 用于当前会话。

Claude Code 插件为 Claude Code 提供了自定义市场源安装流程和 `/frontend-slides:frontend-slides` 命令。其他代理通常不使用该命令界面。

## 使用方法

### 创建新演示文稿

```text
/frontend-slides:frontend-slides

> "我想为我的 AI 初创公司创建一个融资演示"
```

如果手动安装为独立的 Claude Code 技能，请使用 `/frontend-slides`。

在非 Claude 代理中，让代理使用 Frontend Slides 技能，并指向这个仓库或 `SKILL.md`。

该技能将：

1. 询问你的内容（幻灯片、消息、图片）
2. 生成 3 个视觉风格预览供你比较，除非你已经指定了一个，否则会从你的描述中推断氛围
3. 让你选择视觉方向
4. 以你选择的风格创建完整的演示文稿
5. 在浏览器中打开它

### 转换 PowerPoint

```text
/frontend-slides:frontend-slides

> "将我的 presentation.pptx 转换为网页幻灯片"
```

该技能将：

1. 从你的 PPT 中提取所有文本、图片和备注
2. 向你展示提取的内容进行确认
3. 让你选择视觉风格
4. 使用你所有原始资源生成 HTML 演示文稿

## 包含的风格

### 深色主题

- **Bold Signal** — 自信、高冲击力、深色背景上充满活力的卡片
- **Electric Studio** — 干净、专业、分割面板
- **Creative Voltage** — 充满活力、复古现代、电蓝色 + 霓虹
- **Dark Botanical** — 优雅、精致、温暖的点缀

### 浅色主题

- **Notebook Tabs** — 编辑风格、有条理、带有彩色标签的纸张
- **Pastel Geometry** — 友好、平易近人、垂直药丸
- **Split Pastel** — 有趣、现代、双色垂直分割
- **Vintage Editorial** — 诙谐、个性驱动、几何形状

### 特色风格

- **Neon Cyber** — 未来感、粒子背景、霓虹光效
- **Terminal Green** — 开发者导向、黑客美学
- **Swiss Modern** — 极简、包豪斯风格、几何
- **Paper & Ink** — 文学性、首字下沉、引语

### 大胆模板包

该技能还包括来自 `beautiful-html-templates` 的 34 个可选大胆设计系统，例如 **Neo-Grid Bold**、**Editorial Tri-Tone**、**Creative Mode**、**Broadside**、**Signal** 和 **Vellum**。

在风格发现期间，预览集是：

- 1 个来自 `STYLE_PRESETS.md` 的安全预设
- 至少 1 个来自 `bold-template-pack/selection-index.json` 的大胆模板选项
- 1 个通配符选项，可以是另一个大胆模板或自生成的自定义设计

代理首先读取紧凑的大胆模板索引，然后只加载候选的小 `preview.md` 卡片用于标题幻灯片预览。只有在用户选择该模板用于最终演示后，才会加载那个大胆模板的完整 `design.md`。如果用户选择自定义通配符，代理会将该预览自己的 CSS 和布局系统扩展到完整演示中。

## 大胆模板画廊

Frontend Slides 现在可以使用 [`beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) 中的 34 个大胆设计系统。每个模板三张截图，展示每个视觉系统如何处理不同的幻灯片布局。点击任何模板名称可查看源模板库。

### [Soft Editorial](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/soft-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-4.png" width="32.5%" alt="Soft Editorial — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-6.png" width="32.5%" alt="Soft Editorial — 幻灯片 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-10.png" width="32.5%" alt="Soft Editorial — 幻灯片 10" />
</p>

> 暖纸上的 Cormorant Garamond 衬线字体，带有鼠尾草绿、腮红粉和柠檬黄点缀。

### [Editorial Forest](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/editorial-forest/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-1.png" width="32.5%" alt="Editorial Forest — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-2.png" width="32.5%" alt="Editorial Forest — 幻灯片 2" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-5.png" width="32.5%" alt="Editorial Forest — 幻灯片 5" />
</p>

> Source Serif 4 字体中的森林绿、灰粉色和暖奶油色——安静、有意的季度回顾美学。

### [Pin & Paper](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/pin-and-paper/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-1.png" width="32.5%" alt="Pin & Paper — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-11.png" width="32.5%" alt="Pin & Paper — 幻灯片 11" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-3.png" width="32.5%" alt="Pin & Paper — 幻灯片 3" />
</p>

> 黄色纸张，带有安全别针插图，墨蓝色手写 Caveat 字体，纸张纹理。

### [Sakura Chroma](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/sakura-chroma/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-1.png" width="32.5%" alt="Sakura Chroma — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-3.png" width="32.5%" alt="Sakura Chroma — 幻灯片 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-4.png" width="32.5%" alt="Sakura Chroma — 幻灯片 4" />
</p>

> 复古日本磁带包装美学：奶油色纸张、对角彩虹条、压缩粗体字、JIS 风格规格复选框。

### [Stencil & Tablet](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/stencil-tablet/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-1.png" width="32.5%" alt="Stencil & Tablet — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-3.png" width="32.5%" alt="Stencil & Tablet — 幻灯片 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-8.png" width="32.5%" alt="Stencil & Tablet — 幻灯片 8" />
</p>

> 骨色纸张，带有模板切割标题和六色地球色调色板：考古学遇见品牌。

### [Cobalt Grid](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/cobalt-grid/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-1.png" width="32.5%" alt="Cobalt Grid — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-3.png" width="32.5%" alt="Cobalt Grid — 幻灯片 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-5.png" width="32.5%" alt="Cobalt Grid — 幻灯片 5" />
</p>

> 坐标纸画布上的电钴斜体衬线字，由阶梯式像素故障装饰和纤细的细线规则固定。

### [Vellum](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/vellum/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-1.png" width="32.5%" alt="Vellum — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-4.png" width="32.5%" alt="Vellum — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-8.png" width="32.5%" alt="Vellum — 幻灯片 8" />
</p>

> 深海军蓝画布，带有暖黄色斜体 Cormorant 衬线字和单一灰蓝点缀。安静、学者的美学。

### [Emerald Editorial](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/emerald-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-1.png" width="32.5%" alt="Emerald Editorial — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-3.png" width="32.5%" alt="Emerald Editorial — 幻灯片 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-6.png" width="32.5%" alt="Emerald Editorial — 幻灯片 6" />
</p>

> 杂志封面商业演示：祖母绿 + 海军蓝 + 纸张，带有双规则刊头装饰和厚重的 Bodoni 风格显示衬线字。

### [Neo-Grid Bold](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/neo-grid-bold/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-1.png" width="32.5%" alt="Neo-Grid Bold — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-3.png" width="32.5%" alt="Neo-Grid Bold — 幻灯片 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-8.png" width="32.5%" alt="Neo-Grid Bold — 幻灯片 8" />
</p>

> 编辑新野兽主义风格，在米白纸上带有单一霓虹黄点缀。

### [Editorial Tri-Tone](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/editorial-tri-tone/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-1.png" width="32.5%" alt="Editorial Tri-Tone — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-4.png" width="32.5%" alt="Editorial Tri-Tone — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-3.png" width="32.5%" alt="Editorial Tri-Tone — 幻灯片 3" />
</p>

> 三色编辑系统：灰粉色、芥末奶油色和深酒红色，使用 Bricolage + Instrument Serif 字体。

### [Creative Mode](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/creative-mode/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-1.png" width="32.5%" alt="Creative Mode — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-4.png" width="32.5%" alt="Creative Mode — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-6.png" width="32.5%" alt="Creative Mode — 幻灯片 6" />
</p>

> 奶油纸画布，带有自信的多色（绿色、粉色、橙色、黄色）点缀和 Archivo Black 显示字体。

### [Monochrome](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/monochrome/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-1.png" width="32.5%" alt="Monochrome — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-4.png" width="32.5%" alt="Monochrome — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-12.png" width="32.5%" alt="Monochrome — 幻灯片 12" />
</p>

> 象牙色账本纸，全黑文字；Lora 衬线标题，Jost 正文，完全没有颜色。

### [People's Platform (Block & Bold)](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/peoples-platform/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-1.png" width="32.5%" alt="People's Platform (Block & Bold) — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-4.png" width="32.5%" alt="People's Platform (Block & Bold) — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-8.png" width="32.5%" alt="People's Platform (Block & Bold) — 幻灯片 8" />
</p>

> 活动家海报能量：奶油色上的蓝色、橙色、红色，带有 Alfa Slab + Caveat Brush 字体。

### [Pink Script — After Hours](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/pink-script/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-1.png" width="32.5%" alt="Pink Script — After Hours — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-4.png" width="32.5%" alt="Pink Script — After Hours — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-8.png" width="32.5%" alt="Pink Script — After Hours — 幻灯片 8" />
</p>

> 黑色画布，亮粉色点缀，珍珠奶油纸，Instrument Serif 标题：深夜编辑奢华。

### [8-Bit Orbit](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/8-bit-orbit/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-1.png" width="32.5%" alt="8-Bit Orbit — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-6.png" width="32.5%" alt="8-Bit Orbit — 幻灯片 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-5.png" width="32.5%" alt="8-Bit Orbit — 幻灯片 5" />
</p>

> 深海军虚空上的像素艺术霓虹街机美学。

### [BlockFrame](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/block-frame/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-1.png" width="32.5%" alt="BlockFrame — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-4.png" width="32.5%" alt="BlockFrame — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-8.png" width="32.5%" alt="BlockFrame — 幻灯片 8" />
</p>

> 新野兽主义演示，带有粉彩霓虹色块和厚实的黑色边框。

### [Blue Professional](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/blue-professional/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-1.png" width="32.5%" alt="Blue Professional — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-6.png" width="32.5%" alt="Blue Professional — 幻灯片 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-8.png" width="32.5%" alt="Blue Professional — 幻灯片 8" />
</p>

> 奶油纸背景，带有电钴蓝色点缀；干净现代专业。

### [Bold Poster](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/bold-poster/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-1.png" width="32.5%" alt="Bold Poster — 幻灯片 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-4.png" width="32.5%" alt="Bold Poster — 幻灯片 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-8.png" width="32.5%" alt="Bold Poster — 幻灯片 8" />
</p>

> 编辑海报美学，带有巨大的 Shrikhand 显示字体和单一消防车红色点缀。

## 架构

该技能使用**渐进式披露**——主要的 `SKILL.md` 是工作流地图，支持文件仅在需要时按需加载：

| 文件                      | 用途                        | 加载时机                 |
| ------------------------- | --------------------------- | ------------------------ |
| `SKILL.md`                | 核心工作流和规则            | 始终（技能调用）         |
| `STYLE_PRESETS.md`        | 12 个精心策划的视觉预设     | 阶段 2（风格选择）       |
| `bold-template-pack/selection-index.json` | 紧凑的大胆模板元数据 | 阶段 2（候选选择）|
| `bold-template-pack/templates/*/preview.md` | 用于候选大胆预览的小型风格卡片 | 候选选择后的阶段 2 |
| `bold-template-pack/templates/*/design.md` | 选定大胆模板的完整设计系统 | 用户选择后的阶段 3 |
| `viewport-base.css`       | 强制固定舞台 CSS            | 阶段 3（生成）           |
| `html-template.md`        | HTML 结构和 JS 功能         | 阶段 3（生成）           |
| `animation-patterns.md`   | CSS/JS 动画参考             | 阶段 3（生成）           |
| `scripts/extract-pptx.py` | PPT 内容提取                | 阶段 4（转换）           |
| `scripts/deploy.sh`       | 部署到 Vercel               | 阶段 6（分享）           |
| `scripts/export-pdf.sh`   | 导出幻灯片为 PDF            | 阶段 6（分享）           |

仅用于维护的源元数据和再生助手位于用户面对的技能包之外。普通用户不需要它们。

这种设计遵循代理技能最佳实践：首先给代理一个地图，然后只揭示当前选择所需的特定文件。

## 理念

该技能源于以下信念：

1. **你不需要成为设计师就能做出美丽的东西。** 你只需要对你看到的东西做出反应。

2. **依赖是债务。** 单个 HTML 文件在 10 年后仍然可以工作。2019 年的 React 项目？祝你好运。

3. **通用是健忘的。** 每个演示都应该感觉是定制的，而不是模板生成的。

4. **注释是善意。** 代码应该向未来的你（或任何打开它的人）解释自己。

## 分享你的演示文稿

创建演示文稿后，该技能提供两种分享方式：

### 部署到实时 URL

一个命令将你的幻灯片部署到永久的、可分享的 URL，可在任何设备上工作——手机、平板电脑、笔记本电脑：

```bash
bash scripts/deploy.sh ./my-deck/
# 或者
bash scripts/deploy.sh ./presentation.html
```

使用 [Vercel](https://vercel.com)（免费层）。如果是第一次，该技能会引导你完成注册和登录。

### 导出为 PDF

将你的幻灯片转换为 PDF，用于电子邮件、Slack、Notion 或打印：

```bash
bash scripts/export-pdf.sh ./my-deck/index.html
bash scripts/export-pdf.sh ./presentation.html ./output.pdf
```

使用 [Playwright](https://playwright.dev) 以 1920×1080 拍摄每张幻灯片的屏幕截图并组合成 PDF。如果需要会自动安装。动画不会保留（这是静态快照）。

## 要求

- 具有文件系统访问权限和运行 shell 命令能力的本地编码代理
- Claude Code 仅用于自定义市场源安装和 `/frontend-slides:frontend-slides` 命令
- 对于 PPT 转换：带有 `python-pptx` 库的 Python
- 对于 URL 部署：Node.js + Vercel 账户（免费）
- 对于 PDF 导出：Node.js（Playwright 自动安装）

## 致谢

由 [@zarazhangrui](https://github.com/zarazhangrui) 创建。

## 许可证

MIT — 使用它、修改它、分享它。
