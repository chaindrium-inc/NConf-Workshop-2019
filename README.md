
# NConf 2019
## Workshop Supply Chain Management using Blockchains
### von [Chaindrium](https://chaindrium.com)
<br/><br/><br/>

Lassen Sie sich nicht von der Menge an Text abschrecken, Blockchains sind halt kompliziert :)

Dieses Repository enthält **drei** Teile. Sie können ganz nach Ihrem Wunsch eines der drei Projekte im Zuge des Workshops bearbeiten. Wir empfehlen allerdings den Teil "Für ProgrammiererInnen" vor dem Teil "Für Hard-Coder" zu machen.
- Für Nicht-ProgrammiererInnen
- Für ProgrammiererInnen
- Für Hard-Coder

### Für Nicht-ProgrammiererInnen
Diese Anleitung leitet Sie durch den Prozess eine Transaktion auf dem [Ethereum Test Netzwerk](https://ropsten.etherscan.io/) von einer Addresse zu einer anderen ausführen. Dieses Projekt richtet sich explizit an TeilnehmerInnen die keine Programmiererfahrung haben und trotzdem gerne einen Einblick in den praktischen Umgang mit Blockchains haben möchten.
*Sollten Sie Fragen haben geben Sie gerne Handzeichen oder sprechen uns direkt an.*

Dazu sind die folgenden Schritte nötig:
- **Auf das von uns vorbereitete Wallet zu greifen** 
	- Rufen Sie in Ihrem Browser https://www.myetherwallet.com/ auf
	- klicken Sie auf `Access My Wallet`
	- klicken Sie auf `Software` 
	- wählen Sie `Mnemonic Phrase` aus und klicken Sie `continue`
	- geben Sie die von uns bereit gestellten 12 Werte, sie sollten auf dem Beamer zu sehen sein.
		- Jetzt sollten Sie unter `1` das testnet `ROP - myetherwallet.com` auswählen
		- unter `2` müssen Sie oben rechts `Ethereum Testnet (Ropsten)` Auswählen
		- nun sollten Sie eine Liste mit Addressen und Guthaben sehen
		- wähen Sie eine der Addressen, die ein Guthaben hat, aus und klicken Sie auf `Access My Wallet`
			- (Wir koordinieren dann dass nicht alle die selbe Addresse auswählen)
		
- **Eine Transaktion Senden**
	- Sie sollten jetzt eine Übersicht über Ihren Account sehen. Dort können Sie dann unter `Send Transaktion` eine Transaktion senden.
	- Dazu müssen Sie die entsprechenden Felder ausfüllen
		- Tragen Sie unter `To Address` eine Addresse ein, vielleicht finden Sie ja eine(n) PartnerIn dem Sie etwas von Ihrem Guthaben schicken möchten.
		- Unter `Amount` Tragen Sie bitte den Betrag ein den Sie senden möchten. 
	- Ihr Account hat momenten ca 0.5 ROP (Die Währung des Test-Netzwerkes), das heißt sie müssen einen Betrag wählen der kleiner ist, das liegt daran dass Transaktionen Gebühren kosten, sollten Sie also versuchen all Ihr Geld zu versenden haben Sie kein Geld mehr um die Transaktions-Gebühren zu bezahlen (wählen Sie einen Betrag der relativ klein ist, damit nicht alles Geld sofort weg ist und andere auch noch ausprobieren können).
	- Jetzt können Sie auf `Send Transaktion` klicken
	- Danach öffnet sich ein Fenster in dem Sie die Transaktion nochmals überprüfen und dann bestätigen können

- **Fertig**, Sie haben jetzt eine Transaktion von Ihrer Addresse zu der von Ihnen eingegebenen Addresse ausgelöst. Es wird einige Sekunden dauern bis diese Transaktion in der Blockchain eingebettet ist

- **Die Transaktion auf etherscan.io anschauen**
	- Dafür klicken Sie nach dem Bestätigen der Transaktion auf `Check Status on Etherscan.io`
	- Jetzt sollte sich in Ihrem Browser ein neues Fenster geöffnet haben, dort können Sie sich die Detaills ihrer Transaktion anschauen.
	- Zum Beispiel könnten Sie sich den Hash Ihrer Transaktion anschauen
	- Oder Sie könnten den Block, in dem die Transaktion eingebettet ist,  untersuchen und sich ansehen welche anderen Transaktionen noch in diesem Block waren


<br/><br/><br/>

### Für ProgrammiererInnen
Diese Anleitung begleitet Sie anhand eines Beispiels durch den Prozess Entitäten auf der Blockchain zu erstellen, zu versenden und Daten dieser Entitäten von der Blockchain zu holen. Dieses Projekt erklärt die Basis auf der mit einer Blockchain interagiert werden kann. Es richtet sich explizit an TeilnehmerInnen die Erfahrung mit Programmierung haben und nicht davor zurück schrecken selbst Hand an den Code zu legen.
*Sollten Sie Fragen haben geben sie gerne Handzeichen oder sprechen uns direkt an.*

#### Was Sie benötigen: 
- python3.6
- installieren Sie folgende Python Bibliotheken:
	- `pip3 install web3`
- alternativ können Sie auch python-virtualenv benutzen: `pip install virtualenv`
	- `source ./virtual_env/bin/activate`
	- jetzt befinden Sie sich in einer Virtuellen Python3 Umgebung die wir für Sie vorbereitet haben

#### Was wollen wir hier entwickeln:
Nehmen wir an Sie haben ein NConf-Ticket das Sie gerne jemandem schenken würden. Diese Person könnte das Ticket ja auch weiter verschenken. Sie würden aber gerne wissen wer das Ticket letztendlich besitzt. Diesen Prozess würden wir gerne auf einer Blockchain abbilden.

#### Dazu sind die folgenden Schritte nötig:

- laden Sie das Repository von https://github.com/chaindrium-inc/NConf-Workshop-2019 herunter. Sie können `git clone` verwenden oder einfach auf github.com `download` klicken und das zip Archiv entpacken.
- navigieren Sie zu `/src/01_basic/`

- **Erzeugen eines eigenen Wallets**
	- Öffnen Sie die Datei `generate_wallet.py`
		- Hier wird ein Wallet für Sie generiert, Sie sind dazu eingeladen den Code anhand der Dokumentation nach zu vollziehen
		- ändern Sie die Variable `random_string`, diese hilft dabei ein besonders sicheres Wallet zu generieren.
	- Führen Sie die Datei aus
		- Jetzt sollten Sie von dem Skript eine Adresse zurück geliefert bekommen haben, kopieren und speichern Sie diese Adresse, Sie werden sie später noch brauchen
		- Außerdem hat das Skript eine die Datei `wallet/private.key` erzeugt. In dieser befindet sich Ihr privater Schlüssel. Passen Sie gut auf diese Datei auf. Sollten Sie den Schlüssel verlieren, dann haben Sie keine Möglichkeit mehr auf Ihr Wallet zu zu greifen.
	- Da das Skript Ihre `wallet/private.key` Datei überschreibt sollten Sie es lediglich einmal ausführen

- **Guthaben kaufen und abfragen**
	- Sie brauchen Guthaben auf Ihrem Wallet da Transaktionen Gebühren kosten, sonst können Sie keine Transaktionen ausführen
		- Tragen Sie Ihre generierte Addresse [hier](https://medienpad.de/p/chaindrium) ein. Wir werden Ihnen dann etwas Guthaben schenken, damit Sie weiter arbeiten können. Dies kann allerdings einen Moment in Anspruch nehmen.
	- Jetzt können Sie die Datei `see_balance.py` ansehen und (nach dem Sie Ihre Addresse eingefügt haben) ausführen, dann sollten Sie das Aktuelle Guthaben ihres Wallets sehen
	- Sobald Ihr Guthaben großer als 0 ist können Sie mit dem nächsten Schritt fortfahren
		- in der Zwischenzeit könne Sie ja mal einen Blick auf die Datei `token_contract/NConfToken.sol` werfen. Das ist der Smart Contract den wir gleich auf die Blockchain laden werden.

- **Einen Smart Contract auf der Blockchain erstellen**
	- Schauen Sie sich hierzu die Datei `deploy_token.py` an
		- Sie erstellt einen Smart Contract auf dem [Ethereum Test Netzwerk](https://ropsten.etherscan.io/)
	- Hier können Sie in den ersten Zeilen sehen dass einige Variablen gesetzt werden. Vor allem die Variable `token_name` sollten Sie anpassen um Ihrem Token einen eigenen Namen zu geben.
	- Führen Sie die Datei aus
	- Wenn alles geklappt hat sollte die Datei Ihnen einen Hash-Wert Ihrer gerade erzeugten Transaktion anzeigen
	- Öffnen Sie [https://ropsten.etherscan.io/](https://ropsten.etherscan.io/) in Ihrem Browser
		- Auf dieser Website können Sie alle Blöcke und Transaktionen der "Test-Blockchain" sehen
	- Geben Sie in die Suchleiste den Hash Ihrer Transaktion ein
	- Jetzt sollten Sie Ihre Transaktion sehen können
	- vergleichen Sie die `from` Adresse mit der Ihren. Die Adressen sollten Identisch sein.
	- unter `to` sollten Sie die Adresse des von Ihnen erzeugten Smart Contracts sehen
	- kopieren Sie diese

- **Den Namen des Tokens abfragen**
	- Schauen Sie sich hierzu die Datei `get_token_name.py` an
	- ändern Sie die Variable `token_address`, tragen Sie dort die Adresse Ihres Tokens ein
	- Führen Sie die Datei aus
	- Jetzt sollte Ihnen das Skript den Namen Ihres Tokens anzeigen
		- Vielleicht finden Sie ja einen Partner dessen Token Namen Sie auch abfragen können

- **Den Besitzer des Tokens abfragen**
	- Schauen Sie sich hierzu die Datei `get_token_owner.py` an
	- ändern Sie die Variable `token_address`, tragen Sie dort die Adresse Ihres Tokens ein
	- Führen Sie die Datei aus
	- Jetzt sollte Ihnen das Skript den Besitzer Ihres Tokens anzeigen
		- Vielleicht finden Sie ja eine(n) PartnerIn dessen Token Besitzer Sie auch abfragen können

- **Ihr Token jemandem anderen geben**
	- Schauen Sie sich hierzu die Datei `send_token.py` an
	- ändern Sie die Variable `token_address`, tragen Sie dort die Adresse Ihres Tokens ein
	- ändern Sie die Variable `new_owner`, tragen Sie dort die Adresse desjenigen ein dem Sie das Token geben möchten
		- Vielleicht finden Sie ja einen Partner mit dem Sie Tokens tauschen können
	- Führen Sie die Datei aus
		- jetzt sollte das Token nicht mehr Ihnen gehören, sondern der Person der Sie das Token gegeben haben. Dies können Sie mit den Schritten unter "Den Besitzer des Tokens abfragen" nachvollziehen

- **Fertig**
	- Sollten Sie noch Zeit und Muße haben können Sie jetzt 
		- entweder mit dem Advanced Teil fortfahren 
		- oder sie schauen sich unter [https://ropsten.etherscan.io/](https://ropsten.etherscan.io/) Ihre Addresse an
			- geben Sie dazu einfach ihre Adresse in das Suchfenster ein
			- hier sollten Sie jetzt einen Überblick über Ihr Guthaben und die von Ihnen ausgelösten, bzw. Erhaltenen Transaktionen sehen


<br/><br/><br/>

### Für Hard-Coder
Die hier präsentierten Aufgaben sind so gestellt dass Sie mit dem Teil **Für ProgrammiererInnen** lösbar sein sollten. Hier werden Sie mit Absicht nicht an die Hand genommen sondern sollen selbst eine Anwendung für Blockchains entwickeln.
*Sollten Sie Fragen haben geben sie gerne Handzeichen oder sprechen uns direkt an.*

#### Was Sie benötigen: 
- python3.6
- installieren Sie folgende Python Bibliotheken:
	- `pip3 install web3`
- alternativ können Sie auch python-virtualenv benutzen: `pip install virtualenv`
	- `source ./virtual_env/bin/activate`
	- jetzt befinden Sie sich in einer Virtuellen Python3 Umgebung die wir für Sie vorbereitet haben


#### Was wollen wir hier entwickeln:
Wir stellen uns vor Sie sind Bauer (Produzent) und Sie verkaufen Bio-Kartoffeln. Diese Kartoffeln werden von Ihnen an eine Fabrik verkauft die daraus Wodka herstellt. Dieser Wodka wird dann von jemandem gekauft (Konsument).

Der Konsument würde gerne einige Informationen über den von Ihm gekaufen Wodka wissen:
- wer hat die Kartoffeln hergestellt
- wer hat aus den Kartoffeln Wodka gemacht
- sind die Kartoffeln aus Biologischer Erzeugung
- welche Sorte von Kartoffeln wurde für den Wodka genutzt

<br/><br/><br/>

**Tun Sie sich hierzu zu dritt oder zu mehreren zusammen, sodass einer von Ihnen der Produzent, einer von Ihnen die Fabrik und einer von Ihnen der Konsument ist.**

Alternativ können Sie auch so tun als ob sie alle 3 dieser Personen darstellen.

Wir werden im Weiteren Verlauf dieser Aufgaben diese drei Nutzerrollen "Produzent", "Fabrik" und "Konsument" nennen. 


- navigieren Sie zu `/src/01_advanced/`

#### Aufgabe 0:
Zur Modellierung dieser Supply-Chain benutzen wir einen Smart Contract (`potato`). Machen Sie sich mit `potato/potato.sol` vertraut. 
Es ist wichtig dass Sie verstehen was die Felder
- `producer`
- `factory`
- `is_vodka`
- `name`
- `owner`

machen 

und wie Sie mit den Funktionen 
- `constructor`
- `send`
- `set_factory`
- `to_vodka`
- `is_potato_vodka`
- `who_is_owner`
- `who_is_producer`
- `who_is_factory`
- `get_name`
- `is_bio_potato`

diese Felder beeinflussen/auslesen.

#### Aufgabe 1:
- Erstellen Sie eine Datei (`deploy_potato.py`) die den `potato` Smart Contract mit der von Ihnen generierten Adresse auf der Blockchain erstellt
- Geben Sie dem Constructor des `potato` Smart Contracts 
	- sowohl einen `string name` der den Namen der Kartoffel darstellt (https://de.wikipedia.org/wiki/Liste_von_Kartoffelsorten) 
	- die addresse des producers ist automatisch der ersteller des Smart Contracts (`producer = msg.sender` im Constructor des Smart Contracts)
- erzeugen Sie eine Transaktion die den Contract auf der Blockchain erstellt
- geben Sie den Hash der Transaktion am Ende Ihres Skriptes aus

- Erzeugen Sie einen `potato` Smart Contract auf der Blockchain

#### Aufgabe 2:
- Erstellen Sie eine Datei (`send_potato.py`) die den `potato` Smart Contract an die Fabrik sendet
- Senden Sie den in Aufgabe 1 erzeugten `potato` Smart Contract an die Fabrik

#### Aufgabe 3:
- Erstellen Sie eine Datei (`produce_vodka.py`) die auf dem `potato` Smart Contract die Methode `to_vodka` aufruft
- Benutzen Sie die Datei um aus der in Aufgabe 1 erzeugten Kartoffel Wodka zu machen

#### Aufgabe 4:
- Senden Sie (in dem Fall die Fabrik) den Wodka an den Konsumenten 
	- verwenden Sie hierzu das Skript aus Aufgabe 2

#### Aufgabe 5:
- Erstellen Sie eine Datei (`get_potato_information.py`) die die Methoden `is_vodka`, `get_producer`, `get_factory`, `get_name` aufruft und das Ergebnis in der Konsole anzeigt.
- Führen Sie die Datei aus und überprüfen Sie ob alle Informationen korrekt sind


Viel Spass und Erfolg :)
