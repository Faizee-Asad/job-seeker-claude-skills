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
- Job description or pasted posting text.
- Current resume/CV.
- Candidate's target seniority.
- Location, remote preference, and work authorization constraints if relevant.
- Tone preference for cover letter: concise, warm, confident, executive, academic, startup, etc.

Claude should not block if some inputs are unavailable. It should proceed with a best-effort packet and mark assumptions clearly.

## Output modes

### Fast mode

Produces:

- short keyword audit
- resume summary rewrite
- 5 to 8 bullet rewrites
- cover letter draft

### Full packet mode

Produces:

- ATS keyword audit
- role match matrix
- tailored resume
- cover letter
- recruiter DM
- interview prep pack
- follow-up emails
- job tracker row
- combined application packet

### Interview mode

Produces:

- recruiter screen script
- hiring manager interview prep
- technical or portfolio interview prep
- behavioral STAR story bank
- questions to ask interviewers
- salary and negotiation talking points

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

```text
/job-application-tracker Add this job: ExampleCo, Data Analyst, applied today, follow up in 7 days
```
