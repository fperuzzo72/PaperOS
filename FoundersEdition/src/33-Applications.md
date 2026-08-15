Applications

An application, inside PaperOS, is a small and specific promise: it
knows how to do one thing with documents, and it agrees to stay inside
that boundary. It does not reach into hardware directly — the HAL and
rendering layer already stand between it and the screen. It does not
invent its own private document format — the document architecture
already insists otherwise. What is left, once those temptations are
removed, is something closer to what an application was always meant
to be before the word grew to mean an entire platform unto itself: a
focused tool that opens a document, does something useful to it, and
gets out of the way.

This narrowness is a design requirement, not a limitation apologized
for. Chapter 5 already argued that the system should organize itself
around activities — reading, writing, drawing, retrocomputing — rather
than around brand names competing for a launcher slot. Applications
built this way make that argument literally enforceable: a reading
application only needs to know how to read, and has no legitimate
reason to ask for anything beyond the document it was handed and the
small, well-defined surface the rendering layer offers it.

------------------------------------------------------------------------

That narrowness also does the quiet work the Ownership chapter
promised. An application with no direct hardware access and no ability
to invent its own storage has, by construction, very little room left
to do the things that chapter ruled out entirely — watching what a
person reads, phoning home with usage data, holding a document hostage
inside a format only it understands. None of this requires a
permissions dialog asking for trust after the fact. The architecture
simply never hands out the capability in the first place.

------------------------------------------------------------------------

None of this prevents an application from being genuinely powerful
within its own activity. A drawing tool can be as sophisticated as
drawing requires. A programming environment can be as capable as
programming requires, following the same lesson Turbo Pascal already
taught this book about the value of a fast, immediate feedback loop.
What an application in PaperOS never becomes is a destination competing
for a person’s whole day. It remains what Chapter 3 already asked
every part of this system to remain: a tool that disappears the moment
the work it was built for is done.
