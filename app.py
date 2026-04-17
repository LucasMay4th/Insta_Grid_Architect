import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import io
import zipfile
import os


def add_wii_style(img, border_width=25, corner_radius=60):
    """Ajoute le contour GRIS WII et arrondit les coins."""
    wii_grey = (220, 220, 220, 255)

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + img.size, radius=corner_radius, fill=255)

    img_rounded = img.copy()
    img_rounded.putalpha(mask)

    bg_w = img.width + (border_width * 2)
    bg_h = img.height + (border_width * 2)

    wii_frame = Image.new('RGBA', (bg_w, bg_h), (0, 0, 0, 0))
    draw_frame = ImageDraw.Draw(wii_frame)
    draw_frame.rounded_rectangle((0, 0, bg_w, bg_h), radius=corner_radius + border_width, fill=wii_grey)
    wii_frame.paste(img_rounded, (border_width, border_width), img_rounded)

    return wii_frame


def process_images_full(main_image, bg_image_input, num_rows, wii_mode):
    img = Image.open(main_image).convert("RGBA")

    # GESTION DU FOND
    if wii_mode:
        # On utilise l'image Wii_bg.png fournie
        if os.path.exists("Wii_bg.png"):
            bg = Image.open("Wii_bg.png").convert("RGB")
        else:
            # Fallback si le fichier est manquant : gris très clair
            bg = Image.new("RGB", (100, 100), (240, 240, 240))
            st.error("Fichier 'Wii_bg.png' introuvable dans le dossier ! Utilisation d'un fond gris par défaut.")
    else:
        bg = Image.open(bg_image_input).convert("RGB")

    cols = 3
    tile_w = 1080
    tile_h_34 = 1440
    tile_h_45 = 1350

    total_grid_w = tile_w * cols
    total_grid_h = tile_h_34 * num_rows

    if wii_mode:
        img = add_wii_style(img)

    img_ratio = img.width / img.height
    master_ratio = total_grid_w / total_grid_h

    if img_ratio > master_ratio:
        new_w = total_grid_w - 200  # Un peu plus de marge pour le look Wii
        new_h = int(new_w / img_ratio)
    else:
        new_h = total_grid_h - 200
        new_w = int(new_h * img_ratio)

    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Création du Master
    master_bg = bg.resize((total_grid_w, total_grid_h), Image.Resampling.LANCZOS).convert("RGBA")
    offset_x = (total_grid_w - new_w) // 2
    offset_y = (total_grid_h - new_h) // 2
    master_bg.alpha_composite(img_resized, (offset_x, offset_y))
    master_bg = master_bg.convert("RGB")

    tiles = []
    for r in range(num_rows):
        for c in range(cols):
            left = c * tile_w
            top = r * tile_h_34
            right = left + tile_w
            bottom = top + tile_h_34
            tile_34 = master_bg.crop((left, top, right, bottom))

            # Fond blanc pour les marges 4:5
            final_tile = Image.new('RGB', (tile_w, tile_h_45), (255, 255, 255))
            scale = tile_h_45 / tile_h_34
            tile_scaled = tile_34.resize((int(tile_w * scale), tile_h_45), Image.Resampling.LANCZOS)
            final_tile.paste(tile_scaled, ((tile_w - tile_scaled.width) // 2, 0))

            tile_index = (num_rows - r - 1) * 3 + (3 - c)
            tiles.append({"img": final_tile, "name": f"grid_{tile_index}.jpg"})

    return tiles


# --- INTERFACE ---
st.set_page_config(page_title="Insta Grid Architect", layout="wide")
st.title("Insta Grid Architect")

with st.sidebar:
    st.header("Options")
    rows = st.number_input("Nombre de lignes", min_value=1, value=3)
    wii_mode = st.checkbox("Activer le Style Wii (Fond Auto)", value=True)

    st.divider()
    main_file = st.file_uploader("1. Image principale", type=["jpg", "png"])

    # On n'affiche l'uploader de fond que si le mode Wii est désactivé
    bg_file = None
    if not wii_mode:
        bg_file = st.file_uploader("2. Image de fond personnalisée", type=["jpg", "png"])
    else:
        st.success("✅ Fond Wii sélectionné automatiquement")

if main_file and (wii_mode or bg_file):
    if st.button("🚀 Générer la grille"):
        tiles = process_images_full(main_file, bg_file, rows, wii_mode)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for tile in tiles:
                buf = io.BytesIO()
                tile["img"].save(buf, format="JPEG", quality=95)
                zip_file.writestr(tile["name"], buf.getvalue())

        st.download_button("📥 Télécharger le pack ZIP", zip_buffer.getvalue(), "grille_wii.zip")

        # Aperçu
        display_tiles = sorted(tiles, key=lambda x: int(x['name'].split('_')[1].split('.')[0]), reverse=True)
        idx = 0
        for r in range(rows):
            cols_ui = st.columns(3)
            for c in range(3):
                if idx < len(display_tiles):
                    with cols_ui[c]:
                        st.image(display_tiles[idx]["img"])
                    idx += 1