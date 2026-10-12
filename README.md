# PG Founder Skills

Nine [Claude Code](https://claude.com/claude-code) skills that turn Paul Graham's essays on startups into working advisors. Ask Claude to help you find a startup idea, critique one, decide whether to quit your job, raise a round, or get your first users, and the matching skill loads automatically.

> **Unofficial.** This project is not affiliated with or endorsed by Paul Graham or Y Combinator. The essays are Paul Graham's copyright and are **not** included here. The skills contain original summaries with short attributed quotations, plus links to the essays on [paulgraham.com](https://paulgraham.com/articles.html).

## The skills

| Skill | Use it for | Essays |
|---|---|---|
| `pg-idea-hunting` | Finding startup ideas: the organic method, recipes for ideas on demand, what to do when you "have no problems" | 12 |
| `pg-idea-validation` | Critiquing an idea with a 13-point rubric: urgency, wells vs craters, path out, why now, competition | 12 |
| `pg-prepared-mind` | Becoming the kind of person who has ideas: projects, curiosity, frontiers, staying upwind | 22 |
| `pg-should-you-start` | Deciding whether and when to start: the 16 reasons people don't, and which are real | 10 |
| `pg-founder-qualities` | What makes a good founder: determination, resourcefulness, earnestness, founder mode | 10 |
| `pg-running-early-startup` | Operating a young startup: launch, unscalable things, growth rate, hiring, default alive | 15 |
| `pg-fundraising-investors` | Raising money and reading investors, pitching, equity math, corp dev, angel investing | 18 |
| `pg-startup-hubs` | Where to locate, and how cities or universities become startup hubs | 7 |
| `pg-yc-history` | How Y Combinator, Viaweb, and Hacker News worked | 9 |

Each skill has a `SKILL.md` with the distilled principles and a step-by-step way to run a session, and a `references/essays.md` listing its source essays with titles, dates, and links.

## Install

### As a Claude Code plugin (recommended)

Inside Claude Code 2.1.275 or later:

```
/plugin install pg-founder-skills --marketplace masthedude/pg-founder-skills
```

On older versions, add the marketplace first, then install:

```
/plugin marketplace add masthedude/pg-founder-skills
/plugin install pg-founder-skills@pg-founder
```

Plugin skills are namespaced, so they appear as `pg-founder-skills:pg-idea-hunting` and so on. They trigger automatically from what you ask; you don't need to type the names.

### By copying the folders

```bash
git clone https://github.com/masthedude/pg-founder-skills.git
cp -R pg-founder-skills/skills/pg-* ~/.claude/skills/
```

### Optional: download the essays

The skills work without the essay text, falling back to the links. To let them quote exact passages, download the essays for your own local use. Pick the line that matches how you installed:

```bash
# plugin install
python3 ~/.claude/plugins/cache/pg-founder/pg-founder-skills/*/scripts/fetch_essays.py

# copied folders
python3 pg-founder-skills/scripts/fetch_essays.py ~/.claude/skills
```

The script uses only the Python standard library. It fetches each listed essay from paulgraham.com, saves plain text into each skill's `references/essays/` folder, and skips files you already have. A plugin update installs into a new version folder, so run it again after updating. You can also just ask Claude to run it; each skill tells Claude where the script is.

## Try it

- "I'm a backend engineer at a bank and I have no startup ideas. Where do I start?"
- "Here's my idea: a social network for dog owners. Thoughts?"
- "An investor said they're excited and want to keep in close touch. What does that mean?"
- "We have 8 months of runway and growth is flat. What should we do?"

## Contributing

Corrections to summaries, better triggers, and new test prompts are welcome. Please don't add essay text to the repo; `.gitignore` blocks it, and pull requests that include it will be closed.

## License

MIT for the original material in this repo. See [LICENSE](LICENSE). Paul Graham's essays remain his copyright.
