PaperOS Architecture v0.2

See FoundersEdition/src/28-SystemArchitecture.md through
33-Applications.md (Part IV — Architecture) for the reasoning behind
every decision below. This document states the how. The book states
the why.

Goal

Build a portable computing environment whose core is independent from
hardware.

Initial implementation target

The first implementation targets the XTEInk X4 because of its active
developer community.

This is an implementation target, not the identity of the project.

Layered architecture

Applications

↓

Document Model

↓

Rendering

↓

Hardware Abstraction Layer (HAL)

↓

Platform Drivers

↓

Hardware

Compatibility Layer sits beside this stack, not inside it. See
“Compatibility subsystem” below.

Applications never access hardware, rendering or platform drivers
directly. Every layer depends only on the one immediately beneath it.

HAL responsibilities

-   Display
-   Keyboard / Input
-   Storage
-   Time
-   Power
-   Networking
-   Audio (future)

HAL exposes one small, stable vocabulary — draw this, read this key,
report this battery level — that never changes across devices.
Platform Drivers are the concrete, per-device implementations plugged
in underneath that vocabulary: HAL is the interface, drivers are what
fulfill it for a specific chip or panel. Nothing above the HAL is
permitted to reach past it into a driver directly.

Rendering

Rendering sits directly above the HAL. It turns a description of
content — this text, at this position, at this size — into pixels or
ink, and has no knowledge of what that content means or why it is
being shown.

Rendering must support:

-   1-bit displays
-   grayscale displays
-   desktop windows
-   ANSI terminals

without changing application code. E-ink backends must handle partial
and full-region refresh explicitly, to avoid ghosting; other backends
do not need to.

Document Model

The Document Model is the layer applications actually talk to. It
holds a document in the same format on disk and in memory — no import
step, no export step, no proprietary intermediate representation.
Applications read and write through this layer only; they never touch
Rendering or the HAL directly.

Applications

An application is a small, single-purpose program operating on
documents handed to it by the Document Model. It has no direct access
to hardware, no ability to invent its own storage format, and no path
to Rendering except through what the Document Model and the interface
layer expose to it.

Compatibility subsystem

Historic environments (initially DOS) run inside a sealed, sandboxed
container — never inside the main layer stack above. Legacy software
never talks to Rendering or the HAL. It talks only to the Document
Model, through ordinary files: virtual drives expose PaperOS documents
directly to legacy applications, and documents legacy applications
produce are indexed and readable the same way as everything else.

Desktop backend

A desktop implementation will be used for rapid development, testing
and debugging.

Embedded firmware becomes another compilation target, implementing the
same HAL contract.

Long-term portability

Planned targets include:

-   M5Stack Paper S3
-   Desktop (Linux, macOS, Windows)
-   ANSI Terminal
-   Additional e-ink devices

Each new target requires only a new HAL implementation and, where
display behavior differs meaningfully, a new Rendering backend.
Nothing above those two layers should need to change.
