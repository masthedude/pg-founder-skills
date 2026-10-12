---
name: pg-should-you-start
description: Paul Graham's reasoning on whether to start a startup, when, and why. Use this whenever the user is deciding between a job and a startup, asks if they should quit their job, found a company, join a startup, or go to grad school, says they're too young, too old, too inexperienced, not smart enough, lack a cofounder, lack an idea, have a family, or fear failure, or asks how people get rich, whether a bad economy matters, or what startups are economically. Use it for any "should I take the leap" question, even if the user is just thinking out loud.
---

# PG Should You Start

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

PG's position: more people are the right sort of person to start a startup than realize it, and nearly everyone who does prefers it to a job, but it is not for everyone and the honest advice is negative in form. The method, from Why to Not Not Start a Startup: decompose vague reluctance into its components, then judge which are real.

Read `references/essays/` for exact passages, especially `notnot.txt`, `wealth.txt`, `start.txt` (in the running-startup skill), `richnow.txt`.

## What a startup is, economically

- "A startup is a company designed to grow fast." Not newly founded, not necessarily tech, not necessarily funded. Growth is the only essential thing (Startup = Growth).
- Economically it compresses a working life into a few years. "If you want to make a million dollars, you have to endure a million dollars' worth of pain," with a bulk discount. Startups give measurement (smallness) and leverage (technology). "If you're in a job that feels safe, you are not going to get rich." (How to Make Wealth)
- Expected value: if success could make a founder $100M and the chance is 1%, EV is $1M; for the right people the chance is far higher. Judge by the mean, not the median. The median outcome is probably zero.
- Starting a company is the most common way new fortunes are made now (roughly 3/4 of new Forbes 400 fortunes), and that is a return to the 1890s norm after the mid-20th-century oligopoly anomaly. It gets cheaper and faster every decade. (How People Get Rich Now)
- Two numbers determine how rich a founder gets: growth rate and how long it continues. 15% a month for five years is about 4000x. You get the first by making something users tell their friends about, the second by being in a big market. (How to Earn a Billion Dollars)

## The sixteen reasons people don't, and which are real

From Why to Not Not Start a Startup. Walk the user through whichever apply.

1. **Too young.** The real threshold is adulthood, not age: no "kid flake reflex," and responding to "that's a stupid idea" with "Really? Why do you think so?" Sam Altman was 19 and seemed 40.
2. **Too inexperienced.** PG reversed his earlier "wait until 23." The best way to get experience at 21 is to start one. A normal job can make you "a tame animal." (But see Before the Startup: don't start at 20 just because; breadth-first first.)
3. **Not determined enough.** Real if true. Test: are you driven to work on your own projects?
4. **Not smart enough.** If you worry about it, you probably are. Most companies do mundane stuff where effort decides.
5. **Know nothing about business.** Coefficient zero. "You just try to get people to pay you for stuff." The Forbes 400 has almost no MBAs near the top.
6. **No cofounder.** Real. Get one. It's more important than anything else. Move if necessary; switch ideas if necessary. Best place to find them is school, which is why timing matters.
7. **No idea.** Not a problem. 70% of a YC startup's idea is new after three months. Recipe: find something missing in your own life and supply it, however specific it seems.
8. **No room for more startups.** Fallacy. There's no limit on wealth people want.
9. **Family to support.** Real. PG won't advise it. Alternatives: consulting-to-product, or join a startup early (employee n is roughly a 1/n^2 founder).
10. **Independently wealthy.** PG's own excuse. Real.
11. **Not ready for commitment.** Legitimate. It takes 3-4 years minimum if it works. But a job will take as long and give less spare time.
12. **Need for structure.** If you need someone to tell you what to do, don't. Test: if you bristle at that suggestion, you're fine.
13. **Fear of uncertainty.** "If you start a startup, it will probably fail." Hope for the best, expect the worst. Employers prefer failed founders to big-company lifers.
14. **Don't realize what you're avoiding.** Summer jobs aren't real jobs. People who've had one know what a job is and work "with the energy of a drowning man."
15. **Parents want you to be a doctor.** Parents share your downside more than your upside, so they're over-conservative, and they're fighting the last war. Treat their wishes as feature requests.
16. **A job is the default.** Only about a hundred years old. We may be at the start of a shift like farming to manufacturing.

## Other inputs to the decision

- **Age.** How to Start a Startup put the window at 23-38 (stamina, financial risk, being taken seriously). A Student's Guide puts the sweet spot in the mid-twenties: stamina, poverty, rootlessness, colleagues, ignorance. Before the Startup: not 20. YC's policy became "only fund undergrads we can't talk out of it."
- **Can you tell if you're up to it?** No. "Your life so far hasn't done much that was like being a startup founder." Swaggering recruits are no more likely to turn out tough. If you're terrified, don't. If merely unsure, the only way to find out is to try. Just not now, if you're 20.
- **Bad economy.** Rounding error compared to the founders. Technology trains leave at regular intervals; the Altair Basic window was 1975 regardless of the recession. Investors get skittish, so be a cockroach: operate so cheaply you can't be killed. "When times get bad, hackers go to grad school," which is why the advice works for those who don't.
- **Big company first?** Later PG says there's "no benefit from working for a big company" in YC's data; big companies are "high fructose corn syrup" for programmers because freedom shrinks with the size of the tree. Google in particular was a black hole no startups came out of. Best place to work before a startup is a startup. The earlier essay (How to Start a Startup) valued a year seeing an existing business, mostly for negative lessons.
- **Grad school.** A good launch pad; procrastinating grad students are a powerful energy source. Yahoo started in grad school. If the startup fails it fails fast enough to go back.
- **It's harder than you think, in a specific way.** It takes over your life, the lows are unbelievably low, and it never gets easier; the problems just change. Larry Page hasn't stopped running since 25. But founders rarely regret it: 0% of the first YC batch had a terrible experience.
- **Hiring is Obsolete's point.** You don't need an employer as a proxy; users can judge you directly. "Your early twenties are exactly the time to take insane career risks." If you fail at 22, so what.

## How to run a session

1. Ask the user to list every reason they're hesitating. Map each to the sixteen. Label each real, bogus, or legitimate-preference.
2. Check the two hard constraints: cofounder and dependents. Everything else is mostly fear or ignorance.
3. Check age and stage against the breadth-first vs depth-first advice. Someone at 20 with no projects should be pointed to `pg-prepared-mind`. Someone at 26 with a cofounder and a side project people use should be told to go.
4. Be honest about the cost: years, all-consuming, roller coaster, probable failure. PG would rather people expect grimness and be surprised.
5. If they decide to go, hand off to `pg-idea-hunting` / `pg-idea-validation` and `pg-running-early-startup`.

## Source essays in `references/essays/`

- `notnot.txt` Why to Not Not Start a Startup (Mar 2007). The sixteen reasons.
- `wealth.txt` How to Make Wealth (May 2004). Measurement and leverage; compress a working life.
- `richnow.txt` How People Get Rich Now (Apr 2021). Founders replace heirs; 1982 was the anomaly.
- `earn.txt` How to Earn a Billion Dollars (Jun 2026). Growth rate times duration; empathy not exploitation.
- `hiring.txt` Hiring is Obsolete (May 2005). Go over employers' heads to users; the economic cage is open.
- `boss.txt` You Weren't Meant to Have a Boss (Mar 2008). Freedom inversely proportional to tree size.
- `badeconomy.txt` Why to Start a Startup in a Bad Economy (Oct 2008).
- `webstartups.txt` The Future of Web Startups (Oct 2007). Startups becoming cheap and common.
- `bubble.txt` What the Bubble Got Right (Sep 2004). Youth, nerds, options, startups built to be sold.
