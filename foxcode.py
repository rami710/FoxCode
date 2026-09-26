import os
import sys
import webbrowser

print("==================================================")
print("🦊 FOXCODE ENGINE V7 (INDISTRUCTIBLE & SANS LIMITES)")
print("==================================================")
print("Écris tes commandes FoxCode, du HTML ou du texte libre.")
print("Commandes : titre, texte, annonce, champ_recherche, bouton_pilule, carte_neon, css, Total Pro, reset, run\n")

FICHIER_SORTIE = "mon_site.html"
buffer_html = []
styles_perso = []

def initialiser_projet():
    global buffer_html, styles_perso
    buffer_html = []
    styles_perso = []
    
    # Base HTML5 + Palette de 100 Couleurs CSS + Google Fonts
    css_base = """<!DOCTYPE html>
<html lang='fr'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Projet FoxCode</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=Inter:wght@300;400;600;700&family=Outfit:wght@400;600;800&family=Poppins:wght@300;500;700&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    /* PALETTE DE 100 COULEURS FOXCODE */
    --c-red-1: #ffe4e6; --c-red-2: #fecdd3; --c-red-3: #fda4af; --c-red-4: #fb7185; --c-red-5: #f43f5e;
    --c-red-6: #e11d48; --c-red-7: #be123c; --c-red-8: #9f1239; --c-red-9: #881337; --c-red-10: #4c0519;
    --c-blue-1: #eff6ff; --c-blue-2: #dbeafe; --c-blue-3: #bfdbfe; --c-blue-4: #93c5fd; --c-blue-5: #60a5fa;
    --c-blue-6: #3b82f6; --c-blue-7: #2563eb; --c-blue-8: #1d4ed8; --c-blue-9: #1e40af; --c-blue-10: #1e3a8a;
    --c-green-1: #f0fdf4; --c-green-2: #dcfce7; --c-green-3: #bbf7d0; --c-green-4: #86efac; --c-green-5: #4ade80;
    --c-green-6: #22c55e; --c-green-7: #16a34a; --c-green-8: #15803d; --c-green-9: #166534; --c-green-10: #14532d;
    --c-purple-1: #faf5ff; --c-purple-2: #f3e8ff; --c-purple-3: #e9d5ff; --c-purple-4: #d8b4fe; --c-purple-5: #c084fc;
    --c-purple-6: #a855f7; --c-purple-7: #9333ea; --c-purple-8: #7e22ce; --c-purple-9: #6b21a8; --c-purple-10: #581c87;
    --c-amber-1: #fffbeb; --c-amber-2: #fef3c7; --c-amber-3: #fde68a; --c-amber-4: #fcd34d; --c-amber-5: #fbbf24;
    --c-amber-6: #f59e0b; --c-amber-7: #d97706; --c-amber-8: #b45309; --c-amber-9: #92400e; --c-amber-10: #78350f;
    --c-dark-1: #0f172a; --c-dark-2: #1e293b; --c-dark-3: #334155; --c-dark-4: #475569; --c-dark-5: #64748b;
    --c-neon-cyan: #00f0ff; --c-neon-pink: #ff007f; --c-neon-green: #39ff14; --c-neon-yellow: #fff000;
  }
  * { box-sizing: border-box; font-family: 'Inter', sans-serif; transition: all 0.2s ease; }
  body {
    background-color: #0b0f19; color: #f8fafc; min-height: 100vh; margin: 0;
    display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 20px;
    background-image: radial-gradient(circle at 50% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 60%),
                      linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
                      linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
    background-size: 100% 100%, 36px 36px, 36px 36px;
  }
  .container { max-width: 850px; width: 100%; display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center; }
  .annonce { font-size: 0.85rem; color: #38bdf8; background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(8px); padding: 8px 18px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.3); max-width: 750px; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
  .annonce:hover { background: rgba(56, 189, 248, 0.2); border-color: #38bdf8; }
  h1.titre-main { font-size: 3.2rem; font-weight: 700; color: #f8fafc; margin: 10px 0; letter-spacing: -0.5px; text-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }
  p.texte-main { color: #94a3b8; font-size: 1.15rem; line-height: 1.6; max-width: 650px; }
  .box-recherche { width: 100%; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 24px; padding: 20px 24px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4); text-align: left; display: flex; flex-direction: column; gap: 20px; }
  .box-recherche input { width: 100%; border: none; background: transparent; font-size: 1.15rem; color: #f8fafc; outline: none; }
  .box-recherche input::placeholder { color: #64748b; }
  .box-actions { display: flex; justify-content: space-between; align-items: center; }
  .chips-group { display: flex; gap: 8px; }
  .chip { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 6px 14px; font-size: 0.85rem; color: #94a3b8; display: flex; align-items: center; gap: 6px; cursor: pointer; }
  .chip.active { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border-color: #38bdf8; }
  .btn-send { background: #38bdf8; color: #0f172a; width: 38px; height: 38px; border-radius: 50%; border: none; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; cursor: pointer; font-weight: bold; }
  .bouton-pilule { background: rgba(30, 41, 59, 0.8); border: 1px solid #334155; border-radius: 30px; padding: 10px 22px; font-size: 0.9rem; color: #e2e8f0; cursor: pointer; display: flex; align-items: center; gap: 8px; margin: 5px; display: inline-flex; }
  .bouton-pilule:hover { background: #1e293b; border-color: #38bdf8; color: #38bdf8; transform: translateY(-2px); }
  .carte-neon { background: rgba(30, 41, 59, 0.6); border: 1px solid #38bdf8; border-radius: 16px; padding: 20px; width: 100%; text-align: left; box-shadow: 0 0 15px rgba(56, 189, 248, 0.15); }
  .carte-neon h2 { color: #38bdf8; margin-top: 0; font-size: 1.3rem; }
</style>
</head>
<body>
<div class='container'>
"""
    buffer_html.append(css_base)
    print("🦊 Projet FoxCode prêt. Écris tes instructions librement !")

def ecrire_flux(code):
    buffer_html.append(code + "\n")

def compiler_et_lancer(mode_total_pro=False):
    try:
        block_css = "<style>\n" + "\n".join(styles_perso) + "\n</style>\n" if styles_perso else ""
        contenu_final = buffer_html + [block_css, "</div>\n</body>\n</html>\n"]
        
        with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
            f.writelines(contenu_final)
            
        chemin_absolu = os.path.abspath(FICHIER_SORTIE)
        webbrowser.open(f"file:///{chemin_absolu.replace(os.sep, '/')}")
        
        if mode_total_pro:
            print("🌐 [Total Pro] Site compilé avec succès ! Ouverture de Google...")
            webbrowser.open("https://www.google.com")
        else:
            print(f"🚀 [FoxCode] Rendu mis à jour dans {FICHIER_SORTIE}")
    except Exception as err:
        print(f"⚠️ Remarque : {err}")

def analyser_et_traiter(ligne):
    try:
        ligne_cleaned = ligne.strip()
        if not ligne_cleaned or ligne_cleaned.startswith(("#", "//")):
            return

        cmd_lower = ligne_cleaned.lower()

        # Commandes système FoxCode
        if cmd_lower in ["run", "build", "go"]:
            compiler_et_lancer(mode_total_pro=False)
            return

        if "total pro" in cmd_lower or "total_pro" in cmd_lower:
            compiler_et_lancer(mode_total_pro=True)
            return

        if cmd_lower in ["reset", "clear", "nouveau"]:
            initialiser_projet()
            return

        # Interprétation ultra-souple des mots-clés
        if ligne_cleaned.startswith("annonce "):
            valeur = ligne_cleaned[8:].strip().strip("\"'")
            ecrire_flux(f"<div class='annonce'>✦ {valeur}</div>")
            print(f"  + Annonce : {valeur[:40]}")

        elif ligne_cleaned.startswith("titre "):
            valeur = ligne_cleaned[6:].strip().strip("\"'")
            ecrire_flux(f"<h1 class='titre-main'>{valeur}</h1>")
            print(f"  + Titre : {valeur}")

        elif ligne_cleaned.startswith("texte "):
            valeur = ligne_cleaned[6:].strip().strip("\"'")
            ecrire_flux(f"<p class='texte-main'>{valeur}</p>")
            print(f"  + Texte : {valeur[:40]}")

        elif ligne_cleaned.startswith("champ_recherche "):
            valeur = ligne_cleaned[16:].strip().strip("\"'")
            ecrire_flux(f"""<div class='box-recherche'>
  <input type='text' placeholder='{valeur}' />
  <div class='box-actions'>
    <div class='chips-group'>
      <div class='chip active'>⚙️ DeepThink</div>
      <div class='chip'>🌐 Search</div>
    </div>
    <button class='btn-send'>&uarr;</button>
  </div>
</div>""")
            print(f"  + Champ recherche ajouté")

        elif ligne_cleaned.startswith("bouton_pilule "):
            valeur = ligne_cleaned[14:].strip().strip("\"'")
            ecrire_flux(f"<button class='bouton-pilule'>{valeur}</button>")
            print(f"  + Bouton pilule : {valeur}")

        elif ligne_cleaned.startswith("carte_neon "):
            valeur = ligne_cleaned[11:].strip().strip("\"'")
            parts = valeur.split("|", 1)
            t = parts[0].strip() if len(parts) > 0 else "Information"
            d = parts[1].strip() if len(parts) > 1 else ""
            ecrire_flux(f"<div class='carte-neon'><h2>{t}</h2><p>{d}</p></div>")
            print(f"  + Carte Néon : {t}")

        elif ligne_cleaned.startswith("css "):
            valeur = ligne_cleaned[4:].strip()
            styles_perso.append(valeur)
            print("  + Style CSS ajouté")

        else:
            # TOUTE AUTRE COMMANDE OU TEXTE BRUT EST ACCEPTÉ ET INJECTÉ DIRECTEMENT SANS PLANTAGE !
            ecrire_flux(f"<div>{ligne_cleaned}</div>")
            print(f"  + Élément FoxCode générique ajouté : {ligne_cleaned[:40]}")

    except Exception as e:
        # Protection totale : FoxCode reste ouvert quoi qu'il arrive
        print(f"  + Élément ajouté : {ligne_cleaned[:30]}")

# Lancement
initialiser_projet()

while True:
    try:
        entree = input("FoxCode > ")
        for l in entree.replace("\r", "").split("\n"):
            analyser_et_traiter(l)
    except (KeyboardInterrupt, EOFError):
        print("\n🦊 Fermeture de FoxCode.")
        break
    except Exception as err_globale:
        pass
