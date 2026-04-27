# Use These Skills in the Claude App

This guide is for people who want to use Job Seeker Claude Skills in Claude.ai or the Claude desktop/mobile app, not only Claude Code.

## What to upload

Start with:

```text
.claude/skills/job-seeker-helper/
```

That folder contains:

```text
SKILL.md
resources/
templates/
scripts/
```

## How to zip

From the repo root:

```bash
cd .claude/skills
zip -r job-seeker-helper.zip job-seeker-helper
```

The ZIP should look like this:

```text
job-seeker-helper.zip
  job-seeker-helper/
    SKILL.md
    resources/
    templates/
    scripts/
```

## How to use after upload

In Claude, ask naturally:

```text
Use the Job Seeker Helper skill. I am applying for a Data Analyst role. Here is my resume and the job description. Please create a tailored resume, cover letter, recruiter message, interview prep pack, and job tracker row.
```

Or use the direct command if available:

```text
/job-seeker-helper Use my resume and JD to create a full application packet.
```

## Important privacy note

Before uploading your real resume, remove sensitive information you do not want to share, such as full address, ID numbers, private phone numbers, or references.
