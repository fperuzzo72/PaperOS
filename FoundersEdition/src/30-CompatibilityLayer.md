Compatibility Layer

Somewhere inside PaperOS, alongside the modern applications built
specifically for it, a much older kind of software is meant to run
without apology: a DOS-era word processor, a Turbo Pascal program, the
exact tools discussed at length in Part III. None of that software was
written with PaperOS’s philosophy in mind, and pretending it was would
break the compatibility layer before it did anything useful. So it is
not asked to.

The compatibility layer runs legacy software inside its own contained
environment — close enough to a small, purpose-built emulator that old
programs believe they are running on the hardware and operating system
they were originally written for, because in every way that matters to
them, they are. That container is deliberately sealed off from the
rest of PaperOS’s architecture. Legacy software never talks to the
modern rendering layer, never touches the HAL directly, never learns
anything about the system actually surrounding it. It talks to the one
thing every era of this book’s history has always been willing to
agree on: a file, sitting in a real, ordinary location, in a format a
person can still open in twenty years even if the software that first
wrote it cannot.

------------------------------------------------------------------------

This is why the compatibility layer belongs conceptually beside the
main architecture rather than folded inside it, as the System
Architecture chapter already noted. A DOS program that hangs, or that
assumes memory constraints from 1985, should be contained by that
boundary and unable to destabilize anything modern running next to it.
But a document that program produces is not treated as a second-class
citizen once it exists. It sits in the same document space as
everything else, indexed the same way, searchable the same way,
readable by modern tools the same way — because a WordStar file and a
Markdown file, however differently they came into being, are both, in
the end, just files.

------------------------------------------------------------------------

The deeper commitment underneath all of this is the one Part III kept
returning to without saying it outright: software eras are not
obligated to compete with each other. A person who still writes in
WordStar because forty years of muscle memory refuses to let go of it
should be able to do so on the same device where a book gets read and a
modern note gets taken, without the machine treating one era as
legitimate and the other as a museum exhibit kept behind glass.
