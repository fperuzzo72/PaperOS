Documents

Most software keeps two versions of a document at once without ever
admitting it: the version sitting on disk, and the version living
inside the application’s own memory, restructured into whatever
internal format makes the program’s code easiest to write. The two are
kept in sync, more or less, through periodic saves, and the gap between
them is where a surprising share of lost work has always lived — the
file that did not save before the crash, the edit that only existed in
memory when the battery died.

PaperOS’s document architecture tries to close that gap rather than
manage it more carefully. Wherever practical, the format on disk and
the format held in memory while editing are the same format, not two
representations kept loosely aligned. A Markdown file being edited is
still, structurally, a Markdown file while it sits in memory — not a
proprietary editor-internal tree that gets serialized back into
Markdown only at save time. There is no import step when a document is
opened and no export step when it is saved, because nothing was ever
converted into something else to begin with. The Open Formats chapter
already argued that a document should never become a hostage to the
application that happens to be holding it. This is the part of the
architecture that makes that argument literally true rather than
aspirational.

------------------------------------------------------------------------

This has a quieter benefit beyond crash safety. When the in-memory
state and the on-disk state are the same thing, an external program — a
different editor, a synchronization tool, a script written by someone
who has never heard of PaperOS — can safely read or even modify a
document while it happens to be open elsewhere, because there is no
hidden internal state it could conflict with. Two eras of software,
described throughout Part III, meeting peacefully around the same file
is not just a nice image. It is a direct consequence of refusing to
let any application build a private, unshareable model of what a
document actually is.

------------------------------------------------------------------------

Where PaperOS genuinely needs richer structure than a plain open format
naturally offers — the way a journal entry might need a date, or a
task might need a status — that structure is added the way Open
Formats already described: as a visible, human-readable extension
sitting inside or alongside the format, never as a hidden binary layer
bolted underneath it. The document a person can see is always the
whole document. Nothing important is ever kept somewhere they cannot
look.
