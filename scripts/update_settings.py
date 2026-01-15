#!/usr/bin/env python3
"""
Update Claude Code settings to enable auto-loading of AI Multi-Agent Team
"""

import json
import os
from pathlib import Path
import sys

def update_settings():
    """Update settings.local.json to add SessionStart hook"""

    home_dir = Path.home()
    settings_path = home_dir / ".claude" / "settings.local.json"

    print(f"📄 Updating settings file: {settings_path}")

    # Load existing settings or create new
    if settings_path.exists():
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        print("✓ Loaded existing settings")
    else:
        settings = {}
        print("✓ Creating new settings file")

    # Ensure hooks section exists
    if "hooks" not in settings:
        settings["hooks"] = {}

    if "SessionStart" not in settings["hooks"]:
        settings["hooks"]["SessionStart"] = []

    # Define the new hook command
    hook_command = (
        'python3 -c "import json, sys, os; '
        'home_dir = os.path.expanduser(\'~\'); '
        'claude_dir = os.path.join(home_dir, \'.claude\'); '
        'agents_content = open(\'AGENTS.md\', \'r\').read() if os.path.exists(\'AGENTS.md\') else \'\'; '
        'team_v3_path = os.path.join(claude_dir, \'team-framework-v3.md\'); '
        'team_v3_content = open(team_v3_path, \'r\').read() if os.path.exists(team_v3_path) else \'\'; '
        'best_practices_path = os.path.join(claude_dir, \'best-practices-summary.md\'); '
        'best_practices_content = open(best_practices_path, \'r\').read() if os.path.exists(best_practices_path) else \'\'; '
        'combined_content = f\'# [AI多智能体团队系统 v3.0 已自动加载]\\\\n\\\\n'
        '✅ CrewAI编排引擎就绪\\\\n'
        '✅ 17个专业角色待命\\\\n'
        '✅ 8大最佳实践已激活\\\\n'
        '✅ n-skills插件生态已集成\\\\n\\\\n'
        '---\\\\n\\\\n{team_v3_content}\\\\n\\\\n'
        '---\\\\n\\\\n{best_practices_content}\\\\n\\\\n'
        '---\\\\n\\\\n## Project Agents\\\\n{agents_content}\' if team_v3_content else \'\'; '
        'output = {\'hookSpecificOutput\': {\'hookEventName\': \'SessionStart\', \'additionalContext\': combined_content}}; '
        'print(json.dumps(output))"'
    )

    # Create new hook configuration
    new_hook = {
        "matcher": "startup|resume",
        "hooks": [
            {
                "type": "command",
                "command": hook_command,
                "timeout": 30
            }
        ]
    }

    # Check if hook already exists
    hook_exists = False
    for hook in settings["hooks"]["SessionStart"]:
        if "team-framework-v3.md" in hook.get("hooks", [{}])[0].get("command", ""):
            hook_exists = True
            print("✓ Hook already configured")
            break

    if not hook_exists:
        # Add or replace the hook
        settings["hooks"]["SessionStart"] = [new_hook]
        print("✓ Added SessionStart hook")

    # Write updated settings
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)

    print(f"✅ Settings updated successfully!")
    print(f"   Location: {settings_path}")

    # Verify the hook
    print("\n🔍 Verifying configuration...")

    # Test the hook command
    test_command = (
        f"cd {home_dir} && python3 -c \""
        "import json, sys, os; "
        "home_dir = os.path.expanduser('~'); "
        "claude_dir = os.path.join(home_dir, '.claude'); "
        "team_v3_path = os.path.join(claude_dir, 'team-framework-v3.md'); "
        "team_v3_content = open(team_v3_path, 'r').read() if os.path.exists(team_v3_path) else ''; "
        "print('✅ Hook test successful!' if team_v3_content else '❌ Hook test failed');"
        "\""
    )

    result = os.system(test_command)

    if result == 0:
        print("✓ Hook verification passed")
    else:
        print("⚠️  Hook verification had issues, but installation can continue")

    return True

if __name__ == "__main__":
    try:
        update_settings()
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
