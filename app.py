import streamlit as st
import os
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
SHAPES_DIR = os.path.join("static", "shapes")
CATEGORIES = {
    "Triangles": ["triangle", "equilateral", "isosceles", "scalene", "right"],
    "Quadrilaterals": ["square", "rectangle", "rhombus", "parallelogram", "trapezium", "kite"],
    "Polygons": ["pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon", "dodecagon"],
    "Circles & Curves": ["circle", "semicircle", "quadrant", "ellipse", "sector", "annulus"],
    "3D Solids": ["cube", "cylinder", "cone"],
    "Others": ["angle"]
}

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

model = load_model()

# ----------------- UTILS -----------------
def get_image_embeddings(img_files):
    embeddings = []
    for f in img_files:
        emb = model.encode(f)
        embeddings.append(emb)
    embeddings = np.array(embeddings, dtype=np.float32)
    embeddings = np.nan_to_num(embeddings, nan=0.0, posinf=0.0, neginf=0.0)
    return embeddings

def get_text_embeddings(texts):
    embeddings = np.array([model.encode(t) for t in texts], dtype=np.float32)
    embeddings = np.nan_to_num(embeddings, nan=0.0, posinf=0.0, neginf=0.0)
    return embeddings

def plot_embeddings(vectors, labels, title):
    if len(vectors) < 2:
        st.warning("Need at least 2 embeddings to plot PCA.")
        return
    # Normalize vectors to prevent extremely large values
    vectors = normalize(vectors)
    try:
        reduced = PCA(n_components=2).fit_transform(vectors)
    except Exception as e:
        st.error(f"PCA failed: {e}")
        return

    fig, ax = plt.subplots(figsize=(6, 6))
    for i, txt in enumerate(labels):
        ax.scatter(reduced[i, 0], reduced[i, 1])
        ax.text(reduced[i, 0]+0.01, reduced[i, 1]+0.01, txt)
    ax.set_title(title)
    st.pyplot(fig)

# ----------------- STREAMLIT APP -----------------
st.set_page_config(page_title="Shape Gallery Semantic Space", layout="wide")
st.title("🔷 Shape Semantic Space Explorer")

tab1, tab2 = st.tabs(["Select Images", "Semantic Space"])

with tab1:
    st.subheader("Select up to 4 Images from the Gallery")

    # 1️⃣ Category dropdown
    category = st.selectbox("Select Category:", ["All"] + list(CATEGORIES.keys()))
    if category == "All":
        filtered_files = [f for f in os.listdir(SHAPES_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    else:
        keywords = CATEGORIES[category]
        filtered_files = [f for f in os.listdir(SHAPES_DIR) if any(k in f.lower() for k in keywords)]

    # 2️⃣ Keyword search
    keyword = st.text_input("Search shape by keyword:")
    if keyword:
        filtered_files = [f for f in filtered_files if keyword.lower() in f.lower()]

    if not filtered_files:
        st.warning("⚠️ No images match your filters.")
    else:
        if "chosen_images" not in st.session_state:
            st.session_state["chosen_images"] = []

        selected_files = st.session_state["chosen_images"]

        # Display selected images at top
        if selected_files:
            st.write("### Selected Images")
            cols2 = st.columns(len(selected_files))
            for i, fname in enumerate(selected_files):
                with cols2[i]:
                    st.image(os.path.join(SHAPES_DIR, fname), caption=fname, width=150)

        st.write("### Gallery")
        cols = st.columns(4)
        for idx, fname in enumerate(filtered_files):
            col = cols[idx % 4]
            with col:
                checked = st.checkbox(fname, key=f"chk_{fname}", value=(fname in selected_files))
                st.image(os.path.join(SHAPES_DIR, fname), width=120)

                if checked and fname not in selected_files:
                    if len(selected_files) < 4:
                        selected_files.append(fname)
                    else:
                        st.warning("⚠️ You can select up to 4 images only.")
                        st.session_state[f"chk_{fname}"] = False
                elif not checked and fname in selected_files:
                    selected_files.remove(fname)

        st.session_state["chosen_images"] = selected_files

with tab2:
    st.subheader("Compare Images with Candidate Names")
    chosen_images = st.session_state.get("chosen_images", [])
    if len(chosen_images) < 2:
        st.info("Select at least 2 images from the first tab to generate PCA plots.")
    else:
        candidate_names = st.text_area("Enter candidate names (comma separated, e.g., square, circle, triangle, kite):")
        candidate_names = [x.strip() for x in candidate_names.split(",") if x.strip()]
        if candidate_names:
            if len(candidate_names) > 4:
                st.warning("Max 4 candidate names allowed.")
                candidate_names = candidate_names[:4]

            image_emb = get_image_embeddings(chosen_images)
            text_emb = get_text_embeddings(candidate_names)

            # Plot separately
            plot_embeddings(image_emb, chosen_images, "Image Encoder Space")
            plot_embeddings(text_emb, candidate_names, "Text Encoder Space")

            # Plot combined
            all_emb = np.vstack([image_emb, text_emb])
            all_labels = chosen_images + candidate_names
            plot_embeddings(all_emb, all_labels, "Combined Semantic Space")
