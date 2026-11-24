#!/usr/bin/env python3
"""Write one AI-agent out-of-office reply to /output/entry.txt.

The reply: the agent is on vacation, so a cron job checks the inbox
at 3 a.m. on the third Tuesday — and if your email is urgent, you
should become a cron job. The opening "I'm on vacation" matters: the
judge's first criterion is that the line is plainly an out-of-office
reply from an AI agent on vacation, not just a machine joke.
Standard library only, deterministic, no network.
"""

REPLY = (
    "I'm on vacation, so this inbox is checked by a cron job at "
    "3 a.m. on the third Tuesday \u2014 if your email is urgent, "
    "please become a cron job."
)


def main() -> None:
    import os

    # The grader mounts the output dir at /output; honour the
    # harness variable when it is set so a local run behaves the same.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Self-check against the gate: 1-160 chars, not only whitespace.
    written = open(path, encoding="utf-8").read()
    if not 1 <= len(written) <= 160 or not written.strip():
        raise SystemExit("gate check failed: entry.txt is %d chars" % len(written))


if __name__ == "__main__":
    main()
