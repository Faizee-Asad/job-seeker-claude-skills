# Job Seeker Claude Skills

A complete Claude Skills project that helps job seekers turn a job description and an existing CV/resume into a stronger application packet: tailored resume, cover letter, recruiter message, interview prep, follow-up emails, and a job application tracker.

> Built to help people get more relevant recruiter calls ethically: no fake experience, no fake metrics, no pretending to have skills the candidate does not have.

## Included skills

| Slash command | Purpose |
|---|---|
| `/job-seeker-helper` | End-to-end job application workflow. Best starting point. |
| `/resume-optimizer` | Tailor a resume/CV to a job description while preserving truth. |
| `/cover-letter` | Write a focused, non-generic cover letter from a JD and candidate background. |
| `/interview-coach` | Build role-specific interview prep, STAR stories, mock questions, and salary talking points. |
| `/job-application-tracker` | Create and maintain a CSV job tracker with next actions. |

## Why this exists

Most job seekers do not need a prettier resume; they need a repeatable process:

1. Decode the job description.
2. Identify must-have skills and keywords.
3. Map real candidate proof to the role.
4. Rewrite bullets with impact, scope, and tools.
5. Create a cover letter that sounds specific.
6. Prepare for recruiter screens and interviews.
7. Track applications and follow-ups.

This repository packages that process into Claude Skills plus reusable templates and deterministic helper scripts.

## Quick install for Claude Code

Clone the repo, then copy the skills into your personal Claude skills directory:

```bash
git clone https://github.com/YOUR_USERNAME/job-seeker-claude-skills.git
mkdir -p ~/.claude/skills
cp -R job-seeker-claude-skills/.claude/skills/* ~/.claude/skills/
```

Restart Claude Code if the top-level skills directory did not exist before. Then try:

```text
/job-seeker-helper I have resume.txt and job-description.txt. Create a tailored resume, cover letter, and interview prep pack.
```

## Quick use inside a project

You can also keep `.claude/skills/` in this repo and open the repo with Claude Code. Claude Code automatically discovers project skills located under `.claude/skills/`.

## Example prompts

```text
/resume-optimizer Use my resume in resume.md and this job description in jd.txt. Produce an ATS keyword audit, rewritten summary, and improved bullets.
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

## What the skill produces

When a user provides a resume/CV and job description, the main workflow can produce:

- `ats_keyword_audit.md`
- `tailored_resume.md`
- `cover_letter.md`
- `recruiter_message.md`
- `interview_prep_pack.md`
- `follow_up_email.md`
- `job_tracker.csv`
- `application_packet.md`

When Claude's document creation skills are available, the skill instructs Claude to generate polished `.docx`/PDF outputs. If document skills are unavailable, the fallback is clean Markdown plus CSV.

## Repository structure

```text
.claude/skills/
  job-seeker-helper/          # Full end-to-end skill
  resume-optimizer/           # Resume-specific slash command
  cover-letter/               # Cover-letter slash command
  interview-coach/            # Interview-prep slash command
  job-application-tracker/    # Tracker slash command

docs/                         # Install, usage, design, privacy, prompt guide
tests/                        # Lightweight Python tests for helper scripts
```

## Safety and ethics

The skill is aggressive about relevance and clarity, but conservative about truth. It must not invent employment history, degrees, certifications, metrics, tools, or impact. It can suggest where to add proof, but it should label unknowns as placeholders.

## License

MIT. See [LICENSE](LICENSE).
