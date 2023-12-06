#note: 'dark' type does not exist in gen 1 (red/blue/yellow) and was added for potential expansion
types = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'dark', 'Steel', 'Fairy']

# data organized with the following headings:
# number, name, type(s), HP, Attack, Defense, Sp. Atk, Sp. Def, and Speed
pokedex = [["001", "Bulbasaur", ["Grass", "Poison"], "45", "49", "49", "65", "65", "45"],
           ["002", "Ivysaur", ["Grass", "Poison"], "60", "62", "63", "80", "80", "60"],
           ["003", "Venusaur", ["Grass", "Poison"], "80", "82", "83", "100", "100", "80"],
           ["004", "Charmander", ["Fire"], "39", "52", "43", "60", "50", "65"],
           ["005", "Charmeleon", ["Fire"], "58", "64", "58", "80", "65", "80"],
           ["006", "Charizard", ["Fire", "Flying"], "78", "84", "78", "109", "85", "100"],
           ["007", "Squirtle", ["Water"], "44", "48", "65", "50", "64", "43"],
           ["008", "Wartortle", ["Water"], "59", "63", "80", "65", "80", "58"],
           ["009", "Blastoise", ["Water"], "79", "83", "100", "85", "105", "78"],
           ["010", "Caterpie", ["Bug"], "45", "30", "35", "20", "20", "45"],
           ["011", "Metapod", ["Bug"], "50", "20", "55", "25", "25", "30"],
           ["012", "Butterfree", ["Bug", "Flying"], "60", "45", "50", "90", "80", "70"],
           ["013", "Weedle", ["Bug", "Poison"], "40", "35", "30", "20", "20", "50"],
           ["014", "Kakuna", ["Bug", "Poison"], "45", "25", "50", "25", "25", "35"],
           ["015", "Beedrill", ["Bug", "Poison"], "65", "90", "40", "45", "80", "75"],
           ["016", "Pidgey", ["Normal", "Flying"], "40", "45", "40", "35", "35", "56"],
           ["017", "Pidgeotto", ["Normal", "Flying"], "63", "60", "55", "50", "50", "71"],
           ["018", "Pidgeot", ["Normal", "Flying"], "83", "80", "75", "70", "70", "101"],
           ["019", "Rattata", ["Normal"], "30", "56", "35", "25", "35", "72"],
           ["020", "Raticate", ["Normal"], "55", "81", "60", "50", "70", "97"],
           ["021", "Spearow", ["Normal", "Flying"], "40", "60", "30", "31", "31", "70"],
           ["022", "Fearow", ["Normal", "Flying"], "65", "90", "65", "61", "61", "100"],
           ["023", "Ekans", ["Poison"], "35", "60", "44", "40", "54", "55"],
           ["024", "Arbok", ["Poison"], "60", "95", "69", "65", "79", "80"],
           ["025", "Pikachu", ["Electric"], "35", "55", "40", "50", "50", "90"],
           ["026", "Raichu", ["Electric"], "60", "90", "55", "90", "80", "110"],
           ["027", "Sandshrew", ["Ground"], "50", "75", "85", "20", "30", "40"],
           ["028", "Sandslash", ["Ground"], "75", "100", "110", "45", "55", "65"],
           ["029", "Nidoran♀", ["Poison"], "55", "47", "52", "40", "40", "41"],
           ["030", "Nidorina", ["Poison"], "70", "62", "67", "55", "55", "56"],
           ["031", "Nidoqueen", ["Poison", "Ground"], "90", "92", "87", "75", "85", "76"],
           ["032", "Nidoran♂", ["Poison"], "46", "57", "40", "40", "40", "50"],
           ["033", "Nidorino", ["Poison"], "61", "72", "57", "55", "55", "65"],
           ["034", "Nidoking", ["Poison", "Ground"], "81", "102", "77", "85", "75", "85"],
           ["035", "Clefairy", ["Fairy"], "70", "45", "48", "60", "65", "35"],
           ["036", "Clefable", ["Fairy"], "95", "70", "73", "95", "90", "60"],
           ["037", "Vulpix", ["Fire"], "38", "41", "40", "50", "65", "65"],
           ["038", "Ninetales", ["Fire"], "73", "76", "75", "81", "100", "100"],
           ["039", "Jigglypuff", ["Normal", "Fairy"], "115", "45", "20", "45", "25", "20"],
           ["040", "Wigglytuff", ["Normal", "Fairy"], "140", "70", "45", "85", "50", "45"],
           ["041", "Zubat", ["Poison", "Flying"], "40", "45", "35", "30", "40", "55"],
           ["042", "Golbat", ["Poison", "Flying"], "75", "80", "70", "65", "75", "90"],
           ["043", "Oddish", ["Grass", "Poison"], "45", "50", "55", "75", "65", "30"],
           ["044", "Gloom", ["Grass", "Poison"], "60", "65", "70", "85", "75", "40"],
           ["045", "Vileplume", ["Grass", "Poison"], "75", "80", "85", "110", "90", "50"],
           ["046", "Paras", ["Bug", "Grass"], "35", "70", "55", "45", "55", "25"],
           ["047", "Parasect", ["Bug", "Grass"], "60", "95", "80", "60", "80", "30"],
           ["048", "Venonat", ["Bug", "Poison"], "60", "55", "50", "40", "55", "45"],
           ["049", "Venomoth", ["Bug", "Poison"], "70", "65", "60", "90", "75", "90"],
           ["050", "Diglett", ["Ground"], "10", "55", "25", "35", "45", "95"],
           ["051", "Dugtrio", ["Ground"], "35", "100", "50", "50", "70", "120"],
           ["052", "Meowth", ["Normal"], "40", "45", "35", "40", "40", "90"],
           ["053", "Persian", ["Normal"], "65", "70", "60", "65", "65", "115"],
           ["054", "Psyduck", ["Water"], "50", "52", "48", "65", "50", "55"],
           ["055", "Golduck", ["Water"], "80", "82", "78", "95", "80", "85"],
           ["056", "Mankey", ["Fighting"], "40", "80", "35", "35", "45", "70"],
           ["057", "Primeape", ["Fighting"], "65", "105", "60", "60", "70", "95"],
           ["058", "Growlithe", ["Fire"], "55", "70", "45", "70", "50", "60"],
           ["059", "Arcanine", ["Fire"], "90", "110", "80", "100", "80", "95"],
           ["060", "Poliwag", ["Water"], "40", "50", "40", "40", "40", "90"],
           ["061", "Poliwhirl", ["Water"], "65", "65", "65", "50", "50", "90"],
           ["062", "Poliwrath", ["Water", "Fighting"], "90", "95", "95", "70", "90", "70"],
           ["063", "Abra", ["Psychic"], "25", "20", "15", "105", "55", "90"],
           ["064", "Kadabra", ["Psychic"], "40", "35", "30", "120", "70", "105"],
           ["065", "Alakazam", ["Psychic"], "55", "50", "45", "135", "95", "120"],
           ["066", "Machop", ["Fighting"], "70", "80", "50", "35", "35", "35"],
           ["067", "Machoke", ["Fighting"], "80", "100", "70", "50", "60", "45"],
           ["068", "Machamp", ["Fighting"], "90", "130", "80", "65", "85", "55"],
           ["069", "Bellsprout", ["Grass", "Poison"], "50", "75", "35", "70", "30", "40"],
           ["070", "Weepinbell", ["Grass", "Poison"], "65", "90", "50", "85", "45", "55"],
           ["071", "Victreebel", ["Grass", "Poison"], "80", "105", "65", "100", "70", "70"],
           ["072", "Tentacool", ["Water", "Poison"], "40", "40", "35", "50", "100", "70"],
           ["073", "Tentacruel", ["Water", "Poison"], "80", "70", "65", "80", "120", "100"],
           ["074", "Geodude", ["Rock", "Ground"], "40", "80", "100", "30", "30", "20"],
           ["075", "Graveler", ["Rock", "Ground"], "55", "95", "115", "45", "45", "35"],
           ["076", "Golem", ["Rock", "Ground"], "80", "120", "130", "55", "65", "45"],
           ["077", "Ponyta", ["Fire"], "50", "85", "55", "65", "65", "90"],
           ["078", "Rapidash", ["Fire"], "65", "100", "70", "80", "80", "105"],
           ["079", "Slowpoke", ["Water", "Psychic"], "90", "65", "65", "40", "40", "15"],
           ["080", "Slowbro", ["Water", "Psychic"], "95", "75", "110", "100", "80", "30"],
           ["081", "Magnemite", ["Electric", "Steel"], "25", "35", "70", "95", "55", "45"],
           ["082", "Magneton", ["Electric", "Steel"], "50", "60", "95", "120", "70", "70"],
           ["083", "Farfetch'd", ["Normal", "Flying"], "52", "90", "55", "58", "62", "60"],
           ["084", "Doduo", ["Normal", "Flying"], "35", "85", "45", "35", "35", "75"],
           ["085", "Dodrio", ["Normal", "Flying"], "60", "110", "70", "60", "60", "110"],
           ["086", "Seel", ["Water"], "65", "45", "55", "45", "70", "45"],
           ["087", "Dewgong", ["Water", "Ice"], "90", "70", "80", "70", "95", "70"],
           ["088", "Grimer", ["Poison"], "80", "80", "50", "40", "50", "25"],
           ["089", "Muk", ["Poison"], "105", "105", "75", "65", "100", "50"],
           ["090", "Shellder", ["Water"], "30", "65", "100", "45", "25", "40"],
           ["091", "Cloyster", ["Water", "Ice"], "50", "95", "180", "85", "45", "70"],
           ["092", "Gastly", ["Ghost", "Poison"], "30", "35", "30", "100", "35", "80"],
           ["093", "Haunter", ["Ghost", "Poison"], "45", "50", "45", "115", "55", "95"],
           ["094", "Gengar", ["Ghost", "Poison"], "60", "65", "60", "130", "75", "110"],
           ["095", "Onix", ["Rock", "Ground"], "35", "45", "160", "30", "45", "70"],
           ["096", "Drowzee", ["Psychic"], "60", "48", "45", "43", "90", "42"],
           ["097", "Hypno", ["Psychic"], "85", "73", "70", "73", "115", "67"],
           ["098", "Krabby", ["Water"], "30", "105", "90", "25", "25", "50"],
           ["099", "Kingler", ["Water"], "55", "130", "115", "50", "50", "75"],
           ["100", "Voltorb", ["Electric"], "40", "30", "50", "55", "55", "100"],
           ["101", "Electrode", ["Electric"], "60", "50", "70", "80", "80", "150"],
           ["102", "Exeggcute", ["Grass", "Psychic"], "60", "40", "80", "60", "45", "40"],
           ["103", "Exeggutor", ["Grass", "Psychic"], "95", "95", "85", "125", "75", "55"],
           ["104", "Cubone", ["Ground"], "50", "50", "95", "40", "50", "35"],
           ["105", "Marowak", ["Ground"], "60", "80", "110", "50", "80", "45"],
           ["106", "Hitmonlee", ["Fighting"], "50", "120", "53", "35", "110", "87"],
           ["107", "Hitmonchan", ["Fighting"], "50", "105", "79", "35", "110", "76"],
           ["108", "Lickitung", ["Normal"], "90", "55", "75", "60", "75", "30"],
           ["109", "Koffing", ["Poison"], "40", "65", "95", "60", "45", "35"],
           ["110", "Weezing", ["Poison"], "65", "90", "120", "85", "70", "60"],
           ["111", "Rhyhorn", ["Ground", "Rock"], "80", "85", "95", "30", "30", "25"],
           ["112", "Rhydon", ["Ground", "Rock"], "105", "130", "120", "45", "45", "40"],
           ["113", "Chansey", ["Normal"], "250", "5", "5", "35", "105", "50"],
           ["114", "Tangela", ["Grass"], "65", "55", "115", "100", "40", "60"],
           ["115", "Kangaskhan", ["Normal"], "105", "95", "80", "40", "80", "90"],
           ["116", "Horsea", ["Water"], "30", "40", "70", "70", "25", "60"],
           ["117", "Seadra", ["Water"], "55", "65", "95", "95", "45", "85"],
           ["118", "Goldeen", ["Water"], "45", "67", "60", "35", "50", "63"],
           ["119", "Seaking", ["Water"], "80", "92", "65", "65", "80", "68"],
           ["120", "Staryu", ["Water"], "30", "45", "55", "70", "55", "85"],
           ["121", "Starmie", ["Water", "Psychic"], "60", "75", "85", "100", "85", "115"],
           ["122", "Mr. Mime", ["Psychic", "Fairy"], "40", "45", "65", "100", "120", "90"],
           ["123", "Scyther", ["Bug", "Flying"], "70", "110", "80", "55", "80", "105"],
           ["124", "Jynx", ["Ice", "Psychic"], "65", "50", "35", "115", "95", "95"],
           ["125", "Electabuzz", ["Electric"], "65", "83", "57", "95", "85", "105"],
           ["126", "Magmar", ["Fire"], "65", "95", "57", "100", "85", "93"],
           ["127", "Pinsir", ["Bug"], "65", "125", "100", "55", "70", "85"],
           ["128", "Tauros", ["Normal"], "75", "100", "95", "40", "70", "110"],
           ["129", "Magikarp", ["Water"], "20", "10", "55", "15", "20", "80"],
           ["130", "Gyarados", ["Water", "Flying"], "95", "125", "79", "60", "100", "81"],
           ["131", "Lapras", ["Water", "Ice"], "130", "85", "80", "85", "95", "60"],
           ["132", "Ditto", ["Normal"], "48", "48", "48", "48", "48", "48"],
           ["133", "Eevee", ["Normal"], "55", "55", "50", "45", "65", "55"],
           ["134", "Vaporeon", ["Water"], "130", "65", "60", "110", "95", "65"],
           ["135", "Jolteon", ["Electric"], "65", "65", "60", "110", "95", "130"],
           ["136", "Flareon", ["Fire"], "65", "130", "60", "95", "110", "65"],
           ["137", "Porygon", ["Normal"], "65", "60", "70", "85", "75", "40"],
           ["138", "Omanyte", ["Rock", "Water"], "35", "40", "100", "90", "55", "35"],
           ["139", "Omastar", ["Rock", "Water"], "70", "60", "125", "115", "70", "55"],
           ["140", "Kabuto", ["Rock", "Water"], "30", "80", "90", "55", "45", "55"],
           ["141", "Kabutops", ["Rock", "Water"], "60", "115", "105", "65", "70", "80"],
           ["142", "Aerodactyl", ["Rock", "Flying"], "80", "105", "65", "60", "75", "130"],
           ["143", "Snorlax", ["Normal"], "160", "110", "65", "65", "110", "30"],
           ["144", "Articuno", ["Ice", "Flying"], "90", "85", "100", "95", "125", "85"],
           ["145", "Zapdos", ["Electric", "Flying"], "90", "90", "85", "125", "90", "100"],
           ["146", "Moltres", ["Fire", "Flying"], "90", "100", "90", "125", "85", "90"],
           ["147", "Dratini", ["Dragon"], "41", "64", "45", "50", "50", "50"],
           ["148", "Dragonair", ["Dragon"], "61", "84", "65", "70", "70", "70"],
           ["149", "Dragonite", ["Dragon", "Flying"], "91", "134", "95", "100", "100", "80"],
           ["150", "Mewtwo", ["Psychic"], "106", "110", "90", "154", "90", "130"],
           ["151", "Mew", ["Psychic"], "100", "100", "100", "100", "100", "100"]           
    ]

strong_against_normal = ["Fighting"]
weak_against_normal = ["Ghost"]
strong_against_fire = ["Water", "Ground", "Rock"]
weak_against_fire = ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"]
strong_against_water = ["Electric", "Grass"]
weak_against_water = ["Fire", "Water", "Ice", "Steel"]
strong_against_electric = ["Ground"]
weak_against_electric = ["Electric", "Flying", "Steel"]
strong_against_grass = ["Fire", "Ice", "Poison", "Flying", "Bug"]
weak_against_grass = ["Water", "Electric", "Grass", "Ground"]
strong_against_ice = ["Fire", "Fighting", "Rock", "Steel"]
weak_against_ice = ["Ice"]
strong_against_fighting = ["Flying", "Psychic", "Fairy"]
weak_against_fighting = ["Bug", "Rock", "Dark"]
strong_against_poison = ["Ground", "Psychic"]
weak_against_poison = ["Grass", "Fighting", "Poison", "Bug", "Fairy"]
strong_against_ground = ["Water", "Grass", "Ice"]
weak_against_ground = ["Poison", "Rock", "Electric"]
strong_against_flying = ["Electric", "Ice", "Rock"]
weak_against_flying = ["Grass", "Fighting", "Bug", "Ground"]
strong_against_psychic = ["Bug", "Ghost", "Dark"]
weak_against_psychic = ["Fighting", "Psychic"]
string_against_bug = ["Fire", "Flying", "Rock"]
weak_against_bug = ["Grass", "Fighting", "Ground"]
strong_against_rock = ["Water", "Grass", "Fighting", "Ground", "Steel"]
weak_against_rock = ["Normal", "Fire", "Poison", "Flying"]
strong_against_ghost = ["Ghost", "Dark"]
weak_against_ghost = ["Poison", "Bug", "Normal", "Fighting"]
strong_against_dragon = ["Ice", "Dragon", "Fairy"]
weak_against_dragon = ["Fire", "Water", "Electric", "Grass"]
strong_against_dark = ["Fighting", "Bug", "Fairy"]
weak_against_dark = ["Ghost", "Dark", "Psychic"]
strong_against_steel = ["Fire", "Fighting", "Ground"]
weak_against_steel = ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"]
strong_against_fairy = ["Poison", "Steel"]
weak_against_fairy = ["Fighting", "Bug", "Dark", "Dragon"]