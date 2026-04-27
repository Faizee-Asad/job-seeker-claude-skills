# Installation

## Claude Code personal install

```bash
git clone https://github.com/Faizee-Asad/job-seeker-claude-skills.git
mkdir -p ~/.claude/skills
cp -R job-seeker-claude-skills/.claude/skills/* ~/.claude/skills/
```

Then invoke:

```text
/job-seeker-helper
```

## Claude Code project install

Keep `.claude/skills/` inside any project where you want these skills available.

```text
my-job-search-project/
  .claude/skills/job-seeker-helper/SKILL.md
  resume.md
  jd.md
```

Open that project with Claude Code and use:

```text
/job-seeker-helper Use resume.md and jd.md. Create a complete application packet.
```

## Claude app / Claude.ai install

If your Claude plan supports custom Skills:

1. Go to the skill folder you want to upload, for example `.claude/skills/job-seeker-helper/`.
2. Zip the folder so the ZIP root contains the skill folder, not only loose files.
3. Upload the ZIP in Claude under **Customize > Skills**.
4. Enable the skill.
5. Start a new chat and ask Claude to create a job application packet.

Upload order recommendation:

1. `job-seeker-helper`
2. `resume-optimizer`
3. `cover-letter`
4. `interview-coach`
5. `job-application-tracker`

## Verification

```bash
python .claude/skills/job-seeker-helper/scripts/validate_skill.py .claude/skills
python -m unittest discover -s tests
```
