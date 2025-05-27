## Általános információk

Szorgalmi feladatként zenét játszok le Floppy meghajtókon, illetve Piezo csipogókon. A mérés, és mérés kiértékelés a hangolásból áll, tehát megmérem a kiadott hang magasságát, és ez alapján hozok létre kompenzációt, hogy a várt hangmagasságot adja ki.

## Előzmény

A projekt hátterében áll az is, hogy már korábban foglalkoztam hasonló témával, még régen írtam egy programot, ami MIDI fájlokat le tud játszani piezo csipogókon a Raspberry Pi-n:
Itt található a [kód](https://github.com/4321ba/midi_player/tree/master), illetve egy [videó](https://www.youtube.com/watch?v=CFjmTnwveWY&list=PLDa4Vj43E2e9bdgJLPYenDJvnHyA-Bi5w&index=37&t=9s).
Akkoriban is csináltam hangmagasság-korrekciót, mert főleg a magas hangok eléggé eltorzultak.

## Terv

A szorgalmi feladat abból áll, hogy a 3db floppy meghajtót beüzemelem a 10db piezo csipogó mellé, és úgy játszatok le velük zenét, hogy az egyik szólamot a floppy meghajtók, a másik szólamot a piezo csipogók játsszák le. Úgy módosítom a Python programot, hogy ezt megvalósítsa.

## MIDI fájlokra általánosítás nehézsége

Ami miatt nehéz teljesen általánosan MIDI lejátszásra megcsinálni az az, hogy egyrészt mi alapján osszuk szét a két hangszer között a hangokat (track vagy channel, és hányas, ez MIDI fájlonként változik, ha egyáltalán van benne ilyen információ), a másik pedig hogy a floppy meghajtó nem tud szépen túl magas hangot lejátszani (meg túl mélyet se) (és a piezo csipogó sem tud igazán mélyet).
De ezek a problémák nem is igazán részei a projektnek, ha találok pár megfelelő zenét / MIDI fájlt, amit szépen le tud játszani (nincsenek benne túl magas/mély hangok, és szét tudom választani a két szólamot), az már megfelelő szerintem.

## Hardver bekötése

A floppy meghajtók bekötésére [ezt](https://www.instructables.com/Floppy-Drive-music-w-Raspberry-Pi/) a tutorialt használtam.

Viszonylag zökkenőmentesen ment, csak picit az az érzésem, hogy a DIR és a MOTOR pint fordítva írták le. Vagy én kavartam össze, de mindenesetre nagyon precízen végigkövetve pont fordítva sikerült bekötni, mint ahogy kell. Ez egy kis próbálgatással kitalálható.

## Szoftver

A WiringPi könyvtárnak van beépítve softToneCreate és softToneWrite függvénye, ami egy külön szálon tud megadott pinen megadott frekvenciával 1-0-1-0-kat kiírni. Ezt használtam a piezo csipogóknál is, és a floppy meghajtó léptetőmotorjánál is teljesen jól működött. Ez azért kifejezetten hasznos, mert így egymástól független szálakon tudja a PI a különböző hangokat kezelni, és könnyen lehet egyszerre több, különböző frekvenciájú hangot kiadni vele.

Gondolkoztam azon, hogy írok egy olyan logikát, ami megbecsli, hogy a floppy meghajtón az olvasófej, ami előre-hátra megy, éppen hol van, és ez alapján vált irányt (mert végállásban már nem tud jól hangot kiadni), viszont ez függ a sebességtől is, ami az adott hangmagasság. Végül arra jutottam, hogy szebb (kerregőbb, hangosabb) hangot ad, és programozni is könnyebb, ha a DIR-t is folyamatosan változtatom (1-0-1-0), nem csak a léptetőmotornak adok 1-0-1-0 jelet. Persze a DIR-t pl feleakkora frekvenciával). Így nem olyan látványos, de jobban hangzik.

## Hangolás

Elég alacsony maximum frekvencia miatt nem volt nagyon jelentős torzulás a hangmagasságban. A pontos adatok, és az illesztett görbe a diasorban található.

## Fájllista

- `prez.odp`: prezentáció
- `prez.pdf`: prezentáció PDF formátumban
- `vid.mp4`: a Star Wars Medley felvéve, mint példavideó (8:08 sec)
- `hangolas.ods`: hangolások adatai táblázatban, diagramok
- `kep.jpg`: egy kép a kész szerkezetről, a 3. floppy meghajtó a felső alatt van
- `code/star_wars_medley.mid`: a minta MIDI fájl, még régről van meg, a forrást most hirtelen nem tudom, de biztosan megtalálható könnyen
- `code/test_unite*.py`: a zenét lejátszó scriptek, mindben körülbelül ugyanaz van, csak abban különböznek, hogy tracket vagy channelt veszik figyelembe a hangok kettéválasztásakor, illetve, hogy melyik legyen a csipogóké és a floppy meghajtóké, plusz esetleges 2 oktávnyi eltolást a hangmagasságban
- `code/test_unite.py`: a Star Wars Medley lejátszására van beállítva
- `code/test_unite_unswitched_sajatwcmidi.py`: a (saját script által generált) Wynncraft OST MIDI fájlokat tudja úgy lejátszani, hogy a piezo csipogóké a magas, és a floppy meghajtóké a mély hang (nem pontosan [ezek](https://github.com/4321ba/Wynncraft_Noteblock_OST/tree/main/general_midi) a MIDI fájlok, picit más paraméterekkel voltak a csv-kből exportálva: a `--can_same_note_play_twice` be volt kapcsolva, és talán a `--note_length` is hosszabb volt, mint a general_midi mappában található fájlok esetében, mivel a piezo csipogóknál nincs lecsengés, és ezért nagyon rövidek lettek volna a hangok, viszont a script egyszerre 2 totál ugyanolyan hangot is le tud játszani, 2 külön piezo csipogón)
- `code/test_unite_switched_sajatwcmidi.py`: ugyanez, csak a két szólam fel van cserélve, és el van tolva 2 oktávval, ugyan először furi lehet, hogy a mély hang a főszólam, viszont a floppy meghajtók hangja jóval erőteljesebb, így összességében ez szerintem jobban szól, és nem is annyira furcsa, hogy a kis, vékony hangú piezo csipogó a kíséret
- `code/hangolas.py`: a hangoláshoz használható segédscript
- `paper/*`: a dokumentáció, és a hozzá szükséges fájlok

