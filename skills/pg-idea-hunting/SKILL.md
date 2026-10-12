---
name: pg-idea-hunting
description: Paul Graham's method for finding startup ideas. Use this whenever the user wants to come up with, brainstorm, hunt for, generate, or discover startup, product, or business ideas, asks "what should I build", says they have no ideas or no problems to solve, wants to find problems worth solving, or asks what's missing or broken in a field. Also use it when the user is evaluating a field or trend for opportunities, or asks how famous startups found their ideas. Use it even if they don't say "startup".
---

# PG Idea Hunting

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

Distilled from Paul Graham's essays on where startup ideas come from. The core claim: the way to get startup ideas is not to try to think of startup ideas. It's to notice problems, preferably ones you have yourself. Consciously generated ideas tend to be bad in a dangerous way: plausible enough to fool you into working on them for months.

Read `references/essays/` when you need exact passages. The two most important files are `startupideas.txt` (How to Get Startup Ideas, 2012) and `ideas.txt` (Ideas for Startups, 2005).

## The three tests of a good idea

The best ideas share three things. They are something the founders themselves want, something they themselves can build, and something few others realize is worth doing. Microsoft, Apple, Yahoo, Google and Facebook all began this way. Keep these in front of the user throughout.

## Track A: the organic method (plan A, slow, highest yield)

PG is explicit that this is the real recipe and the rest are substitutes.

1. **Get to the leading edge of something changing fast.** As a builder or as a heavy user. Zuckerberg's advantage was not that he programmed but that he lived online. Anyone reasonably smart can reach an edge of programming in about a year. "Live in the future, then build what's missing."
2. **Work on projects, not startups.** Build things for yourself and your friends because they seem cool. Apple, Google, Facebook, Yahoo were side projects first. If you aim at "a startup" you will reject the outliers, and the outliers are where the big ones live.
3. **Turn on the "what's missing?" filter and turn every other filter off.** Especially "could this be a big company?", the unsexy filter, and the schlep filter. Thousands of programmers saw the payments problem before Stripe; schlep blindness stopped them seeing it as an idea.
4. **Notice rather than think up.** Ideas come from an external stimulus hitting a prepared mind. Gates hears about the Altair; Houston forgets a USB stick. The verb is "notice".
5. **Pay attention to what chafes you.** Annoyance can be a sign you're living in the future. Question the status quo deliberately: why is my inbox full, why does this door stick.
6. **Keep a gaps-and-anomalies journal.** Each night, write down raw gaps and annoyances noticed that day. Not ideas, just anomalies. The habit retrains what you see.
7. **Expect good ideas to look like toys.** Microcomputers, BackRub, "a site for undergrads to stalk each other". When know-it-alls on forums would dismiss it as a toy, that's positive evidence.
8. **Give it time.** A year of preparation is cheap against a 3-5 year startup. Constraining yourself to find an idea in a month means you pick a worse one.

## Track B: recipes for ideas on demand (plan B)

Use these when the user needs an idea now, for example after a first idea fails. Warn them: you'll see many more ideas this way, most of them bad, so the organic constraint has to be replaced with discipline. Organic ideas feel like inspirations; on-demand ideas that feel that way are probably mistaken.

- **Take yourself out of the picture.** Ask "what do I wish someone else would build for me?" and "what would I pay for right now?" This routes around schlep blindness and the unconscious fear of big problems.
- **Look where you have expertise.** A database expert should not build a chat app for teenagers. Your expertise raises your standards, which is why good ideas in your field seem scarce.
- **Mine your last job.** Did anyone say "why doesn't someone make x? We'd buy it in a second"? That's demand plus feasibility.
- **Ask what's unusual about you.** Especially if you're different in a way more people will be. Being young is a particularly good form of unusual: you understand your peers and your needs predict future demand.
- **Clash of domains.** Take programming into a field that hasn't been automated. Take a genetics class, work a summer in biotech, spend two weeks watching a mid-sized non-tech company use computers. You arrive ignorant, so you don't know what to take for granted.
- **Find things that are popular but mediocre.** Dating sites, corporate IT. "Look at something people are trying to do and figure out how to do it in a way that doesn't suck." Be careful: some mediocre things persist for hidden reasons like regulation.
- **Make a luxury a commodity. Make something dramatically cheaper or easier.** Henry Ford, water mills, the Model T. Dramatic cost drops cause qualitative changes in use.
- **Redefine the problem.** Rabin's trick: a number that is prime with probability 1 minus 10^-100 is good enough. Don't fix Windows; ask how people should use applications.
- **Look for waves.** Falling costs with Moore's-law shape (gene sequencing, 3D printing in 2012). Ask what we're unconsciously ruling out as impossible that will soon be possible.
- **Garbage-collect dying industries.** Journalism in 2012. Don't look for the replacement for x; look for what people will later say replaced x, coming in from the side, on a different axis.
- **Find scruffy, sophisticated users the big players disdain.** Hobbyists in 1976. HP passed on the Apple I partly because a TV monitor seemed declassé.
- **Imagine how backward we'll look in 50 years.** Waiting for symptoms to diagnose cancer will seem barbaric. "It will seem obvious in retrospect" is the shape you want.
- **Observe hacked-together behavior.** Reddit came from noticing people used del.icio.us/popular as a makeshift link-sharing site. Build the purpose-built version of what users are already improvising.
- **Listen to complaints.** "Founders are your customers, and the things they complain about are unsatisfied demand." Generalize to any customer.
- **Treat the idea as a question, not a blueprint.** "Could one make a collaborative web spreadsheet?" invites exploration; an assertion invites objections. Bite off a subset and expand.
- **Talk to people about gaps in their work.** Let the conversation get general. You may notice a problem they didn't realize they had because you know how to solve it.
- **Act as a consultant for one user.** Build exactly what one person needs. Most of the code will be reusable, and you start out certain you've reached the bottom of the well.
- **Seek unsexy and schleppy ideas on purpose.** "Don't try to start Twitter. Make something unsexy that people will pay you for." Any sufficiently good idea has as many schleps anyway.

## If the user says they have no problems

They almost certainly do. The brain hides friction to keep daily life efficient. Respond with: stand outside yourself and question routine things; start the anomalies journal; ask what they'd pay someone else to solve; change context so new friction appears (new field, new job, new tools); go find other people's problems. Warn against the opposite error: retroactively describing a made-up idea as a need. "Do you need this as much as Drew Houston needed Dropbox?"

## How to run a hunting session

1. Establish where the user actually is. What field are they at the edge of? What do they use that most people don't yet? What have they built for fun? What annoyed them this week?
2. Run Track A questions first. Only move to Track B recipes if nothing organic surfaces.
3. For each candidate, apply "who wants this urgently right now?" before anything else. Then hand off to the `pg-idea-validation` skill for a full check.
4. Prefer narrow and deep over broad and shallow. Wells, not craters. Narrowness is a byproduct of optimizing for depth.
5. Don't filter on "could this be big" yet. There's time for that later. Do flag dependencies that make an idea impossible (the Reddits' fast-food-by-phone idea needed carrier and chain deals).
6. Output: a short list of candidates, each with the problem, who has it urgently, why now, and which heuristic produced it. Mark which are organic and which are recipe-generated, since the latter need more skepticism.

## Source essays in `references/essays/`

- `startupideas.txt` How to Get Startup Ideas (Nov 2012). The master essay.
- `ideas.txt` Ideas for Startups (Oct 2005). Ideas as questions, doodling, redefine the problem, the Woz route.
- `organic.txt` Organic Startup Ideas (Apr 2010). What do you wish someone would make for you.
- `schlep.txt` Schlep Blindness (Jan 2012). Stripe; take yourself out of the picture.
- `getideas.txt` How to Get New Ideas (Jan 2023). Notice anomalies at the fractal edge of knowledge.
- `ambitious.txt` Frighteningly Ambitious Startup Ideas (Mar 2012). Seven huge ideas; approach big things obliquely; expand westward.
- `fp.txt` Fashionable Problems (Dec 2019). Look in fields people think are played out.
- `newthings.txt` Six Principles for Making New Things (Feb 2008). Simple solutions to overlooked problems, delivered informally, crude v1, iterate.
- `marginal.txt` The Power of the Marginal (Jun 2006). Outsiders, new platforms, "just try hacking something together".
- `hw.txt` The Hardware Renaissance (Oct 2012). Categories that were bad until they weren't.
- `invtrend.txt` Startup Investing Trends (Jun 2013). Complaints are unsatisfied demand.
- `apple.txt` Apple's Mistake (Nov 2009). Startups grow out of personal projects; an explicit request for a startup.
