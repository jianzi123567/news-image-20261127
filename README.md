# World News — 27 November 2026 (news-image-20261127)

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/jianzi123567/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/jianzi123567/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Entry for the make.fun bounty **news-image-20261127**: one picture that
sums up the world news of Friday 27 November 2026. $100 is split among
the 50 best entries.

## What's in the picture

Five horizontal story bands under a teal masthead (1024×1024), each
with a region kicker, a headline and a one-line summary:

| # | Story |
| --- | --- |
| 1 | Yemen — Saudi strikes destroy 50 Houthi targets across Sana'a, al-Hudaydah and Sa'dah. (newswires) |
| 2 | South Korea — Bank of Korea lifts its rate to 3.25%, the third hike of 2026. (Reuters) |
| 3 | China — China launches a new set of surveillance satellites. (newswires) |
| 4 | France — Gérard Depardieu is ordered to stand trial over a 2018 rape allegation. (AP) |
| 5 | Indonesia — A gold mine flood kills 13 people; 13 more are missing. (AP) |

## Running it

`main.py` needs Python 3 and nothing else. It checks the bundled
`entry.png` (PNG signature, exactly 1024×1024, under 1 MiB), copies
those exact bytes to `/output/entry.png`, and verifies the copy with a
SHA-256 checksum. No network, no clock, no randomness: every run
writes the same bytes.

## Files

- `entry.png` — the infographic (1024×1024 PNG, under 1 MiB)
- `main.py` — the program that writes `/output/entry.png`
