import time,sys
import os
import random
import pygame
pygame.mixer.init()

import sys
import os

#load xml file for bar kochba campaign
from bs4 import BeautifulSoup as bs
content = []
# Read the XML file and pass into beautiful soup xml library
#ask users if they want to import a custom xml if just press enter import default Bar Kochba Campaign
userxml = input("What XML campaign do you wish to import. Pls type the file name and make sure its in the same directory as the game is running from")
try:
    infile = open(userxml,"r")
except:
    infile = open("bar-kochba-campaign.xml","r")
contents = infile.read()
soup = bs(contents,'xml')
#get name,strength,defense and health from bar kochba campaign xml
names = soup.find_all('name')
strengths = soup.find_all('strength')
defenses = soup.find_all('defense')
healths = soup.find_all('health')


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#fix music issue by changing music handling so first loaded then played
pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.play(-1)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)


#important stuff
#player_health = 600
class YiddisheCommander:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self,Enemy):
        time.sleep(1)
        print ("what move would you like to make? (attack openly (1), guerilla strike(2) or get health?(3)")
        print("")
        answer = input()

        if answer == "1":
            Enemy.health = Enemy.health - (self.strength * random.uniform(0.1, 1.4))
            Enemy.health = int(Enemy.health)
        elif answer == "2":
            Enemy.health = float(Enemy.health) - (self.strength * random.uniform(0.1, 2.0))
            Enemy.health = int(Enemy.health)
        elif answer == "3":
            self.health = self.health + (self.strength * random.uniform(0.1, 1.4))
            self.health = int(self.health)
        else:
            print("Invalid, so do nothing")

        time.sleep(1)

        print (Enemy.name + "'s health is now: " + str(int(Enemy.health)))
        print("")

        return int(Enemy.health)

class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health



    def enemy_attack(self,commanders):

        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        commanders.health = int(commanders.health) - (int(self.strength) * random.uniform(0.1, 2.0))
        commanders.health = int(commanders.health)
        time.sleep(1)
        print (commanders.name + "'s health is now " + str(int(commanders.health)))
        print ("")
        return(commanders)



    def battle_script(self,commanders):

        print ("A Roman enemy " + self.name + " appears to fight "+ commanders.name +".")
        print ("")
        time.sleep(1)
        while int(commanders.health) > 0 and int(self.health) > 0:
            commanders.attack_enemy(random_enemy)
            if self.health <=0:
                time.sleep(1)
                print ("You have defeated  " + self.name)

                return "defeat1"
            self.enemy_attack(commanders)
            if commanders.health <=0:
                time.sleep(1)
                print ("Sorry, " + commanders.name +  " was defeated.")
                return "defeat2"
def endprompt():
    go_back = input("do you want to go back to main screen? Type 'yes' or 'no.'")
    if (go_back == "yes"):
        start()
    elif (go_back == "no"):
        quit()
    else:
        endprompt()
def game():
    print("You, Bar Kochba have been appointed for this mission.")
    time.sleep(0)


    print_slow("You will fight several Roman armies throughout Judea.\n")
    print_slow("You will fight your Roman opponents\n")
    #read xml files and put into variables, then fill in these variables to commanders and enemies data


    commanders = [YiddisheCommander((names[0].get_text()),int((strengths[0].get_text())),int((defenses[0].get_text())),int((healths[0].get_text()))),YiddisheCommander((names[1].get_text()),int(((strengths[1].get_text()))),int((defenses[1].get_text())),int((healths[1].get_text()))),YiddisheCommander((names[2].get_text()),int(((strengths[2].get_text()))),int((defenses[2].get_text())),int((healths[2].get_text())))]
    enemies = [Enemy((names[3].get_text()), int((strengths[3].get_text())), int((defenses[3].get_text())), int((healths[3].get_text()))), Enemy((names[4].get_text()), int((strengths[4].get_text())), int((defenses[4].get_text())), int((healths[4].get_text()))), Enemy((names[5].get_text()), int((strengths[5].get_text())), int((defenses[5].get_text())), int((healths[5].get_text()))), Enemy ((names[6].get_text()), int((strengths[6].get_text())), int((defenses[6].get_text())), int((healths[6].get_text()))), Enemy ((names[7].get_text()),int((strengths[7].get_text())),int((defenses[7].get_text())),int((healths[7].get_text()))),Enemy((names[8].get_text()),int((strengths[8].get_text())),int((defenses[8].get_text())),int((healths[8].get_text())))]


    #game loop
    while len(commanders) !=0 and len(enemies) != 0:
        global random_enemy
        random_enemy = random.choice(enemies)
        global random_commander
        random_commander = random.choice(commanders)
        global result
        result = random_enemy.battle_script(random_commander)
        if (result=="defeat1"):
            index = enemies.index(random_enemy)
            enemies.pop(index)
        if (result=="defeat2"):
            index = commanders.index(random_commander)
            commanders.pop(index)
    endprompt()
def print_sources():
    print("Welcome to the Bar Kochba literature library.")
    print("From 1 to 10 select which source you wish to review")
    print("""
    1.Midrash Lamentations
    2.Gittin
    3.Cassius Dio
    4.Justin Martyr
    5.Eusebius
    6.Eusebius latin edition
    7.Jerome
    8.Epiphanus
    9.Song
    10.play game""")
    choice = int(input("Select your source:"))
    if choice == 1:
        print("[1] When Rabbi Akiva beheld Bar Kozeba, he exclaimed: 'This is\nthe king Messiah!' Rabbi Johanan ben Torta retorted: 'Akiva, grass will\ngrow in your cheeks and he will still not have come!'")

        print("[2] Eighty thousand trumpeters besieged Bethar where Bar Kozeba\nwas located, who had with him two hundred thousand men with an amputated\nfinger.The Sages sent him the message, 'How long will you continue\nto make the men of Israel blemished?'He asked them, 'How else shall they\nbe tested?' They answered, 'Let anyone who cannot uproot a cedar from\nLebanon be refused enrollment in your army.' He thereupon had two\nhundred thousand men of each class; and when they went forth to battle\nthey cried, 'O God, neither help nor discourage us!'That is what is\nwritten, Hast not Thou, o God, cast us off? And go not forth, o God,\nwith our hosts?And what did Bar Kozeba use to do? He would catch the\nmissiles from the enemy's catapults on one of his knees and hurl them\nback, killing many of the foe. On that account, Rabbi Akiva made his\nremark.")
        print("[3] For three and a half years the emperor Hadrian surrounded \nBethar. In the city was rabbi Eleazar of Mode'in, who continually \n wore sackcloth and fasted, and used to pray daily: 'Lord of the universe\n , sit not in judgment today!' so that Hadrian thought of returning home.\n A Cuthean went [to the emperor] and found him and said: 'My lord, so \n long as that old cock wallows in ashes, you will not conquer the city. But wait \n for me, because I will do something that will enable you to subdue it today.'\n He immediately entered the gate of the city, where he found rabbi Eleazar \n standing and praying. He pretended to whisper in the ear of rabbi Eleazar of Mode'in. \n People went and informed Bar Kozeba: 'Your friend, rabbi Eleazar, wishes to \n surrender the city to Hadrian.' He sent and had the Cuthean brought to him and \n asked: 'What did you say to him?' He replied: 'If I tell you, the emperor will\n kill me; and if I do not tell you, you will kill me. It is better that I should \n kill myself and the secrets of the government be not divulged.' Bar Kozeba was\n convinced that rabbi Eleazar wanted to surrender the city, so when the latter \n finished his praying, he had him brought into his presence and asked him: 'What\n did the Cuthean tell you?' He answered: 'I do not know what he whispered in my \n ear, nor did I hear anything, because I was standing in prayer and am unaware \n what he said.' Bar Kozeba flew into a rage, kicked him with his foot and killed \n him. A heavenly voice issued forth and proclaimed: 'Woe to the worthless shepherd\n that leaveth the flock! The sword shall be upon his arm, and upon his right arm!'\n It was intimated to him, 'Thou hast paralyzed the arm of Israel and blinded their\n right eye; therefore shall thy arm wither and thy right arm grow dim!' Forthwith\n the sins [of the people] caused Bethar to be captured. Bar Kozeba was slain and \n his head taken to Hadrian. He asked: 'Who killed him?' A Cuthean said to him:'I\n killed him.' 'Bring his body to me,' he ordered. He went and and found a snake \n encircling its neck. So Hadrian, when told of this, exclaimed: 'If his God had \nnot slain him, who could have overcome him?'  And there was applied to him the \n verse: Except their rock had given them over.")
        print("[4]There were two brothers in Kefar Haruba, who did not allow any Roman to pass there, because they killed him. They said: 'The conclusion of the whole matter is that we must take Hadrian's crown and set it upon our own head.'They heard that the Romans were coming towards them; and when they set out \n against them, an old man met them and said: 'May the Creator be your help against them!' They retorted: 'Let him neither help nor discourage us!'\n Their sins immediately caused them to be slain. Their heads were brought to \n Hadrian, who asked: 'Who killed them?' A Cuthean replied: 'I slew him.'\n And the emperor ordered him to fetch their bodies.\n He went and and found a snake encircling their necks. So Hadrian, when told of \n this, exclaimed: 'If their God had not slain them, who could have overcome them?'\n And there was applied to him the verse: Except their rock had given them over")
        print("[5] Rabbi Jonathan said: The voice is the voice of Jacob - the \nvoice of distress caused by the emperor Hadrian, who slew eighty thousand myriads of human beings at Bethar.")
        print("[6]They slew the inhabitants until the horses waded in blood up \n to the nostrils, and the blood rolled along stones (with the size of 284\n liters) and flowed into the sea, staining it for a distance of six kilometers.\n (In case you think that Bethar is close to the sea: was it not in fact \n sixty kilometers distant from it?) Now Hadrian possessed a large vineyard\n 46 kilometers square, as far as from Tiberias to Sepphoris, and they surrounded\n it with a fence consisting of the slain of Bethar. And it was decreed that\n they should not be buried, until a certain emperor arose and ordered their\n interment. Rabbi Huna said: 'On the day when the slain of Bethar were allowed\n burial, the benediction Who art kind and dealest kindly was instituted -\n Who art kind because the bodies did not putrefy, and dealest kindly because\n they were allowed burial.'")
        print("[7] Rabbi Johanan said: 'The brains of three hundred children were dashed upon one stone, and three hundred baskets of capsules of phylacteries were found in Bethar, each capsule having a capacity of 2130 liters.' Rabbi Gamaliel said: 'There were five hundred schools in Bethar, and the smallest of them had no less than three hundred children. They used to say: 'If the enemy comes against us, with these styluses we will go out and stab them.' When, however, the people's sins did cause the enemy to come, they enwrapped each pupil in his book and burnt him, so that I alone was left. He affected to himself the verse: Mine eye affecteth my soul, because of all the daughters of my city")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice == 2:
        print("[1] 'Through the shaft of a litter, Betar was destroyed.' It \n was the custom when a boy was born to plant a cedar tree, and when a girl\n was born to plant a pine tree. When they married, the tree was cut down \n and a canopy was made of the branches. One day, the daughter of the emperor\n was passing when the shaft of her litter broke, so they lopped some branches\n off a cedar tree and brought it to her. The Jews thereupon fell upon them\n and beat them. They reported to the emperor that the Jews were rebelling,\n and he marched against them.")
        print("[2]He hath cut off in fierce anger all the horn of Israel. Rabbi \n Zera said in the name of rabbi Abbahu, who quoted rabbi Johanan: 'These are the eighty thousand battle trumpets which assembled in the city of Betar \n when it was taken and men, women and children were slain until their blood\n run into the great sea.' It has been taught that rabbi Eleazar the Great\n said: 'There are two streams in the valley of Yadaim, one running in one\n direction and one in another, and the Sages estimated that at that time \n they ran with two parts of water to one of blood.' In a Baraitha it has been taught: 'For seven years the gentiles fertilized their vineyards with the blood of Israel without using manure.'")
        print("[3]'The voice of Jacob': this is the cry caused by the emperor Hadrian\n who killed in the city of Betar four hundred thousand myriads, or as some\n say, four thousand myriads")
        print("[4]Rabban Bar Hanah said in the name of rabbi Johanan: 'Forty times\ntwenty-four phylactery boxes were found on the heads of the victims of Betar.'\nRabbi Jannai son of rabbi Ishmael said there were three chests each containing\n 284 liters.")
        print("[5]Rab Judah reported Samuel as saying in the name of rabban Simeon\n ben Gamaliel: 'What is signified by the verse, Mine eye affecteth my soul,\n because of all the daughters of my city?' There were four hundred synagogues\n in the city of Betar, and in every one were four hundred teachers of children,\n and each one had under him four hundred pupils, and when the enemy entered there,\n they pierced them with their staves, and when the enemy prevailed and captured them,\n they wrapped them in their scrolls and burnt them with fire.")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==3:
        print("[69.12.1] At Jerusalem, Hadrian founded a city in place of the one\n which had been razed to the ground, naming it Aelia Capitolina, and on the\nsite of the temple of the [Jewish] god, he raised a new temple to Jupiter.\n         This brought on a war of no slight importance nor of brief duration,\n [69.12.2] for the Jews deemed it intolerable that foreign races should be settled\nin their city and foreign religious rites planted there. So long, indeed, as Hadrian\nwas close by in Egypt and again in Syria, they remained quiet, save in so far as\nthey purposedly made of poor quality such weapons as they were called upon to furnish,\nin order that the Romans might reject them and they themselves might thus have the\nuse of them. But when Hadrian went farther away, they openly revolted.\n[69.12.3] To be sure, they did not dare try conclusions with the Romans in the open\nfield, but they occupied the advantageous positions in the country and strengthened\nthem with mines and walls, in order that they might have places of refuge whenever\nthey should be hard pressed, and might meet together unobserved under ground; and\nthey pierced these subterranean passages from above at intervals to let in air and light.\n[69.13.1] At first, the Romans took no account of them. Soon, however, all Judaea had\nbeen stirred up, and the Jews everywhere were showing signs of disturbance, were \ngathering toghether, and giving evidence of great hostility to the Romans, partly \nby secret and partly by overt acts. \n[69.13.2] Many outside nations, too, were joining them through eagerness for gain,\nand the whole earth, one might almost say, was being stirred up over the matter.\n Then, indeed, Hadrian sent against them his best generals. First of these was Julius\nSeverus, who was dispatched from Britain, where he was governor, against the Jews.\n[69.13.3] Severus did not venture to attack his opponents in the open at any one\npoint, in view of their numbers and their desperation, but by intercepting small \ngroups, thanks to the number of his soldiers and his under-officers. By depriving\nthem of food and shutting them up, he was able - rather slowly, to be sure, but \nwith comparatively little danger - to crush, exhaust and exterminate them. Very \nfew of them in fact survived.\n[69.14.1] Fifty of their most important outposts and nine hundred and eighty-five\nof their most famous villages were razed to the ground. Five hundred and eighty \nthousand men were slain in the various raids and battles, and the number of those \nthat perished by famine, disease and fire was past finding out.\n[69.14.2] Thus nearly the whole of Judaea was made desolate, a result of which the\npeople had had forewarning before the war. For the tomb of Solomon, which the Jews\nregard as an object of veneration, fell to pieces of itself and collapsed, and many\nwolves and hyenas rushed howling into their cities.\n[69.14.3] Many Romans, moreover, perished in this war. Therefore Hadrian, in writing\nto the Senate, did not employ the opening phrase commonly affected by the emperors,\n'If you and your children are in health, it is well; I and the legions are in health.'")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==4:
        print("They are also in the possession of all Jews throughout the world; \n but they, though they read, do not understand what is said, but count us \n foes and enemies; and, like yourselves, they kill and punish us whenever \n they have the power, as you can well believe. For in the Jewish war which\n lately raged, Barchochebas, the leader of the revolt of the Jews, gave orders \n that Christians alone should be led to cruel punishments, unless they would\n deny Jesus Christ and utter blasphemy. ")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==5:
        print(" [4.6.1] The rebellion of the Jews once more progressed in character\nand extent, and Rufus, the governor of Judaea, when military aid had been\n sent him by the emperor, moved out against them, treating their madness \n without mercy. He destroyed in heaps thousands of men, women and children,\nand, under the law of war, enslaved their land.[4.6.2] The Jews were at that\n time led by a certain Barchochebas, which means 'star', a man who was \nmurderous and a bandit, but relied on his name, as if dealing with slaves,\nand claimed to be a luminary come from heaven and was magically enlightening\n those who were in misery.\n[4.6.3] The war reached its height in the eighteenth year of Hadrian in Betar, \nwhich was a strong citadel not very far from Jerusalem. The siege lasted a long time\nbefore the rebels were driven to final destruction by famine and thirst and the \ninstigator of their madness paid the penalty he deserved. Hadrian then commanded \nthat by a legal decree and ordinances the whole nation should be absolutely prevented \nfrom entering from thenceforth even the district round Jerusalem, so that it could \nnot even see from a distance its ancestral home.\n[4.6.4] Ariston of Pella tells the following story: 'Thus when the city came to \nbe bereft of the nation of the Jews, and its ancient inhabitants had completely perished\n, it was colonized by foreigners, and the Roman city which afterwards arose changed\nits name, and in honor of the reigning emperor Aelius Hadrian was called Aelia.\nThe Church, too, it was composed of gentiles, and after the Jewish bishops the first\nwho appointed to minister to those was Marcus.'")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==6:
        print("Hadrian's year 16(AD 132) The Jews,w ho took up arms,devastated Palestine\n during the period in which the Governor of the province was Tineus Rufus\n to whom Hadrian sent an army in order to crush the rebels.\n Hadrian's Year 17(AD 133) Cochebas,duke of the Jewish sect, killed the Christians\n with all kinds of persecutions when they refused to help him aginst the Roman troops.\n Hadrian's year 18 [alternatively:19 in the Armenian](AD 134 [or 135])\n The Jewish war that was conducted in Palestine reached its conclusion\n all Jewish problems having been completely supressed. From that time,\n the permission was denied them even to enter Jerusalem; first and foremost\n because of the commandment of God, as the prophets had prophesied and secondly\n by the authority of the interdictions of the Romans.\n In Jerusalem the first bishop was appointed from the Gentiles, since bishops\n ceased to be appointed from among the Jews.\n Hadrian's year 20(AD 136) Aelia was founded by Aelius Hadrianus and before its gate\n that of the road by which we go to Bethlehem, he set up an idol of a pig\n in marble, signifying the subjugation of the Jews to Roman authority\n")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==7:
        print("[3.31] ...just as that famed Barchochebas, the instigator of the Jewish uprising,\n kept fanning a lighted blade of straw in his mouth with puffs of breath so \n as to give the impression that he was spewing out flames\n [Is.2.12-17] The Lord has a day in store for all the proud and lofty, for\n all that is exalted. They will be humbled. [...] For every lofty tower and \n every fortified wall, for every trading ship [...] will be be brought low:\ and those who ascribe this to the time of Vespasian and Hadrian say that \n the writing here was completely fulfilled, for no high tower, no most fortified\n wall, no mightiest navy and not the most diligent commerce, could overcome\n the might of the Roman army; and the citizens of Judaea came to such distress\n that they, together with their wives, their children, their gold and their\n silver, in which they trusted, remained in underground tunnels and deepest caves.\n[Dan.9.24-27] He shall establish a covenant with many for one week: The division \nis between the reigns of Vespasian and Hadrian. According to the History of Josephus,\nVespasian and Titus concluded peace with the Jews for three years and six month. And \nthe [other] three years and six months are accounted for in Hadrian's reign, when \nJerusalem was completely destroyed and the Jewish nation was massacred in large groups \nat a time, with the result that they were even expelled from the borders of Judaea.\nThis is what the Hebrews have to say on the subject, paying little attention to the\nfact that from the first year of Darius, King of the Persians, until the final overthrow\nof Jerusalem, which befell them under Hadrian, the period involved is a hundred and\nseventy-four Olympiads or six hundred ninety-six years, which total up to ninety-nine\nHebrew weeks plus three years - that being the time when Barcochebas, the leader of \nthe Jews, was crushed and Jerusalem was demolished to the very ground.\n[Mt.24.15] So when you see the standing in the holy place the abomination that causes\ndesolation: or to the statue of the mounted Hadrian, which stands to this very day\non the site of the Holy of Holies.\n")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice==8:
        print("[14] And Hadrian went up to Jerusalem, the famous and illustrious city which\n Titus, son of Vespasian, had overthrown in the second year of his father's \n reign. And Hadrian found the temple of God throdden down and the whole city \n devastated, save for a few houses and the very small church of God, where\n the disciples, when they had returned after the Savior had ascended from \n the Mount of Olives, went to the upper room. For there it had been built, \n        that is, in that portion of Zion that escaped destruction, together with \n blocks of houses in the neighborhood of Zion and the seven synagogues that\n        alone remained standing in Zion, like solitary huts, one of which remained\nuntil the time of Maximinus, the bishop and the emperor Constantine, like a\n        booth in a vineyard, as it is written.Therefore, Hadrian made up his mind \nto rebuild the city, but not the temple. And he took the Aquila mentioned \n        above, who was a Greek interpreter. Now Aquila was related to the emperor \nby marriage and was from Sinope in Pontus. Hadrian established him there \n        in Jerusalem as overseer if the work of building the city. And he gave to\nthe city that was being built his own name and the appellation of the royal\n        title. For as he was named Aelius Hadrian, so he also called the city Aelia.\n[15] So Aquila, while he was in Jerusalem, also saw the disciples of the disciples\nof the apostles flourishing in the faith and working great signs, healings and other\nmiracles. For they were such as had come back from the city of Pella to Jerusalem[...]\nSo Aquila, after he had been strongly stirred in mind, believed in Christianity,\nand after a while, when he asked, he received the seal in Christ. But according \nto his former habit, still thinking the things of the heathen, he had been thoroughly\ntrained in vain astrology, so that also after he had become a Christian he never departed\nfrom this fault of his, but every day he made calculations on the horoscope of his\nbirth. He was reproved by the teachers, and they rebuked him for this every day,\nbut did not accomplish anything. But instead of standing rebuked, he became bold \nin disputation and tried to establish things that have no existence, tales about fate.\nHence, as one who proved useless and could not be saved, he was expelled from the Church.\nBut as one who had become embittered in mind over how he had suffered dishonor, \nhe was puffed up with vain jealousy, and having cursed Christianity and renounced \nhis life [after death in Heaven], he became a proselyte and was circumcised as a Jew.\nAnd, being painfully ambitious, he dedicated himself to learning the language of \nthe Hebrews and their writings. After he had first been thoroughly trained for it,\nhe made his translation. He was moved not by the right motive, but by the desire \nto distort certain of the words occurring in the translation of the seventy-two.\n")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice == 9:
        print("There was a man in Israel,\n Bar Kochba of name,\n A young and tall man,\n eyes glowing upon seeing him.\n He was a hero,\n He called to freedom.\n The entire nation loved him,\n He was a hero.\n One day an incident happened\n A sad incident,\n Bar Kochba fell into captivity\n and he was placed in a cage\n What a wonderous cage was this\n Therein was a roaring lion\n There we saw Bar Kochba\n A fallen lion\n Now know please,\n Bar Kochba, strong and hero\n He jumped on a lion,\n and rode it easily like an eagle\n On a mountain and ravine did he rebel\n And the flag of freedom in hand,\n All the people clapped and shouted 'Great'\n Bar Kochba, cheers,\n Cheers\n")
        input("Press any key to go back to selection screen")
        print_sources()
    if choice == 10:
        game()

def start():
    print("Welcome to Bar Kochba revolt. If you press 1 you will be able to view\n all sources relating to Bar Kochba as well as an English translation of the\n Hebrew song used for this game. If you press 2 you will play the main game.If you press 3 you will make the music the opposite of what it is now")
    choice = int(input("1,2 or 3:" ))
    if (choice == 1):
        print_sources()
    elif (choice == 2):
        game()
    elif (choice == 3):
        #check if music is playing if playing stop it and if stopped play it
        if (pygame.mixer.music.get_busy() == True):
            pygame.mixer.music.pause()
            game()
        elif (pygame.mixer.music.get_busy() == False):

            pygame.mixer.music.unpause()
            game()
    else:
        start()



'''print_slow("This is a revival of the genre of text-based games.\n")
time.sleep(0)
print ("\n" * 50)
print_slow ("Welcome to Bar Kochba revolt\n")
print_slow ("Your objective is to defeat the Romans")
print ("\n" * 22)
time.sleep(0)
print_slow ("Historical resource for mission: Cassius Dio Book 69")
print_slow ("""
[69.12.1] At Jerusalem, Hadrian founded a city in place of the\n one which had been razed to the ground,\n naming it Aelia Capitolina, and on the site of \nthe temple of the [Jewish] god, he\n raised a new temple to Jupiter. \nThis brought on a war of no slight\n importance nor of brief duration,

\n[69.12.2] for the Jews deemed it intolerable that foreign races \nshould be settled in their city and foreign religious \nrites planted there. So long, indeed, as Hadrian was close \n by in Egypt and again in Syria, they remained quiet,\n save in so far as they purposedly made of \npoor quality such weapons as they were called upon \nto furnish, in order that the Romans \nmight reject them and they themselves might thus have\n the use of them. But when Hadrian went farther away,\n they openly revolted.""")
print("\n" * 22)
revoltsuccess = 100
'''
#call start function before playing





start()

#game()
