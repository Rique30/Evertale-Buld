"""Importa somente imagens com permissão de redistribuição verificada.
Edite image_manifest.json e acione o workflow manualmente. Não contorna bloqueios.
"""
import json
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / "image_manifest.json").read_text(encoding="utf-8"))
catalog_path = ROOT / "catalogo.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
by_id = {str(c["id"]): c for c in catalog}
folder = ROOT / "assets" / "personagens"
folder.mkdir(parents=True, exist_ok=True)
count = 0
for entry in manifest:
    name = str(entry.get("name", "")).strip()
    url = str(entry.get("url", "")).strip()
    license_name = str(entry.get("license", "")).strip()
    proof = str(entry.get("permission_url", "")).strip()
    ident = str(entry.get("catalog_id", "")).strip()
    if not all((name, url, license_name, proof, ident)):
        print(f"IGNORADO {name or '?'}: faltam dados de autorização")
        continue
    if ident not in by_id:
        print(f"IGNORADO {name}: ID do catálogo inválido")
        continue
    if license_name.lower() in ("desconhecida", "unknown", "não verificada", "nao verificada"):
        print(f"IGNORADO {name}: licença não verificada")
        continue
    parsed = urlparse(url)
    if parsed.scheme != "https":
        print(f"IGNORADO {name}: apenas HTTPS")
        continue
    try:
        req = Request(url, headers={"User-Agent": "EvertaleManagerImageImport/1.0"})
        with urlopen(req, timeout=20) as response:
            mime = response.headers.get_content_type()
            if mime not in ("image/png", "image/jpeg", "image/webp"):
                raise ValueError("Formato de imagem não permitido: " + mime)
            binary = response.read(3_000_001)
            if len(binary) > 3_000_000:
                raise ValueError("Imagem maior que 3 MB")
        ext = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}[mime]
        filename = f"personagem-{ident}{ext}"
        (folder / filename).write_bytes(binary)
        c = by_id[ident]
        c["imageUrl"] = "assets/personagens/" + filename
        c["imageAttribution"] = {
            "source": url, "license": license_name, "permission": proof,
            "credit": entry.get("credit", "")
        }
        count += 1
        print(f"OK {name} -> {filename}")
    except Exception as error:
        print(f"FALHOU {name}: {error}")
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Imagens importadas: {count}")
