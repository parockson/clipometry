import torch
import clip
from PIL import Image

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_embedding(image_path):
    """Return CLIP embedding for an image."""
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        embedding = model.encode_image(image)
    return embedding / embedding.norm(dim=-1, keepdim=True)

def get_text_embedding(text):
    """Return CLIP embedding for a text string."""
    tokens = clip.tokenize([text]).to(device)
    with torch.no_grad():
        embedding = model.encode_text(tokens)
    return embedding / embedding.norm(dim=-1, keepdim=True)

def cosine_similarity(emb1, emb2):
    """Cosine similarity between two embeddings."""
    return torch.matmul(emb1, emb2.T).cpu().numpy()[0][0]
