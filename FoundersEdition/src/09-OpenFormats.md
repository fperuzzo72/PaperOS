Open Formats

A sheet of paper needs no manual. Anyone who has ever learned to read
can pick one up, centuries after it was written, and understand it
without consulting a specification, a license, or a company that may
no longer exist. That is the entire ambition behind an open format: a
way of storing an idea that asks nothing of the reader except the
ability to read.

PaperOS commits to formats that already met that bar before this
project existed, rather than inventing new ones that would need to
earn it. Markdown for text that wants light structure. Plain text for
text that wants none. CSV for anything tabular. TOML and INI for
configuration a person might actually want to open and edit by hand.
EPUB for books, and PDF for documents whose layout matters as much as
their words. None of these formats belong to PaperOS, and none of them
need PaperOS’s permission to be read. They are specifications,
published and stable, that any programmer anywhere could implement
from scratch with nothing more than the documentation and enough
patience.

------------------------------------------------------------------------

Every software project eventually faces the same temptation: design a
smarter format, one purpose-built for the exact features the product
wants to offer, richer than anything generic that already exists. It
is rarely a bad-faith decision. It usually starts as an honest
engineering trade-off, made by people who can plainly see what an
off-the-shelf format cannot do. PaperOS resists that temptation
deliberately, because the cost of a proprietary format is never paid
by the team that designs it. It is paid later, by whoever is still
holding a file the software that once read it can no longer open.

When PaperOS genuinely needs to represent something a plain Markdown
file cannot — metadata about a journal entry, structure for a task
list, configuration for an application — the answer is to extend an
open format rather than replace one. A block of structured frontmatter
at the top of a Markdown file. A companion file sitting quietly next
to the original, in a format just as legible as the one it describes.
The document underneath stays exactly what it always was: readable by
anything, including software that will exist only after everyone
currently working on this project has moved on to something else.

------------------------------------------------------------------------

This is also why the filesystem itself carries philosophical weight in
this project, not merely a technical one. A folder full of Markdown
files is not a database PaperOS happens to expose. It is the actual,
complete, final storage of a person’s work, with nothing hidden behind
it. Nothing needs to be exported, because nothing was ever imported
into some proprietary container to begin with. Copy the folder to a
USB drive, a different operating system, a computer that will not
exist for another twenty years, and the files inside it will still
open, still make sense, and still belong entirely to whoever is
holding them.

Open formats are sometimes treated as a courtesy — a nice thing to
offer users who care about such things. PaperOS treats them as a
precondition. A format that only one piece of software can read is not
really a document. It is a hostage, however comfortable the room it is
being held in.
