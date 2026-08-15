HAL

Somewhere beneath every screen PaperOS will ever draw on sits a
boundary that is not allowed to move: the line between code that knows
what hardware it is running on, and code that does not, and never gets
to ask.

That boundary is the hardware abstraction layer, and its entire job is
narrower than its name suggests. It does not try to make every device
the same. An electronic paper display and a desktop monitor behave
nothing alike, and the HAL does not pretend otherwise. What it does
instead is translate: whatever a display, a keyboard, a battery sensor
or a storage chip actually does, in whatever specific and idiosyncratic
way that particular piece of hardware does it, the HAL restates it in
one small, stable vocabulary that the rest of the system is allowed to
depend on completely. Draw this. Read this key. Report this battery
level. Everything above the HAL speaks only that vocabulary, and never
learns the dialect underneath it.

------------------------------------------------------------------------

This is where the argument made in the Hardware Independence chapter
stops being a philosophical position and becomes an engineering
discipline. It is easy to promise, in prose, that a system will not
depend on any one device. It is a different thing entirely to
structure the code so that the promise cannot quietly be broken by a
developer in a hurry, reaching one layer too far down because it was
faster than doing things properly. The HAL exists specifically to make
that shortcut impossible, not merely discouraged. If a new panel, a
new input method, or an entirely new class of device — a desktop, a
terminal, hardware that does not exist yet — needs support, the work
happens once, inside the HAL, and nothing above it has to be touched,
let alone rewritten.

------------------------------------------------------------------------

The first implementation of this boundary targets the XTEInk X4, and
everything the HAL exposes to the rest of the system is deliberately
written as though a second, very different device were going to be
plugged in tomorrow. That discipline is expensive in the short term. A
team in a hurry could always ship something faster by letting the
layers blur together, just this once. PaperOS treats that shortcut as
a debt the project refuses to take on, because a HAL that gets
compromised once tends to get compromised everywhere, quietly, until
portability is a claim the documentation makes rather than a property
the code actually has.

A boundary that can be crossed under pressure is not a boundary. It is
a suggestion, and this is the one place in the system PaperOS is not
interested in being flexible about it.
