import os
import webbrowser

print("=== 🦊 FOXCODE ENGINE - VERSION STABLE RENDU WEB ===")
print("Commandes : 'generer_geant 5000', 'generer_boutons 5000', ou ton lexique (titre, texte, bouton...).\n")

FICHIER_SORTIE = "mon_site.html"
buffer_html = []

def initialiser_projet():
    global buffer_html
    buffer_html = []
    buffer_html.append("<!DOCTYPE html>\n")
    buffer_html.append("<html lang='fr'>\n")
    buffer_html.append("<head>\n")
    buffer_html.append("<meta charset='UTF-8'>\n")
    buffer_html.append("<title>FoxCode Projet</title>\n")
    buffer_html.append("<style>\n")
    buffer_html.append("    body { background: #0f172a; color: #f8fafc; font-family: monospace; padding: 20px; }\n")
    buffer_html.append("    h1 { color: #38bdf8; border-bottom: 2px solid #1e293b; padding-bottom: 10px; }\n")
    buffer_html.append("    p { color: #94a3b8; margin: 8px 0; }\n")
    buffer_html.append("    div.block { background: #1e293b; padding: 10px; margin: 6px 0; border-left: 4px solid #38bdf8; }\n")
    buffer_html.append("</style>\n")
    buffer_html.append("</head>\n")
    buffer_html.append("<body>\n")
    print("[OK] Projet initialisé.")

def ecrire_flux(texte):
    buffer_html.append(texte + "\n")

def compiler_et_lancer():
    buffer_html.append("</body>\n")
    buffer_html.append("</html>\n")
    
    with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
        f.writelines(buffer_html)
        
    chemin_absolu = os.path.abspath(FICHIER_SORTIE)
    webbrowser.open(f"file:///{chemin_absolu.replace(os.sep, '/')}")
    print(f"🚀 Site généré et ouvert dans le navigateur ! ({FICHIER_SORTIE})")

# Lexique complet de FoxCode
LEXIQUE = {
    "titre": "h1", "h1": "h1", "title": "h1",
    "sous_titre": "h2", "h2": "h2",
    "texte": "p", "paragraphe": "p", "p": "p", "ecrire": "p", "print": "p",
    "bouton": "button", "button": "button",
    "div": "div", "boite": "div"
}

# Initialisation de base
initialiser_projet()

while True:
    try:
        ligne = input("FoxCode > ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nFermeture...")
        break

    if not ligne or ligne.startswith(("#", "//")):
        continue

    # Commande de stress test lignes
    if ligne.startswith("generer_geant"):
        parties = ligne.split()
        limite = int(parties[1]) if len(parties) > 1 and parties[1].isdigit() else 1000

        print(f"Génération de {limite} lignes en cours...")
        buffer_html.append(f"<h1>STRESS TEST : {limite} LIGNES</h1>\n")

        for i in range(1, limite + 1):
            buffer_html.append(f"<div class='block'>Bloc numéro {i} - Système stable</div>\n")

        compiler_et_lancer()
        continue

    # Commande de stress test boutons
    if ligne.startswith("generer_boutons"):
        parties = ligne.split()
        limite = int(parties[1]) if len(parties) > 1 and parties[1].isdigit() else 5000

        print(f"Génération de {limite} boutons en cours...")
        buffer_html.append("<div style='background: #090d16; color: #f8fafc; font-family: sans-serif; padding: 20px; text-align: center;'>\n")
        buffer_html.append(f"<h1 style='color: #38bdf8; font-size: 2.5rem; margin-bottom: 20px;'>FOXCODE MATRIX : {limite} BOUTONS ACTIFS</h1>\n")
        buffer_html.append("<div style='display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; max-width: 1400px; margin: 0 auto;'>\n")

        for i in range(1, limite + 1):
            buffer_html.append(f"<button onclick=\"alert('Action validée sur le Bouton #{i}')\" style='background: #1e293b; color: #38bdf8; border: 1px solid #334155; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-weight: bold;'>Bouton_{i}</button>\n")

        buffer_html.append("</div>\n</div>\n")
        compiler_et_lancer()
        continue

    if ligne.lower() in ["totalpro", "run", "build"]:
        compiler_et_lancer()
        continue

    if ligne.lower() in ["reset", "clear"]:
        initialiser_projet()
        print("[OK] Réinitialisé.")
        continue

    # Analyse du lexique FoxCode
    mots = ligne.split()
    premier_mot = mots[0].lower() if mots else ""

    if premier_mot in LEXIQUE:
        balise = LEXIQUE[premier_mot]
        contenu = ligne[len(premier_mot):].strip()
        if (contenu.startswith('"') and contenu.endswith('"')) or (contenu.startswith("'") and contenu.endswith("'")):
            contenu = contenu[1:-1]
        
        ecrire_flux(f"<{balise}>{contenu}</{balise}>")
        print(f"[OK] Élément <{balise}> ajouté.")
    else:
        ecrire_flux(ligne)
        print("[OK] Code brut injecté.")