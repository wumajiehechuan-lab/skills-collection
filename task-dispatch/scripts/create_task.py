#!/usr/bin/env python3
"""
任务创建脚本 - 简化 JJC 任务创建流程

用法:
    python3 create_task.py --title "任务标题" --from 尚书省 --to 工部 --desc "任务描述"
    python3 create_task.py --title "任务标题" --from 尚书省 --to 工部 --desc "任务描述" --auto-flow
"""

import argparse
import subprocess
import datetime
import random
import sys
import pathlib

# 获取脚本所在目录
SCRIPT_DIR = pathlib.Path(__file__).parent.parent

# 查找 kanban_update.py（优先查找工部 workspace）
KANBAN_SCRIPT = None
possible_paths = [
    pathlib.Path.home() / '.openclaw/workspace-gongbu/scripts/kanban_update.py',
    pathlib.Path.home() / '.openclaw/workspace-taizi/scripts/kanban_update.py',
    SCRIPT_DIR.parent.parent.parent / 'kanban_update.py',
]

for path in possible_paths:
    if path.exists():
        KANBAN_SCRIPT = path
        break

if KANBAN_SCRIPT is None:
    print("❌ 错误：找不到 kanban_update.py 脚本", file=sys.stderr)
    print("请在以下位置之一创建此脚本:", file=sys.stderr)
    for path in possible_paths:
        print(f"  - {path}", file=sys.stderr)
    sys.exit(1)

def create_task_id():
    """生成唯一任务 ID"""
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    num = random.randint(0, 999)
    return f"JJC-{date_str}-{num:03d}"

def run_command(cmd):
    """执行命令"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 命令执行失败：{cmd}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description='创建 JJC 任务')
    parser.add_argument('--title', required=True, help='任务标题')
    parser.add_argument('--from', dest='from_dept', required=True, help='派发省部')
    parser.add_argument('--to', dest='to_dept', required=True, help='接收省部')
    parser.add_argument('--desc', default='', help='任务描述')
    parser.add_argument('--state', default='Doing', help='任务状态')
    parser.add_argument('--auto-flow', action='store_true', help='自动创建 flow')
    parser.add_argument('--progress', help='实时进展上报内容')
    
    args = parser.parse_args()
    
    # 创建任务 ID
    task_id = create_task_id()
    
    # 获取角色映射
    role_mapping = {
        '太子': '太子',
        '中书省': '中书令',
        '门下省': '侍中',
        '尚书省': '尚书令',
        '工部': '工部尚书',
        '户部': '户部尚书',
        '礼部': '礼部尚书',
        '兵部': '兵部尚书',
        '刑部': '刑部尚书',
        '吏部': '吏部尚书',
    }
    
    from_role = role_mapping.get(args.from_dept, '尚书令')
    
    print(f"📋 创建任务：{task_id}")
    print(f"   标题：{args.title}")
    print(f"   派发：{args.from_dept} → {args.to_dept}")
    print(f"   描述：{args.desc}")
    
    # 创建任务
    create_cmd = f'python3 {KANBAN_SCRIPT} create {task_id} "{args.title}" {args.state} {args.from_dept} {from_role} "{args.desc}"'
    run_command(create_cmd)
    print(f"✅ 任务已创建")
    
    # 自动创建 flow
    if args.auto_flow:
        print(f"📮 派发：{args.from_dept} → {args.to_dept}")
        flow_cmd = f'python3 {KANBAN_SCRIPT} flow {task_id} "{args.from_dept}" "{args.to_dept}" "📋 派发执行"'
        run_command(flow_cmd)
        print(f"✅ 任务已派发")
    
    # 实时进展上报
    if args.progress:
        print(f"📊 上报进展：{args.progress}")
        progress_cmd = f'python3 {KANBAN_SCRIPT} progress {task_id} "{args.progress}" "准备✅|执行🔄|完成"'
        run_command(progress_cmd)
        print(f"✅ 进展已上报")
    
    print(f"\n✨ 任务创建完成：{task_id}")
    print(f"💡 提示：工部执行时使用相同的任务 ID: {task_id}")

if __name__ == '__main__':
    main()
