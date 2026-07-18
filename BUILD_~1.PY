# -*- coding: utf-8 -*-
import csv

rows = []

def add(team, code, entries):
    for num, name, typ in entries:
        rows.append([team, code, num, name, typ])

# PANINI
add("Panini", "PANINI", [
    (0, "Panini Logo - We Are Panini", "panini special · foil"),
])

# WORLD CUP HISTORY
add("World Cup History", "FWC", [
    (1, "Official Emblem", "FIFA World Cup special · foil"),
    (2, "Official Emblem", "FIFA World Cup special · foil"),
    (3, "Official Mascots", "FIFA World Cup special · foil"),
    (4, "Official Slogan", "FIFA World Cup special · foil"),
    (5, "Official Ball", "FIFA World Cup special · foil"),
    (6, "Canada - Host Countries & Cities", "FIFA World Cup special · foil"),
    (7, "Mexico - Host Countries & Cities", "FIFA World Cup special · foil"),
    (8, "USA - Host Countries & Cities", "FIFA World Cup special · foil"),
    (9, "Italy 1934 - World Cup History", "FIFA World Cup special · foil"),
    (10, "Uruguay 1950 - World Cup History", "FIFA World Cup special · foil"),
    (11, "West Germany 1954 - World Cup History", "FIFA World Cup special · foil"),
    (12, "Brazil 1962 - World Cup History", "FIFA World Cup special · foil"),
    (13, "West Germany 1974 - World Cup History", "FIFA World Cup special · foil"),
    (14, "Argentina 1986 - World Cup History", "FIFA World Cup special · foil"),
    (15, "Brazil 1994 - World Cup History", "FIFA World Cup special · foil"),
    (16, "Brazil 2002 - World Cup History", "FIFA World Cup special · foil"),
    (17, "Italy 2006 - World Cup History", "FIFA World Cup special · foil"),
    (18, "Germany 2014 - World Cup History", "FIFA World Cup special · foil"),
    (19, "Argentina 2022 - World Cup History", "FIFA World Cup special · foil"),
])

def standard_team(team, code, players):
    """players: list of (num, name) for 2..12 and 14..20; team logo=1, team photo=13"""
    entries = [(1, "Team Logo", "team logo · foil")]
    for num, name in players:
        if num < 13:
            entries.append((num, name, "player sticker"))
    entries.append((13, "Team Photo", "team photo"))
    for num, name in players:
        if num > 13:
            entries.append((num, name, "player sticker"))
    add(team, code, entries)

def standard_team_variant(team, code, players, ptype="player sticker"):
    entries = [(1, "Team Logo", "team logo · foil")]
    for num, name in players:
        if num < 13:
            entries.append((num, name, ptype))
    entries.append((13, "Team Photo", "team photo"))
    for num, name in players:
        if num > 13:
            entries.append((num, name, ptype))
    add(team, code, entries)

# ALGERIA
standard_team("Algeria", "ALG", [
    (2,"Alexis Guendouz"),(3,"Ramy Bensebaini"),(4,"Youcef Atal"),(5,"Rayan Aït-Nouri"),
    (6,"Mohamed Amine Tougai"),(7,"Aïssa Mandi"),(8,"Ismael Bennacer"),(9,"Houssem Aquar"),
    (10,"Hicham Boudaoui"),(11,"Ramiz Zerrouki"),(12,"Nabil Bentalab"),
    (14,"Farés Chaibi"),(15,"Riyad Mahrez"),(16,"Said Benrahma"),(17,"Anis Hadj Moussa"),
    (18,"Amine Gouiri"),(19,"Baghdad Bounedjah"),(20,"Mohammed Amoura"),
])

# ARGENTINA
standard_team("Argentina", "ARG", [
    (2,"Emiliano Martinez"),(3,"Nahuel Molina"),(4,"Cristian Romero"),(5,"Nicolas Otamendi"),
    (6,"Nicolas Tagliafico"),(7,"Leonardo Balerdi"),(8,"Enzo Fernandez"),(9,"Alexis Mac Allister"),
    (10,"Rodrigo De Paul"),(11,"Exequiel Palacios"),(12,"Leandro Paredes"),
    (14,"Nico Paz"),(15,"Franco Mastantuono"),(16,"Nico Gonzalez"),(17,"Lionel Messi"),
    (18,"Lautaro Martinez"),(19,"Julian Alvarez"),(20,"Giuliano Simeone"),
])

# AUSTRALIA
standard_team("Australia", "AUS", [
    (2,"Mathew Ryan"),(3,"Joe Gauci"),(4,"Harry Souttar"),(5,"Alessandro Circati"),
    (6,"Jordan Bos"),(7,"Aziz Behich"),(8,"Cameron Burgess"),(9,"Lewis Miller"),
    (10,"Milos Degenek"),(11,"Jackson Irvine"),(12,"Riley McGree"),
    (14,"Aiden O'Neill"),(15,"Connor Metcalfe"),(16,"Patrick Yazbek"),(17,"Craig Goodwin"),
    (18,"Kusini Vengi"),(19,"Nestory Irankunda"),(20,"Mohamed Touré"),
])

# AUSTRIA
standard_team("Austria", "AUT", [
    (2,"Alexander Schlager"),(3,"Patrick Pentz"),(4,"David Alaba"),(5,"Kevin Danso"),
    (6,"Philipp Lienhart"),(7,"Stefan Posch"),(8,"Phillipp Mwene"),(9,"Alexander Prass"),
    (10,"Xaver Schlager"),(11,"Marcel Sabitzer"),(12,"Konrad Laimer"),
    (14,"Florian Grillitsch"),(15,"Nicolas Seiwald"),(16,"Romano Schmid"),(17,"Patrick Wimmer"),
    (18,"Christoph Baumgartner"),(19,"Michael Gregoritsch"),(20,"Marko Arnautović"),
])

# BELGIUM
standard_team("Belgium", "BEL", [
    (2,"Thibaut Courtois"),(3,"Arthur Theate"),(4,"Timothy Castagne"),(5,"Zeno Debast"),
    (6,"Brandon Mechele"),(7,"Maxim De Cuyper"),(8,"Thomas Meunier"),(9,"Youri Tielemans"),
    (10,"Amadou Onana"),(11,"Nicolas Raskin"),(12,"Alexis Saelemaekers"),
    (14,"Hans Vanaken"),(15,"Kevin De Bruyne"),(16,"Jérémy Doku"),(17,"Charles De Ketelaere"),
    (18,"Leandro Trossard"),(19,"Loïs Openda"),(20,"Romelu Lukaku"),
])

# BOSNIA AND HERZEGOVINA
standard_team("Bosnia and Herzegovina", "BIH", [
    (2,"Nikola Vasilj"),(3,"Amer Dedic"),(4,"Sead Kolasinac"),(5,"Tarik Muharemovic"),
    (6,"Nihad Mujakic"),(7,"Nikola Katic"),(8,"Amir Hadziahmetovic"),(9,"Benjamin Tahirovic"),
    (10,"Armin Gigovic"),(11,"Ivan Sunjic"),(12,"Ivan Basic"),
    (14,"Dzenis Burnic"),(15,"Esmir Bajraktarevic"),(16,"Amar Memic"),(17,"Ermedin Demirovic"),
    (18,"Edin Dzeko"),(19,"Samed Bazdar"),(20,"Haris Tabakovic"),
])

# BRAZIL
standard_team("Brazil", "BRA", [
    (2,"Alisson"),(3,"Bento"),(4,"Marquinhos"),(5,"Éder Militão"),
    (6,"Gabriel Magalhães"),(7,"Danilo"),(8,"Wesley"),(9,"Lucas Paquetá"),
    (10,"Casemiro"),(11,"Bruno Guimarães"),(12,"Luiz Henrique"),
    (14,"Vinicius Júnior"),(15,"Rodrygo"),(16,"João Pedro"),(17,"Matheus Cunha"),
    (18,"Gabriel Martinelli"),(19,"Raphinha"),(20,"Estévão"),
])

# CANADA
standard_team("Canada", "CAN", [
    (2,"Dayne St.Clair"),(3,"Alphonso Davies"),(4,"Alistair Johnston"),(5,"Samuel Adekugbe"),
    (6,"Riche Larvea"),(7,"Derek Cornelius"),(8,"Moïse Bombito"),(9,"Kamal Miller"),
    (10,"Stephen Eustáquio"),(11,"Ismaël Koné"),(12,"Jonathan Osorio"),
    (14,"Jacob Shaffelburg"),(15,"Mathieu Choinière"),(16,"Niko Sigur"),(17,"Tajon Buchanan"),
    (18,"Liam Millar"),(19,"Cyle Larin"),(20,"Jonathan David"),
])

# COTE D'IVOIRE
standard_team("Côte d'Ivoire", "CIV", [
    (2,"Yahia Fofana"),(3,"Ghislain Konan"),(4,"Wilfried Singo"),(5,"Odilon Kossounou"),
    (6,"Evan Ndicka"),(7,"Willy Boly"),(8,"Emmanuel Agbadou"),(9,"Ousmane Diomande"),
    (10,"Franck Kessie"),(11,"Seko Fofana"),(12,"Ibrahim Sangare"),
    (14,"Jean-Philippe Gbamin"),(15,"Amad Diallo"),(16,"Sébastien Haller"),(17,"Simon Adingra"),
    (18,"Yan Diomande"),(19,"Evann Guessand"),(20,"Oumar Diakite"),
])

# DR CONGO
standard_team("DR Congo", "COD", [
    (2,"Lionel Mpasi"),(3,"Aaron Wan-Bissaka"),(4,"Axel Tuanzebe"),(5,"Arthur Masuaku"),
    (6,"Chancel Mbemba"),(7,"Joris Kayembe"),(8,"Charles Pickel"),(9,"Ngal'ayel Mukau"),
    (10,"Edo Kayembe"),(11,"Samuel Moutoussamy"),(12,"Noah Sadiki"),
    (14,"Théo Bongonda"),(15,"Meschak Elia"),(16,"Yoane Wissa"),(17,"Brian Cipenga"),
    (18,"Fiston Mayele"),(19,"Cédric Bakambu"),(20,"Nathanaël Mbuku"),
])

# COLOMBIA
standard_team("Colombia", "COL", [
    (2,"Camilo Vargas"),(3,"David Ospina"),(4,"Dávinson Sánchez"),(5,"Yerry Mina"),
    (6,"Daniel Munoz"),(7,"Johan Mojica"),(8,"Jhon Lucumí"),(9,"Santiago Arias"),
    (10,"Jefferson Lerma"),(11,"Kevin Castaño"),(12,"Richard Rios"),
    (14,"James Rodriguez"),(15,"Juan Fernando Quintero"),(16,"Jorge Carrascal"),(17,"Jon Arias"),
    (18,"Jhon Cordova"),(19,"Luis Suarez"),(20,"Luis Diaz"),
])

# CAPE VERDE
standard_team("Cape Verde", "CPV", [
    (2,"Vozinha"),(3,"Logan Costa"),(4,"Pico"),(5,"Diney"),
    (6,"Steven Moreira"),(7,"Wagner Pina"),(8,"Joao Paulo"),(9,"Yannick Semedo"),
    (10,"Kevin Pina"),(11,"Patrick Andrade"),(12,"Jamiro Monteiro"),
    (14,"Deroy Duarte"),(15,"Garry Rodrigues"),(16,"Jovane Cabral"),(17,"Ryan Mendes"),
    (18,"Dailon Livramento"),(19,"Willy Semedo"),(20,"Bebe"),
])

# CROATIA
standard_team("Croatia", "CRO", [
    (2,"Dominik Livaković"),(3,"Duje Caleta-Car"),(4,"Josko Gvardiol"),(5,"Josip Stanišić"),
    (6,"Luka Vušković"),(7,"Josip Sutalo"),(8,"Kristijan Jakic"),(9,"Luka Modrić"),
    (10,"Mateo Kovacic"),(11,"Martin Baturina"),(12,"Lovro Majer"),
    (14,"Mario Pasalic"),(15,"Petar Sucic"),(16,"Ivan Perišić"),(17,"Marco Pasalic"),
    (18,"Ante Budimir"),(19,"Andrej Kramarić"),(20,"Franjo Ivanovic"),
])

# CURACAO
standard_team("Curaçao", "CUW", [
    (2,"Eloy Room"),(3,"Armando Obispo"),(4,"Sherel Floranus"),(5,"Jurien Gaari"),
    (6,"Joshua Brenet"),(7,"Roshon Van Eijma"),(8,"Shurandy Sambo"),(9,"Livano Comenencia"),
    (10,"Godfried Roemeratoe"),(11,"Juninho Bacuna"),(12,"Leandro Bacuna"),
    (14,"Tahith Chong"),(15,"Kenji Gorre"),(16,"Jearl Margaritha"),(17,"Jurgen Locadia"),
    (18,"Jeremy Antonisse"),(19,"Gervane Kastaneer"),(20,"Sontje Hansen"),
])

# CZECHIA
standard_team("Czechia", "CZE", [
    (2,"Matej Kovar"),(3,"Jindrich Stanek"),(4,"Ladislav Krejci"),(5,"Vladimir Coufal"),
    (6,"Jaroslav Zeleny"),(7,"Tomas Holes"),(8,"David Zima"),(9,"Michal Sadilek"),
    (10,"Lukas Provod"),(11,"Lukas Cerv"),(12,"Tomas Soucek"),
    (14,"Pavel Sulc"),(15,"Matej Vydra"),(16,"Vasil Kusej"),(17,"Tomas Chory"),
    (18,"Vaclav Cerny"),(19,"Adam Hlozek"),(20,"Patrik Schick"),
])

# ECUADOR (type = "player")
standard_team_variant("Ecuador", "ECU", [
    (2,"Hernán Galíndez"),(3,"Gonzalo Valle"),(4,"Piero Hincapié"),(5,"Pervis Estupiñán"),
    (6,"Willian Pacho"),(7,"Ángelo Preciado"),(8,"Joel Ordóñez"),(9,"Moises Caicedo"),
    (10,"Alan Franco"),(11,"Kendry Paez"),(12,"Pedro Vite"),
    (14,"John Veboah"),(15,"Leonardo Campana"),(16,"Gonzalo Plata"),(17,"Nilson Angulo"),
    (18,"Alan Minda"),(19,"Kevin Rodriguez"),(20,"Enner Valencia"),
], ptype="player")

# EGYPT
standard_team("Egypt", "EGY", [
    (2,"Mohamed El Shenawy"),(3,"Mohamed Hany"),(4,"Mohamed Hamdy"),(5,"Yasser Ibrahim"),
    (6,"Khaled Sobhi"),(7,"Ramy Rabia"),(8,"Hossam Abdelmaguid"),(9,"Ahmed Fatouh"),
    (10,"Marwan Attia"),(11,"Zizo"),(12,"Hamdy Fathy"),
    (14,"Mohamed Lasheen"),(15,"Emam Ashour"),(16,"Osama Faisal"),(17,"Mohamed Salah"),
    (18,"Mostafa Mohamed"),(19,"Trezeguet"),(20,"Omar Marmoush"),
])

# ENGLAND
standard_team("England", "ENG", [
    (2,"Jordan Pickford"),(3,"John Stones"),(4,"Marc Guéhi"),(5,"Ezri Konsa"),
    (6,"Trent Alexander-Arnold"),(7,"Reece James"),(8,"Dan Burn"),(9,"Jordan Henderson"),
    (10,"Declan Rice"),(11,"Jude Bellingham"),(12,"Cole Palmer"),
    (14,"Morgan Rogers"),(15,"Anthony Gordon"),(16,"Phil Foden"),(17,"Bukayo Saka"),
    (18,"Harry Kane"),(19,"Marcus Rashford"),(20,"Ollie Watkins"),
])

# SPAIN
standard_team("Spain", "ESP", [
    (2,"Unai Simon"),(3,"Robin Le Normand"),(4,"Aymeric Laporte"),(5,"Dean Huijsen"),
    (6,"Pedro Porro"),(7,"Dani Carvajal"),(8,"Marc Cucurella"),(9,"Martín Zubimendi"),
    (10,"Rodri"),(11,"Pedri"),(12,"Fabian Ruiz"),
    (14,"Mikel Merino"),(15,"Lamine Yamal"),(16,"Dani Olmo"),(17,"Nico Williams"),
    (18,"Ferran Torres"),(19,"Álvaro Morata"),(20,"Mikel Oyarzabal"),
])

# FRANCE
standard_team("France", "FRA", [
    (2,"Mike Maignan"),(3,"Theo Hernandez"),(4,"William Saliba"),(5,"Jules Kounde"),
    (6,"Ibrahima Konate"),(7,"Dayot Upamecano"),(8,"Lucas Digne"),(9,"Aurélien Tchouaméni"),
    (10,"Eduardo Camavinga"),(11,"Manu Kone"),(12,"Adrien Rabiot"),
    (14,"Michael Olise"),(15,"Ousmane Dembele"),(16,"Bradley Barcola"),(17,"Désiré Doué"),
    (18,"Kingsley Coman"),(19,"Hugo Ekitike"),(20,"Kylian Mbappe"),
])

# GERMANY
standard_team("Germany", "GER", [
    (2,"Marc-André ter Stegen"),(3,"Jonathan Tah"),(4,"David Raum"),(5,"Nico Schlotterbeck"),
    (6,"Antonio Rüdiger"),(7,"Waldemar Anton"),(8,"Ridle Baku"),(9,"Maximilian Mittelstadt"),
    (10,"Joshua Kimmich"),(11,"Florian Wirtz"),(12,"Felix Nmecha"),
    (14,"Leon Goretzka"),(15,"Jamal Musiala"),(16,"Serge Gnabry"),(17,"Kai Havertz"),
    (18,"Leroy Sane"),(19,"Karim Adeyemi"),(20,"Nick Woltemade"),
])

# GHANA
standard_team("Ghana", "GHA", [
    (2,"Lawrence Ati Zigi"),(3,"Tariq Lamptey"),(4,"Mohammed Salisu"),(5,"Alidu Seidu"),
    (6,"Alexander Djiku"),(7,"Gideon Mensah"),(8,"Caleb Yirenkyi"),(9,"Abdul Issahaku Fatawu"),
    (10,"Thomas Partey"),(11,"Salis Abdul Samed"),(12,"Kamaldeen Sulemana"),
    (14,"Mohammed Kudus"),(15,"Inaki Williams"),(16,"Jordan Ayew"),(17,"Andrew Ayew"),
    (18,"Joseph Paintsil"),(19,"Osman Bukari"),(20,"Antoine Semenyo"),
])

# HAITI (ptype = "player")
standard_team_variant("Haiti", "HAI", [
    (2,"Johny Placide"),(3,"Carlens Arcus"),(4,"Martin Expérience"),(5,"Jean-Kevin Duverne"),
    (6,"Ricardo Adé"),(7,"Duke Lacroix"),(8,"Garven Metusala"),(9,"Hannes Delcroix"),
    (10,"Leverton Pierre"),(11,"Danley Jean Jacques"),(12,"Jean-Ricner Bellegarde"),
    (14,"Christopher Attys"),(15,"Derrick Etienne Jr"),(16,"Josue Casimir"),(17,"Ruben Providence"),
    (18,"Duckens Nazon"),(19,"Louicius Deedson"),(20,"Frantzdy Pierrot"),
], ptype="player")

# IRAN
standard_team("Iran", "IRN", [
    (2,"Alireza Beiranvand"),(3,"Morteza Pouraliganji"),(4,"Ehsan Hajsafi"),(5,"Milad Mohammadi"),
    (6,"Shojae Khalilzadeh"),(7,"Ramin Rezaeian"),(8,"Hossein Kanaani"),(9,"Sadegh Moharrami"),
    (10,"Saleh Hardani"),(11,"Saeed Ezatolahi"),(12,"Saman Ghoddos"),
    (14,"Omid Noorafkan"),(15,"Roozbeh Cheshmi"),(16,"Mohammad Mohebi"),(17,"Sardar Azmoun"),
    (18,"Mehdi Taremi"),(19,"Alireza Jahanbakhsh"),(20,"Ali Gholizadeh"),
])

# IRAQ
standard_team("Iraq", "IRQ", [
    (2,"Jalal Hassan"),(3,"Rebin Sulaka"),(4,"Hussein Ali"),(5,"Akam Hashem"),
    (6,"Merchas Doski"),(7,"Zaid Tahseen"),(8,"Manaf Younis"),(9,"Zidane Iqbal"),
    (10,"Amir Al-Ammari"),(11,"Ibrahim Bavesh"),(12,"Ali Jasim"),
    (14,"Youssef Amyn"),(15,"Aimar Sher"),(16,"Marko Farji"),(17,"Osama Rashid"),
    (18,"Ali Al-Hamadi"),(19,"Aymen Hussein"),(20,"Mohanad Ali"),
])

# JORDAN
standard_team("Jordan", "JOR", [
    (2,"Yazeed Abulaila"),(3,"Ihsan Haddad"),(4,"Mohammad Abu Hashish"),(5,"Yazan Al-Arab"),
    (6,"Abdallah Nasib"),(7,"Saleem Obaid"),(8,"Mohammad Abualnadi"),(9,"Ibrahim Saadeh"),
    (10,"Nizar Al-Rashdan"),(11,"Noor Al-Rawabdeh"),(12,"Mohannad Abu Taha"),
    (14,"Amer Jamous"),(15,"Musa Al-Taamari"),(16,"Yazan Al-Naimat"),(17,"Mahmoud Al-Mardi"),
    (18,"Ali Olwan"),(19,"Mohammad Abu Zrayq"),(20,"Ibrahim Sabra"),
])

# JAPAN
standard_team("Japan", "JPN", [
    (2,"Zion Suzuki"),(3,"Henry Heroki Mochizuki"),(4,"Ayumu Seko"),(5,"Junnosuke Suzuki"),
    (6,"Shogo Taniguchi"),(7,"Tsuyoshi Watanabe"),(8,"Kaishu Sano"),(9,"Yuki Soma"),
    (10,"Ao Tanaka"),(11,"Daichi Kamada"),(12,"Takefusa Kubo"),
    (14,"Ritsu Doan"),(15,"Keito Nakamura"),(16,"Takumi Minamino"),(17,"Shuto Machino"),
    (18,"Junya Ito"),(19,"Koki Ogawa"),(20,"Ayase Ueda"),
])

# SOUTH KOREA
standard_team("South Korea", "KOR", [
    (2,"Hyeon-woo Jo"),(3,"Seung-Gyu Kim"),(4,"Min-jae Kim"),(5,"Yu-min Cho"),
    (6,"Young-woo Seol"),(7,"Han-beom Lee"),(8,"Tae-seok Lee"),(9,"Myung-jae Lee"),
    (10,"Jae-sung Lee"),(11,"In-beom Hwang"),(12,"Kang-in Lee"),
    (14,"Seung-ho Paik"),(15,"Jens Castrop"),(16,"Dongg-yeong Lee"),(17,"Gue-sung Cho"),
    (18,"Heung-min Son"),(19,"Hee-chan Hwang"),(20,"Hyeon-Gyu Oh"),
])

# SAUDI ARABIA
standard_team("Saudi Arabia", "KSA", [
    (2,"Nawaf Alaqidi"),(3,"Abdulrahman Al-Sanbi"),(4,"Saud Abdulhamid"),(5,"Nawaf Bouwashl"),
    (6,"Jihad Thakri"),(7,"Moteb Al-Harbi"),(8,"Hassan Altambakti"),(9,"Musab Aljuwayr"),
    (10,"Ziyad Aljohani"),(11,"Abdullah Alkhaibari"),(12,"Nasser Aldawsari"),
    (14,"Saleh Abu Alshamat"),(15,"Marwan Alsahafi"),(16,"Salem Aldawsari"),(17,"Abdulrahman Al-Aboud"),
    (18,"Feras Akbrikan"),(19,"Saleh Alshehri"),(20,"Abdullah Al-Hamdan"),
])

# MOROCCO
standard_team("Morocco", "MAR", [
    (2,"Yassine Bounou"),(3,"Munir El Kajoui"),(4,"Achraf Hakimi"),(5,"Noussair Mazraoui"),
    (6,"Nayef Aguerd"),(7,"Roman Saiss"),(8,"Jawad El Yamio"),(9,"Adam Masina"),
    (10,"Sofyan Amrabat"),(11,"Azzedine Ounahi"),(12,"Eliesse Ben Seghir"),
    (14,"Bilal El Khannouss"),(15,"Ismael Saibari"),(16,"Youssef En-Nesyri"),(17,"Abde Ezzalzouli"),
    (18,"Soufiane Rahimi"),(19,"Brahim Diaz"),(20,"Ayoub El Kaabi"),
])

# MEXICO
standard_team("Mexico", "MEX", [
    (2,"Luis Malagón"),(3,"Johan Vasquez"),(4,"Jorge Sánchez"),(5,"Cesar Montes"),
    (6,"Jesus Gallardo"),(7,"Israel Reyes"),(8,"Diego Lainez"),(9,"Carlos Rodriguez"),
    (10,"Edson Alvarez"),(11,"Orbelin Pineda"),(12,"Marcel Ruiz"),
    (14,"Érick Sánchez"),(15,"Hirving Lozano"),(16,"Santiago Giménez"),(17,"Raúl Jiménez"),
    (18,"Alexis Vega"),(19,"Roberto Alvarado"),(20,"Cesar Huerta"),
])

# NETHERLANDS (ptype = "player")
standard_team_variant("Netherlands", "NED", [
    (2,"Bart Verbruggen"),(3,"Virgil van Dijk"),(4,"Micky van de Ven"),(5,"Jurrien Timber"),
    (6,"Denzel Dumfries"),(7,"Nathan Aké"),(8,"Jeremie Frimpong"),(9,"Jan Paul van Hecke"),
    (10,"Tijjani Reijnders"),(11,"Ryan Gravenberch"),(12,"Teun Koopmeiners"),
    (14,"Frenkie de Jong"),(15,"Xavi Simons"),(16,"Justin Kluivert"),(17,"Memphis Depay"),
    (18,"Donyell Malen"),(19,"Wout Weghorst"),(20,"Cody Gakpo"),
], ptype="player")

# NORWAY
standard_team("Norway", "NOR", [
    (2,"Orjan Nyland"),(3,"Julian Ryerson"),(4,"Leo Ostigård"),(5,"Kristoffer Vassbakk Ajer"),
    (6,"Marcus Holmgren Pedersen"),(7,"David Møller Wolfe"),(8,"Torbjørn Heggem"),(9,"Morten Thorsby"),
    (10,"Martin Ødegaard"),(11,"Sander Berge"),(12,"Andreas Schjelderup"),
    (14,"Patrick Berg"),(15,"Erling Haaland"),(16,"Alexander Sørloth"),(17,"Aron Dønnum"),
    (18,"Jorgen Strand Larsen"),(19,"Antonio Nusa"),(20,"Oscar Bobb"),
])

# NEW ZEALAND
standard_team("New Zealand", "NZL", [
    (2,"Max Crocombe Payne"),(3,"Alex Paulsen"),(4,"Michael Boxall"),(5,"Liberato Cacace"),
    (6,"Tim Payne"),(7,"Tyler Bindon"),(8,"Francis de Vries"),(9,"Finn Surman"),
    (10,"Joe Bell"),(11,"Sarpreet Singh"),(12,"Ryan Thomas"),
    (14,"Matthew Garbett"),(15,"Marko Stamenić"),(16,"Ben Old"),(17,"Chris Wood"),
    (18,"Elijah Just"),(19,"Callum McCowatt"),(20,"Kosta Barbarouses"),
])

# PANAMA
standard_team("Panama", "PAN", [
    (2,"Orlando Mosquera"),(3,"Luis Mejia"),(4,"Fidel Escobar"),(5,"Andres Andrade"),
    (6,"Michael Amir Murillo"),(7,"Eric Davis"),(8,"Jose Cordoba"),(9,"Cesar Blackman"),
    (10,"Cristian Martinez"),(11,"Aníbal Godoy"),(12,"Adalberto Carrasquilla"),
    (14,"Édgar Bárcenas"),(15,"Carlos Harvey"),(16,"Ismael Díaz"),(17,"Jose Fajardo"),
    (18,"Cecilio Waterman"),(19,"Jose Luiz Rodriguez"),(20,"Alberto Quintero"),
])

# PARAGUAY
standard_team("Paraguay", "PAR", [
    (2,"Roberto Fernandez"),(3,"Orlando Gill"),(4,"Gustavo Gomez"),(5,"Fabián Balbuena"),
    (6,"Juan José Cáceres"),(7,"Omar Alderete"),(8,"Junior Alonso"),(9,"Mathías Villasanti"),
    (10,"Diego Gomez"),(11,"Damián Bobadilla"),(12,"Andres Cubas"),
    (14,"Matias Galarza Fonda"),(15,"Julio Enciso"),(16,"Alejandro Romero Gamarra"),(17,"Miguel Almirón"),
    (18,"Ramon Sosa"),(19,"Angel Romero"),(20,"Antonio Sanabria"),
])

# PORTUGAL
standard_team("Portugal", "POR", [
    (2,"Diogo Costa"),(3,"Jose Sa"),(4,"Ruben Dias"),(5,"João Cancelo"),
    (6,"Diogo Dalot"),(7,"Nuno Mendes"),(8,"Gonçalo Inácio"),(9,"Bernardo Silva"),
    (10,"Bruno Fernandes"),(11,"Ruben Neves"),(12,"Vitinha"),
    (14,"João Neves"),(15,"Cristiano Ronaldo"),(16,"Francisco Trincao"),(17,"João Felix"),
    (18,"Gonçalo Ramos"),(19,"Pedro Neto"),(20,"Rafael Leão"),
])

# QATAR
standard_team("Qatar", "QAT", [
    (2,"Meshaal Barsham"),(3,"Sultan Albrake"),(4,"Lucas Mendes"),(5,"Homam Ahmed"),
    (6,"Boualem Khoukhi"),(7,"Pedro Miguel"),(8,"Tarek Salman"),(9,"Mohamed Al-Mannai"),
    (10,"Karim Boudiaf"),(11,"Assim Madibo"),(12,"Ahmed Fatehi"),
    (14,"Mohammed Waad"),(15,"Abdulaziz Hatem"),(16,"Hassan Al-Haydos"),(17,"Edmilson Junior"),
    (18,"Akram Hassan Afif"),(19,"Ahmed Al Ganehi"),(20,"Almoez Ali"),
])

# SOUTH AFRICA
standard_team("South Africa", "RSA", [
    (2,"Ronwen Williams"),(3,"Sipho Chaine"),(4,"Aubrey Modiba"),(5,"Samukele Kabini"),
    (6,"Mbekezeli Mbokazi"),(7,"Khulumani Ndamane"),(8,"Siyabonga Ngezana"),(9,"Khuliso Mudau"),
    (10,"Nkosinathi Sibisi"),(11,"Teboho Mokoena"),(12,"Thalente Mbatha"),
    (14,"Bathasi Aubaas"),(15,"Yaya Sithole"),(16,"Sipho Mbule"),(17,"Lyle Foster"),
    (18,"Iqraam Rayners"),(19,"Mohau Nkota"),(20,"Oswin Appollis"),
])

# SCOTLAND
standard_team("Scotland", "SCO", [
    (2,"Angus Gunn"),(3,"Jack Hendry"),(4,"Kieran Tierney"),(5,"Aaron Hickey"),
    (6,"Andrew Robertson"),(7,"Scott McKenna"),(8,"John Souttar"),(9,"Anthony Ralston"),
    (10,"Grant Hanley"),(11,"Scott McTominay"),(12,"Billy Gilmour"),
    (14,"Lewis Ferguson"),(15,"Ryan Christie"),(16,"Kenny McLean"),(17,"John McGinn"),
    (18,"Lyndon Dykes"),(19,"Che Adams"),(20,"Ben Gannon-Doak"),
])

# SENEGAL
standard_team("Senegal", "SEN", [
    (2,"Edouard Mendy"),(3,"Yehvann Diouf"),(4,"Moussa Niakhaté"),(5,"Abdoulaye Seck"),
    (6,"Ismail Jakobs"),(7,"El Hadji Malick Diouf"),(8,"Kalidou Koulibaly"),(9,"Idrissa Gana Gueye"),
    (10,"Pape Matar Sarr"),(11,"Pape Gueye"),(12,"Habib Diarra"),
    (14,"Lamine Camara"),(15,"Sadio Mane"),(16,"Ismaïla Sarr"),(17,"Boulaye Dia"),
    (18,"Iliman Ndiaye"),(19,"Nicolas Jackson"),(20,"Krepin Diatta"),
])

# SWITZERLAND
standard_team("Switzerland", "SUI", [
    (2,"Gregor Kobel"),(3,"Yvon Mvogo"),(4,"Manuel Akanji"),(5,"Ricardo Rodriguez"),
    (6,"Nico Elvedi"),(7,"Aurèle Amenda"),(8,"Silvan Widmer"),(9,"Granit Xhaka"),
    (10,"Denis Zakaria"),(11,"Remo Freuler"),(12,"Fabian Rieder"),
    (14,"Ardon Jashari"),(15,"Johan Manzambi"),(16,"Michel Aebischer"),(17,"Breel Embolo"),
    (18,"Ruben Vargas"),(19,"Dan Ndoye"),(20,"Zeki Amdouni"),
])

# SWEDEN
standard_team("Sweden", "SWE", [
    (2,"Victor Johansson"),(3,"Isak Hien"),(4,"Gabriel Gudmundsson"),(5,"Emil Holm"),
    (6,"Victor Nilsson Lindelöf"),(7,"Gustaf Lagerbielke"),(8,"Lucas Bergvall"),(9,"Hugo Larsson"),
    (10,"Jesper Karlström"),(11,"Yasin Ayari"),(12,"Mattias Svanberg"),
    (14,"Daniel Svensson"),(15,"Ken Sema"),(16,"Roony Bardghji"),(17,"Dejan Kulusevski"),
    (18,"Anthony Elanga"),(19,"Alexander Isak"),(20,"Viktor Gyökeres"),
])

# TUNISIA
standard_team("Tunisia", "TUN", [
    (2,"Bechir Ben Said"),(3,"Aymen Dahmen"),(4,"Yan Valery"),(5,"Montassar Talbi"),
    (6,"Yassine Meriah"),(7,"Ali Abdi"),(8,"Dylan Bronn"),(9,"Ellyes Skhiri"),
    (10,"Aissa Laidouni"),(11,"Ferjani Sassi"),(12,"Mohamed Ali Ben Romdhane"),
    (14,"Hannibal Mejbri"),(15,"Elias Achouri"),(16,"Elias Saad"),(17,"Hazem Mastouri"),
    (18,"Ismael Gharbi"),(19,"Sayfallah Ltaief"),(20,"Naim Sliti"),
])

# TURKEY
standard_team("Turkey", "TUR", [
    (2,"Ugurcan Cakir"),(3,"Mert Muldur"),(4,"Zeki Celik"),(5,"Abdulkerim Bardakci"),
    (6,"Caglar Soyuncu"),(7,"Merih Demiral"),(8,"Ferdi Kadioglu"),(9,"Kaan Ayhan"),
    (10,"Ismail Yuksek"),(11,"Hakan Calhanoglu"),(12,"Orkun Kokcu"),
    (14,"Arda Guler"),(15,"Irfan Can Kahveci"),(16,"Yunus Akgun"),(17,"Can Uzun"),
    (18,"Baris Alper Yilmaz"),(19,"Kerem Akturkoglu"),(20,"Kenan Yildiz"),
])

# URUGUAY
standard_team("Uruguay", "URU", [
    (2,"Sergio Rochet"),(3,"Santiago Mele"),(4,"Ronald Araujo"),(5,"José María Giménez"),
    (6,"Sebastian Caceres"),(7,"Mathias Olivera"),(8,"Guillermo Varela"),(9,"Nahitan Nandez"),
    (10,"Federico Valverde"),(11,"Giorgian De Arrascaeta"),(12,"Rodrigo Bentancur"),
    (14,"Manuel Ugarte"),(15,"Nicolás de la Cruz"),(16,"Maxi Araujo"),(17,"Darwin Núñez"),
    (18,"Federico Viñas"),(19,"Rodrigo Aguirre"),(20,"Facundo Pellistri"),
])

# UNITED STATES
standard_team("United States", "USA", [
    (2,"Math Freese"),(3,"Chris Richards"),(4,"Tim Ream"),(5,"Mark McKenzie"),
    (6,"Alex Freeman"),(7,"Antonee Robinson"),(8,"Tyler Adams"),(9,"Tanner Tessmann"),
    (10,"Weston McKenny"),(11,"Christian Roldan"),(12,"Timothy Weah"),
    (14,"Diego Luna"),(15,"Malik Tillman"),(16,"Christian Pulisic"),(17,"Brenden Aaronson"),
    (18,"Ricardo Pepi"),(19,"Haji Wright"),(20,"Folarin Balogun"),
])

# UZBEKISTAN (ptype = "player")
standard_team_variant("Uzbekistan", "UZB", [
    (2,"Utkir Yusupov"),(3,"Farrukh Savfiev"),(4,"Sherzod Nasrullaev"),(5,"Umar Eshmurodov"),
    (6,"Husniddin Aliqulov"),(7,"Rustamjon Ashurmatov"),(8,"Khojiakbar Alijonov"),(9,"Abdukodir Khusanov"),
    (10,"Odiljon Hamrobekov"),(11,"Otabek Shukurov"),(12,"Jamshid Iskanderov"),
    (14,"Azizbek Turgunboev"),(15,"Khojimat Erkinov"),(16,"Eldor Shomurodov"),(17,"Oston Urunov"),
    (18,"Jaloliddin Masharipov"),(19,"Igor Sergeev"),(20,"Abbosbek Fayzullaev"),
], ptype="player")

print("Total rows:", len(rows))

from collections import Counter
c = Counter(r[0] for r in rows)
for team, cnt in c.items():
    if cnt != 20 and team not in ("Panini","World Cup History"):
        print("WARNING:", team, cnt)
print("Panini:", c.get("Panini"))
print("World Cup History:", c.get("World Cup History"))
print("Number of teams total:", len(c))

with open("wc26_checklist.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["team","team_code","number","name","type"])
    for r in rows:
        w.writerow(r)

print("Done.")
