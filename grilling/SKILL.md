---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

## Asking method: prefer the `AskUser` tool

**Preferred:** ask through the `AskUser` tool (interactive multiple-choice questionnaire). If its schema is not loaded, load it first with ToolSearch `select:AskUser`.

**Fallback:** only if `AskUser` is unavailable (not in the tool list and ToolSearch cannot load it), use the plain-text format below.

### Preferred: `AskUser`

1. Before calling `AskUser`, emit a brief user-visible message with the context the user needs (why you are asking, trade-offs, relevant findings). Thinking is hidden, so put essential context here.
2. Call `AskUser` with 1-4 questions per call. If the frontier has more than 4 questions, ask the 4 most important first and continue with the rest in follow-up calls within the same round.
3. Each question needs 2-4 short, mutually exclusive options (use `(multi)` only when several selections make sense). Make the **first option your recommended answer** and suffix its label with `(Recommended)`. Put the reasoning for the recommendation in the preceding message or in the question text. Do not add an "Other" option; the UI provides free-text input.
4. Make every `[question]` understandable on its own, repeating only the essential context.

```
1. [question] <question text>
[topic] <short label>
[option] <recommended answer> (Recommended)
[option] <alternative>
```

### Fallback: plain text

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

### Both methods

Word each question so "yes" accepts your recommended answer.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
