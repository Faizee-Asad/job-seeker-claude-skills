# Job Seeker Claude Skills

**Job Seeker Claude Skills** is a complete Claude Skills package by **Asad Faizee** for job seekers who want a repeatable, honest, and practical workflow for applying to jobs.

It helps turn a job description and an existing CV/resume into a stronger application packet:

- ATS keyword audit
- tailored resume or CV
- focused cover letter
- recruiter message
- interview prep pack
- follow-up emails
- CSV job application tracker
- combined application packet

> Ethical rule: improve clarity and relevance, but never invent experience, degrees, employers, titles, dates, metrics, certifications, tools, or projects.

## Included skills

| Slash command | Purpose |
|---|---|
| `/job-seeker-helper` | End-to-end job application workflow. Best starting point. |
| `/resume-optimizer` | Tailor a resume/CV to a job description while preserving truth. |
| `/cover-letter` | Write a specific, non-generic cover letter from a JD and candidate background. |
| `/interview-coach` | Build role-specific interview prep, STAR stories, mock questions, and salary talking points. |
| `/job-application-tracker` | Create and maintain a CSV job tracker with next actions. |

## Why this exists

Most job seekers do not need a prettier resume. They need a repeatable process:

1. Decode the job description.
2. Identify must-have skills and keywords.
3. Map real candidate proof to the role.
4. Rewrite bullets with impact, scope, and tools.
5. Create a cover letter that sounds specific.
6. Prepare for recruiter screens and interviews.
7. Track applications and follow-ups.

This repository packages that process into Claude Skills plus reusable Markdown templates and standard-library Python helper scripts.

## Repository structure

```text
.claude/skills/
  job-seeker-helper/          # Full end-to-end skill
  resume-optimizer/           # Resume-specific slash command
  cover-letter/               # Cover-letter slash command
  interview-coach/            # Interview-prep slash command
  job-application-tracker/    # Tracker slash command
docs/                         # Install, usage, design, privacy, prompt guide
examples/                     # Sample resume, JD, and tracker data
tests/                        # Python tests for helper scripts
```

## Quick install for Claude Code

Clone the repo, then copy the skills into your personal Claude skills directory:

```bash
git clone https://github.com/Faizee-Asad/job-seeker-claude-skills.git
mkdir -p ~/.claude/skills
cp -R job-seeker-claude-skills/.claude/skills/* ~/.claude/skills/
```

Restart Claude Code if the top-level skills directory did not exist before. Then try:

```text
/job-seeker-helper I have resume.md and job-description.md. Create a tailored resume, cover letter, recruiter message, interview prep pack, and job tracker row.
```

## Quick use inside a project

You can also keep `.claude/skills/` inside any project where you want the skills available. Claude Code discovers project skills from `.claude/skills/`.

## Use in the Claude app / Claude.ai

If your Claude plan supports custom Skills:

1. Zip one skill folder, for example `.claude/skills/job-seeker-helper/`.
2. Make sure the ZIP contains the skill folder as the root folder and includes `SKILL.md`.
3. Upload it in Claude under **Customize > Skills**.
4. Enable the Skill.
5. Start a chat and ask Claude to use it for your resume and job description.

For a full workflow, upload `job-seeker-helper` first. Upload the companion skills if you also want direct commands such as `/resume-optimizer`, `/cover-letter`, `/interview-coach`, and `/job-application-tracker`.

## Example prompts

```text
/job-seeker-helper Use my resume in resume.md and this job description in jd.md. Create a complete application packet.
```

```text
/resume-optimizer Compare my resume to this job description. Identify missing keywords, rewrite my summary, and improve the bullets without inventing experience.
```

```text
/cover-letter Write a concise cover letter for this Senior Data Analyst role. Use my resume.md and avoid sounding generic.
```

```text
/interview-coach Prepare me for a first recruiter call and a technical interview for this role. Include likely questions and strong answer outlines.
```

```text
/job-application-tracker Create a tracker and add this job: Stripe, Product Analyst, Applied today, follow up next Friday.
```

## Helper scripts

All scripts use the Python standard library only.

```bash
python .claude/skills/job-seeker-helper/scripts/keyword_audit.py \
  --resume examples/resume.example.md \
  --job examples/job-description.example.md \
  --output ats_keyword_audit.md

python .claude/skills/job-seeker-helper/scripts/job_tracker.py \
  --file job_tracker.csv \
  --company "ExampleCo" \
  --role "Data Analyst" \
  --status "Applied" \
  --next-action "Follow up with recruiter"

python .claude/skills/job-seeker-helper/scripts/packet_builder.py \
  --output application_packet.md \
  ats_keyword_audit.md tailored_resume.md cover_letter.md interview_prep_pack.md
```

## Validate the repo

```bash
python .claude/skills/job-seeker-helper/scripts/validate_skill.py .claude/skills
python -m unittest discover -s tests
```

## Safety and ethics

The skill is aggressive about relevance and clarity, but conservative about truth. It must not invent employment history, degrees, certifications, metrics, tools, or impact. It can suggest where to add proof, but it should label unknowns as placeholders like `[add metric if true]`.

## Author

Created by **Asad Faizee**.

GitHub: <https://github.com/Faizee-Asad/job-seeker-claude-skills>

## License

MIT. See [LICENSE](LICENSE).
