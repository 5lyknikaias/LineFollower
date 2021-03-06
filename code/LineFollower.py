#Εισαγωγή συναρτήσεων που θα χρησιμοποιηθούν για τον έλεγχο του Raspberry Pi
from gpiozero import PWMOutputDevice,InputDevice
#Σύνδεση κινητήρων με τα αντίστοιχα GPIO, με ενεργοποιημένες τις pull-up
leftforward=PWMOutputDevice(26,True,0,1000)
leftreverse=PWMOutputDevice(19,True,0,1000)
rightforward=PWMOutputDevice(13,True,0,1000)
rightreverse=PWMOutputDevice(12,True,0,1000)
#Σύνδεση αισθητήρων με τα αντίστοιχα GPIO
left_sensor=InputDevice(6,True)
centre_sensor=InputDevice(5,True)
right_sensor=InputDevice(4,True)
#Ορισμός συνάρτησης που κινεί τους κινητήρες με τη δεδομένη ταχύτητα μπροστά (αν η ταχύτητα είναι θετική) ή πίσω (αν η ταχύτητα είναι αρνητική)
def MotorsSpeed(LSpeed,RSpeed):
    if LSpeed>=0:
        leftforward.value=LSpeed
        leftreverse.value=0
    else:
        leftforward.value=0
        leftreverse.value=-LSpeed
    if RSpeed>=0:
        rightforward.value=RSpeed
        rightreverse.value=0
    else:
        rightforward.value=0
        rightreverse.value=-RSpeed
#Ορισμός συνάρτησης που διαβάζει τις εισόδους των αισθητήρων και τις επιστρέφει σαν string
#Η πρώτη τιμή είναι του αριστερού, μετά του μεσαίου και μετά του δεξιού και είναι 1 αν βλέπει γραμμή, αλλιώς 0
def SensorRead():
    return str(1-left_sensor.value)+str(1-centre_sensor.value)+str(1-right_sensor.value)
#Διαβάζουμε την πρώτη τιμή των αισθητήρων
sensorvalue=SensorRead()
#Περνάμε την τιμή αυτή σε μία μεταβλητή, ώστε, αν χάσει τη γραμμή, να "θυμάται" πού ήταν την τελευταία φορά
lastvalue=sensorvalue
#Αν δει γραμμή μόνο ο αριστερός ή μόνο ο δεξιός αισθητήρας 10 ή περισσότερες φορές, τότε είναι πιθανό να υπάρχει στροφή, οπότε ο ένας κινητήρας σταματά
#και ο άλλος πηγαίνει πιο αργά, άρα οι ταχύτητες είναι μεταβλητές
s1=0.7#Αυτή είναι η ταχύτητα των κινητήρων στην ευθεία και του κινητήρα που δεν είναι σταματημένος σε μία στροφή
s2=0.3#Αυτή είναι η ταχύτητα του κινητήρα που στρίβει, όταν δεν έχει αναγνωριστεί στροφή, αλλά απαιτείται διόρθωση στην πορεία
counter=0#Αυτή η μεταβλητή μετράει πόσες φορές έχει δει μόνο ο αριστερός ή μόνο ο δεξιός αισθητήρας γραμμή
#Συνεχώς διαβάζονται οι είσοδοι των αισθητήρων και μεταβάλεται, αν χρειάζεται, η ταχύτητα του κάθε κινητήρα
while True:
    #Αν υπάρχει στροφή, ο ένας κινητήρας πρέπει να πάει πιο αργά, ενώ ο άλλος να σταματήσει
    if counter>=10:
        s1=0.3
        s2=0
    #Αλλιώς, οι ταχύτητες πρέπει να είναι κανονικές
    else:
        s1=0.7
        s2=0.3
    #Αν δει γραμμή μόνο ο μεσαίος αισθητήρας, τότε πάει ευθεία
    if sensorvalue=="010":
        MotorsSpeed(s1,s1)
        counter=0
    #Αν δει γραμμή μόνο ο αριστερός αισθητήρας, τότε πάει αριστερά (αν δεν υπάρχει στροφή, κινείται ο αριστερός κινητήρας πιο αργά, αλλιώς σταματά και κινείται ο δεξιός πιο αργά)
    elif sensorvalue=="100":
        MotorsSpeed(s2,s1)
        counter+=1
    #Αν δουν γραμμή ο αριστερός και ο μεσαίος αισθητήρας, τότε πάει αριστερά (κινείται ο αριστερός κινητήρας πιο αργά)
    elif sensorvalue=="110":
        MotorsSpeed(0.3,s1)
        counter=0
    #Αν δει γραμμή μόνο ο δεξιός αισθητήρας, τότε πάει δεξιά (αν δεν υπάρχει στροφή, κινείται ο δεξιός κινητήρας πιο αργά, αλλιώς σταματά και κινείται ο αριστερός πιο αργά)
    elif sensorvalue=="001":
        MotorsSpeed(s1,s2)
        counter+=1
    #Αν δουν γραμμή ο δεξιός και ο μεσαίος αισθητήρας, τότε πάει δεξιά (κινείται ο δεξιός κινητήρας πιο αργά)
    elif sensorvalue=="011":
        MotorsSpeed(s1,0.3)
        counter=0
    #Αν δεν ισχύει τίποτα από αυτά και την τελευταία φορά είδε γραμμή μόνο ο αριστερός αισθητήρας ή είδαν ο αριστερός και ο μεσαίος αισθητήρας, τότε, αν δε βλέπει γραμμή κανένας αισθητήρας ή βλέπουν όλοι, ξεκινά να στρίβει αριστερά και περιμένει μέχρι να μην ισχύει αυτό (επίσης, στο τέλος μηδενίζεται η μεταβλητή counter)
    elif lastvalue=="100" or lastvalue=="110":
        if sensorvalue=="000" or sensorvalue=="111":
            MotorsSpeed(0,1)
        while sensorvalue=="000" or sensorvalue=="111":
            sensorvalue=SensorRead()
        counter=0
    #Αν δεν ισχύει τίποτα από αυτά, τότε, αν δε βλέπει γραμμή κανένας αισθητήρας ή βλέπουν όλοι, ξεκινά να στρίβει δεξιά και περιμένει μέχρι να μην ισχύει αυτό (επίσης, στο τέλος μηδενίζεται η μεταβλητή counter)
    else:
        if sensorvalue=="000" or sensorvalue=="111":
            MotorsSpeed(1,0)
        while sensorvalue=="000" or sensorvalue=="111":
            sensorvalue=SensorRead()
        counter=0
    #Επίσης, αν δει γραμμή μόνο ο αριστερός ή μόνο ο δεξιός αισθητήρας, τότε η μεταβλητή counter αυξάνεται, αλλιώς μηδενίζεται
    #Τέλος, οι μεταβλητές lastvalue και sensorvalue ανανεώνονται
    lastvalue=sensorvalue
    sensorvalue=SensorRead()
