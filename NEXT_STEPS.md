# Editorial Roadmap

Immediate priorities

1. Complete the philosophical chapters (Part II): done.
   - Ownership ✓ (includes Freedom, folded in from the Manifesto)
   - Longevity ✓
   - Open Formats ✓
   - Hardware Independence ✓

2. Complete the historical chapters (Part III): all originally planned
   sub-chapters are done.
   - MSX ✓
   - Sinclair ✓
   - Commodore 64 ✓
   - MS-DOS ✓
   - Macintosh ✓
   - Amiga ✓
   - UNIX ✓
   - WordStar ✓
   - Turbo Pascal ✓
   - Amstrad (not originally planned — suggested addition, still open;
     the Sinclair chapter references the 1986 acquisition and flags
     Amstrad as deserving its own chapter)

   Three further additions, suggested in the previous pass, are now
   written and placed for narrative impact rather than tacked onto the
   end:
   - Xerox PARC ✓ — placed between MS-DOS and Macintosh, since the
     Macintosh chapter's whole argument (consistency applied to a
     borrowed idea) depends on PARC's story landing first. The
     Macintosh chapter's opening was trimmed to cross-reference PARC
     instead of re-explaining it.
   - Palm and Newton ✓ — placed after Turbo Pascal, closing the
     hardware/software platform chapters before the two additions
     below and setting up the shift toward PaperOS's own device class.
   - E Ink ✓ — placed last in Part III, deliberately, as the direct
     hardware lineage PaperOS's own display descends from — the
     chapter that hands off straight into Part IV's Rendering and HAL.

   The Chapter 7 introduction's platform tag list and the Epilogue's
   enumeration paragraph were both updated to include all thirteen
   sub-chapters in final order (previously only referenced the
   original ten).

   Chapter numbering: Part II-IV chapters are currently unnumbered in
   the source files (only Chapters 1-7 carry numbers, a holdover from
   before the book was split into Parts). This needs a full
   renumbering pass once the Part I-V structure is finalized.

3. Complete Part IV (Architecture): done.
   - System Architecture ✓
   - HAL ✓
   - Rendering ✓
   - Documents ✓
   - Compatibility Layer ✓
   - Applications ✓

4. Write:
   - Preface ✓
   - Bibliography ✓
   - Glossary ✓
   - Epilogue ✓ ("The Computer That Waits")

   Ordering: resolved. Part V now exists (see item 7), so the Epilogue
   was moved to sit after it, with Bibliography and Glossary as the
   final back matter, as originally planned.

5. Manifesto: distilled ✓ — MANIFESTO.md rewritten as v2.0, drawing on
   the full book rather than standing alone. Intended as a first draft
   ahead of a general review pass across the whole project.

6. Reconcile docs/architecture.md with Part IV: done ✓ — bumped to v0.2.
   - Fixed the layer stack: it previously read Applications → System
     Services → User Interface → HAL → Platform Drivers → Hardware,
     which didn't match the book (and put UI in an odd place, below
     System Services). Now reads Applications → Document Model →
     Rendering → HAL → Platform Drivers → Hardware, matching Part IV
     exactly, with HAL as the stable interface and Platform Drivers as
     the concrete per-device implementations beneath it.
   - Rendering is now named as its own layer (previously only implied
     under "User Interface").
   - Compatibility subsystem reframed as sitting beside the stack, not
     nested inside System Services, matching the Compatibility Layer
     chapter's "sits slightly apart, deliberately."
   - Both docs/architecture.md and docs/design.md now point back to
     the relevant Founder's Edition chapters at the top ("this
     document states the how, the book states the why"), so the two
     registers stay explicitly linked instead of silently drifting
     apart again.

7. Complete Part V (The Future): done ✓
   - The Community ✓ — the XTEInk X4 developer community and the
     retrocomputing community from Part III, plus the tension between
     welcoming contribution and keeping the architecture's boundaries
     non-negotiable (ties to Calm Computing and the HAL/Document Model
     split).
   - Roadmap ✓ — explains the reasoning behind ROADMAP.md's existing
     version sequence (why compatibility waits for 0.3, why plugins
     wait for 0.4) rather than repeating the list. ROADMAP.md now
     points back to this chapter.
   - Why PaperOS Matters ✓ — the direct case against reading the whole
     project as nostalgia, closing Part V before the Epilogue.

   All five Parts, plus front and back matter, are now written.

8. Not yet started:
   - General review pass across the whole book plus the new Manifesto
     (planned next, per the author).
   - Chapter numbering pass (see item 2) is still open.

9. Publish Founder's Edition v1.0
