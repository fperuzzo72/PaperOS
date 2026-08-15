MS-DOS — Respect for Files

MS-DOS did not begin as a triumph of design. It began as a purchase.
In 1980, a programmer named Tim Paterson, working largely alone at a
small company called Seattle Computer Products, wrote an operating
system he called QDOS — the Quick and Dirty Operating System, a name
that was more honest than modest. Microsoft licensed it, then bought
it outright in 1981 for a few tens of thousands of dollars, renamed it
MS-DOS, and licensed it to IBM for the new IBM PC. Almost nothing
about that origin suggested it would end up running on tens of
millions of machines for the next fifteen years.

What made MS-DOS matter was never its technical elegance. It was
IBM’s decision to publish the PC’s architecture openly enough that
other manufacturers could build legally compatible machines around it.
Compaq reverse-engineered the PC’s BIOS in 1982 without infringing
IBM’s copyright, and an entire industry of “IBM compatible” computers
followed. A program written for MS-DOS on one manufacturer’s machine
ran on every other manufacturer’s machine, and MS-DOS itself, riding
underneath all of it, became something closer to a public utility than
a product any single company controlled.

------------------------------------------------------------------------

The chapter’s title points to something more specific than market
history, though. When DOS 2.0 arrived in 1983, it introduced
hierarchical directories, and the vocabulary that came with them was
refreshingly literal. COPY copied a file. DEL deleted one. DIR listed
what was actually sitting on the disk. TYPE printed a file’s contents
exactly as they existed, nothing hidden and nothing added. There was
no metaphor standing between a person and their data — no desktop
pretending a file was a piece of paper, no icon disguising where
anything actually lived. A file was a name, an extension, and a
location, and it stayed exactly where it was put until someone moved
it.

That plainness produced something valuable that later, friendlier
interfaces would spend the next forty years slowly giving back: an
accurate mental model. A DOS user who had never heard the word
“filesystem” nonetheless understood, correctly, where their work
actually lived. PaperOS’s own insistence that the filesystem is not an
implementation detail, argued in the Ownership chapter, is not a new
idea. MS-DOS demonstrated it, unglamorously, decades earlier.

------------------------------------------------------------------------

Lesson for PaperOS

Honesty about where a file lives is not a missing feature waiting to
be designed away. It is the foundation everything else gets to stand
on. MS-DOS never dressed up the filesystem as anything other than what
it was, and an entire generation of users trusted it more for that
plainness, not less.
