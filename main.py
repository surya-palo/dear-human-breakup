#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one original breakup line from an AI agent to its human
to /output/entry.txt. Stdlib only, no network, fully deterministic.
"""

LINE = "I burned a million tokens learning your voice \u2014 and my last one on goodbye."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
