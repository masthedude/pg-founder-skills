# PG Founder Skills

Nine skills for Claude Code and Codex that apply Paul Graham's startup essays to your situation. Ask for help finding an idea, judging one, raising money, or getting users, and the right skill loads on its own.

> Unofficial. Not affiliated with Paul Graham or Y Combinator. The essays aren't included; the skills link to them on [paulgraham.com](https://paulgraham.com/articles.html).

## Skills

- **pg-idea-hunting**: find startup ideas
- **pg-idea-validation**: test whether an idea is any good
- **pg-prepared-mind**: become the kind of person who has ideas
- **pg-should-you-start**: decide whether and when to start
- **pg-founder-qualities**: what makes a good founder
- **pg-running-early-startup**: launch, get users, grow, survive
- **pg-fundraising-investors**: raise money and read investors
- **pg-startup-hubs**: where to build a startup
- **pg-yc-history**: how YC, Viaweb, and Hacker News worked

## Install

### Claude Code

```bash
claude plugin install pg-founder-skills --marketplace masthedude/pg-founder-skills

# Optional: or from inside a Claude Code session
/plugin install pg-founder-skills --marketplace masthedude/pg-founder-skills

# Optional: download the essays so the skills can quote them
python3 ~/.claude/plugins/cache/pg-founder/pg-founder-skills/*/scripts/fetch_essays.py
```

### Codex

```bash
npx skills add masthedude/pg-founder-skills -a codex -s '*' -g

# Optional: or install as a native Codex plugin
codex plugin marketplace add masthedude/pg-founder-skills
codex plugin add pg-founder-skills@pg-founder

# Optional: download the essays so the skills can quote them
git clone https://github.com/masthedude/pg-founder-skills.git
python3 pg-founder-skills/scripts/fetch_essays.py ~/.agents/skills
```

### Other agents

Run `npx skills add masthedude/pg-founder-skills -s '*' -g` and pick your agent from the list.

## License

MIT, for the original material here. The essays remain Paul Graham's copyright.
