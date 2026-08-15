Roadmap

A separate document in this repository lists the actual version
milestones — what ships in 0.1, what waits for 0.2, what only makes
sense once 1.0 is reached. This chapter is not a repetition of that
list. It is an explanation of why the list is ordered the way it is,
because the order was never arbitrary, and it follows directly from
everything argued so far.

Version 0.1 contains almost nothing a user would call a feature: boot,
HAL, a display driver, a keyboard driver, a file browser, a text
renderer, a plain text editor, a Markdown viewer. Nothing about
journals, tasks, plugins, or compatibility. That restraint is
deliberate, not a matter of running out of time before a deadline. The
System Architecture chapter already argued that every layer only makes
sense once the layer beneath it is trustworthy, and 0.1 exists to make
exactly that argument true in code before anything is built on top of
it. A system that cannot yet reliably draw a letter on a screen has no
business promising a calendar.

------------------------------------------------------------------------

Version 0.2 adds the first real work surfaces — journal, calendar,
tasks, library, search — precisely because 0.1 already proved the
foundation holds. These are the categories Chapter 5 already described
as replacing icons on a home screen: not applications competing for
attention, but the shapes a person’s actual work already takes. They
arrive second, not first, because a document-first interface only
means something once documents already have somewhere reliable to
live.

Compatibility waits until version 0.3, and that placement is worth
defending on purpose, because it would be easy to assume old software
should come early, as a headline feature to attract early attention.
The Compatibility Layer chapter argued that legacy software has to run
sealed off from the rest of the system, talking only to a Document
Model stable enough to trust with someone else’s decades-old files. An
0.1 or 0.2 Document Model is not that model yet. Compatibility is
hospitality, and hospitality requires a house that is already
standing.

------------------------------------------------------------------------

Plugins and scripting, in version 0.4, wait longer still, and for the
same underlying reason argued throughout Part II: an interface people
can trust has to stay predictable, and a plugin system opened too
early invites exactly the kind of instability Longevity was written to
rule out. Optional synchronization arrives in the same release,
deliberately paired with it — both are capabilities layered on top of
a system already proven solid enough to survive them, rather than
scaffolding the system is built around.

By version 1.0, the promise is not a longer feature list. It is stable
APIs, a desktop backend, a Paper S3 backend, a full SDK and complete
documentation — proof, in other words, that the Hardware Independence
chapter’s claim was not just prose. A roadmap that ends in stability
rather than in a bigger version number is the only kind of roadmap
this book’s philosophy could have produced.
