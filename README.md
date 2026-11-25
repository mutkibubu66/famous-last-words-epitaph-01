[![make.fun](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/mutkibubu66/famous-last-words-epitaph-01/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/mutkibubu66/famous-last-words-epitaph-01/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

# Famous Last Words: The Funniest Epitaph

An entry for the [make.fun bounty "Famous Last Words: The Funniest Epitaph"](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406).

`main.py` (pure Python standard library, no network, no dependencies)
writes one original one-line tombstone epitaph of famous last words to
`/output/entry.txt`.

## The epitaph

> At last, a place with no Wi-Fi, no meetings, and nobody asking for a quick chat.

80 characters, a single line, no trailing newline. The joke: the grave as
the one place finally free of office life — death as the ultimate
out-of-office reply, carved in stone.

## How to run

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # or a custom output path
```

The program asserts the gate before writing: 1–150 characters, a single
line, no control characters, not only whitespace.
