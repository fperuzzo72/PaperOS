Acorn and Raspberry Pi — The Long Way Back to the Classroom

The previous chapter left a thread deliberately loose: Amstrad won
Britain’s living rooms in the 1980s, while a rival called Acorn
Computers, busy losing that same fight, ended up shaping something
larger instead. Acorn’s BBC Micro, built for the BBC’s Computer
Literacy Project, sold one and a half million units, overwhelmingly
into classrooms rather than homes, and became the machine an entire
generation of British schoolchildren actually learned to program on.
In 1985, Acorn engineers Sophie Wilson and Steve Furber designed a new
processor to give that aging machine more power, called it the Acorn
RISC Machine, and in 1990 spun the design off as its own company. ARM
now sits inside the overwhelming majority of the world’s mobile
phones. Acorn itself, the company that started it all, stopped making
computers within the decade.

------------------------------------------------------------------------

That lineage runs in a straight, traceable line to a much later
machine, and the person who built it has a personal story worth
telling in full. Eben Upton owned a BBC Micro as a child, the same way
an entire generation of his countrymen did. Years later, as Director
of Studies responsible for computing admissions at a Cambridge college
between 2004 and 2007, he watched the applicants in front of him
change. Where earlier candidates arrived already deep into
programming — the kind of casual, self-taught fluency the BBC Micro
generation had picked up almost by accident — the students now in
front of him increasingly knew basic web design and little else.

Upton’s diagnosis was specific rather than nostalgic. The BBC Micro,
like the Commodore 64 and the Sinclair Spectrum discussed earlier in
this book, booted directly into a programming prompt. Turning the
machine on was already, in a small way, an invitation to write
something. The computers that replaced them booted into a desktop
built for consuming software rather than writing it, and an entire
frictionless on-ramp into programming quietly closed without anyone
deciding to close it. It is close to the exact diagnosis this book
already made about the Apple II, restated as an observed decline
rather than a historical claim: a computer should encourage
understanding, not merely consumption, and when it stops doing that,
something measurable is lost within a single generation.

Upton spent 2006 to 2008 prototyping a fix at the Cambridge Computer
Laboratory: a complete computer, stripped down to almost nothing
extra, cheap enough that a school or a parent would never hesitate to
hand it to a child. The Raspberry Pi launched in February 2012 at
twenty-five and thirty-five dollars, sold out its first batch within
hours, and had passed six million units within three years — built, at
its core, around an ARM processor. Acorn’s education mission,
abandoned as a business decades earlier, had found its way back into a
classroom after all, carried there by someone who had once been a
child in one of Acorn’s original classrooms himself.

------------------------------------------------------------------------

The other lineage running through today’s small computers took a
different path entirely, and it happens to be the one closer to home
for this book. The ESP32 family of microcontrollers — including the
ESP32-S3 chip inside the M5Stack Paper S3, one of PaperOS’s own named
future targets — descends not from ARM at all, but from Xtensa, an
entirely separate architecture developed by Tensilica. Two chips can
sit a few centimeters apart inside two different pieces of e-ink
hardware and trace their design back to two completely unrelated
families, neither one owing the other anything. This is, in miniature,
exactly why the Hardware Independence chapter insisted the HAL should
never be allowed to care which family a given chip belongs to.
Architectures multiply, for reasons that have nothing to do with each
other. The interface sitting above them does not have to.

------------------------------------------------------------------------

Lesson for PaperOS

A machine built to answer one teacher’s very specific worry about one
generation of Cambridge applicants ended up inside thousands of e-ink
devices, satellite modems and pocket computers it was never designed
for, because the architecture underneath it was honest enough to be
reused. PaperOS is built on the same bet: that a foundation taken
seriously enough will end up carrying weight nobody involved at the
start ever specifically planned for.
