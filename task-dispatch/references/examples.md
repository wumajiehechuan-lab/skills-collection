# Task Dispatch 使用示例

## 场景 1：太子派发中书省

**皇上旨意：** "测试工部编程能力"

**太子操作：**

```bash
# 方法 1：直接使用 kanban_update.py
TASK_ID="JJC-20260312-001"
python3 scripts/kanban_update.py create $TASK_ID "工部编程能力测试" Doing 太子 太子 "测试工部复杂项目编程能力，使用 opencode 完成"
python3 scripts/kanban_update.py flow $TASK_ID "太子" "中书省" "📋 旨意传达：测试工部编程能力"

# 方法 2：使用 create_task.py 脚本（推荐）
python3 scripts/create_task.py --title "工部编程能力测试" --from 太子 --to 中书省 --desc "测试工部复杂项目编程能力" --auto-flow
```

**预期总控台显示：**
- 之意看板：JJC-20260312-001（Doing）
- 省部调度：太子 → 中书省

---

## 场景 2：尚书省派发工部

**中书省旨意：** "开发 Python 计算器"

**尚书省操作：**

```bash
# 方法 1：直接使用 kanban_update.py
TASK_ID="JJC-20260312-002"
python3 scripts/kanban_update.py create $TASK_ID "Python 计算器开发" Doing 尚书省 尚书令 "开发完整 Python 计算器，支持加减乘除"
python3 scripts/kanban_update.py flow $TASK_ID "尚书省" "工部" "📋 派发执行：开发 Python 计算器"

# 方法 2：使用 create_task.py 脚本（推荐）
python3 scripts/create_task.py --title "Python 计算器开发" --from 尚书省 --to 工部 --desc "开发完整 Python 计算器，支持加减乘除" --auto-flow
```

**预期总控台显示：**
- 之意看板：JJC-20260312-002（Doing）
- 省部调度：尚书省 → 工部

---

## 场景 3：工部执行任务

**尚书省派发：** "开发 Python 计算器"

**工部操作：**

```bash
# 1. 使用尚书省的任务 ID（保持一致！）
TASK_ID="JJC-20260312-002"

# 2. 接任务时更新
python3 scripts/kanban_update.py state $TASK_ID Doing "工部开始执行 Python 计算器开发"
python3 scripts/kanban_update.py flow $TASK_ID "工部" "工部" "▶️ 开始执行：使用 opencode 开发计算器"

# 3. 实时进展上报
python3 scripts/kanban_update.py progress $TASK_ID "正在使用 opencode 编写计算器代码" "需求分析✅|设计方案✅|编码实现🔄|测试验证|提交成果"

# 4. 完成任务时更新
python3 scripts/kanban_update.py flow $TASK_ID "工部" "尚书省" "✅ 完成：Python 计算器已开发完成，支持加减乘除和错误处理"

# 5. 回奏尚书省
sessions_send(agentId="shangshu", message="工部回奏：Python 计算器已完成，文件位于 /tmp/calculator.py")
```

**预期总控台显示：**
- 之意看板：JJC-20260312-002（Done）
- 省部调度：工部 → 尚书省
- 工部 merit_score 增加

---

## 场景 4：完整流程示例

**皇上旨意：** "开发一个完整的用户认证系统"

**完整流程：**

```
1. 太子创建总任务
   TASK_ID="JJC-20260312-003"
   python3 scripts/create_task.py --title "用户认证系统开发" --from 太子 --to 中书省 --desc "开发完整的用户认证系统" --auto-flow

2. 中书省创建子任务
   TASK_ID="JJC-20260312-003"  # 使用相同 ID
   python3 scripts/create_task.py --title "用户认证系统 - 旨意起草" --from 中书省 --to 尚书省 --desc "起草用户认证系统开发旨意" --auto-flow

3. 尚书省创建执行任务
   TASK_ID="JJC-20260312-003"  # 使用相同 ID
   python3 scripts/create_task.py --title "用户认证系统 - 执行" --from 尚书省 --to 工部 --desc "执行用户认证系统开发" --auto-flow

4. 工部执行
   TASK_ID="JJC-20260312-003"  # 使用相同 ID
   python3 scripts/kanban_update.py state $TASK_ID Doing
   python3 scripts/kanban_update.py progress $TASK_ID "正在使用 opencode 开发认证系统" "需求✅|设计✅|编码🔄|测试"
   # ... 执行任务 ...
   python3 scripts/kanban_update.py flow $TASK_ID "工部" "尚书省" "✅ 完成"

5. 回奏流程
   工部 → 尚书省 → 中书省 → 皇上
   每级都更新看板：python3 scripts/kanban_update.py flow $TASK_ID "尚书省" "中书省" "✅ 回奏"
```

**预期总控台显示：**
- 之意看板：JJC-20260312-003（Done）
- 省部调度：完整流转历史
- 各省部 merit_score 增加

---

## 常见错误

### 错误 1：任务 ID 不一致

```bash
# ❌ 错误：尚书省和工部使用不同的任务 ID
尚书省：TASK_ID="JJC-20260312-002"
工部：  TASK_ID="JJC-20260312-999"  # 错误！

# ✅ 正确：使用相同的任务 ID
尚书省：TASK_ID="JJC-20260312-002"
工部：  TASK_ID="JJC-20260312-002"  # 正确！
```

### 错误 2：忘记创建 JJC 任务

```bash
# ❌ 错误：直接 sessions_send，不创建 JJC 任务
sessions_send(agentId="gongbu", message="执行任务...")

# ✅ 正确：先创建 JJC 任务
python3 scripts/create_task.py --title "任务" --from 尚书省 --to 工部 --desc "描述" --auto-flow
sessions_send(agentId="gongbu", message="执行任务...")
```

### 错误 3：忘记更新看板

```bash
# ❌ 错误：只创建任务，不更新进展
python3 scripts/kanban_update.py create $TASK_ID ...
# ... 执行任务 ...
# 忘记更新 flow！

# ✅ 正确：每个步骤都更新
python3 scripts/kanban_update.py create $TASK_ID ...
python3 scripts/kanban_update.py flow $TASK_ID "尚书省" "工部" "派发"
python3 scripts/kanban_update.py progress $TASK_ID "正在执行" "计划🔄"
python3 scripts/kanban_update.py flow $TASK_ID "工部" "尚书省" "完成"
```

---

## 最佳实践

1. **任务 ID 一致性** — 整个流程使用相同的任务 ID
2. **及时更新看板** — 每个步骤都要更新 flow/progress
3. **明确回奏路径** — 工部→尚书省→中书省→皇上
4. **使用脚本简化** — 优先使用 `create_task.py` 脚本
