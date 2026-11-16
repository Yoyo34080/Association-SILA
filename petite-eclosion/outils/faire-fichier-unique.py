# Produit une version "fichier unique" du jeu : les images sont intégrées dans le HTML,
# pour pouvoir l'envoyer, la mettre sur un Drive ou l'ouvrir sans le dossier assets/.
# Usage : python3 outils/faire-fichier-unique.py index.html sortie.html
import base64, pathlib, re, sys

src, out = map(pathlib.Path, sys.argv[1:3])
ici = src.resolve().parent
s = src.read_text(encoding="utf-8")
uri = {p.stem: "data:image/webp;base64," + base64.b64encode(p.read_bytes()).decode()
       for p in sorted((ici / "assets").glob("*.webp"))}

s = re.sub(r'<link rel="preload" as="image"[^>]*>\n?', "", s)
# chemins calculés dans le code -> table des images intégrées
s = s.replace("assets/${z.thumb}.webp", "${IMGS[z.thumb]}")
s = s.replace("assets/papillon-${n}.webp", '${IMGS["papillon-"+n]}')
s = s.replace("(()=>{\n", "(()=>{\nconst IMGS=" + "{" + ",".join(f'"{k}":"{v}"' for k, v in uri.items()) + "};\n", 1)
# chemins écrits en clair : chaque image n'est intégrée qu'une fois, dans IMGS
s = re.sub(r':"assets/([a-z-]+)\.webp"', r':IMGS["\1"]', s)
s = re.sub(r"assets/([a-z-]+)\.webp", r'${IMGS["\1"]}', s)
assert "assets/" not in s
out.write_text(s, encoding="utf-8")
print(out, round(out.stat().st_size / 1e6, 2), "Mo")
