PaperOS Architecture v0.1

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

System Services

↓

User Interface

↓

Hardware Abstraction Layer (HAL)

↓

Platform Drivers

↓

Hardware

Applications never access hardware directly.

HAL responsibilities

-   Display
-   Keyboard / Input
-   Storage
-   Time
-   Power
-   Networking
-   Audio (future)

User Interface

The UI describes interface elements rather than pixels.

Backends decide how those elements are rendered.

Rendering

The rendering engine must support:

-   1-bit displays
-   grayscale displays
-   desktop windows
-   ANSI terminals

without changing application code.

Compatibility subsystem

Historic environments (initially DOS) are integrated as system services.

Virtual drives expose PaperOS documents directly to legacy applications.

Desktop backend

A desktop implementation will be used for rapid development, testing and
debugging.

Embedded firmware becomes another compilation target.

Long-term portability

Planned targets include:

-   M5Stack Paper S3
-   Desktop (Linux, macOS, Windows)
-   ANSI Terminal
-   Additional e-ink devices
