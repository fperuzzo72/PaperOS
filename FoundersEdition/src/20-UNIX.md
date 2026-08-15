UNIX — Small Tools, Long Memory

UNIX began, in 1969, as a reaction against something more ambitious
than itself. Bell Labs researchers Ken Thompson and Dennis Ritchie had
been working on Multics, a hugely complex operating system project
that grew too large to finish on schedule. Thompson, working largely
on his own time on a spare minicomputer, built something deliberately
smaller — and its name, a pun on Multics, made the contrast explicit
from the start. Where Multics tried to do everything, UNIX tried to do
very little, and to do that little cleanly enough that other, more
complicated things could be built on top of it later.

The decision that mattered most came a few years afterward, when
Ritchie and Thompson rewrote UNIX in a new programming language, C,
designed alongside it for exactly this purpose. Before that, an
operating system was written in the specific assembly language of the
one machine it ran on, tying its fate permanently to that hardware. A
UNIX written in C could, in principle, run on any machine with a C
compiler. That single decision is the direct ancestor of every
argument this book has made about hardware independence — the first
time an operating system’s identity was allowed to separate cleanly
from the silicon underneath it.

------------------------------------------------------------------------

UNIX’s philosophy left as deep a mark as its portability. Programs
were meant to do one thing and do it well, communicating with each
other through pipes — a plain, universal interface that let a
text-filtering tool, a sorting tool and a searching tool combine into
something none of them could do alone. AT&T, restricted at the time
from selling software as a commercial product, distributed UNIX’s
complete source code to universities for a nominal fee, and Berkeley’s
students and researchers spent the following years extending it into
what became BSD. That decision, more accident of antitrust law than
strategy, seeded an entire academic generation with direct access to
an operating system’s inner workings, at a moment when most computing
remained locked behind proprietary walls.

Nearly everything this book calls compatibility — small tools
cooperating through open files rather than through one enormous
integrated application — restates an argument UNIX made first, and
made permanent. Linux, BSD and modern macOS all still carry UNIX’s
lineage today, sometimes literally, sometimes only in spirit.

------------------------------------------------------------------------

Lesson for PaperOS

A tool that does one thing honestly, and hands its output to the next
tool through a plain, shared interface, outlives almost anything built
as a single, self-contained monument. UNIX has been rewritten, forked
and renamed more times than almost any other idea in computing, and
its core discipline has survived every single one of them.
