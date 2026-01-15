"""
Test configuration files and setup
"""

import os
import yaml
import pytest
from pathlib import Path


class TestConfiguration:
    """Test configuration file validity"""

    def test_crewai_config_exists(self):
        """Test CrewAI configuration file exists"""
        config_path = Path("config/crewai-team-config.yaml")
        assert config_path.exists(), "CrewAI config file not found"

    def test_crewai_config_valid_yaml(self):
        """Test CrewAI configuration is valid YAML"""
        config_path = Path("config/crewai-team-config.yaml")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        assert config is not None, "Config file is empty"
        assert isinstance(config, dict), "Config is not a dictionary"

    def test_crewai_config_has_required_keys(self):
        """Test CrewAI configuration has required keys"""
        config_path = Path("config/crewai-team-config.yaml")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        required_keys = ['meta', 'crew', 'agents', 'best_practices', 'quality_standards']
        for key in required_keys:
            assert key in config, f"Missing required key: {key}"

    def test_agents_configuration(self):
        """Test agents are properly configured"""
        config_path = Path("config/crewai-team-config.yaml")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        agents = config.get('agents', [])
        assert len(agents) > 0, "No agents configured"

        # Check first agent has required fields
        first_agent = agents[0]
        required_fields = ['id', 'role', 'goal', 'backstory', 'llm', 'tools']
        for field in required_fields:
            assert field in first_agent, f"Agent missing required field: {field}"

    def test_best_practices_enabled(self):
        """Test best practices are enabled"""
        config_path = Path("config/crewai-team-config.yaml")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        best_practices = config.get('best_practices', {})

        # Check key best practices are configured
        practices_to_check = [
            'role_clarity',
            'memory_localization',
            'tool_permissions',
            'termination',
            'logging'
        ]

        for practice in practices_to_check:
            assert practice in best_practices, f"Missing best practice: {practice}"
            assert best_practices[practice].get('enabled', False), \
                f"Best practice not enabled: {practice}"


class TestScripts:
    """Test script files"""

    def test_run_crew_script_exists(self):
        """Test run_crew.py exists"""
        script_path = Path("scripts/run_crew.py")
        assert script_path.exists(), "run_crew.py not found"

    def test_install_script_exists(self):
        """Test install.sh exists"""
        script_path = Path("install.sh")
        assert script_path.exists(), "install.sh not found"

    def test_install_script_executable(self):
        """Test install.sh is executable"""
        script_path = Path("install.sh")
        assert os.access(script_path, os.X_OK), "install.sh is not executable"


class TestDocumentation:
    """Test documentation files"""

    def test_readme_exists(self):
        """Test README.md exists"""
        readme_path = Path("README.md")
        assert readme_path.exists(), "README.md not found"

    def test_license_exists(self):
        """Test LICENSE file exists"""
        license_path = Path("LICENSE")
        assert license_path.exists(), "LICENSE file not found"

    def test_team_framework_exists(self):
        """Test team framework documentation exists"""
        doc_path = Path("docs/team-framework-v3.md")
        assert doc_path.exists(), "team-framework-v3.md not found"

    def test_best_practices_doc_exists(self):
        """Test best practices documentation exists"""
        doc_path = Path("docs/best-practices-summary.md")
        assert doc_path.exists(), "best-practices-summary.md not found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
