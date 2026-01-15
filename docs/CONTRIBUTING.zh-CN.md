# 为 AI 多智能体开发团队做贡献

首先，感谢您考虑为 AI 多智能体开发团队做贡献！🎉

**[English](CONTRIBUTING.md)** | **简体中文**

## 行为准则

本项目及所有参与者均受我们的行为准则约束。通过参与，您应该遵守这些准则。

## 如何贡献？

### 报告 Bug

在创建 Bug 报告之前，请检查现有问题以避免重复。创建 Bug 报告时，请尽可能包含详细信息：

- **使用清晰且描述性的标题**
- **描述重现问题的确切步骤**
- **提供具体示例**
- **描述您观察到的行为以及您期望的行为**
- **如果相关，请包含屏幕截图**
- **注明您的环境**（操作系统、Python 版本、CrewAI 版本）

### 建议增强功能

增强建议作为 GitHub Issues 进行跟踪。创建增强建议时，请包括：

- **使用清晰且描述性的标题**
- **提供建议功能的详细描述**
- **解释为什么这个增强功能会有用**
- **列出一些使用示例**

### Pull Request

1. **Fork 仓库**并从 `main` 创建您的分支
2. **进行更改**：
   - 如果适用，添加测试
   - 更新文档
   - 遵循代码风格
3. **确保测试通过**
4. **提交更改**并使用清晰的提交信息
5. **推送到您的 Fork** 并提交 Pull Request

#### Pull Request 准则

- 遵循现有的代码风格
- 编写有意义的提交信息
- 更新任何已更改功能的文档
- 为新功能添加测试
- 确保所有测试通过
- 保持 Pull Request 专注 - 每个 PR 一个功能/修复

## 开发设置

### 前置要求

- Python 3.11+
- Git
- Claude Code（或 Claude Pro 订阅）

### 设置说明

```bash
# 克隆您的 Fork
git clone https://github.com/YOUR_USERNAME/ai-multi-agent-team.git
cd ai-multi-agent-team

# 安装依赖
pip3 install -r requirements.txt

# 安装开发依赖
pip3 install pytest black flake8 mypy

# 运行测试
pytest tests/

# 运行代码检查
black .
flake8 .
mypy .
```

## 项目结构

```
ai-multi-agent-team/
├── config/           # 配置文件
├── scripts/          # 工具脚本
├── docs/             # 文档
├── examples/         # 使用示例
├── tests/            # 测试文件
└── prompts/          # 提示词模板
```

## 编码标准

### Python 风格指南

- 遵循 PEP 8
- 使用 Black 进行格式化
- 在适用的地方使用类型提示
- 为函数和类编写文档字符串

### 提交信息

遵循常规提交规范：

```
feat: 添加新的智能体角色
fix: 解决编排器中的内存泄漏
docs: 更新安装指南
test: 添加 CTO 智能体的单元测试
refactor: 简化配置加载
```

### 文档

- 为面向用户的更改更新 README.md
- 为代码更改更新文档字符串
- 为新功能添加示例
- 保持文档清晰简洁

## 测试

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_agents.py

# 运行并查看覆盖率
pytest --cov=.
```

### 编写测试

- 为新功能编写测试
- 保持测试覆盖率在 80% 以上
- 使用描述性的测试名称
- 测试边界情况和错误条件

## 添加新智能体

要添加新的智能体角色：

1. **在 `config/crewai-team-config.yaml` 中更新配置**：
```yaml
- id: "new_agent"
  role: "智能体角色名称"
  goal: "清晰的目标陈述"
  backstory: "详细的背景"
  llm: "claude-3-5-sonnet-20241022"
  tools: ["tool1", "tool2"]
```

2. **在 `docs/team-framework-v3.md` 中记录智能体**

3. **在 `tests/test_new_agent.py` 中添加测试**

4. **使用新角色更新 README.md**

## 添加新技能

要集成 n-skills 插件：

1. **在 `docs/skills-integration.md` 中记录技能**

2. **在 README.md 中添加安装说明**

3. **在 `examples/` 中提供示例**

4. **测试与现有智能体的集成**

## 发布流程

1. 更新配置文件中的版本
2. 更新 CHANGELOG.md
3. 创建新标签：`git tag -a v3.x.x -m "Release v3.x.x"`
4. 推送标签：`git push origin --tags`
5. 创建包含发布说明的 GitHub Release

## 问题？

- 为问题开启 Issue
- 加入 GitHub Discussions 的讨论
- 查看现有文档

## 致谢

贡献者将被认可在：
- README.md 贡献者部分
- 发布说明
- 项目文档

感谢您的贡献！🙏
