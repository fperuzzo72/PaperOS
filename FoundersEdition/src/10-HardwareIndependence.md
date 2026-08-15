Hardware Independence

A philosophy does not need a specific machine to be true. PaperOS
could describe every idea in this book without a single line of code
ever running, and every idea would still hold. That is worth
remembering whenever the project gets described, understandably, as
“the operating system for e-ink devices.” It is not wrong. It is just
smaller than what is actually being built.

Electronic paper is today’s best available expression of everything
this book has argued for — quiet, low-glare, patient with a battery,
honest about its own limitations in exactly the way paper has always
been honest about its own. It earns its place as PaperOS’s first and
most natural home. But it is an expression of the philosophy, not its
definition, and the two should never be confused for one another. If a
better display technology exists in ten years, quieter still, more
comfortable still, more respectful of attention than even the best
e-ink panel available today, PaperOS should move toward it without a
moment of loyalty to the hardware it started on.

------------------------------------------------------------------------

The first implementation targets the XTEInk X4, and the reason is
almost entirely practical rather than ideological: an active developer
community already surrounds it, and a philosophy without a working
implementation is only ever a book. Future targets are expected to
include the M5Stack Paper S3, conventional desktop operating systems,
and even plain text terminals, because the ideas in this book do not
actually require a screen shaped like a page. They require an
environment willing to stay quiet, stay legible, and stay out of the
way. A terminal can do that. So, in its own way, can a desktop.

------------------------------------------------------------------------

This independence has to be built into the architecture from the
beginning, not bolted on afterward once porting becomes urgent.
Applications should never reach directly into hardware. Rendering has
to stay separated from interface logic, so that a change in display
technology does not require rewriting how software actually behaves.
Platform-specific code stays isolated in its own layer, small and
replaceable, rather than spread invisibly through everything else.
None of this is unusual engineering advice — most well-built software
separates concerns this way as a matter of course. What is unusual is
treating it as a philosophical commitment rather than a convenience,
because the alternative is a system that quietly becomes hostage to
whichever chip or panel happened to be available when it was first
written.

Portability, under this reading, is not a milestone sitting somewhere
on a future roadmap. It is a constraint accepted from the very first
commit, the same way a notebook’s usefulness was never limited to a
single desk. Hardware will keep changing, faster than any philosophy
should have to. PaperOS is designed on the assumption that it will
need to survive hardware it has not been introduced to yet.
