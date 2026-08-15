Amstrad — Computers by the Bundle

Alan Sugar built Amstrad on a single, blunt insight: most people did
not want to assemble a computer. They wanted to buy one, plug it in,
and use it, the same way they bought a stereo or a television. When
Amstrad entered the home computer market in 1984 with the CPC 464, it
did not sell a bare circuit board waiting for a separate monitor, tape
deck and manuals from three different companies. It sold a complete
package — computer, screen, and cassette or disk drive, one box, one
price — at a moment when most of its competitors still expected a
customer to assemble a working system out of parts bought separately.
The CPC sold three million units over an unusually long eight-year
production run, competing directly against the Commodore 64, the
Sinclair Spectrum and the BBC Micro without ever being the most
powerful machine among them.

A year later, Sugar repeated the trick for an entirely different
customer. The Amstrad PCW 8256, launched in 1985, bundled a computer,
monitor and printer into a single dedicated word processor, priced at
a little over three hundred pounds against machines like the Apple
Macintosh selling for well over two thousand dollars. It was never
meant to be a general-purpose computer. It was meant to replace a
typewriter, completely, for a price a small business or a household
could actually justify — and for years, in offices and homes across
Britain, it did exactly that.

------------------------------------------------------------------------

The Sinclair chapter already told part of what happened next: in 1986,
with Sinclair Research in financial trouble after the failure of the
QL computer and the TV80 pocket television, Amstrad bought the rights
to the Sinclair name and the ZX Spectrum outright, and kept the line
alive for several more years afterward. It was a fittingly Amstrad
move — buying an already-loved product at a distressed price and
continuing to sell it, rather than trying to out-engineer it.

------------------------------------------------------------------------

There is a tempting but inaccurate story that connects Amstrad
directly to ARM, the processor architecture that now runs inside the
overwhelming majority of the world’s mobile phones. It is not true,
and the real story is more interesting for being about a rival rather
than a relative. ARM traces back to Acorn Computers, a different
Cambridge-based company that spent the 1980s losing the retail battle
Amstrad was busy winning. Acorn’s BBC Micro, built for the BBC’s
Computer Literacy Project, became the machine an entire generation of
British schoolchildren actually learned on — one and a half million
units, overwhelmingly sold into classrooms rather than living rooms,
at a moment when Amstrad’s cheaper, flashier machines were outselling
Acorn everywhere else. In 1985, engineers Sophie Wilson and Steve
Furber, working to give the aging BBC Micro more power, designed the
Acorn RISC Machine — ARM — as a processor nobody outside Cambridge
thought much about at the time. Acorn spun the design off as its own
company in 1990. It now sits inside more devices than either Amstrad
or Acorn ever sold as computers, combined.

That lineage runs in a direct, traceable line to a machine built
explicitly in the BBC Micro’s own spirit. In 2012, engineer Eben
Upton — who had owned a BBC Micro as a child and wanted a new
generation to have the same experience he did — released the
Raspberry Pi, a complete computer the size of a credit card, built
around an ARM processor and priced to sit on a school desk rather than
in a boardroom. Acorn’s education mission, abandoned as a business
decades earlier, effectively returned to classrooms wearing new
silicon.

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
Architectures multiply. The interface above them does not have to.

------------------------------------------------------------------------

Lesson for PaperOS

Two answers came out of the same country, in the same decade, to the
same underlying question, and neither was wrong. Amstrad proved that a
complete, affordable bundle wins the living room. Acorn proved that a
machine built for a classroom, funded by a broadcaster, can quietly
seed the architecture the rest of the world ends up standing on
decades later. PaperOS needs a version of both instincts: cheap enough
to reach a bedroom desk, and serious enough about its own foundations
to still matter after everyone has forgotten which device it first
shipped on.
