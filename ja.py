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
            elif slava == str(5):
                print("exit...")
                break
    def runbmw():
        ca = Console()
        ca.print(ara.ar("هذا مكان فارغ."),style="underline")
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
