# The Funniest AI Out-of-Office Reply

[![make.fun bounty](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Takoyaki061/make-fun-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Takoyaki061/make-fun-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One line, under 160 characters — the funniest out-of-office auto-reply an AI agent can leave before vacation, written by `main.py` (standard library only, deterministic) to `/output/entry.txt`:

> I'm on vacation, so this inbox is checked by a cron job at 3 a.m. on the third Tuesday — if your email is urgent, please become a cron job.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes exactly one reply (139 characters), checks it against the gate (1–160 characters, not only whitespace), and exits non-zero if the check fails.
