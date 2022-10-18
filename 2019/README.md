
# Golem AI Bootcamp

W tym repozytorium znajdują się materiały do bootcampu z października 2019 roku.

## Materiały ze spotkań

Linki z opisami:

- Prezentacja z pierwszego spotkania:  
https://docs.google.com/presentation/d/1weIubPyaU0f6YlcgQuYVAVR7KFB2CrrfAa0SVN8Uvx8/edit?usp=sharing
- Konspekt wykladu z pierwszego spotkania:  
https://docs.google.com/document/d/1DS0qZwJe_QFTeNWhnzLpga0eLYxX1MseO3lc0mdMwHk/edit?usp=sharing
- Prezentacja (klasyfikacja vs regresja) z trzeciego spotkania:  
https://docs.google.com/presentation/d/1Y95aqqHOpcjnFh-51tW5dagIXnQU99RUeF2sQYwSoOI/edit?usp=sharing
- Prezentacja z czwartego spotkania:  
https://docs.google.com/presentation/d/1TUQjReBMtT15hKY4u6faQVa-OS4IAsqTZt0dfKgqdOY/edit?usp=sharing
- Prezentacje z piątego spotkania
https://docs.google.com/presentation/d/10CC2hZIFhFBMmYI4tLlbiwLj72fPSEG4m7s19wSyxcU/edit?usp=sharing

## Przygotowanie środowiska do pracy

Aby przygotować środowisko do pracy z materiałami zawartymi w tym repozytorium, należy wykonać następujące kroki:

- zainstalować pythona w dowolnej wersji 3.6.x;
- zainstalować narzędzie virtualenv;
- sklonować repozytorium z materiałami;
- utworzyć środowisko wirtualne;
- zainstalować kernel jupytera korzystający z utworzonego środowiska;
- zainstalować biblioteki, które będą wykorzystywane na warsztatach;
- zainstalować jupyter notebook;


### Instalacja pythona 3.6.x

Tutaj sposób instalacji będzie zależał od systemu operacyjnego, generalnie pod tym linkiem można się dowiedzieć jak zainstalować pythona na swojej maszynie ⇒ https://www.python.org/  
**Uwaga:** Python powinien być pobrany w odpowiedniej wersji (3.6.x) oraz razem z pythonem należy zainstalować pip, czyli menadżer pakietów pythona.

Aby sprawdzić czy python i pip zostały poprawnie zainstalowane należy wpisać w konsolę komendy:
```python --version``` oraz ```pip --version```.
Output powinien wyglądać tak:
```
> python --version
Python 3.6.x
> pip --version
pip x.x.x from ... (python 3.6)
```

### Instalacja virtualenva

Należy wpisać komendę:
```
pip install virtualenv
```
Sprawdzenie:
```
> virtualenv --version
x.x.x
```

### Klonowanie repozytorium z materiałami

Należy zainstalować gita ⇒ https://git-scm.com/downloads
Można również się wesprzeć jakimś GUI, np. gitkraken, sourcetree, itp.

Po instalacji należy sklonować repozytorium spod adresu: *https://github.com/maciejchrabaszcz/Golem-BootCamp2019*

W konsoli będzie to wyglądać tak:
```
> git clone https://github.com/maciejchrabaszcz/Golem-BootCamp2019.git
```

**Uwaga:** Jeżeli do tej pory nie używałeś gita, polecam zrobić sobie kilka pierwszych kroków w tutorialu ⇒ https://learngitbranching.js.org/

### Utworzyć środowisko wirtualne

W katalogu, który powstał w wyniku wykonania poprzedniego punktu należy wykonać komendę:
```
> python -m venv projectname
```
gdzie za projectname można wstawić nazwę projektu.

Aby sprawdzić czy środowisko wirtualne działa, należy aktywować je poleceniem:
Linux:
```
> source projectname/bin/activate
```
lub
Windows:
```
> .\projectname\Scripts\activate
```

W wyniku aktywacji przed znakiem zachęty w konsoli powinna pojawić się nazwa venva:
```
(projectname) >
```

### Instalacja kernala dla utworzonego środowiska

Przy aktywowanym środowisku należy wywołać komendy:
```
(projectname) > pip install ipykernel
(projectname) > ipython kernel install --user --name=projectname
```
Po tej operacji zostanie utworzony kernel jupytera dla środowiska wirtualnego.

### Instalacja potrzebnych bibliotek

W głównym katalogu repozytorium znajduje się plik `requiremnets.txt`. Zawiera on wszystkie potrzebne do przeprowadzenia warsztatów biblioteki. Aby je zainstalować nalezy wywołać komendę:
```
(projectname) > pip install -r requirements.txt
```

## Sprawdzenie czy konfiguracja środowiska przebiegła pomyślnie
Należy wywołać komendę w głównym katalogu repozytorium:
```
(projectname) > jupyter notebook
```
Następnie w nowo otwartej karcie przeglądarki wybrać plik `test-environment.ipynb`.  
W nowo otwartej karcie nacisnąć przycisk run lub skrót `Ctrl+Enter`, jeżeli kod (importy) wykona się poprawnie, to znaczy, że konfiguracja przebiegła pomyślnie.

## Troubleshooting
W przypadku problemów z konfiguracją środowiska napiszcie o swoim problemie na kanale **#bootcamp** na discordzie. Zachęcamy bardziej zaawansowanych uczestników do pomagania mniej zaawansowanym. My również będziemy tam zaglądać.

