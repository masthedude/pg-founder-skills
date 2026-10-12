---
name: pg-yc-history
description: How Y Combinator started, why, and how it works, plus Paul Graham's accounts of Viaweb and Hacker News. Use this whenever the user asks about YC's origin, its model (batches, standard terms, Demo Day, the 7% deal, office hours), why it funds in batches, what YC actually does for startups, how the first batch was chosen, what PG learned from running Hacker News or a community site, or wants to model an accelerator, seed program, or founder community on YC. Also use it for questions about Viaweb's history or what early web startups looked like.
---

# PG YC History

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

YC is the clearest worked example of PG's own advice: a side project that launched fast with part of an idea, whose most important feature (synchronous batches) was discovered rather than planned, that was dismissed as a toy, and that was built to be exactly what the founders had wanted for themselves.

Read `references/essays/` for exact passages, especially `ycstart.txt`, `ycombinator.txt`, `whyyc.txt`.

## How it started (March 11, 2005)

- PG and Jessica Livingston decided it walking home from dinner in Harvard Square. Three threads converged: PG's long-delayed intention to do angel investing, his Harvard Computer Society talk on how to start a startup, and wanting to work with Robert Morris and Trevor Blackwell again. PG put in $100k, Robert and Trevor $50k each.
- The ideas PG had been telling Jessica VCs should adopt: more, smaller investments; fund hackers instead of suits; fund younger founders; let founders stay CEO.
- Modeled on Viaweb's own seed deal: $10k from Julian Weber for 10%, plus incorporation, legal work, and business advice. "Without Julian, Viaweb would never have made it." YC's deal became $6k per founder for 6%.
- Originally "Cambridge Seed"; renamed within days so it wouldn't be regional. Orange because no VC used it.
- The Summer Founders Program existed because undergrads were choosing summer jobs; the batch model was adopted to learn investing fast on many startups at once. They expected it to be "an educational expense and a charitable donation." 225 applications, 20 interviews, 8 funded: including Reddit, Justin Kan and Emmett Shear, Aaron Swartz, Sam Altman.
- "The Y Combinator effect": the moment visitors realized it wasn't lame. This is why YC likes funding ideas others dismiss as toys.
- Moved to Silicon Valley for the second batch, partly so no one else could be "the Y Combinator of Silicon Valley."

## What YC actually does

- "Funding very early stage startups is not mainly about funding." A $50M mezzanine round is all money; a $2M series A is money plus help; YC is almost all help, since founders' living expenses are the main cost. "You can't make a mouse by scaling down an elephant."
- It gets startups launched straight: a steam catapult. In three months it sorts cofounder tensions, does the paperwork, decides what to focus on first, removes obstacles, then Demo Day presents to nearly every Silicon Valley investor.
- The first question is always "what do you make?", so YC partners have to be hackers. YC competes with employers, not VCs; it creates deal flow by turning would-be employees into founders.
- It's not an incubator; founders don't work in YC's space. It's an "excubator."
- The batch model solved founders' isolation and created colleagues who face the same problems at the same time. Alumni help the current batch; batchmates become each other's first customers ("YC GDP").
- Office hours are individualized, not a bootcamp. The 2012 batch of 84 "broke YC" because an O(n^2) algorithm (every partner knowing every startup) blew up; sharding into groups fixed it.
- Most startups have the same problems; founders are bad at knowing which of their problems matters; founders often don't listen because the advice is counterintuitive and sounds wrong. "Speed defines startups. Focus enables speed. YC improves focus."
- Selection: a 10-minute read plus a 10-minute interview, ~10% regret rate. YC cares about projects built, not grades. "What cool things have you made?" They'll accept "we have no idea" as an idea.
- Economics: effectively all returns come from a few big winners (Dropbox and Airbnb were three quarters of $10B in 2012); fundraising success after Demo Day is an inversely correlated metric; YC knows it should take more risk than it can bring itself to.
- Why PG did it: not mainly money, not mainly charity, but because it's "such a great hack" on the world's economy, "which fortunately happens to be open source."

## Viaweb (1995-1998)

- Started as Artix (art galleries online), which failed because galleries didn't want it. Pivoted to software for building online stores when PG noticed the stores appearing were identical to gallery sites plus order buttons.
- The web app idea came on a mattress in Robert's apartment: run the software on the server, control it by clicking links. Working prototype in two days (August 12, 1995).
- $100/month small store, $300 large, an order of magnitude below the norm, set because the founders were poor. Built stores for merchants by hand (doing things that don't scale before the phrase existed). 70 stores end of 1996, 500 end of 1997. Hired too many people because investors and the Bubble expected it; reached breakeven only when Yahoo bought it in summer 1998.
- June 1998 snapshot: tiny pages, text as images, 7 search engines that mattered and no Google, PR firm at $16k/month, servers in Trevor's office ("the Hot Tub"), RTML as Lisp under a structure editor, fake version numbers for the trade press.

## Hacker News (2007-)

- Written to test Arc; began as Startup News, renamed because the audience should be future founders. Grew from 1600 to 22,000 daily uniques in two years; PG wanted slow growth.
- Dilution is measured in behavior, not users; keep out bad behavior and bad people leave on their own. Broken windows applies.
- The Fluff Principle: links easiest to judge take over unless you prevent it. Countermeasures: ban off-topic fluff, kill empty rants, auto-kill characteristic sites, rewrite linkbait titles, show killed items transparently.
- Comment quality correlates with length; "stupidity more often takes the form of having few ideas than wrong ones." Bad comments are kudzu. Banning meanness also cuts stupidity.
- The site should attract the right people and repel everyone else: plain design, no dramatic titles, only ideas as the draw.
- HN was PG's biggest source of stress at YC, about 60% of urgent problems, and in hindsight a mistake in that sense.

## How to run a session

For questions about modeling a program on YC: emphasize what's load-bearing (help over money, synchronous batches, colleagues, hacker partners, fast decisions, standard terms, a filter that selects builders, founders as users of the program) and what isn't (office space, curriculum, business plan competitions). For community sites: apply the HN rules. For history questions: answer from the essays with dates and names.

## Source essays in `references/essays/`

- `ycstart.txt` How Y Combinator Started (Mar 2012).
- `whyyc.txt` Why YC (Mar 2006).
- `ycombinator.txt` A New Venture Animal (Mar 2008).
- `vw.txt` Snapshot: Viaweb, June 1998 (Jan 2012).
- `hackernews.txt` What I've Learned from Hacker News (Feb 2009).

Related essays in sibling skills: `worked.txt` (What I Worked On) in `pg-prepared-mind` for the full Viaweb and YC narrative; `users.txt` (What I've Learned from Users) and `airbnbs.txt` in `pg-running-early-startup`; `swan.txt` (Black Swan Farming) in `pg-idea-validation`.
