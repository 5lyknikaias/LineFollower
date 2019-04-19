# Ακόλουθος γραμμής (Line Follower) με χαμηλό κόστος κατασκευής
Xρησιμοποιείται για σασί του οχήματος μια διάτρητη πλακέτα, η οποία φιλοξενεί ταυτόχρονα και την καλωδίωση των υπολοίπων υλικών. Η κατασκευή έχει γίνει με το raspberry pi zero w, έναν οδηγό κινητήρων (H bridge) (L293D), 3 υπέρυθρους αισθητήρες ανάκλασης (CNY70), ένα κυλινδρικό Power Bank καθώς και δύο κινητήρες συνεχούς ρεύματος. Η επιλογή του  raspberry pi zero w γίνεται έτσι ώστε να μπορεί να χρησιμοποιηθεί η γλώσσα προγραμματισμού Python και για λόγους μελλοντικής επέκτασης του έργου, όπως: 
-Την υλοποίηση της ανίχνυεσης της γραμμής μέσω κάμερας.
-Ακόμη, η συγκεκριμένη πλατφόρμα διαθέτει συσκευή Bluetooth για την επικοινωνία με κινητό τηλέφωνο γράφοντας εφαρμογές σε περιβάλλον appinventor.

# Πως λειτουργεί
Χρησιμοποιούμε έναν υπολογιστή pi zero w τον οποίο τοποθετούμε σε μία διάτρητη πλακέτα. Αυτός, λαμβάνει δεδομένα άπο τους τρεις αισθητήρες, προκειμένου να καθορίσει πού βρίσκεται η γραμμή που πρέπει να ακολουθήσει, σε σχέση με αυτούς. Έτσι, αναλόγως με τα δεδομένα που δέχεται, δίνει τις κατάλληλες πληροφορίες στους κινητήρες ώστε να ακολουθεί τη γραμμή. Επιπλέον, για τη τροφοδοσία της κατασκευής, χρησιμοποιείται ένα powerbank, για λόγους οικονομίας, αφού είναι εύκολα επαναφορτιζόμενο. 



