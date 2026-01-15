# Contributing to AI Multi-Agent Development Team

First off, thank you for considering contributing to AI Multi-Agent Development Team! 🎉

**English** | **[简体中文](CONTRIBUTING.zh-CN.md)**

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Note your environment** (OS, Python version, CrewAI version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the proposed functionality**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes**:
   - Add tests if applicable
   - Update documentation
   - Follow the coding style
3. **Ensure tests pass**
4. **Commit your changes** with clear commit messages
5. **Push to your fork** and submit a pull request

#### Pull Request Guidelines

- Follow the existing code style
- Write meaningful commit messages
- Update documentation for any changed functionality
- Add tests for new features
- Ensure all tests pass
- Keep pull requests focused - one feature/fix per PR

## Development Setup

### Prerequisites

- Python 3.11+
- Git
- Claude Code (or Claude Pro subscription)

### Setup Instructions

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-multi-agent-team.git
cd ai-multi-agent-team

# Install dependencies
pip3 install -r requirements.txt

# Install development dependencies
pip3 install pytest black flake8 mypy

# Run tests
pytest tests/

# Run linting
black .
flake8 .
mypy .
```

## Project Structure

```
ai-multi-agent-team/
├── config/           # Configuration files
├── scripts/          # Utility scripts
├── docs/             # Documentation
├── examples/         # Usage examples
├── tests/            # Test files
└── prompts/          # Prompt templates
```

## Coding Standards

### Python Style Guide

- Follow PEP 8
- Use Black for formatting
- Use type hints where applicable
- Write docstrings for functions and classes

### Commit Messages

Follow the conventional commits specification:

```
feat: add new agent role
fix: resolve memory leak in orchestrator
docs: update installation guide
test: add unit tests for CTO agent
refactor: simplify config loading
```

### Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add examples for new features
- Keep documentation clear and concise

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agents.py

# Run with coverage
pytest --cov=.
```

### Writing Tests

- Write tests for new features
- Maintain test coverage above 80%
- Use descriptive test names
- Test edge cases and error conditions

## Adding New Agents

To add a new agent role:

1. **Update configuration** in `config/crewai-team-config.yaml`:
```yaml
- id: "new_agent"
  role: "Agent Role Name"
  goal: "Clear goal statement"
  backstory: "Detailed background"
  llm: "claude-3-5-sonnet-20241022"
  tools: ["tool1", "tool2"]
```

2. **Document the agent** in `docs/team-framework-v3.md`

3. **Add tests** in `tests/test_new_agent.py`

4. **Update README.md** with the new role

## Adding New Skills

To integrate n-skills plugins:

1. **Document the skill** in `docs/skills-integration.md`

2. **Add installation instructions** in README.md

3. **Provide examples** in `examples/`

4. **Test integration** with existing agents

## Release Process

1. Update version in configuration files
2. Update CHANGELOG.md
3. Create a new tag: `git tag -a v3.x.x -m "Release v3.x.x"`
4. Push tags: `git push origin --tags`
5. Create GitHub release with notes

## Questions?

- Open an issue for questions
- Join discussions in GitHub Discussions
- Check existing documentation

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🙏
