---
name: pg-prepared-mind
description: Paul Graham's advice on becoming the kind of person who has good ideas and does great work. Use this whenever the user asks what to learn, what to study, what to work on, how to prepare to start a startup later, what to do in college or their twenties, how to choose a field or career direction, how to follow curiosity, how to do great work, whether to follow their passion, or how to get past fear of starting something that looks lame. Also use it for questions about curiosity, obsession, "staying upwind", unlearning school habits, or how famous founders prepared before their startups. Use it even if the user never mentions startups.
---

# PG Prepared Mind

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

Startup ideas come from an external stimulus hitting a prepared mind. This skill is about preparing the mind. PG's claim, borrowed from Pirsig: "You want to know how to paint a perfect painting? It's easy. Make yourself perfect and then just paint naturally." Empirically the way to have good startup ideas is to become the sort of person who has them.

Read `references/essays/` for exact passages, especially `greatwork.txt` (How to Do Great Work), `before.txt` (Before the Startup), `google.txt` (How to Start Google).

## The core recipe

From Before the Startup, the six-word version of how to turn your mind into the type startup ideas form in: "(1) learn a lot about things that matter, (2) work on problems that interest you (3) with people you like and respect." The third part is also how you get cofounders. The two-word version: "just learn."

From How to Start Google, for a 15-year-old: get good at some technology by working on your own projects, and do well enough in school to get into a university where the cofounders are. "Projects aren't just the best way to learn about technology. They're also the best source of startup ideas."

From How to Do Great Work, the four steps: choose a field, learn enough to get to the frontier, notice gaps, explore promising ones. Curiosity drives all four.

## Principles to apply

**Work on your own projects.** This is the thread through every essay. Skating vs walking. YC cared about applicants' projects, not grades. Facebook, Microsoft, Apple, Google were all projects before they were companies. Don't let "work" mean something other people tell you to do.

**Follow curiosity, especially strange curiosity.** "What are you excessively curious about, curious to a degree that would bore most other people?" The stranger your tastes, the stronger the evidence of what you should do. Heuristic from What Doesn't Seem Like Work: what seems like work to others but not to you? That's what you're suited for. The bus-ticket theory: a disinterested obsession with something that matters is the recipe for genius, and interest is a proxy for ability and a substitute for determination.

**Get to a frontier.** Knowledge grows fractally; edges look smooth from afar and are full of gaps up close. You don't have to push the frontier yourself, you can be at the edge as a user. In practice "sufficiently expert" takes about a year of focused work plus caring a lot. Learning to program is sufficient though not necessary, and "software is eating the world" has decades left.

**Stay upwind.** When unsure, choose options that keep more options open. Math is upwind of economics. Pick a type of work that could turn into either an organic career or a two-job career. Downwind jobs pay more precisely because they close doors.

**Don't plan too much.** Great work is a depth-first search; you can't discover natural selection by deciding to. At each stage do what's most interesting and gives the best options. Try lots of things, make yourself a big target for luck.

**Optimize for interestingness, not prestige or money.** Prestige is fossilized inspiration; if you do anything well enough you'll make it prestigious. "If it didn't suck, they wouldn't have had to make it prestigious." Money combined with prestige (corporate law, medicine) is the dangerous trap. Test: would you do it for free with a day job on the side? PG's own pattern: still life, Viaweb, YC, online essays all looked unprestigious at the start, and that was a sign.

**When to do what you love (the midwit curve).** If you don't need much money, do what interests you. If you want to be moderately rich, you usually can't afford to. If you want to be super rich and you're young and technical, working on what interests you becomes correct again, because that's how you discover startup ideas. If you want to do great work at all, it's simply necessary.

**Build things that seem like toys. Push through the lame phase.** Early work on ambitious projects looks feeble even to its creator. Techniques: overestimate the importance of what you're doing, be slightly overconfident, call it "just a sketch" or "just a hack", focus on rate of improvement, treat it as an experiment, surround yourself with people who can tell an ugly duckling from a baby swan.

**Unlearn school.** School trains you to win by hacking bad tests. Startups are where that stops working: there's no boss to trick, only users. Founders who ask "what's the trick for raising money" are playing house. Also unlearn passivity: think of your education as your project and teachers as working for you.

**Be a noob on purpose.** The more of a noob you feel locally, the less of one you are globally. Move to the new country, the new field.

**Pay attention to what seems wrong when learning something new.** 99% of the time the problem is you. Note it, keep going, come back later; if it still seems wrong, it's probably an undiscovered idea.

**Protect the top idea in your mind.** What you think about in the shower is what you'll make progress on. Money matters and disputes push out interesting ideas. Arrange your life so the urgent problems are ones you want to think about.

**Clash of domains.** Learn about a second field. Importing ideas from distant fields is where the virgin territory is. A CS major is better off taking genetics than entrepreneurship.

**Treat new ideas as challenges to the imagination.** Switch from listing reasons it won't work to thinking of ways it could. When a reasonable domain expert proposes something that sounds wrong, that's a sign of something interesting.

**Don't start a startup at 20.** Breadth-first search is right at 20; a startup is a brutally fast depth-first search that takes over your life. "You're not sacrificing anything by forgoing a startup at 20, because you're more likely to succeed if you wait." The exception is if a side project takes off anyway.

## How to run a session

1. Find out what the user is actually curious about, what they've built for fun, what feels like play to them that others find work, and what frontier they're near.
2. Diagnose the common failure modes: chasing prestige, waiting for permission, planning instead of starting, judging early work by finished standards, letting school habits drive, having no projects.
3. Recommend concrete moves: a project to start this week, a field to get a year into, people to seek out, what to stop doing. Prefer "start small and ugly now" over "study first".
4. Hand off to `pg-idea-hunting` once they're at an edge and noticing gaps, and to `pg-should-you-start` when the question is whether to commit.

## Source essays in `references/essays/`

- `greatwork.txt` How to Do Great Work (Jul 2023). The master essay on choosing and doing work.
- `before.txt` Before the Startup (Oct 2014). Six counterintuitive points; "just learn."
- `google.txt` How to Start Google (Mar 2024). For teenagers: projects, technology, cofounders.
- `prepare.txt` How Universities Should Prepare Founders (Aug 2026). Teach building, give free time, don't teach "entrepreneurship."
- `mit.txt` A Student's Guide to Startups (Oct 2006). Advantages of youth; class projects vs real problems.
- `own.txt` A Project of One's Own (Jun 2021). Skating vs walking.
- `genius.txt` The Bus Ticket Theory of Genius (Nov 2019). Disinterested obsession with something that matters.
- `superlinear.txt` Superlinear Returns (Oct 2023). Seek compounding work; curiosity over careerism.
- `love.txt` How to Do What You Love (Jan 2006). Prestige, money, the two routes, always produce.
- `when.txt` When To Do What You Love (Sep 2024). The midwit curve; staying upwind.
- `work.txt` What Doesn't Seem Like Work? (Jan 2015).
- `do.txt` What to Do (Mar 2025). Make good new things.
- `noob.txt` Being a Noob (Jan 2020).
- `ecw.txt` How to Be an Expert in a Changing World (Dec 2014). Bet on people; don't discount weird hunches.
- `lesson.txt` The Lesson to Unlearn (Dec 2019). Hacking bad tests.
- `early.txt` Early Work (Oct 2020). Getting through the lame phase.
- `sun.txt` General and Surprising (Sep 2017).
- `disc.txt` The Risk of Discovery (Jan 2017). Newton's three bets.
- `want.txt` What You (Want to)* Want (Nov 2022).
- `top.txt` The Top Idea in Your Mind (Jul 2010).
- `laundry.txt` A Version 1.0 (Oct 2004). Essays as figuring things out; look for surprise; "look for anomalies."
- `worked.txt` What I Worked On (Feb 2021). PG's own winding path; prestige as a danger sign; low end eats high end.
