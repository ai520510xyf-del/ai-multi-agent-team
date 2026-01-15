#!/bin/bash

# AI Multi-Agent Development Team - Installation Script
# Version: 3.0
# Date: 2026-01-15

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════"
echo "   🤖 AI Multi-Agent Development Team"
echo "   Installation Script v3.0"
echo "════════════════════════════════════════════════════════════"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}📋 Checking prerequisites...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed. Please install Python 3.11+ first.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1-2)
echo -e "${GREEN}✓ Python $PYTHON_VERSION detected${NC}"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}❌ pip3 is not installed. Please install pip3 first.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ pip3 detected${NC}"

# Create Claude directory if not exists
CLAUDE_DIR="$HOME/.claude"
if [ ! -d "$CLAUDE_DIR" ]; then
    echo -e "${BLUE}📁 Creating Claude configuration directory...${NC}"
    mkdir -p "$CLAUDE_DIR"/{scripts,prompts,logs,skills}
fi
echo -e "${GREEN}✓ Claude directory ready${NC}"

# Install Python dependencies
echo ""
echo -e "${BLUE}📦 Installing Python dependencies...${NC}"
echo -e "${YELLOW}This may take a few minutes...${NC}"

pip3 install --quiet --upgrade pip
pip3 install --quiet crewai crewai-tools anthropic langchain-anthropic

echo -e "${GREEN}✓ Dependencies installed${NC}"

# Copy configuration files
echo ""
echo -e "${BLUE}📄 Copying configuration files...${NC}"

cp config/crewai-team-config.yaml "$CLAUDE_DIR/" && echo -e "${GREEN}✓ CrewAI config${NC}"
cp docs/team-framework-v3.md "$CLAUDE_DIR/" && echo -e "${GREEN}✓ Team framework${NC}"
cp docs/best-practices-summary.md "$CLAUDE_DIR/" && echo -e "${GREEN}✓ Best practices${NC}"
cp scripts/run_crew.py "$CLAUDE_DIR/scripts/" && echo -e "${GREEN}✓ Run script${NC}"

# Make script executable
chmod +x "$CLAUDE_DIR/scripts/run_crew.py"

# Update Claude settings
echo ""
echo -e "${BLUE}⚙️  Configuring auto-load mechanism...${NC}"

SETTINGS_FILE="$CLAUDE_DIR/settings.local.json"
BACKUP_FILE="$CLAUDE_DIR/settings.local.json.backup.$(date +%Y%m%d_%H%M%S)"

# Backup existing settings
if [ -f "$SETTINGS_FILE" ]; then
    cp "$SETTINGS_FILE" "$BACKUP_FILE"
    echo -e "${YELLOW}⚠️  Existing settings backed up to: $BACKUP_FILE${NC}"
fi

# Run Python script to update settings
python3 scripts/update_settings.py

echo -e "${GREEN}✓ Settings configured${NC}"

# Create README in Claude directory
echo ""
echo -e "${BLUE}📝 Creating documentation...${NC}"

cat > "$CLAUDE_DIR/README.md" << 'EOF'
# AI Multi-Agent Development Team - Local Configuration

This directory contains your local AI multi-agent team configuration.

## Files

- `crewai-team-config.yaml` - CrewAI team configuration
- `team-framework-v3.md` - Main framework documentation
- `best-practices-summary.md` - 8 Best Practices guide
- `scripts/run_crew.py` - CrewAI launcher script

## Auto-Load

The team configuration automatically loads when you start Claude Code.

## Usage

### Quick Commands

```bash
/cto        # Chief Technology Officer
/pm         # Project Manager
/arch       # System Architect
/front      # Frontend Lead
/back       # Backend Lead
/qa         # QA Lead
/devops     # DevOps Engineer
```

### CrewAI Script

```bash
python3 ~/.claude/scripts/run_crew.py --task "Your task description"
```

## Documentation

Full documentation: https://github.com/YOUR_USERNAME/ai-multi-agent-team

---

Installed: $(date)
Version: 3.0
EOF

echo -e "${GREEN}✓ Documentation created${NC}"

# Verification
echo ""
echo -e "${BLUE}🔍 Verifying installation...${NC}"

# Check if files exist
FILES_TO_CHECK=(
    "$CLAUDE_DIR/crewai-team-config.yaml"
    "$CLAUDE_DIR/team-framework-v3.md"
    "$CLAUDE_DIR/best-practices-summary.md"
    "$CLAUDE_DIR/scripts/run_crew.py"
)

ALL_GOOD=true
for FILE in "${FILES_TO_CHECK[@]}"; do
    if [ -f "$FILE" ]; then
        echo -e "${GREEN}✓ $(basename $FILE)${NC}"
    else
        echo -e "${RED}✗ $(basename $FILE) missing${NC}"
        ALL_GOOD=false
    fi
done

# Test CrewAI import
if python3 -c "import crewai" 2>/dev/null; then
    echo -e "${GREEN}✓ CrewAI import successful${NC}"
else
    echo -e "${RED}✗ CrewAI import failed${NC}"
    ALL_GOOD=false
fi

echo ""
echo "════════════════════════════════════════════════════════════"

if [ "$ALL_GOOD" = true ]; then
    echo -e "${GREEN}✅ Installation completed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Restart Claude Code"
    echo "2. The team will auto-load in new sessions"
    echo "3. Try: /cto or /meeting to get started"
    echo ""
    echo -e "${YELLOW}📖 Documentation: $CLAUDE_DIR/README.md${NC}"
else
    echo -e "${RED}❌ Installation completed with errors${NC}"
    echo "Please check the error messages above."
fi

echo "════════════════════════════════════════════════════════════"
