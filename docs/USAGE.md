# Usage Guide

## Recommended workflow

1. Save the candidate's current resume as `resume.md` or `resume.txt`.
2. Save the job description as `jd.md` or `job-description.txt`.
3. Ask Claude:

```text
/job-seeker-helper Use resume.md and jd.md. Create a complete application packet.
```

## Inputs Claude should request when missing

- Target role and company.
- Job description or posting link text.
- Current resume/CV.
- Candidate's target seniority and location/work authorization constraints.
- Tone preference for cover letter: concise, warm, confident, executive, academic, startup, etc.

Claude should not block if some inputs are unavailable. It should proceed with a best-effort packet and mark assumptions clearly.

## Output modes

### Fast mode

Produces a short keyword audit, resume summary rewrite, 5-8 bullet rewrites, and a cover letter draft.

### Full packet mode

Produces a complete application package:

- ATS keyword audit
- Role match matrix
- Tailored resume
- Cover letter
- Recruiter DM
- Interview prep pack
- Follow-up emails
- Job tracker row

### Interview mode

Produces:

- Recruiter screen script
- Hiring manager interview prep
- Technical/portfolio interview prep
- Behavioral STAR story bank
- Questions to ask interviewers
- Salary and negotiation talking points

## Example commands

```text
/resume-optimizer resume.md jd.md
```

```text
/cover-letter "Product Manager, Canva" using resume.md and jd.txt
```

```text
/interview-coach Prepare me for the Meta data analyst role using jd.md and my resume.md
```
