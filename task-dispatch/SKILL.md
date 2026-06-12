---
name: task-dispatch
description: 三省六部任务派发专用技能。当 agent 需要派发任务给其他 agent 时，使用此技能创建 JJC 任务并追踪进度。确保总控台（之意看板、省部调度）有完整数据。使用场景：(1) 中书省派发尚书省，(2) 尚书省派发工部/六部，(3) 工部执行复杂任务，(4) 任何需要总控台追踪的跨省部任务。
---

# Task Dispatch · 任务派发

**三省六部任务派发专用技能**

---

## 🎯 何时使用

| 场景 | 使用 | 说明 |
|------|------|------|
| 中书省→尚书省 | ✅ 必须 | 跨省部派发 |
| 尚书省→工部/六部 | ✅ 必须 | 派发执行任务 |
| 工部执行复杂任务 | ✅ 必须 | 需要追踪进度 |
| 简单消息回复 | ❌ 不需要 | 直接 sessions_send |

---

## 📋 快速使用

### 基础用法

```bash
# 1. 创建任务 ID
TASK_ID="JJC-$(date +%Y%m%d)-$(printf '%03d' $((RANDOM % 1000)))"

# 2. 创建看板任务
python3 scripts/kanban_update.py create $TASK_ID "任务标题" Doing 当前省部 当前角色 "任务描述"

# 3. 派发下级
python3 scripts/kanban_update.py flow $TASK_ID "当前省部" "下级省部" "📋 派发"

# 4. 等待回奏
python3 scripts/kanban_update.py flow $TASK_ID "下级省部" "当前省部" "✅ 完成"
```

### 使用脚本（推荐）⭐

```bash
# 调用创建任务脚本
python3 scripts/create_task.py --title "任务标题" --from 当前省部 --to 下级省部 --desc "任务描述" --auto-flow
```

---

## 🏛️ 完整流程

```
皇上 → 太子 (创建 JJC) → 中书省 (创建子 JJC) → 尚书省 (创建子 JJC) → 工部 (执行)
                                                                         ↓
尚书省 ← 工部回奏 ← 尚书省回奏 ← 中书省回奏 ← 皇上回奏
```

**详细流程：** 见 [references/workflow.md](references/workflow.md)

---

## 📝 各省部示例

### 太子派发中书省

```bash
TASK_ID="JJC-$(date +%Y%m%d)-001"
python3 scripts/kanban_update.py create $TASK_ID "工部编程测试" Doing 太子 太子 "测试工部编程能力"
python3 scripts/kanban_update.py flow $TASK_ID "太子" "中书省" "📋 旨意传达"
```

### 尚书省派发工部

```bash
TASK_ID="JJC-$(date +%Y%m%d)-002"
python3 scripts/kanban_update.py create $TASK_ID "Python 计算器开发" Doing 尚书省 尚书令 "开发计算器"
python3 scripts/kanban_update.py flow $TASK_ID "尚书省" "工部" "📋 派发执行"
```

### 工部执行任务

```bash
TASK_ID="JJC-$(date +%Y%m%d)-002"  # 与派发 ID 一致
python3 scripts/kanban_update.py state $TASK_ID Doing "工部开始执行"
python3 scripts/kanban_update.py progress $TASK_ID "正在编码" "分析✅|设计✅|编码🔄|测试"
python3 scripts/kanban_update.py flow $TASK_ID "工部" "尚书省" "✅ 完成"
```

**更多示例：** 见 [references/examples.md](references/examples.md)

---

## ⚠️ 合规要求

- **必须创建 JJC 任务** — 否则总控台无法追踪
- **必须更新看板** — 每个步骤都要更新 flow
- **任务 ID 一致性** — 下级使用上级的任务 ID

---

## 🔧 工具

| 工具 | 用途 |
|------|------|
| `scripts/create_task.py` | 创建任务（自动处理 ID） |
| `scripts/kanban_update.py` | 看板操作 |

---

## 📚 参考文档

- [工作流程](references/workflow.md) — 完整三省六部流程
- [使用示例](references/examples.md) — 各省部详细示例
