Glossary

Calm Computing
An approach to software design in which technology remains available
without constantly demanding attention. Not to be confused with slow
computing — calm computing does not ask hardware or software to be
less capable, only less interruptive.

Compatibility Layer
The contained environment inside PaperOS where legacy software runs,
sealed off from the modern rendering layer and HAL, communicating with
the rest of the system only through ordinary documents.

Documents Before Applications
The principle that a document should be the first thing a person sees
when returning to their work, with the application that opens it
arriving only in service of it — not the other way around.

HAL (Hardware Abstraction Layer)
The lowest layer of PaperOS’s architecture, and the only part of the
system permitted to know the specifics of the hardware it runs on.
Everything above it depends on a small, stable vocabulary the HAL
guarantees, regardless of the device underneath.

Hardware Independence
The design principle that PaperOS’s identity is philosophical rather
than technological, and that the system must be able to move to new
hardware without its ideas being rewritten along with it.

Longevity
The requirement that documents, interfaces and keyboard shortcuts
remain usable and familiar for decades, treated as a non-negotiable
constraint rather than an aspiration.

Open Format
A file format, such as Markdown, plain text, CSV, TOML, INI, EPUB or
PDF, that is published, stable, and implementable by anyone without
needing PaperOS’s permission or cooperation.

Ownership
The principle that a person’s documents, habits and data belong to
them alone — measured concretely by their ability to close a notebook,
walk away, and find everything exactly as it was left, without
advertising, surveillance or a mandatory account standing in the way.

Rendering
The layer responsible for turning a description of content into
pixels or ink on a specific display, kept deliberately ignorant of
what that content means or why it is being shown.
