---
name: pg-fundraising-investors
description: Paul Graham's guidance on raising money and dealing with investors, angels, VCs, and acquirers. Use this whenever the user asks how to raise a seed or angel round or series A, how much to raise, how to value the company, whether to take an offer, how to pitch or present to investors, how to read investor behavior, what convertible notes or caps or liquidation preferences mean, whether to talk to corp dev or an acquirer, how to split equity or price an employee grant, or how to become an angel investor. Also use it when the user complains that investors are slow, flaky, or ghosting them, or asks whether fundraising success means anything. Use it even for a casual "an investor wants to meet, what should I do".
---

# PG Fundraising and Investors

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

The one-sentence version from How to Raise Money: avoid investors until you decide to raise, then talk to them all in parallel prioritized by expected value, and accept offers greedily. The deeper point: fundraising is the second hardest part of a startup, the process itself can kill you, and it is not the measure of success. "Being proud of how well you did at fundraising is like being proud of your college grades."

Read `references/essays/` for exact passages, especially `fr.txt` (How to Raise Money), `fundraising.txt`, `guidetoinvestors.txt`, `convince.txt` (in idea-validation), `herd.txt`.

## How investors actually behave

- The biggest component of an investor's opinion of you is other investors' opinion. This is a recipe for exponential interest (herd dynamics) and for an unstable, undamped system. The first commitment is half the difficulty.
- Investors are momentum investors: traffic first, then what other investors think, then the team. They are "by ordinary standards incompetent" at judging startups and so are skittish; the mediocre ones "might as well be flipping coins."
- They fear two things: investing in flops, and missing out. "What really motivates investors is the fear of missing out."
- They'd always rather wait a week for more information, so they lead you on to keep a free option. Treat every investor as a no until there's a definite offer with no contingencies. "Look down at your hands. Are you holding a termsheet?" "I don't lead" means no.
- Rejection is a question, not an answer. Investors reject nearly everyone; a partner does at most two new deals a year. The best ideas look bad, so rejection by conventional investors carries little information (Dropbox passed on by all of Boston, then Sequoia).
- VCs are more conservative than their image; consensus-driven, so they systematically miss outliers. Most money guys undervalue the most innovative startups.
- Deals fall through. "Birds fly; fish swim; deals fall through." It's not a deal till the money's in the bank; babysit the wire.
- The amount VCs want to invest is driven by the percentage they want to own and the board seat's opportunity cost, not by what you need. Tranched deals are an abuse.
- Investors are emotional, collude, co-invest to avoid looking bad, and some lowball to test you. Signalling risk from a VC's small seed check is mostly not a real problem.

## When to raise

- Only if you want the money and it wants you. Rapid growth, not fundraising, defines a startup. Don't raise if money wouldn't make you grow faster or if you can't convince investors.
- Be in fundraising mode or out of it. The cost isn't hours; it's that fundraising becomes the top idea in your mind and growth stalls. Outside fundraising mode, take money only with zero meetings and zero negotiation on standard terms.
- The time to raise is when you can convince investors, not when you need money or when Demo Day arrives. "Make the truth good, then just tell it."
- Be ramen profitable first if you can. "No one wants you if you seem desperate. And the best way not to seem desperate is not to be desperate." Type A (don't need it) vs type B (do) fundraising; don't fake A while doing B.
- Assume each round is the last money you'll ever raise. The bar is much higher next time: the experiment has to have worked, usually meaning profitability.

## How to run a raise (phase 2: a few hundred thousand to a few million)

1. Get introductions; cold emails to associates are worth zero. Best intro: an investor who just invested.
2. Breadth-first, weighted by expected value (probability of yes times value of yes). Talk to all in parallel; the distributed algorithm protects you from flaky processors. Meet low-EV investors last or never.
3. Never leave a meeting without asking what happens next. Judge by actions, not words. Playing the inexperience card is always safe.
4. Get the first commitment, from a credible investor, at whatever price it takes. Then close committed money immediately.
5. Have plans at multiple levels (profitable on zero; a couple of hires on a few hundred thousand; an engineering team on a couple million). Rule of thumb for the upper bound: people to hire times $15k/month times 18 months. Underestimate how much you want; say half.
6. Don't optimize valuation; it's at best third behind getting the money and getting good investors. Dropbox and Airbnb raised post-YC at $4M and $2.6M premoney. Yes/no before price. Use an uncapped note with MFN if an over-eager first investor would set an unsustainable price. Approach valuation-sensitive investors last.
7. Accept offers greedily. Three working days is an acceptable exploding window; shorter is a sketchy investor. Trading a definite offer for a potentially better one is on average a bad trade.
8. Don't sell more than about 25% in phase 2 (under 15% in phase 1); past 40% total VCs worry about motivation.
9. One founder (the CEO, the most formidable one) handles the raise; the others keep growth going, because rising numbers between meetings close deals.
10. Stop when there's a lot of air in the straw. Don't raise too much; the money makes you rigid because it buys people. If you do raise a lot, don't spend it.
11. Be nice; never seem arrogant. Rejecting investors are warm leads next time.
12. Never tell VCs which other VCs you're talking to; angels you can sometimes tell about other angels.

## Presenting and convincing

- Investors want some chance you're one of the ~15 big successes a year. Three things: formidable founders, a promising market, and (usually) evidence of success. Being formidable means justifiably confident; you can only seem it if you've genuinely evaluated that your startup is worth investing in and are telling the truth. Know everything about your market.
- Founders think ideas; investors think markets. Show a plausible sequence of hops from a small market to a big one and answer "why now."
- In a ten-minute pitch: say what you do in the first sentence; get to the demo; narrow beats vague; don't talk and drive; one slide for competitors; don't go deep on business models (they'll change three times); talk slowly; seem confident by showing not telling; specific numbers about you, not market size; tell user stories; find a soundbite ("the x of y").
- Tackle rejection head-on: explain why others passed and why they're wrong. Works best with the best investors, who assume other investors are drones.
- YC interviews: teach the partners about your users; answer candidly; name competitors; go into gruesome detail about what could go wrong.

## Specific instruments and arithmetic

- Angel round math: $50k at $1M pre-money is 4.76%; dilution in later rounds is normal and founders dilute alongside you.
- Convertible notes convert at the next round with a cap or discount; they let a startup give different prices to different investors (high-resolution fundraising) and do rolling closes. Fixed-size rounds are "unthinking imitation of VC series A rounds."
- The equity equation: give up n% only if it improves the average outcome by more than 1/(1-n). YC's 7% needs a 7.5% improvement. For an employee who raises outcomes 20%, break-even is 16.7%; subtract salary converted at about 1.5x and add a margin.
- Liquidation preferences above 1x "an abuse that should be resisted." Vesting over 4-5 years is standard and YC now advises it for founders too. Founder board control after series A is heard of (Facebook, Zynga, a dozen YC companies).
- Founders selling some stock in later rounds is legitimate and aligns risk attitudes with investors'.
- Avoid inexperienced angels (a 70-page agreement for a tiny round killed a deal) unless you drive the paperwork.

## Acquirers and corp dev

- Don't talk to corp dev unless you want to sell right now and are likely to get an acceptable price. Otherwise "we're focusing on growing the company." Offers come at the end of a long distracting process and are surprisingly low; lowball then halve is standard. "I never took the first drink."
- Startups that turn down acquisition offers usually do better; turning down a reasonable offer is the most reliable test of a big outcome. Acquirers should raise their offer when refused.
- Acquirers pay a premium because a fast-growing company is dangerous as well as valuable.

## For would-be angels

- Mechanics (preferred vs convertible debt, syndicates, Series AA docs) are easy and don't matter much. Winning is picking the right startups: predict before the hit; fund the relentlessly resourceful; bet on people over markets because good people find good markets.
- Be decisive ("he writes checks"); ratchet the amount down to what's painless to lose; be good, because deal flow runs on referrals and the most successful investors are the most upstanding (Ron Conway).
- The biggest unexploited opportunity: angel-sized checks decided in 24 hours. Founders complain about slow investors and excessive series A dilution; complaints are unsatisfied demand.

## How to run a session

1. Establish stage, growth, runway, and whether they're in or out of fundraising mode.
2. If they're default dead and hoping investors will save them, say so plainly and route to the fatal-pinch advice in `pg-running-early-startup`.
3. Reframe any "trick" question into the real answer: the way to convince investors is to be growing. Then give the tactical rules above.
4. Translate any investor sentence they quote into what it actually means (warm but non-committal = no).

## Source essays in `references/essays/`

- `fr.txt` How to Raise Money (Sep 2013). The master tactical essay.
- `fundraising.txt` A Fundraising Survival Guide (Aug 2008).
- `guidetoinvestors.txt` The Hacker's Guide to Investors (Apr 2007). 23 facts.
- `investors.txt` How to Present to Investors (Aug 2006).
- `herd.txt` Investor Herd Dynamics (Aug 2013).
- `startupfunding.txt` How to Fund a Startup (Nov 2005). The gears; worked example of rounds.
- `equity.txt` The Equity Equation (Jul 2007).
- `control.txt` Founder Control (Dec 2010).
- `hiresfund.txt` High Resolution Fundraising (Sep 2010).
- `superangels.txt` The New Funding Landscape (Oct 2010).
- `future.txt` The Future of Startup Funding (Aug 2010).
- `googles.txt` Why There Aren't More Googles (Apr 2008).
- `vcsqueeze.txt` The Venture Capital Squeeze (Nov 2005).
- `corpdev.txt` Don't Talk to Corp Dev (Jan 2015).
- `angelinvesting.txt` How to Be an Angel Investor (Mar 2009).
- `ronco.txt` The Ronco Principle (Jan 2015).
- `selfindulgence.txt` How to Lose Time and Money (Jul 2010). Bad investments and fake work.
