---
name: pg-idea-validation
description: Paul Graham's tests for whether a startup or product idea is any good. Use this whenever the user describes a startup idea, business idea, side project, or product and wants feedback, a critique, a sanity check, a go/no-go, a "would this work", a "is this a good idea", or wants to compare several ideas. Also use it when the user is worried about competitors, market size, or whether they're too late, or asks why a famous startup looked bad at first. Apply it even when the user only wants encouragement; run the tests anyway and report honestly.
---

# PG Idea Validation

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

A rubric assembled from Paul Graham's essays. The organizing fact: most startups die from building something no one wants, and the most dangerous ideas are the plausible-sounding ones. Validation is mostly about detecting plausibility without demand.

Two warnings before scoring anything. First, the best ideas initially look like bad ideas (Peter Thiel's Venn diagram: "seems like a bad idea" intersected with "is a good idea"). So a bad first impression is not disqualifying; it's expected. Second, the vast majority of ideas that seem bad are bad. Don't let the first warning become an excuse.

Read `references/essays/` for exact passages, especially `startupideas.txt`, `bronze.txt`, `ace.txt`, `swan.txt`, `convince.txt`.

## The rubric

Work through these in order. Record an answer for each. The user's inability to answer a question is itself a finding.

### 1. Does anyone want this urgently, right now?
The single most important question. "If I had to fund on one question it would be: how do you know people want this?" The gold-standard answer: "we and our friends want it," plus a crude prototype that friends actually use and that's spreading by word of mouth. The fallback: founders who understand the users so deeply you can't ask them a question they don't know the answer to (Airbnb, who had been the first hosts).

Specifically: who would use a crappy version one made by a two-person startup they've never heard of? If the user can't name those people, the idea is probably a "sitcom" idea. The biggest flaw in most startup ideas is that the initial market doesn't exist at all.

Watch for the fatal response pattern: friends say "yeah, maybe I could see using something like that." Summed across the population that's zero users.

### 2. Well or crater?
Plot people who want it against how much they want it. A startup can't dig a crater. Choose a well: a small number of people who want it a lot, over a large number who want it a little. Altair Basic (a couple thousand owners who were otherwise programming in machine language). Facebook at Harvard. Narrowness is a byproduct of depth, and it's a good sign when an idea appeals strongly to a specific group.

Corollary from the 13 Sentences: better a few users who love you than many who are ambivalent. It's easier to expand user-wise than satisfaction-wise, and it's harder to lie to yourself about user counts.

### 3. Is there a path out of the well?
A well is necessary, not sufficient. Facebook was good because colleges are similar enough that it would work at any college, then everyone. Microsoft: Basic for Altair, Basic for other machines, other languages, OS, applications. Ask for a plausible sequence of hops to a big market. "Founders think of startups as ideas; investors think of them as markets." The path is often hard to see, even for PG. Airbnb didn't see theirs. So weight this less than test 1, and ask the Altair question: "What Microsoft is this the Altair Basic of?" Sometimes there are several answers; let the founders follow the most exciting.

Beachhead rule: if the beachhead consists of people doing what lots more people will be doing in the future (works only on the newest phones), it's big enough however small it is.

### 4. Why now?
Every huge company rides an external wave. Rapid change in one area uncovers big soluble problems in another: chip costs made Wozniak's computer buildable; web growth made Google's problem everyone's. Ask what recently changed that makes this a good idea, and why no one else has noticed. If nothing changed, ask why it doesn't exist already.

### 5. Would the founders use it themselves?
"Would you use this thing yourself, if you hadn't written it?" PG asks founders this at YC and is surprised how often the answer is no. Building for other people is possible (Viaweb) but you're flying on instruments, so you must be empirical: find specific users and measure. "Teenagers," "business users," "people interested in local events" are tarpits, not users.

### 6. Is it derivative, marginal, or made-up?
From the 18 Mistakes: imitations of existing companies are a weak source; marginal niches chosen to avoid competition are the eight-year-old shutting his eyes at fly balls ("you can only avoid competition by avoiding good ideas"); made-up ideas are the first thing you thought of. Check the still-life effect: has the user plunged into an idea and now feels too invested to drop it? Time invested doesn't make an idea good. Did they consider other ideas at all? "Of all the things we could make, is this the thing people will pay most for?"

### 7. Is it a toy?
If the only criticism is "that's just a toy," that's good. A toy has everything an idea needs except importance, and if you're living in the future, importance follows. Similarly "inappropriate" and "unqualified" are null criticisms. Real criticisms are "it doesn't work" and "nobody wants it."

### 8. Competition
Feeling late is a sign of a good idea. Ten minutes of web search settles whether someone else is doing it; even if so, you're probably not too late. Startups are almost never killed by competitors; poor execution kills them. A crowded market means demand exists and nothing is good enough yet. Required: a thesis about what everyone in the market is overlooking, phrased more precisely than "we'll make one that doesn't suck." Best case: incumbents lacked the courage of their own convictions (search engines before Google de-emphasizing search). Discard only if a competitor has lock-in that prevents users choosing you.

### 9. Dependencies and schleps
Does the idea depend on deals with big companies to exist (the Reddits' fast-food-by-phone needed carriers and chains)? Those usually don't happen and the delays are fatal. Separate this from schleps, which are fine: a company is defined by the schleps it will undertake, and the fear of them is what keeps competitors away (Stripe).

### 10. The unscalable thing
Think of an idea as a vector: what you'll build plus the unscalable thing you'll do to get going. Can the founders recruit users manually? If there's no way to find and recruit the first users by hand (no peers to sell to, no community to go to), that's a bad idea at least for these founders. Enterprise software in a domain where you have no connections: "should you even be working on such an idea?"

### 11. Activation energy
The user's need has to supply enough activation energy to start using what you make. This varies by domain: enterprise software through traditional channels has very high activation energy; switching search engines is low. The question is not whether what you built is good but whether it's good enough to supply the activation energy required.

### 12. Can it be described in a sentence?
"You probably shouldn't even start a company to do something that can't be described compellingly in one or two sentences." A narrow description beats a vague one. If there's no soundbite ("the Microsoft Word of ecommerce"), the plan may not be focused.

### 13. Does the real test exist yet?
Growth is the measure. If the idea is live, ask the weekly growth rate. 5-7% a week is good in YC; 1% means you haven't figured it out. "A hundred new users a month" is not a rate. Ideas without any usage are hypotheses; treat them as such. If feasible, suggest Paul Buchheit's test: go try to sell it before building it. Founders often come back with a real idea discovered while failing to sell the bad one.

## Things that are not evidence

- Big-market statistics ("millions of people have pets"). Stone soup.
- A business model. Making something people want is ten times harder; the model can come later. Google worked out revenue after search worked.
- Investor interest or rejection. Investors are consensus-driven and systematically miss outliers (Dropbox rejected by all Boston VCs, then Sequoia; Airbnb thought a bad idea by YC). Hot deals don't correlate with success.
- The founders' enthusiasm when the idea was consciously generated. Organic ideas feel like inspirations; manufactured ones that feel that way are probably mistaken.
- Easy money from a source that isn't the real market (Yahoo's banner ads hid that search traffic was worth more).

## Output format

Give a verdict in the first line (promising / needs work / probably a sitcom idea), then the rubric findings as short bullets, then the two or three questions the user most needs to answer and the fastest way to answer them (talk to N specific users, build a crude prototype this week, try to sell it). Be direct. PG's lesson from Artix: he took embarrassingly long to catch on because he was attached to his model of the world. Help the user avoid that.

## Source essays in `references/essays/`

- `startupideas.txt` How to Get Startup Ideas. Wells, paths out, the urgency test, competition, filters.
- `bronze.txt` Why Smart People Have Bad Ideas. The Artix phase, still-life effect, muck and brass, hyenas.
- `ace.txt` Billionaires Build. "How do you know people want this?", larval markets, the YC interview.
- `swan.txt` Black Swan Farming. Best ideas look bad; fundraising success is misleading.
- `altair.txt` What Microsoft Is this the Altair Basic of?
- `newideas.txt` Crazy New Ideas. Take implausible ideas from reasonable domain experts seriously.
- `convince.txt` How to Convince Investors. Markets not ideas, why now, formidable founders.
- `reddits.txt` The Reddits. An idea rejected for its dependencies; one found by observing behavior.
- `airbnb.txt` Subject: Airbnb. How PG argued for an idea investors didn't get; continuum of markets.
- `growth.txt` Startup = Growth. Growth rate as the test; growth as evolutionary pressure on the idea.
- `segway.txt` The Trouble with the Segway. Why secrecy and money hide fatal flaws.
- `yahoo.txt` What Happened to Yahoo. Easy money as an obstacle to seeing value.
