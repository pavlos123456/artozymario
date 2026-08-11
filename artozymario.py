# artozymario.py - Το τετράδιο αρτοποιίας σου με διαγραφή

class Syntagi:
    """Κλάση που αντιπροσωπεύει μια συνταγή αρτοποιίας"""
    
    def __init__(self, onoma, aleuri_grammaria=1000):
        self.onoma = onoma
        self.aleuri_grammaria = aleuri_grammaria
        self.ylika = {}  # dict: {yliko: pososto}
        self.odigies = ""
    
    def prosthese_yliko(self, yliko, pososto):
        """Προσθέτει ένα υλικό με το ποσοστό του"""
        self.ylika[yliko] = pososto
    
    def prosthese_odigies(self, odigies):
        """Προσθέτει οδηγίες εκτέλεσης"""
        self.odigies = odigies
    
    def ypologise_varh(self, neo_aleuri=None):
        """Υπολογίζει τα βάρη για κάθε υλικό"""
        if neo_aleuri:
            aleuri = neo_aleuri
        else:
            aleuri = self.aleuri_grammaria
        
        apotelesma = {}
        for yliko, pososto in self.ylika.items():
            varos = (pososto / 100) * aleuri
            apotelesma[yliko] = round(varos, 1)
        
        return apotelesma, aleuri
    
    def emfanise(self, neo_aleuri=None):
        """Εμφανίζει τη συνταγή σε όμορφη μορφή"""
        varh, aleuri = self.ypologise_varh(neo_aleuri)
        
        print("\n" + "="*50)
        print(f"🍞 {self.onoma.upper()}")
        print("="*50)
        print(f"Βάση: {aleuri} γρ. αλεύρι (100%)\n")
        
        print("📋 ΥΛΙΚΑ:")
        print("-"*50)
        print(f"{'Υλικό':<25} {'Ποσοστό':<12} {'Βάρος (γρ)':<12}")
        print("-"*50)
        
        for yliko in self.ylika:
            pososto = self.ylika[yliko]
            varos = varh[yliko]
            print(f"{yliko:<25} {pososto:>6}%     {varos:>10.1f}")
        
        print("-"*50)
        synolo = sum(varh.values())
        print(f"{'ΣΥΝΟΛΟ ΖΥΜΗΣ':<25} {'':<12} {synolo:>10.1f} γρ.")
        
        if self.odigies:
            print("\n📖 ΟΔΗΓΙΕΣ:")
            print("-"*50)
            print(self.odigies)
        
        print("="*50 + "\n")


def dimiourgise_syntages():
    """Δημιουργεί τις βασικές συνταγές"""
    
    # --- 1. ΛΕΥΚΟ ΨΩΜΙ ---
    psomi = Syntagi("Λευκό Ψωμί", 1000)
    psomi.prosthese_yliko("Αλεύρι για ψωμί", 100)
    psomi.prosthese_yliko("Νερό χλιαρό", 62)
    psomi.prosthese_yliko("Αλάτι", 2)
    psomi.prosthese_yliko("Ζάχαρη", 4)
    psomi.prosthese_yliko("Ξηρή μαγιά", 2)
    psomi.prosthese_yliko("Βούτυρο", 4)
    psomi.prosthese_odigies(
        "1. Ανακατέψτε όλα τα υλικά εκτός από το βούτυρο.\n"
        "2. Ζυμώστε μέχρι να γίνει ελαστική η ζύμη.\n"
        "3. Προσθέστε το βούτυρο και συνεχίστε το ζύμωμα.\n"
        "4. Αφήστε να φουσκώσει για 1 ώρα.\n"
        "5. Πλάστε και αφήστε να φουσκώσει ξανά για 30-45 λεπτά.\n"
        "6. Ψήστε στους 200°C για 30 λεπτά."
    )
    
    # --- 2. ΣΤΑΡΕΝΙΟ ΨΩΜΙ ---
    stareno = Syntagi("Σταρένιο Ψωμί (Ολικής)", 1000)
    stareno.prosthese_yliko("Αλεύρι σίτου ολικής", 100)
    stareno.prosthese_yliko("Νερό", 72)
    stareno.prosthese_yliko("Αλάτι", 2)
    stareno.prosthese_yliko("Ξηρή μαγιά", 1)
    stareno.prosthese_odigies(
        "1. Αναμείξτε όλα τα υλικά.\n"
        "2. Ζυμώστε καλά (η ζύμη θα είναι πιο υγρή).\n"
        "3. Αφήστε να φουσκώσει για 1.5 ώρα.\n"
        "4. Πλάστε και ψήστε στους 200°C για 35-40 λεπτά."
    )
    
    # --- 3. ΣΟΚΟΠΑΝ (Shokupan) ---
    shokupan = Syntagi("Σοκοπάν (Ιαπωνικό)", 1000)
    shokupan.prosthese_yliko("Αλεύρι για ψωμί", 100)
    shokupan.prosthese_yliko("Νερό", 34)
    shokupan.prosthese_yliko("Γάλα", 32)
    shokupan.prosthese_yliko("Ζάχαρη", 8)
    shokupan.prosthese_yliko("Αλάτι", 2)
    shokupan.prosthese_yliko("Ξηρή μαγιά", 1.2)
    shokupan.prosthese_yliko("Κρέμα γάλακτος", 8)
    shokupan.prosthese_yliko("Βούτυρο", 6)
    shokupan.prosthese_odigies(
        "1. Αναμείξτε όλα τα υλικά εκτός από βούτυρο και κρέμα.\n"
        "2. Ζυμώστε καλά για 10-15 λεπτά.\n"
        "3. Προσθέστε βούτυρο και κρέμα, συνεχίστε το ζύμωμα.\n"
        "4. Αφήστε να φουσκώσει για 1 ώρα.\n"
        "5. Πλάστε, βάλτε σε φόρμα και αφήστε να φουσκώσει ξανά.\n"
        "6. Ψήστε στους 200°C για 30 λεπτά."
    )
    
    # --- 4. ΜΕΙΓΜΑ 80-20 (η σωστή σου συνταγή) ---
    meigma = Syntagi("Μείγμα 80-20", 1000)
    meigma.prosthese_yliko("Αλεύρι σίτου", 80)
    meigma.prosthese_yliko("Σίκαλη", 20)
    meigma.prosthese_yliko("Νερό", 60)
    meigma.prosthese_yliko("Μαγιά", 2)
    meigma.prosthese_yliko("Αλάτι", 2)
    meigma.prosthese_odigies(
        "ΑΥΤΟΛΥΣΗ: Ρίχνουμε αλεύρι και νερό. Μόλις ομογενοποιηθούν σταματάμε και αφήνουμε 20 λεπτά.\n"
        "Μετά προσθέτουμε τα υπόλοιπα υλικά και ζυμώνουμε (3 αργή, 5 γρήγορη).\n"
        "Ξεκούραση 25 λεπτά.\n"
        "Ψήσιμο στους 220°C για 15 λεπτά και 200°C για 20 λεπτά."
    )
    
    return [psomi, stareno, shokupan, meigma]


def main():
    syntages = dimiourgise_syntages()
    
    while True:
        print("\n" + "🧑‍🍳 ΑΡΤΟΠΟΙΙΑΚΟ ΣΥΝΤΑΓΟΛΟΓΙΟ 🧑‍🍳")
        print("="*50)
        print("1. Δες όλες τις συνταγές")
        print("2. Δες μια συνταγή με προσαρμοσμένη ποσότητα")
        print("3. Πρόσθεσε νέα συνταγή")
        print("4. Διαγραφή συνταγής")  # ΝΕΟ!
        print("5. Έξοδος")
        print("="*50)
        
        epilogi = input("Επίλεξε (1-5): ")
        
        if epilogi == "1":
            for i, s in enumerate(syntages, 1):
                print(f"{i}. {s.onoma}")
            epi = int(input("Ποια συνταγή θες να δεις (αριθμός); ")) - 1
            if 0 <= epi < len(syntages):
                syntages[epi].emfanise()
            else:
                print("❌ Μη έγκυρη επιλογή!")
        
        elif epilogi == "2":
            for i, s in enumerate(syntages, 1):
                print(f"{i}. {s.onoma}")
            epi = int(input("Ποια συνταγή (αριθμός); ")) - 1
            if 0 <= epi < len(syntages):
                poso = float(input("Πόσα γραμμάρια αλεύρι θέλεις; "))
                syntages[epi].emfanise(poso)
            else:
                print("❌ Μη έγκυρη επιλογή!")
        
        elif epilogi == "3":
            onoma = input("Όνομα συνταγής: ")
            nea = Syntagi(onoma)
            print("Πρόσθεσε υλικά (γράψε 'stop' για να τελειώσεις):")
            while True:
                yliko = input("Υλικό: ")
                if yliko.lower() == "stop":
                    break
                pososto = float(input("Ποσοστό (%): "))
                nea.prosthese_yliko(yliko, pososto)
            odigies = input("Οδηγίες (μια γραμμή): ")
            nea.prosthese_odigies(odigies)
            syntages.append(nea)
            print(f"✅ Η συνταγή '{onoma}' προστέθηκε!")
        
        elif epilogi == "4":  # ΝΕΟ! Διαγραφή
            if len(syntages) == 0:
                print("❌ Δεν υπάρχουν συνταγές για διαγραφή!")
                continue
            
            print("\n📋 ΣΥΝΤΑΓΕΣ ΠΟΥ ΥΠΑΡΧΟΥΝ:")
            for i, s in enumerate(syntages, 1):
                print(f"{i}. {s.onoma}")
            
            epi = int(input("Ποια συνταγή θέλεις να διαγράψεις (αριθμός); ")) - 1
            if 0 <= epi < len(syntages):
                onoma = syntages[epi].onoma
                syntages.pop(epi)
                print(f"✅ Η συνταγή '{onoma}' διαγράφηκε!")
            else:
                print("❌ Μη έγκυρη επιλογή!")
        
        elif epilogi == "5":
            print("👋 Καλή αρτοποιία!")
            break
        
        else:
            print("❌ Μη έγκυρη επιλογή. Δοκίμασε ξανά.")


if __name__ == "__main__":
    main()