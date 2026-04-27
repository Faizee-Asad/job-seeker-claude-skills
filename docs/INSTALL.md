# Installation

## Claude Code personal install

```bash
git clone https://github.com/YOUR_USERNAME/job-seeker-claude-skills.git
mkdir -p ~/.claude/skills
cp -R job-seeker-claude-skills/.claude/skills/* ~/.claude/skills/
```

Then invoke:

```text
/job-seeker-helper
```

## Project install

Keep `.claude/skills/` inside any project where you want the skills available. Claude Code discovers project skills from `.claude/skills/<skill-name>/SKILL.md`.

## Claude.ai / Claude apps

If your Claude plan supports custom Skills, upload the skill folder that contains `SKILL.md`. For the full package, upload `job-seeker-helper` first. Upload the companion skills if you want direct slash commands such as `/cover-letter`.

## Verification

Run:

```bash
python .claude/skills/job-seeker-helper/scripts/validate_skill.py .claude/skills
```
