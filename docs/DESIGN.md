# Skill Design

## Design goals

- Minimize the user's effort.
- Load detailed resources only when needed.
- Separate deterministic text analysis from judgment-heavy writing.
- Preserve the candidate's truth and voice.
- Produce practical outputs people can send.

## Progressive disclosure

The main `SKILL.md` is an index and operating procedure. Deep guidance lives in resource files:

- `resources/workflow.md`
- `resources/resume_tailoring.md`
- `resources/cover_letter.md`
- `resources/recruiter_message.md`
- `resources/interview_prep.md`
- `resources/followups.md`
- `resources/tracker.md`
- `resources/document_output.md`
- `resources/ethics.md`

## Helper scripts

Scripts are optional. Claude can run them when local files are available:

- `keyword_audit.py`: deterministic keyword and gap analysis.
- `job_tracker.py`: create and update a CSV tracker.
- `packet_builder.py`: assemble Markdown outputs into one packet.
- `validate_skill.py`: validate skill folder structure and frontmatter.

Scripts use Python standard library only.

## Companion skills

The companion skills are smaller entry points for users who know exactly what they want:

- `resume-optimizer`
- `cover-letter`
- `interview-coach`
- `job-application-tracker`

Each companion skill can work alone, but the main `job-seeker-helper` skill is the recommended full workflow.
