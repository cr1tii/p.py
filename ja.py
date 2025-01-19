from rich.console import Console
import ara

class cars:
    def __init__(self, mercedes , bmw ,lexus):
        self.mercedes = mercedes
        self.bmw = bmw
        self.lexus = lexus 
    def runcars(self):
        while True:
            print("—"*12)
            c = Console()
            c.print("type:",style="underline")
            c.print("   1. to see mercedes collection",style="bold")
            c.print("   2. to see bmw collection",style="blue")
            c.print("   3. to see lexus collection",style="color(8)")
            print("or type 4 to exit")
            se = input("\n   :")
            print("—"*12)
            if se == str(1):
                self.mercedes()
            elif se == str(2):
                self.bmw()
            elif se == str(3): 
                self.lexus() 
            elif se == str(4):
                break 
            else:
                c1= Console()
                c1.print(ara.ar("\n خطأ ، ارجوك اكتب قيمة مقبولة."),style="underline red")
                c1.print("error, please type a known value.",style="red")
    def runmer():
        while True:
            print("—"*12)
            print("\n")
            se1 = print("1. about mercedes")
            se2 = print("2. amg")
            se3 = print("3. s class")
            se4 = print("4. brabus")
            se4 = print("5. to exit")
            slava = input("\n      :")
            if slava == str(4):
                while True:
                    print("\n")
                    print("—"*12)
                    print("1. about brabus")
                    print("2. brabus cars")
                    print("3. brabus last works ")
                    print("4. to break")
                    slava2 = input("     :")
                    if slava2 == str(1):
                        cons = Console()
                        cons.print(ara.ar("ماهي برابوس؟"),style="bold ")
                        print(ara.ar("\n برابوس هي شركة تعديل سيارات ألمانية متخصصة في"))
                        print(ara.ar("\nتحسين سيارات مرسيدس-بنز، مايباخ، وسمارت."))
                        print(ara.ar("\n تأسست في عام 1977 من قبل بودو بوشمان وكلاوس براكمان"))
                        cons.print(ara.ar("\n\n ماذا تفعل؟"),style="bold")
                        print(ara.ar("\n تقوم الشركة بتعديل الأداء، التصميم الداخلي والخارجي، والإضافات الفاخرة"))
                    elif slava2 == str(2):
                        print("\n")
                        print("—"*24)
                        print('1. Rocket 900')
                        print('2. G900')
                        print('3. GT 800')
                        print('4. Maybach S-Class 900')
                        print('5. X-Class')
                        print('6. Ultimate E-Class')
                        print('7. Smart Fortwo Cityflame')
                        print('8. CLS K8')
                        print('9. G63 AMG 6x6 B63-900') 
                        print("\n")
                        print("—"*24)
                    elif slava2 == str(3):
                        print('you can visit their web:')
                        print('brabus.com')
                                       
                    elif slava2 == str(4): 
                        print("wait...")
                        break
            elif slava == str(2):
                while True:
                    print("—"*12)
                    print("1. about amg.")
                    print("2. amg cars")
                    print("3. amg last works. ")
                    print("4. to exit")
                    slava3 = input("   : ")
                    if slava3 == str(1):
                        print("type 1 for arabic/2 for english")
                        input1 = input("1/2: ")
                        if input1 == str(1):
                            print(ara.ar("AMG هو قسم الأداء العالي التابع لشركة مرسيدس-بنز، المعروف بتطوير السيارات ذات الأداء الرياضي الفائق. تأسست "))
                            print(ara.ar("AMG عام 1967 على يد اثنين من المهندسين السابقين في مرسيدس، وهما هانز ويرنر أوفريخت وإيرهارد ميلشر. لاحقًا أصبحت الشركة جزءًا من مرسيدس-بنز، وتُعرف الآن باسم مرسيدس-AMG"))
                            cona = Console()
                            cona.print(ara.ar("\n \nولو تسألني عن سيارتي المفضله صراحه كنت بقول amg 53s 4doors بحق"),style="bold yellow underline")
                        elif input1 == str(2):
                            print("AMG is the high-performance division of Mercedes-Benz, known for developing cars")
                            print("with exceptional sporting capabilities. AMG was founded in 1967 by two former")
                            print("Mercedes engineers, Hans Werner Aufrecht and Erhard Melcher. It later became part of")
                            print("Mercedes-Benz and is now known as Mercedes-AMG.")
                            conse = Console() 
                            conse.print("\n \n btw if you asked me id say my fav car is amg 53s 4doors fr fr ",style="bold yellow underline")
                    elif slava3 == str(2):
                        list12 = [
                            "AMG A45 S - 421 HP",
                            "AMG C63 S - 503 HP",
                            "AMG E63 S - 603 HP",
                            "AMG G63 - 577 HP",
                            "AMG S63 - 603 HP",
                            "AMG GT R - 577 HP",
                            "AMG GT Black Series - 720 H",
                            "AMG GLE 63 S - 603 HP",
                            "AMG CLS 53 - 429 HP",
                            "AMG EQS 53 (Electric) - 649 HP",
                            ]
                        for list1 in list12:
                            print("\n")
                            print("—"*12,list1,"—"*12)
                            print("\n")
                    elif slava3 == str(4):
                        print("wait...")
                        break
                    elif slava3 == str(3):
                        print("they dropped a collection of a lot of cars you can see them in their web in here:")
                        print("\nhttps://www.mercedes-amg.com\n")
            elif slava == str(1):
                print("you can visit their website to know more about mercedes:")
                print("https://www.mercedes-benz.com")
            elif slava == str(3):
                while True:
                    print("1. about s class")
                    print("2. s class cars")
                    print("3. s class last works")
                    print("4. to exit")
                    in2 = input("  : ")
                    if in2 == str(1):
                        lines = [
                                "The Mercedes-Benz S-Class is a flagship",
                                "luxury sedan renowned for its advanced",
                                "technology, exceptional comfort, and",
                                "superior performance. It has long been",
                                "considered a benchmark in the luxury car",
                                "segment, combining innovative features with",
                                ]
                        for line in lines:
                            print("\n")
                            print("—"*24)
                            print(line)
                            print("—"*24)
                            print("\n")
                    elif in2 == str(2):
                        lines2 = [
                                "Mercedes-Benz S 350",
                                "Mercedes-Benz S 450",
                                "Mercedes-Benz S 500",
                                "Mercedes-Benz S 580",
                                "Mercedes-Maybach S 580",
                                "Mercedes-Maybach S 680",
                                "Mercedes-AMG S 63 E",
                                ]
                        for line2 in lines2:
                            console = Console()
                            console.print(f"\n","—"*12,line2,"—"*12,"\n",style="bold")
                    elif in2 == str(3):
                        print("visit their web to see more:")
                        print("sclass.com")
                    elif in2 == str(4):
                        print("     wait...")
                        break
            elif slava == str(5):
                print("exit...")
                break
    def runbmw():
        while True:
            ca = Console()
            ca.print("1. about bmw.",style="blue")
            ca.print("2. m power team",style="blue")
            ca.print("3. to exit",style="blue")
            ca2 = input("\n :  ")
            if ca2 == str(1):
                print("type 1 to english/2 to arabic")
                ara1 = input("1/2 :   ")
                if ara1 == str(1):
                    lists = [
                            "BMW, founded in 1916, is a German brand",
                            "known for luxury cars, sporty performance",
                            "and advanced technology. It focuses on",
                            "innovation, sustainability, and a premium driving experience.",
                            ]
                    for line in lists:
                        print("\n")
                        print(line)
                        print("\n")
                elif ara1 == str(1):
                    listss = [
                            "بي إم دبليو شركة ألمانية تأسست عام ١٩١٦، متخصصة في",
                            "صناعة السيارات الفاخرة والأداء الرياضي والتقنيات المتقدمة",
                            "وتركز على الابتكار والاستدامة وتجربة القيادة المميزة."
                            ]
                    for line2 in listss:
                        print("\n")
                        print(ara.ar(line2))
                        print("\n")
        print("this place is empty")
    def runlexus():
        caa = Console()
        caa.print(ara.ar("هذا مكان فارغ ايضاً"),style="underline")
        print("this place is empty too")

def mercedes():
    cars.runmer()
def bmw():
    cars.runbmw() 
def lexus(): 
    cars.runlexus()

aw1 = cars(mercedes , bmw ,lexus)
aw1.runcars()
