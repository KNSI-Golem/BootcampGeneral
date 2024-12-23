# Oficjalne Repo corocznych Bootcampów KNSI Golem

W tym repozytorium znajdują się materiały do wszystkich edycji bootcampu

## Materiały ze spotkań

Są w odpowiednich folderach dla danej edycji

## Przygotowanie środowiska do pracy

Aby przygotować środowisko do pracy z materiałami zawartymi w tym repozytorium, należy wykonać następujące kroki:

- zainstalować pythona w wersji 3.9.7 (albo wyższego);
- zainstalować narzędzie virtualenv;
- sklonować repozytorium z materiałami;
- utworzyć środowisko wirtualne;
- zainstalować kernel jupytera korzystający z utworzonego środowiska;
- zainstalować biblioteki, które będą wykorzystywane na warsztatach;
- zainstalować jupyter notebook;


### Instalacja pythona 3.9.7

Tutaj sposób instalacji będzie zależał od systemu operacyjnego, generalnie pod tym linkiem można się dowiedzieć jak zainstalować pythona na swojej maszynie ⇒ https://www.python.org/  
**Uwaga:** Python powinien być pobrany w odpowiedniej wersji (3.9.7 lub nowsza) oraz razem z pythonem należy zainstalować pip, czyli menadżer pakietów pythona.

Aby sprawdzić czy python i pip zostały poprawnie zainstalowane należy wpisać w konsolę komendy:
```python --version``` oraz ```pip --version```.
Output powinien wyglądać tak:
```
> python --version
Python 3.9.7
> pip --version
pip x.x.x from ... (python 3.9)
```

### Instalacja virtualenva

Należy wpisać komendę:
```
pip install virtualenv
```

### Klonowanie repozytorium z materiałami

Należy zainstalować gita ⇒ https://git-scm.com/downloads
Można również się wesprzeć jakimś GUI, np. gitkraken, sourcetree, itp.

Po instalacji należy sklonować repozytorium spod adresu: *https://github.com/KNSI-Golem/BootcampGeneral*

W konsoli będzie to wyglądać tak:
```
> git clone https://github.com/KNSI-Golem/BootcampGeneral
```

**Uwaga:** Jeżeli do tej pory nie używałeś gita, polecam zrobić sobie kilka pierwszych kroków w tutorialu ⇒ https://learngitbranching.js.org/

### Wejść w odpowedni katalog

```
> cd [TUTAJ NAZWA ROKU, W KTÓRYM JEST EDYCJA]   # np. cd 2022
```

### Utworzyć środowisko wirtualne

W katalogu, którym znaleźliście się należy wykonać komendę:
```
> python -m venv bootcamp_env
```
gdzie za **bootcamp_env** można wstawić nazwę projektu.

Aby sprawdzić czy środowisko wirtualne działa, należy aktywować je poleceniem:
Linux:
```
> source bootcamp_env/bin/activate
```
lub
Windows:
```
> .\bootcamp_env\Scripts\activate
```

W wyniku aktywacji przed znakiem zachęty w konsoli powinna pojawić się nazwa venva:
```
(bootcamp_env) >
```

### Instalacja potrzebnych bibliotek

W katalogu, w którym się znajdujecie jest plik `requirements.txt`. Zawiera on wszystkie potrzebne do przeprowadzenia warsztatów biblioteki. Aby je zainstalować nalezy wywołać komendę:
```
(bootcamp_env) > pip install -r requirements.txt
```

### Instalacja kernela dla utworzonego środowiska

Przy aktywowanym środowisku należy wywołać komendę:
```
(bootcamp_env) > ipython kernel install --user --name=bootcamp_env
```
Po tej operacji zostanie utworzony kernel jupytera dla środowiska wirtualnego.

## Sprawdzenie czy konfiguracja środowiska przebiegła pomyślnie
Należy wywołać komendę w głównym katalogu repozytorium:
```
(bootcamp_env) > jupyter notebook
```
Następnie w nowo otwartej karcie przeglądarki wybrać plik `test-environment.ipynb`.  
W nowo otwartej karcie nacisnąć przycisk run lub skrót `Ctrl+Enter`, jeżeli kod (importy) wykona się poprawnie, to znaczy, że konfiguracja przebiegła pomyślnie.

## Troubleshooting
W przypadku problemów z konfiguracją środowiska napiszcie o swoim problemie na kanale **#bootcamp** na discordzie. Zachęcamy bardziej zaawansowanych uczestników do pomagania mniej zaawansowanym. My również będziemy tam zaglądać.

