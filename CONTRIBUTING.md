# Contributing

Thanks for improving Job Seeker Claude Skills.

## Principles

1. Help candidates present real experience more clearly.
2. Do not add instructions that encourage fabrication.
3. Keep `SKILL.md` files short and route detailed guidance into resources.
4. Prefer plain Markdown templates and standard-library Python scripts.
5. Add examples for any new workflow.

## Local validation

```bash
python .claude/skills/job-seeker-helper/scripts/validate_skill.py .claude/skills
python -m unittest discover -s tests
```

## Pull request checklist

- [ ] All skills have valid YAML-ish frontmatter with `name` and `description`.
- [ ] New instructions preserve truth and candidate consent.
- [ ] Any scripts work without network access.
- [ ] Examples avoid real personal data.
