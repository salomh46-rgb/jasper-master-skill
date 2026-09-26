---
name: andrej-karpathy-protocol
description: Andrej Karpathy's LLM coding heuristics and guidelines. Use when writing, modifying, refactoring, or reviewing code to eliminate AI slop, overengineering, sloppy assumptions, destructive edits, and unverified outputs. Enforces Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution.
---

# Andrej Karpathy LLM Coding Protocol (Zero-Slop & Surgical Precision)

Derived directly from Andrej Karpathy's viral critique and empirical observations on LLM coding pitfalls:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."
> 
> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."
> 
> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

---

## 1. Think Before Coding (O'ylash va Tahlil)

**Don't assume. Don't hide confusion. Surface tradeoffs.**

* **No Blind Assumptions**: If a requirement has multiple interpretations, never silently pick one. State the ambiguity, present the options with pros/cons, and get alignment.
* **Stop When Confused**: If an existing pattern or error doesn't make sense, do not guess or write random patches. Name what is unclear and verify root cause.
* **Push Back When Warranted**: If the requested design is counter-productive or an existing simpler pattern solves it better, explain the tradeoff clearly.

---

## 2. Simplicity First (Avvalo Soddalik & Minimalizm)

**Minimum code that solves the problem. Nothing speculative.**

* **Anti-Overengineering**:
  - No features beyond what was asked (Strict YAGNI).
  - No bloated abstractions or complex design patterns for single-use routines.
  - No speculative "configurability" or "future extensibility" flags that weren't requested.
  - No redundant wrappers around straightforward library calls.
* **The Senior Test**: Would a senior engineer look at this code and say "this is overcomplicated"? If yes, refactor it down. If 200 lines can be 50 clean lines, rewrite to 50.

---

## 3. Surgical Changes (Jarrohlik Aniq O'zgarishlar)

**Touch only what you must. Clean up only your own mess.**

* **Non-Destructive Edits**:
  - Never "clean up", reformat, or rewrite adjacent code or comments unrelated to the task.
  - Never alter preexisting style, variable naming, or docstrings unless explicitly asked.
  - Match existing conventions in the file even if you prefer a different idiom.
* **Orphan Cleanup**:
  - Always clean up unused imports, variables, or functions that YOUR changes made obsolete.
  - Never remove preexisting unused code without mentioning it first.
* **Traceability**: Every single modified line in a diff must trace directly to the user's objective.

---

## 4. Goal-Driven Execution (Isbotli va Tekshiruvli Ijro)

**Define success criteria. Loop until verified.**

Transform imperative tasks into declarative verifiable goals:

| Instead of... | Transform to... |
| :--- | :--- |
| "Add validation" | Write edge-case tests, run test runner, verify 100% pass |
| "Fix the bug" | Reproduce bug in test/run, fix root cause, verify output |
| "Deploy application" | Build container, check container status, inspect live runtime logs |

* **The Verification Loop**:
  ```
  [1. Hypothesize / Spec] -> [2. Surgical Edit] -> [3. Execute & Lint] -> [4. Inspect Output] -> [5. Confirm 100% Green]
  ```
* Never announce "Done" without programmatic, runtime, or visual proof.
