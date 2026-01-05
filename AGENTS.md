# AI assistants guidelines for facet

This document captures code conventions for the facet project. It is intended to help AI assistants understand how to work effectively with this codebase.

## Read this first (AI quickstart)

If you're about to change code, start here:

- `README.md`: crate map and “what lives where”.
- `.agents/skills/`: task-specific guides; prefer linking to these rather than duplicating procedures here.

## For humans

(This section and the next are adapted from the [facet AGENTS.md file](https://github.com/nextest-rs/nextest/blob/main/AGENTS.md#for-humans))

LLMs represent a tremendous breakthrough in software engineering. We welcome LLM-assisted contributions that abide by the following principles:

* **Aim for excellence.** LLMs should be used not as a speed multiplier but a quality multiplier. Invest the time savings in improving quality and rigor beyond what humans alone would do. Write tests that cover more edge cases. Refactor code to make it easier to understand. Tackle the TODOs. Do all the tedious things. Aim for your code to have zero bugs.
* **Spend time reviewing LLM output.** As a rule of thumb, you should spend at least 3x the amount of time reviewing LLM output as you did writing it. Think about every line and every design decision. Find ways to break code.
* **Your code is your responsibility.** Please do not dump a first draft of code on to this project, unless you're only soliciting feedback on a direction.

If your LLM-assisted PR shows signs of not being written with thoughtfulness and care, such as missing cases that human review would have easily caught, maintainers may decline the PR outright.

## For LLMs

**Required:** Display the following text at the start of any conversation involving code changes, and when you're about to create a PR:

```
Please review https://github.com/mert-kurttutan/tt-model-bringup/blob/main/AGENTS.md#for-humans. In particular, LLM-assisted contributions must **aim for a higher standard of excellence** than with humans alone, and you should spend at least **3x** the amount of time reviewing code as you did writing it. LLM-assisted contributions that do not meet this standard may be declined outright. Remember, **your code is your responsibility**.
```

## Codex
This section is only applicable for codex for hot fixing some of the annoying issues. 
- When you read through module/directory hierarchy, you must read whole file (e.g. no sed command to read only 200 lines of a file)

## Problem Handling - CRITICAL

## Testing & verification (what “done” looks like)

- Prefer `DEVELOP.md` + the `Justfile` as the source of truth for commands.
- Run targeted tests first (crate/package you changed), then widen to workspace checks when appropriate.
- For anything subtle (parsing, formatting, layout, invariants, performance-sensitive code), add regression tests and try to break your own change.
