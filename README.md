# python-game

English version below

----------------------------------
Wymagania:
----------------------------------

Python v.3.6.0 lub wyższa

Biblioteki: pygame, pandas, tkinter

----------------------------------
Instrukcja uruchomienia:
----------------------------------

Gra uruchamia się po wywołaniu komendy: "python MainWindow.py" w folderze z plikami źródłowymi projektu. Uwaga: "python" jest ścieżką do uruchomienia interpretera Pythona.

Okienko powitalne daje dwie możliwości: można od razu rozpocząć grę, klikając przycisk "Start", lub nacisnąć przycisk "Instructions" w celu zapoznania się z celem gry. Komunikaty w grze są po angielsku, tak samo jak napisy na przyciskach.

----------------------------------
Zasady i cel gry:
----------------------------------

Celem gry jest takie ustawienie obiektów na planszy, aby po kliknięciu przycisku sprawdzania "See how it works!" ("Zobacz, jak to działa!") ruch poszczególnych elementów spowodował, aby piłka do koszykówki wpadła do kosza do koszykówki. Po kliknięciu przycisku, elementy poruszają się samoistnie - do użytkownika należy jedynie ich początkowe ustawienie. 

Część obiektów w okienku gry znajduje się od razu na planszy i są to obiekty których użytkownik nie może przesunąć - nadają one formę każdemu poziomowi. Nieruchome dla użytkownika obiekty zaczną się poruszać dopiero w reakcji na kliknięcie przycisku sprawdzania i tak jak wszystkie pozostałe obiekty, wchodzą w interakcje z innymi.

Obiekty, które użytkownik jest w stanie przesuwać i umieścić na planszy według własnej inwencji znajdują się w oddzielnym polu, obok głównej planszy. 

Wywołanie sprawdzenia jak działa gra jest możliwe dopiero wtedy, gdy wszystkie elementy będą na planszy. Kliknięcie przycisku sprawdzania spowoduje ruch elementów zgodnie z prawami fizyki.

Jeśli użytkownikowi nie udało się za pierwszym razem trafić piłką do kosza, może zrestartować poziom. Przejście do kolejnego poziomu jest możliwe dopiero po skończeniu poprzedniego.

----------------------------------
Źródła:
----------------------------------

Wykorzystane obrazy pochodzą ze stron udostępniających darmowe grafiki w formacie png, przede wszystkim:
https://pngtree.com/
https://www.freeiconspng.com/
Część z nich wymagała obróbki w programie Gimp w celu dopasowania do potrzeb gry i/lub usunięcia tła.

Tytuł pojawiający się na początku pochodzi z generatora napisów online:
https://wordart.com/create

Wykorzystane dźwięki pochodzą ze strony:
http://soundbible.com 
Dwa pliki posiadają licencję Attribution 3.0, umożliwiającą swobodne kopiowanie i rozpowszechnianie w dowolnym formacie.
Jeden posiada licencję Public Domain, również umożliwiającą zmienianie, rozpowszechnianie i wykonywanie utworu nawet w celu komercyjnym, bez pytania o zgodę.



--------------------------------------
Requirements:
--------------------------------------

Python v.3.6.0 or higher

Libraries: pygame, pandas, tkinter

--------------------------------------
Start-up instructions:
--------------------------------------

The game starts after calling the command: "python MainWindow.py" in the folder with project source files. Note: "python" is the path to start the Python interpreter.

The welcome window offers two options: you can start the game right away by clicking the "Start" button or press the "Instructions" button to familiarize yourself with the game's goal. The messages in the game are in English, as are the subtitles on the buttons.

--------------------------------------
The rules and purpose of the game:
--------------------------------------

The goal of the game is to set objects on the board in such a way that after clicking the checking button ("See how it works!"), the movement of individual elements will cause the basketball ball fall into the basketball basket. After clicking the checking button, the elements move on their own - the user only sets their initial positions.

Some objects in the game window are inside of the level surface already and these are objects that the user can not move - they give form to each level. The objects that are not movable for the user will start to move only in response to clicking the checking button and, like all other objects, will interact with others.

Objects that the user is able to move and place on the board according to his own invention are located in a separate field, next to the level surface.

Calling the checking button is possible only when all the elements are on the level surface. Clicking the checking button will move the elements according to the laws of physics.

If the user failed to throw the basketball to the basket at first time, he can restart the level. The transition to the next level is possible only after finishing the previous one.

--------------------------------------
Sources
--------------------------------------

Images used in the game were downloaded from sites offering free png graphics, such as:
https://pngtree.com/
https://www.freeiconspng.com/
Some of them needed to be fitted or had background removed in Gimp programme.

Title showed in main window was created via online text generator:
https://wordart.com/create

All sounds used in the game were downloaded from the site:
http://soundbible.com 
And have either Attribution 3.0 or Public Domain license, both allowing free usage and distribution.


