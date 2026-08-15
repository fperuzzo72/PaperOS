System Architecture

A philosophy earns the right to call itself an architecture only once
it can survive contact with actual hardware, actual memory limits, and
an actual screen that only wants to be touched a few times a second.
This chapter is where that contact happens.

PaperOS is built in layers, and the layers exist for exactly one
reason: so that a change at the bottom never forces a rewrite at the
top. At the very bottom sits the hardware abstraction layer, the only
part of the system allowed to know anything about the specific chip,
the specific display panel, the specific keyboard controller
underneath it. Above that sits rendering, which knows how to put
pixels and text on a screen but has no opinion about what that text
means. Above rendering sits the document model, which understands
documents — their structure, their formats, their location on disk —
but has no idea what shape a screen is, or whether there is a screen
at all. At the top sit applications, which understand a single
activity — reading, writing, drawing — and reach everything else only
through the layers beneath them, never around them.

------------------------------------------------------------------------

This shape is not a diagram drawn after the fact to explain decisions
already made. It is close to the actual order the decisions had to be
made in, because each layer only makes sense once the one below it is
trustworthy. An application cannot commit to being calm if rendering
might interrupt it with an unpredictable delay. Rendering cannot commit
to being predictable if the hardware abstraction layer might leak some
device-specific quirk through it. Every philosophical promise made
earlier in this book — that the system will wait, that documents will
outlive applications, that hardware can be swapped without rewriting
everything above it — depends on a layer beneath it actually holding
that line.

The compatibility layer, discussed later in this part, sits slightly
apart from this stack rather than inside it, deliberately. Old software
was never written with any of these layers in mind, and pretending
otherwise would corrupt the whole design. It is easier, and more
honest, to let legacy systems run inside their own contained space,
talking to the rest of PaperOS only through documents — the one
interface every era of computing has always been willing to agree on.

------------------------------------------------------------------------

None of this is exotic engineering. Layered architecture is one of the
oldest, most thoroughly proven ideas software has, and PaperOS makes no
claim to have invented it. What it claims is something more specific:
that here, the layering is not a convenience for engineers. It is the
mechanism the entire philosophy runs on. Remove it, and every promise
made in the earlier parts of this book becomes a hope instead of a
guarantee.
