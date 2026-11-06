# TP INF151 - YEPMEN Jovanie
# Portefeuille électronique multi devises

class EWallet:
    def __init__(self, nom):
        self.nom = nom
        self.solde = {"XAF": 0, "EUR": 0, "USD": 0}  # Multi-devises
        self.taux = {"EUR": 655.957, "USD": 600}  # 1 EUR = 655.957 XAF, 1 USD = 600 XAF

    def deposer(self, montant, devise):
        if devise in self.solde:
            self.solde[devise] += montant
            print(f"Depot de {montant} {devise} effectue")
        else:
            print("Devise non supportee")

    def retirer(self, montant, devise):
        if self.solde[devise] >= montant:
            self.solde[devise] -= montant
            print(f"Retrait de {montant} {devise} effectue")
        else:
            print("Solde insuffisant")

    def convertir(self, montant, devise_depart, devise_arrivee):
        # Convertit tout en XAF d'abord
        montant_xaf = montant * self.taux.get(devise_depart, 1)
        montant_final = montant_xaf / self.taux.get(devise_arrivee, 1)
        
        if self.solde[devise_depart] >= montant:
            self.solde[devise_depart] -= montant
            self.solde[devise_arrivee] += montant_final
            print(f"{montant} {devise_depart} = {montant_final:.2f} {devise_arrivee}")
        else:
            print("Solde insuffisant")

    def afficher_solde(self):
        print(f"\n--- Solde de {self.nom} ---")
        for devise, montant in self.solde.items():
            print(f"{devise}: {montant:.2f}")

# Test du portefeuille
mon_wallet = EWallet("YEPMEN Jovanie")
mon_wallet.deposer(100000, "XAF")
mon_wallet.deposer(100, "EUR")
mon_wallet.afficher_solde()
mon_wallet.convertir(50, "EUR", "XAF")
mon_wallet.retirer(20000, "XAF")
mon_wallet.afficher_solde()
