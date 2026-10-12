---
name: pg-running-early-startup
description: Paul Graham's operating advice for an early-stage startup, from first prototype to product-market fit. Use this whenever the user is running or about to run a startup and asks what to focus on, when to launch, how to get first users, how to grow, whether to hire, how much to spend, how to handle a cofounder dispute, whether they're default alive or dead, how to survive a cash crunch, how to make the company more powerful, what metric to track, or why their startup feels stuck or demoralizing. Also use it when the user mentions MVP, launch, growth rate, ramen profitability, customer development, doing things that don't scale, or the 18 mistakes. Use it even if the user just describes their situation without asking a direct question.
---

# PG Running an Early Startup

> **Essay text is not bundled.** Paul Graham's essays are copyrighted, so this repo ships only links. Run `scripts/fetch_essays.py` once to download them into `references/essays/` for local use. The script sits two folders above this skill (`../../scripts/`) in both the repo and a plugin install, and needs no arguments from there. If a file there is missing, read the essay from its URL in `references/essays.md` instead.

One mistake kills startups: not making something users want. Everything here is in service of that. Use growth as the compass: pick a weekly growth rate and hit it; whatever gets you there is ipso facto right.

Read `references/essays/` for exact passages, especially `13sentences.txt`, `startupmistakes.txt`, `ds.txt`, `startuplessons.txt`, `aord.txt`, `powerful.txt`.

## The 13 sentences (Feb 2009)

1. Pick good cofounders. 2. Launch fast. 3. Let your idea evolve. 4. Understand your users. 5. Better to make a few users love you than a lot ambivalent. 6. Offer surprisingly good customer service. 7. You make what you measure. 8. Spend little. 9. Get ramen profitable. 10. Avoid distractions. 11. Don't get demoralized. 12. Don't give up. 13. Deals fall through.

If only one survives: understand your users. It underlies half the rest.

## Launch and iterate

- Launch fast because you haven't started working on the product until you've launched. "Launching teaches you what you should have been building." Version one's main value is as a pretext for engaging users. Identify a core that's (a) useful on its own and (b) incrementally expandable; ship that.
- "If your first version is so impressive that trolls don't make fun of it, you waited too long to launch." No startup has died from launching something stable but minimal too early; many have died from launching too slowly.
- Treat the idea as a hypothesis, not a blueprint. Most successful startups end up doing something different. Test for whether pivots are converging: can you reuse most of what you built? Ask users whether they're excited about the new direction.
- Keep pumping out features; each is "one quantum of making users' lives better." If your product seems finished, either it is or you lack imagination, and (b) is a thousand times likelier.
- "No idea for a product could ever be so clever as the ones you can discover by smashing a beam of prototypes into a beam of users."

## Do things that don't scale

- Startups take off because founders make them take off. Recruit users manually. The Collison installation: "give me your laptop" and set them up on the spot. Airbnb went door to door in New York; 30 days of in-person engagement was the difference between success and failure.
- The numbers look small, and that's fine: 10% a week from 100 users is 14,000 in a year and 2 million in two.
- Delight the first users to a degree that would be pathological at scale. Wufoo's handwritten thank-you notes. "I have never once seen a startup lured down a blind alley by trying too hard to make their initial users happy."
- Contained fire: start in a deliberately narrow market where you can get critical mass (Facebook at Harvard). The best early adopters for B2B are other startups.
- Consult for one user; be your own software by hand; pull a Meraki (assemble hardware yourself). Stripe manually set up merchant accounts behind an "instant" interface.
- The Big Launch and the big partnership almost never work. How many successful startups' launches do you remember?
- Think of ideas as vectors: the thing you build plus the unscalable thing you'll do to get going.

## Growth as the compass

- Measure weekly growth, ideally in revenue, else active users. 5-7% a week is good; 10% exceptional; 1% means you haven't figured it out. "A hundred new customers a month" is not a rate.
- Decide every question (conference? hire? feature?) by whether it gets you your target rate. Hill-climbing works in practice because acting beats strategizing and good ideas are adjacent to better ones.
- Growth is evolutionary pressure that can discover a better idea than you started with.
- Excluded: trickery like buying users above lifetime value or metering invites. You'd be throwing off your own compass.

## Money and hiring

- Be cheap. Running out of money is the proximate cause of nearly every death; cheapness is almost interchangeable with iterating fast and keeps companies young.
- Ramen profitable: enough to cover founders' living expenses. The point where survival becomes the default and you no longer need investors' permission to exist. Airbnb's number was $4000 a month taped to the bathroom mirror. Not the destination; a trick for not dying en route. Danger: sliding into consulting.
- Default alive or default dead: assuming constant expenses and current growth, do you reach profitability on the money you have? Half of founders don't know. Start asking too early. The fatal pinch is default dead, slow growth, and not enough time to fix it, usually caused by assuming the next round is easy. Plan B must exist in writing.
- Don't hire too fast. It's the biggest killer of funded startups. The product needs to evolve, not be "built out," and that's easier with fewer people. Airbnb waited four months after raising to hire anyone. Hire only people who write code or get users; pay with equity; "when you raise a lot of money, your company moves to the suburbs and has kids."
- In the fatal pinch: the probability of raising more is zero. Fire the people you already know you should fire; have everyone sell; switch the question to "what do you need that you'd pay a lot for?"; keep IP and don't bill hourly; watch for narrow openings with wide vistas beyond.

## Morale and focus

- Startups rarely die in mid-keystroke. Keep typing. The underlying cause of death is demoralization; the immediate cause is running out of money.
- The number one thing not to do is other things. Any sentence ending "but we're going to keep working on the startup" means you've given up. Grad school is a huge predictor of death.
- Put yourself where failure will be public and humiliating; founders are more motivated by not looking bad than by millions.
- Deals fall through. Treat them as background processes and ignore them till they terminate. Be optimistic only about what you control.
- Startups take over your life, the lows are very low, everything takes 2-3x longer, and it's a grind of lots of little things. Everyone's model of work is a job; that's why it surprises them.
- Not having a specific user in mind, raising too much, obstinacy, fights between founders, and a half-hearted effort are the other killers from the 18 Mistakes. Vest. Don't suppress misgivings about cofounders.

## Making the company more powerful (Sep 2026)

Beyond "how do we make more money," ask what would make the company more powerful; that yields order-of-magnitude changes. Transformations to try: own the customer relationship instead of being a component; make the money (or tokens) flow through you; introduce network effects (even by letting users share benchmarks or opt into training); become a marketplace (can your users pay each other?); go full stack; eat your way through the customer; watch tails that could wag the dog (PayPal was a demo); listen when users "misuse" the product; help users make money; play the long game; be generous (create more value than you capture, open source, APIs); sell to customers who decide fast and early (Stripe signing startups at founding); get the data early (Rippling onboarding). Every move must make customers' lives better or there's no uptake. Often the fix is "just y": stand up straight.

## How to run a session

1. Get the numbers: users, revenue, weekly growth rate, cash, burn, months of runway, headcount. Compute default alive or dead.
2. Find the one problem that matters most this week. Founders know their problems but not their relative importance ("never mind your boyfriend, think about that door").
3. Prescribe actions at a resolution of a week or less, with measurable results. Prefer talking to users, shipping, and manual recruiting over strategy.
4. Check for the classic denials: waiting on a deal, waiting on investors, hiring to fix slow growth, over-engineering, big-launch thinking, not being able to say who the user is.
5. If the question is about an idea rather than execution, hand off to `pg-idea-validation`; if about money, to `pg-fundraising-investors`.

## Source essays in `references/essays/`

- `13sentences.txt` Startups in 13 Sentences (Feb 2009).
- `startupmistakes.txt` The 18 Mistakes That Kill Startups (Oct 2006).
- `start.txt` How to Start a Startup (Mar 2005). Good people, something customers want, spend little.
- `ds.txt` Do Things that Don't Scale (Jul 2013).
- `startuplessons.txt` The Hardest Lessons for Startups to Learn (Apr 2006).
- `really.txt` What Startups Are Really Like (Oct 2009). 19 surprises.
- `die.txt` How Not to Die (Aug 2007).
- `ramenprofitable.txt` Ramen Profitable (Jul 2009).
- `aord.txt` Default Alive or Default Dead? (Oct 2015).
- `pinch.txt` The Fatal Pinch (Dec 2014).
- `powerful.txt` Making Startups Powerful (Sep 2026).
- `users.txt` What I've Learned from Users (Sep 2022). Focus enables speed; founders don't listen because advice is counterintuitive.
- `name.txt` Change Your Name (Aug 2015). Get the .com.
- `foundersatwork.txt` Learning from Founders (Jan 2007). What real productivity looks like.
- `airbnbs.txt` The Airbnbs (Dec 2020). Earnestness; focus on the hottest market; ramen profitable in three weeks.
