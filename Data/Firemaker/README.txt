
Disclaimer and terms of use:
============================

/*****************************************************************************\
*                                                                             *
*                                                                             *
*   This is the Firemaker NFI-images Distribution                             *
*                                                                             *
*   This distribution contains 1000 images of scanned handwritten text,       *
*   scanned at resolution 300dpi grey scale, containing pages of              *
*   handwritten text by 250 writers, four pages per writer, from four         *
*   writing conditions, one condition per page. The conditions are:           *
*   p1: copied, natural style, p2: copied, UPPER case, p3: copied and forged, *
*   i.e.,"try to write in a different style than your natural style", and p4, *
*   self generated, i.e., text produced to describe a given cartoon.          *
*                                                                             *
*                                                                             *
*                                                                             *
*   Copyright The International Unipen Foundation, 2000, All rights reserved  *
*******************************************************************************
*                                                                             *
*                                                                             *
*  DISCLAIMER AND COPYRIGHT NOTICE FOR ALL DATA CONTAINED ON THIS CDROM:      *
*                                                                             *
*                                                                             *
*  1) PERMISSION IS HEREBY GRANTED TO USE THE DATA FOR RESEARCH               *
*     PURPOSES. IT IS NOT ALLOWED TO DISTRIBUTE THIS DATA FOR COMMERCIAL      *
*     PURPOSES.                                                               *
*                                                                             *
*                                                                             *
*  2) PROVIDER GIVES NO EXPRESS OR IMPLIED WARRANTY OF ANY KIND AND ANY       *
*     IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR PURPOSE ARE       *
*     DISCLAIMED.                                                             *
*                                                                             *
*  3) PROVIDER SHALL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL,         *
*     INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THIS      *
*     DATA.                                                                   *
*                                                                             *
*  4) THE USER SHOULD REFER TO THE FIRST PUBLIC ARTICLE ON THIS DATA SET:     *
*                                                                             *
*     M. Bulacu, L. Schomaker & L. Vuurpijl (2003).                           *
*     Writer identification using edge-based directional features.            *
*     ICDAR '03: Proceedings of the 7th International Conference on Document  *
*     Analysis and Recognition, pp. 937-941.                                  *
*     Piscataway: IEEE Computer, ISBN 0-7695-1960-1                           *
*                                                                             *
*  5) THE RECIPIENT SHOULD REFRAIN FROM PROLIFERATING THE DATA SET TO THIRD   *
*  PARTIES EXTERNAL TO HIS/HER LOCAL RESEARCH GROUP. PLEASE REFER INTERESTED  *
*  RESEARCHERS TO HTTP://UNIPEN.ORG FOR OBTAINING THEIR OWN COPY.             *
\*****************************************************************************/

BibTeX entry:                                                               

  @inproceedings{Firemaker,                                                  
    author = {Bulacu, M. and Schomaker, L.R.B. and Vuurpijl, L.},    
    title = {Writer Identification Using Edge-Based Directional Features},
    booktitle = {ICDAR '03: Proceedings of the 7th International 
                 Conference on Document Analysis and Recognition},
    year = {2003},
    isbn = {0-7695-1960-1},
    pages = {937-941},
    publisher = {IEEE Computer Society},
    address = {Washington, DC, USA},
   }

In the project "Vergelijk", a grant obtained from the Dutch Forensic Science
Institute, two existing professional writer-identification systems have been 
compared regarding usability studies and in particular recognition 
performance (Schomaker & Vuurpijl, 2000). The results of this comparison 
are contained in a confidential report:

  L.R.B. Schomaker and L.G. Vuurpijl (2000). 
  Forensic writer identification: A benchmark data set 
  and a comparison of two systems. Technical report, 
  Nijmegen Institute for Cognition and Information (NICI), 
  University of Nijmegen, The Netherlands.

Informative and non-confidential details from this report are 
given in the accompanying file:  'firemaker-dbase.pdf'

To compare both systems, a carefully designed experiment was conducted to
record handwritten samples from male and female writers in several conditions:

Condition 1: Normal constrained handwriting
==============================================

Below, the Dutch text writers had to produce in normal handwriting is given. 

--- start text ----
Zij bezochten veilingen en reisden met de KLM. Voor
korte afstanden huurden ze een auto, meestal een VW
of een Ford.
<EMPTY LINE>
De veilingen waren van 7-4-1993 tot 3-5-1993 in New
York, Tokyo, Québec, Rome, Parijs, Zürich en Oslo.
<EMPTY LINE>
Omdat de veilingen steeds begonnen om 12 uur en je
gemiddeld 200 tot 300 kilometer moest rijden,
stonden zij steeds om 6.30 uur op en vertrokken om
8 uur uit het hotel.
<EMPTY LINE>
Elke dag hadden ze vijfhonderd (f 500,-) gulden
nodig. Daarvoor gebruikten ze elke keer een cheque
van tweehonderd (f 200,-) en een cheque van
driehonderd (f 300,-) gulden. Aan geschenken gaven
ze ongeveer honderd gulden (f 100,-) uit.
--- end text ----


Condition 2: Production of constrained block capital handwriting
================================================================

In this condition, the writers had to produce the following text
in block-capital handwriting:

--- start text ----
NADAT ZE IN NEW YORK, TOKYO, QUÉBEC, PARIJS, ZÜRICH
EN OSLO WAREN GEWEEST, VLOGEN ZE UIT DE USA TERUG
MET VLUCHT KL 658 OM 12 UUR.
<empty line>
ZE KWAMEN AAN IN DUBLIN OM 7 UUR EN IN AMSTERDAM OM
9.40 UUR 'S AVONDS. DE FIAT VAN BOB EN DE VW VAN
DAVID STONDEN IN R3 VAN HET PARKEERTERREIN.
HIERVOOR MOESTEN ZE HONDERD GULDEN (F 100,-)
BETALEN.
--- end text ----


Condition 3: Production of free-forged handwriting
==================================================

Below, the text writers had to produce in the free-forged handwriting
condition is given. No example of handwriting is given which they have to
mimick (forge), the condition concerns a self-conceived distorted 
handwriting style.

--- start text ----
Nog dezelfde avond reden ze naar hun vrienden
Chris, Emile, Jan, Irene en Henk, nadat ze hun
vriendinnen Greta en Maria hadden opgehaald.
<EMPTY LINE>
Samen hadden ze vijfhonderd (500) zeldzame
postzegels gekocht, Bob driehonderd (300) en David
tweehonderd (200).
<EMPTY LINE>
De reis was de moeite waard geweest.
--- end text ----


Condition 4: Production of unconstrained handwriting
====================================================

The final text writers had to produce is unconstrained handwriting.
The cartoon, a series of pictures concerning a 'UFO' landing had
to be described in their own words, in at least six lines of text.
See image file "space.gif".


Thruth labels and writer identifications
========================================

Each writer has a unique id, specified as:

   id:   {num}{set}
  num:   a three-digit number
 set:    either 01, 02, 03 or 04, identifying one of the 4 experiments

The vast majority of the writers producing sets 01, 02 and 03 mimicked the
content and layout (empty lines) of the constrained texts they had to copy
sufficiently accurately, such that the example texts are a good indication of
the contents. However, as set 04 ("describe cartoon story")  contains
unconstrained self-generated handwriting, the corresponding thruth  labels had
to be extracted manually. The resulting label files are contained in  the
directory ./300dpi/p4-self-natural/labels/

Note: no letter, word, line or paragraph segmentation is provided with this
data set. The main text can be cropped easily. Since the orientation is
horizontal, projection techniques can be used to extract lines, using
a line-spacing parameter (~94 pixels line height) as an additional check. 


Overview of directories:

300dpi/
   p1-copy-normal/      Copying task, normal writing style  
   p2-copy-upper/       Copying task, UPPER-case 
   p3-copy-forged/      Copying task, instructed to mimic another script style
   p4-self-natural/     Self-generated text, natural writing condition

Note: the original raw collection contained writer #155, who has been removed
from this data set, as his first condition (p1) was started in upper case and
the page was not  completed. Deleted files were 15501.tif, 15502.tif, 15503.tif
and 15504.tif.

Note: the name of this data set (Firemaker) is a contraction of the names
Vuurpijl and Schomaker.

Note b: Example of a cutout of essential handwritten text using NetPBM tools:  
 tifftopnm 15201.tif | pnmcut -left 50 -right 2400 -top 700 -bottom 3250 > handwriting.pgm

 For an experiment, the upper and lower halves of the resulting image were
 usually used in the Schomaker & Bulacu studies to obtain two samples of 
 handwriting for a writer.

 http://www.ai.rug.nl/~lambert
 http://www.ai.rug.nl/~bulacu

Our features for writer identification:

Lambert Schomaker
 http://www.ai.rug.nl/~lambert/allographic-fraglet-codebooks/allographic-fraglet-codebooks.html
 L. Schomaker & M. Bulacu (2004). 
 Automatic writer identification using connected-component contours and edge-based features of upper-case Western script. 
 IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol 26(6), June 2004, pp. 787 - 798.

Marius Bulacu
 http://www.ai.rug.nl/~lambert/hinge/hinge-transform.html
 Bulacu, M. & Schomaker, L.R.B. (2007). 
 Text-independent Writer Identification and Verification Using Textural and Allographic Features, 
 IEEE Trans. on Pattern Analysis and Machine Intelligence (PAMI), Special Issue - Biometrics: Progress and Directions, April, 29(4), p. 701-717.

Axel Brink
 http://www.ai.rug.nl/~axel/  'Quill' feature
 A.A. Brink, J. Smit, M.L. Bulacu, and L.R.B. Schomaker (2011). 
 Writer identification using directional ink-trace width measurements, 
 Pattern Recognition (July 2011), doi: 10.1016/j.patcog.2011.07.005
 
These three feature groups (hinge, fraglets, quill) have been combined in
a single MS Windows application, GIWIS which is available for scientific
use upon request (schomaker@ai.rug.nl)

Note c.

The accompanying file 'Firemaker-writer-info.dat' contains some
writer information: 
Column 1: writer identification code
Column 2: sex
Column 3: handedness, 
Column 4: age in years
Column 5: major Western script group (print,cursive or mixed)

README version Tue Jul 26 11:26:35 CEST 2011

