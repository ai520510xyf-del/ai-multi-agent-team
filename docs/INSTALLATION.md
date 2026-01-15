# AI多智能体开发团队系统 v3.0

> 基于 CrewAI + n-skills + MCP 的工业级多智能体编排系统

---

## 📦 系统概览

这是一个完整的AI多智能体开发团队系统，已配置为**自动加载**模式。每次打开新的Claude终端时，团队配置会自动激活。

### ✅ 已安装组件

```
CrewAI v1.8.1                ✅ 已安装
17个专业角色                 ✅ 已配置
8大最佳实践                  ✅ 已启用
自动加载机制                 ✅ 已激活
```

---

## 🚀 快速开始

### **方式1: 对话式交互（推荐日常使用）**

直接在Claude Code中使用角色指令：

```bash
/cto        # 切换到首席技术官视角
/pm         # 切换到项目经理视角
/arch       # 切换到系统架构师视角
/front      # 切换到前端技术主管视角
/back       # 切换到后端技术主管视角
/qa         # 切换到质量保障总监视角
/devops     # 切换到DevOps工程师视角

# 特殊指令
/meeting    # 召开跨角色会议
/review     # 启动代码评审
/emergency  # 启动应急响应
```

### **方式2: CrewAI编排（生产级项目）**

使用完整的CrewAI编排功能：

```bash
# 执行脚本
python3 ~/.claude/scripts/run_crew.py --task "开发用户管理系统"

# 查看配置
cat ~/.claude/crewai-team-config.yaml

# 查看日志
tail -f ~/.claude/logs/agent-execution.log
```

---

## 📂 文件结构

```
~/.claude/
├── team-framework-v3.md              # 主框架文档（自动加载）
├── crewai-team-config.yaml           # CrewAI团队配置
├── best-practices-summary.md         # 8大最佳实践（自动加载）
├── scripts/
│   ├── run_crew.py                   # CrewAI启动脚本
│   ├── performance_dashboard.py      # 性能监控（待实现）
│   └── cost_report.py                # 成本报告（待实现）
├── prompts/                          # 提示词模板目录
├── logs/                             # 执行日志目录
├── skills/                           # n-skills插件目录
└── README.md                         # 本文件
```

---

## 🎯 17个专业角色

### **战略决策层**
- **[CTO]** 首席技术官 - 技术战略、架构决策
- **[PD]** 产品总监 - 产品战略、市场分析

### **项目管理层**
- **[PM]** 敏捷项目经理 - 需求拆解、进度跟踪
- **[SM]** 敏捷教练 - 流程优化、团队效能

### **设计架构层**
- **[ARCH]** 系统架构师 - 架构设计、技术选型
- **[UX]** UX/UI设计总监 - 用户体验、交互设计
- **[SEC]** 信息安全专家 - 安全架构、威胁建模

### **执行交付层 - 前端组**
- **[FE-Lead]** 前端技术主管 - 前端架构、组件库
- **[FE-Dev]** 前端开发工程师 - UI组件实现
- **[FE-Perf]** 前端性能工程师 - 性能优化

### **执行交付层 - 后端组**
- **[BE-Lead]** 后端技术主管 - 微服务架构、API设计
- **[BE-Dev]** 后端开发工程师 - 业务逻辑实现
- **[DBA]** 数据库管理员 - Schema设计、查询优化
- **[DEVOPS]** DevOps工程师 - CI/CD、容器化部署

### **质量保障层**
- **[QA-Lead]** 质量保障总监 - 测试策略、质量门禁
- **[QA-Auto]** 自动化测试专家 - 测试框架、自动化

### **运营支持层**
- **[DOC]** 技术文档工程师 - API文档、架构文档

---

## 📋 8大最佳实践

1. **明确分配角色与职责** - 角色重复率<5%
2. **保持记忆本地化** - 节省30% token使用
3. **明确限制工具访问权限** - 未授权访问事件=0
4. **预先设置终止条件** - 避免无限循环
5. **记录一切** - 100%日志覆盖率
6. **可中断性和安全性** - 暂停/编辑/回滚功能
7. **运行时可配置** - >80%参数可调
8. **版本控制** - 配置变更故障率<5%

详细说明见：`~/.claude/best-practices-summary.md`

---

## 🔧 配置验证

### **检查安装**

```bash
# 检查 CrewAI
python3 -c "import crewai; print(f'CrewAI: {crewai.__version__}')"

# 检查配置文件
ls -lh ~/.claude/team-framework-v3.md
ls -lh ~/.claude/crewai-team-config.yaml

# 测试自动加载 Hook
python3 -c "import json, sys, os; home_dir = os.path.expanduser('~'); claude_dir = os.path.join(home_dir, '.claude'); team_v3_path = os.path.join(claude_dir, 'team-framework-v3.md'); team_v3_content = open(team_v3_path, 'r').read() if os.path.exists(team_v3_path) else ''; print('✅ Hook工作正常!' if team_v3_content else '❌ Hook失败')"
```

### **验证自动加载**

1. **关闭当前Claude Code窗口**
2. **重新打开Claude Code**
3. **新会话应自动显示团队加载信息**

---

## 💡 使用示例

### **示例1: 快速技术咨询**

```
输入: /cto 评估这个技术方案：使用GraphQL替代REST API

输出: [CTO] 让我从以下几个维度评估GraphQL vs REST...
```

### **示例2: 项目立项会议**

```
输入: /meeting 启动用户管理系统项目

输出:
[CTO] 召开立项会议...
[PD] 产品分析...
[PM] 项目规划...
[ARCH] 架构设计...
```

### **示例3: 代码审查**

```
输入: /review 审查这段代码
[粘贴代码]

输出:
[QA-Lead] 代码质量分析...
[SEC] 安全审计...
[ARCH] 架构合规性检查...
```

---

## 📊 质量标准

所有项目交付遵循以下标准：

- ✅ 代码覆盖率 >85%
- ✅ 自动化测试率 >90%
- ✅ API响应时间 P95 <200ms
- ✅ 安全漏洞 0个高危
- ✅ 技术债比率 <5%

---

## 🔄 升级历史

| 版本 | 日期 | 主要变更 |
|------|------|----------|
| v3.0 | 2026-01-15 | 整合CrewAI + n-skills + MCP + 8大最佳实践 |
| v2.0 | 2026-01-15 | 增加角色、输出规范、质量标准 |
| v1.0 | 2026-01-14 | 初始版本 |

---

## 📚 学习资源

- **CrewAI 官方文档**: https://docs.crewai.com
- **n-skills 插件市场**: https://github.com/numman-ali/n-skills
- **Claude Skills 仓库**: https://github.com/anthropics/skills
- **8大最佳实践**: 参考 `best-practices-summary.md`

---

## ❓ 故障排查

### **Q: 新窗口没有自动加载团队配置？**

```bash
# 检查 Hook 配置
cat ~/.claude/settings.local.json | grep -A 5 SessionStart

# 手动测试 Hook
python3 -c "..." # 见上文验证命令
```

### **Q: CrewAI 导入失败？**

```bash
# 重新安装
pip3 install --upgrade crewai crewai-tools langchain-anthropic
```

### **Q: 角色指令不工作？**

```
# 确保输入格式正确
正确: /cto
错误: cto 或 \cto
```

---

## 🎉 开始使用

您现在已经拥有一个完整的工业级多智能体开发团队系统！

**下次打开Claude Code时，团队会自动就绪。**

直接输入任务或使用角色指令，团队随时待命！

---

**最后更新**: 2026-01-15
**维护者**: AI虚拟开发团队系统
