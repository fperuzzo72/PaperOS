Rendering

A page of paper and a page on a screen share a word, and almost
nothing else about how they come to exist. Ink sits still once it
dries. Pixels have to be told, over and over, to keep being what they
were a moment ago, and the way that telling happens is where an entire
category of design mistakes usually enters a system uninvited. PaperOS
keeps rendering in its own layer specifically so those mistakes have
nowhere to hide.

Rendering’s job is narrow on purpose: take a description of what
should appear — this text, in this position, at this size — and put it
on the screen. It has no opinion about what the text means, why it is
being shown, or what happens when someone taps near it. That
separation is what lets the same interface logic run, unmodified, on
hardware that behaves completely differently underneath. An electronic
paper display refreshes slowly, partially, and unevenly if pushed
carelessly — a full-screen redraw can leave a visible ghost of whatever
was there a moment before, which is why e-ink rendering has to think
deliberately about which regions actually need to change and which can
be left alone. A desktop monitor has none of these constraints and
almost the opposite failure mode: it can redraw so fast that
unnecessary motion becomes a distraction rather than a limitation.
Interface logic sitting above the rendering layer never has to know
which of these situations it is in. It describes intent. Rendering
decides how that intent becomes light.

------------------------------------------------------------------------

This division also protects the calm computing argument made earlier
in this book in a very literal way. An animation that exists only
because a rendering engine makes animation easy is not a decision
interface logic gets to make casually, because interface logic does
not control motion directly — it can only ask, and rendering is
designed to say no by default. Restraint here is not a matter of
discipline enforced by a style guide. It is a property of the boundary
itself: the layer that would need to cooperate with unnecessary
movement simply is not asked to unless a real reason exists.

------------------------------------------------------------------------

Keeping rendering separate also means keeping it replaceable. A future
backend for a different display technology, or for a completely
different form factor, only has to reimplement this one layer
faithfully. Everything built on top of it — every application, every
document view, every piece of interface logic already written —
continues working exactly as it did, because none of it was ever
allowed to know how the pixels actually got there.
