# NConf 2019
## Workshop Supply Chain Management
### by Chaindrium.com

Dieses Repository enthält 2 Teile. Sie können ganz nach Ihrem Wunsch eines der beiden Projekte im Zuge des Workshops bearbeiten.
- Für nicht Programmierer
- Für Programmierer

### Für nicht Programmierer
Dieses Projekt leitet Sie durch den Prozess eine Transaktion auf dem [Ethereum Test Netzwerk](https://ropsten.etherscan.io/) von einer Addresse zu einer anderen ausführen. Dieses Projekt richtet sich explizit an Menschen die keine Programmiererfahrung haben und trotzdem gerne einen Einblick in den Praktischen Umgang mit Blockchains haben möchten.
*Sollten Sie Fragen haben geben Sie gerne Handzeichen oder sprechen uns direkt an.*

Dazu sind die vollgenden Schritte nötig:
- **Auf das von uns vorbereitete Wallet zu greifen** 
	- Rufen Sie in Ihrem Browser https://www.myetherwallet.com/ auf
	- klicken Sie auf "Access My Wallet"
	- klicken Sie auf "Software" 
	- wählen Sie Mnemonic Phrase aus und klicken Sie "continue"
	- geben Sie die von uns bereit gestellten 12 Werte ein
		- Jetzt sollten Sie unter "1" das testnet "ROP - myetherwallet.com" auswählen
		- unter "2" müssen Sie jetzt noch oben rechts "Ethereum Testnet (Ropsten)" Auswählen
		- nun sollten Sie eine Liste mit Addressen und Guthaben sehen
		- wähen Sie eine der Addressen, die ein Guthaben hat, aus und klicken Sie auf "Access My Wallet"
			- (Wir koordinieren dann dass nicht alle die selbe Addresse auswählen)
		
- **Eine Transaction Senden**
	- Sie sollten jetzt eine Übersicht über Ihren Account sehen. Dort können Sie dann unter "Send Transaction" eine Transaktion senden.
	- Dazu müssen Sie die entsprechenden Felder ausfüllen
		- Tragen Sie unter "To Address" eine Addresse ein, vielleicht finden Sie ja einen Partner dem Sie etwas von Ihrem Guthaben schicken möchten.
		- Unter "Amount" Tragen Sie bitte den Betrag ein den Sie senden möchten. 
	- Ihr Account hat momenten ca 0.5 ROP (Die Währung des Test-Netzwerkes), das heißt sie müssen einen Betrag wählen der kleiner ist, das liegt daran dass Transaktionen Gebühren kosten, sollten Sie also versuchen all Ihr Geld zu versenden haben Sie kein Geld mehr um die Transaktions-Gebühren zu bezahlen.
	- Jetzt können Sie auf "Send Transaction" klicken
	- Danach öffnet sich ein Fenster in dem Sie die Transaction nochmals überprüfen und dann bestätigen können
- **Fertig**, Sie haben jetzt eine Transaction von Ihrer Addresse zu der von Ihnen eingegebenen Addresse ausgelöst. Es wird einige Sekunden dauern bis diese Transaction in der Blockchain eingebettet ist
- **Die Transaction auf etherscan.io anschauen**
	- Dafür klicken Sie nach dem Bestätigen der Transaction auf "Check Status on Etherscan.io"
	- Jetzt sollte sich in Ihrem Browser ein neues Fenster geöffnet haben, dort können Sie sich die Detaills ihrer Transaction anschauen.
	- Zum Beispiel könnten Sie sich den Hash Ihrer Transaction anschauen
	- Oder Sie könnten den Block, in dem die Transaction eingebettet ist,  untersuchen und sich ansehen welche anderen Transactionen noch in diesem Block waren


### Für Programmierer
