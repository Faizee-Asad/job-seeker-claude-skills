# Skill Design

## Design goals

- Minimize the user's effort.
- Load detailed resources only when needed.
- Separate deterministic text analysis from judgment-heavy writing.
- Preserve the candidate's truth and voice.
- Produce practical outputs people can send.

## Progressive disclosure

The main `SKILL.md` is an index and operating procedure. Deep guidance lives in resource files:

- `resources/resume_tailoring.md`
- `resources/cover_letter.md`
- `resources/interview_prep.md`
- `resources/followups.md`
- `resources/document_output.md`
- `resources/ethics.md`

## Helper scripts

Scripts are optional. Claude can run them when local files are available:

- `keyword_audit.py`: deterministic keyword and gap analysis.
- `job_tracker.py`: create and update a CSV tracker.
- `packet_builder.py`: assemble Markdown outputs into one packet.
- `validate_skill.py`: validate skill folder structure and frontmatter.

Scripts use Python standard library only.
