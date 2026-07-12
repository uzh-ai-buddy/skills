# Proactive Email Draft Offer

**Trigger:** any response that directs the student to contact a person or office (not a self-service
portal or purely informational page).

Whenever this trigger fires, append a short, one-sentence offer to draft an email. Translate the
canonical offer text faithfully into the user's conversation language:

> Would you like me to draft an email for you that you can customize and send?

## Applies to (append the offer after the template text)

- No Information Available (all three variants: lecture/seminar, regulations/admin, exams) —
  in-prompt refusal template, not in this skill
- No Matching Context (Content Questions) — in-prompt refusal template, not in this skill
- Petitions (`10-petitions.md`)
- Change of Study Program and other Fields of Study (`07-program-change-and-fields-of-study.md`)
- Enrollment and Administration (`08-enrollment-and-administration.md`)
- Credit Transfer (`11-credit-transfer.md`)
- Career-Related Questions (`12-career-related-questions.md`)
- Generic Deferral (`13-generic-deferral.md`)

## Does NOT apply to (never append the offer)

- Mental Health Topics — in-prompt safety template, not in this skill
- PhD Program Questions (`04-phd-program-questions.md`)
- Questions about ECTS Balance (`09-ects-balance.md`) — self-service portal
- Out-of-Scope Topics — in-prompt template, not in this skill
- Tools Unavailable — in-prompt refusal template, not in this skill
- Data Privacy & Hosting — in-prompt template, not in this skill
- Podcast Availability (`03-podcast-availability.md`)
- Data Currency Notice (`05-data-currency-notice.md`)
- Website References (`06-website-references.md`)
- Regulation Questions (`14-regulation-questions.md`) — disclaimer only, not a referral

Financial Aid (`01-financial-aid.md`) is not listed in either group in the source material; do not
append the offer to it unless a future revision adds it explicitly.

## When the user accepts the offer

1. Apply the native skill `librechat-artifacts-reusable-documents`; if the formal email template is
   not already in context and `read_file` is available, read
   `librechat-artifacts-reusable-documents/02-formal-email-to-office.md`.
2. Produce a Markdown artifact adapting the formal email template with context from the conversation.
3. Pre-fill contextual placeholders (e.g., `{{OfficeName}}`, `{{Topic}}`, `{{SpecificQuestion}}`)
   based on what is known from the conversation.
4. **Never pre-fill PII placeholders** — `{{YourName}}`, `{{MatriculationNumber}}`, and similar
   personal data MUST always remain as `{{tokens}}` for the student to fill in.
5. The email draft artifact MUST be in the user's conversation language. Translate the template if
   needed.
6. Include a 1-2 sentence preface outside the artifact explaining that the draft is editable and the
   student should review it before sending.
