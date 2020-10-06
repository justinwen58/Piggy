#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 83
        self.SAFEDISTANCE = 300
        self.CLOSEDISTANCE = 30
        self.MIDPOINT = 1475 #robot17 # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing

        if not self.safe_to_dance():
            return False
        
        for x in range(1):
            self.gangnamstyle()
            self.mikesdancefor()
            self.turn_by_deg(-180)
            self.mikesdanceback()
            self.stylemove()
            for x in range(2):
                self.circledance()
                self.sliding()


    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        #check for all fail condition
        for _ in range(4):
            if self.read_distance() < 300:
                return False
            else:
                self.turn_by_deg(90)
        #after all check have been done, deduce it is safe
        print ("safe to dance, Mike Wazowski!")
        return True

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

   
    def gangnamstyle(self):
        """forward and turning 180 and back up"""
        for x in range(6):
            self.fwd()
            time.sleep(0.3)
            self.stop()
            
            #Glancing for audience before ready to turn
            self.servo(1000)
            time.sleep(.1) 
            self.servo(2000)
            time.sleep(.1) 
            
            #An 180 turning and backward
            self.right(primary=340, counter =-340)
            time.sleep (.5)
            self.stop()
            self.back()
            time.sleep(0.3)
            self.stop()
            

    def stylemove(self):
        """swiftly run forward and backward by increasing distance for each time"""
        for x in range(3):
            #int created
            a = 0
            b = 0
            #forward
            self.fwd()
            time.sleep(.25+a)
            self.stop()
            self.servo(1000)
            time.sleep(.5)
            #backward
            self.back()
            time.sleep(0.25+b)
            self.stop()
            self.servo(2000)
            time.sleep(.5)
            #amount of time adding while running forward and back
            a += .5
            b += .5

    def sliding(self):
        """turning about 45 two times with head shaking"""
        for x in range(2):
            #turns
            self.turn_by_deg(-350)
            time.sleep (2)  

            self.servo(1000) 
            time.sleep(.5)
            self.servo(2000)
            time.sleep(.5)

    def circledance(self):
        """make 90 angle turn four times"""
        for x in range(4):
             self.servo(2000) 
             time.sleep(.125)
             self.servo(1000)
             #angles adjust for 90 or less
             self.turn_by_deg(90)
             time.sleep(.5)       
        self.servo(2000) 
        time.sleep(.5)
        self.servo(1000)
        time.sleep(.5)

    def mikesdancefor(self):
        """Shimmy forward and make a 180 turn and shimmy back with the head shaking"""
        for x in range(2):
            for x in range(5):
                #right turn
                self.right(primary=80, counter=30)
                time.sleep(.5)
                self.servo(1000)
                time.sleep(.125)
                #left turn
                self.left(primary=80, counter=30)
                time.sleep(.5)
                self.servo(2000)
                time.sleep(.125)
            #180 turn
            self.turn_by_deg(-180)
            time.sleep(.75)
                
    def mikesdanceback(self):
        """Shimmy backward and make a 180 turn and shimmy back with the head shaking"""
        for x in range(2):
            for x in range(5):
                #back right
                self.right(primary=-80, counter=-30)
                time.sleep(.5)
                self.servo(1000)
                time.sleep(.125)
                #back left
                self.left(primary=-80, counter=-30)
                time.sleep(.5)
                self.servo(2000)
                time.sleep(.125)
            #180 turn
            self.turn_by_deg(-180)
            time.sleep(.75)

           

    def run(self):
        self.fwd()

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        self.fwd()
        while True:
            if self.read_distance() < self.CLOSEDISTANCE:  
                self.stop()
                print("no stop it!")
                self.back()
                time.sleep(.1)
                self.turn_by_deg(90)
                time.sleep(.1)
            else:
                self.fwd()
        
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
