0.Descarca postgres
1.Am pus arhiva chrome driverul
2.in config.json iti setezi path-ul la chromeDriver cu locatia unde ai exe-ul
3. tot in config. json portul trebuie sa corespunda cu cel pe care ai setat sa ruleze serverul de postgres
	pass - parola pentru userul postgres (este parola pe care o setezi la instalare)
4. in EnvironmentVariables -> variabila Path  adaugi path-ul catre folderul bin al postres:ceva de genul ("C:\Program Files\PostgreSQL\15\bin")

5. dai niste pip installuri
pip install sqlalchemy
pip install webdriver-manager
pip install bs4
PS: posibil sa mai trebuiasca si alte installuri, dar nu mai stiu care erau
6.rulezi database/createDb.py -> evident creeaza baza in forma actuala
	
	daca ai nevoie sa stergi baza rulezi in terminal dropdb -U postgres csgoitems (userul si numele bazei de date)

7.rulezi database/getAllItemsData.py -> adauga in tabela Item toate iteme din cs tradable
8.database/getNewPriceData.py -> adauga inregistrari in tabelele BuyOrder si SellOrder pentru toate itemele
	--chestia asta poate fi apelata de oricate ori, pentru ca pastram instoricul orderelor(avem Date pe tabele)
9.database/createNewItemStats.py -> creeaza staticile curente pentru fiecare item


10.in utils.functions am pus niste functii care citesc configurarile app-ului

11.In api am pus niste metode de care cred ca vom avea nevoie

12.infrastructure/classes e deampulea , probabil va fi sters.
