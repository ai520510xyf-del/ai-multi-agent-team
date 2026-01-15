#!/usr/bin/env python3
"""
CrewAI多智能体团队启动脚本
用法: python3 run_crew.py --task "你的任务描述" [--workflow web_app_development]
"""

import yaml
import argparse
import os
from pathlib import Path
from datetime import datetime

def load_config(config_path):
    """加载CrewAI配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def create_agents_from_config(config):
    """从配置创建智能体（简化版示例）"""
    try:
        from crewai import Agent
        from langchain_anthropic import ChatAnthropic
    except ImportError:
        print("❌ 缺少依赖库，请运行:")
        print("   pip3 install crewai crewai-tools langchain-anthropic")
        return []

    agents = []
    for agent_config in config['agents']:
        # 创建LLM实例
        llm = ChatAnthropic(
            model=agent_config['llm'],
            temperature=0.7,
            max_tokens=2000
        )

        # 创建智能体
        agent = Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=llm,
            verbose=agent_config.get('verbose', False),
            allow_delegation=agent_config.get('allow_delegation', False),
            max_iter=agent_config.get('max_iter', 10)
        )
        agents.append(agent)
        print(f"✅ 创建智能体: {agent_config['role']}")

    return agents

def run_crew(task_description, workflow_name=None):
    """运行CrewAI团队"""
    print("=" * 60)
    print(" CrewAI 多智能体团队启动")
    print("=" * 60)
    print(f"📋 任务: {task_description}")
    print(f"🔄 工作流: {workflow_name or '默认流程'}")
    print(f"⏰ 启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 加载配置
    config_path = Path.home() / ".claude" / "crewai-team-config.yaml"
    if not config_path.exists():
        print(f"❌ 配置文件不存在: {config_path}")
        return

    print(f"\n📂 加载配置: {config_path}")
    config = load_config(config_path)
    print(f"✅ 配置加载成功! 团队: {config['crew']['name']}")
    print(f"   智能体数量: {len(config['agents'])}")

    # 创建智能体
    print("\n🤖 正在创建智能体...")
    agents = create_agents_from_config(config)

    if not agents:
        print("\n⚠️  智能体创建失败，请检查依赖安装")
        print("💡 提示: 当前为演示模式，CrewAI功能需要完整安装")
        print("\n📝 建议在 Claude Code 中使用对话式交互:")
        print("   输入: /cto 或 /pm 等角色指令")
        return

    # TODO: 创建任务和启动Crew
    print("\n💡 提示: 完整CrewAI执行需要配置ANTHROPIC_API_KEY")
    print("   当前可以在Claude Code中使用对话式交互更方便")

    print("\n" + "=" * 60)
    print(" 执行完成")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="CrewAI多智能体团队启动脚本")
    parser.add_argument("--task", required=True, help="任务描述")
    parser.add_argument("--workflow", help="工作流名称（可选）")
    parser.add_argument("--config", default=str(Path.home() / ".claude" / "crewai-team-config.yaml"),
                       help="配置文件路径")

    args = parser.parse_args()

    run_crew(args.task, args.workflow)

if __name__ == "__main__":
    main()
