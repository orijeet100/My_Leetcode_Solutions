# Speech Recognition Dataset Preparation (Ello Screener)

This repo contains a small ASR dataset and a reproducible pipeline to:
1. Explore & clean labels in a notebook
2. Save a cleaned `dataset_clean.json`
3. Load audio + labels via a minimal PyTorch `Dataset`

We use **uv** for fast, isolated Python environments.

## 📋 Prerequisites

* Python 3.10+
* **uv** installed:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
* FFmpeg not required (we use `torchaudio.load` on WAV)

## 📁 Repo Structure

```
.
├─ label_files/
│  ├─ dataset.json              # raw labels (given)
│  └─ dataset_clean.json        # created by the notebook (output)
├─ wav_files/                   # WAV audio files (given)
├─ dataset.py                   # minimal PyTorch Dataset (trusts cleaned JSON)
├─ result.ipynb                 # EDA + cleaning + stats + outliers
└─ README.md
```

## 🚀 Setup with uv

### Option A — Quick ad-hoc install:

```bash
uv venv
source .venv/bin/activate
uv pip install torch torchaudio pandas numpy matplotlib jupyter ipykernel ipywidgets
```

### Option B — Using a `pyproject.toml` (optional):

If you add one, then:
```bash
uv sync
source .venv/bin/activate
```

## 🔄 Reproduce Results

### A) Run the notebook to explore & clean

This will:
* Analyze casing / unexpected characters
* Normalize transcripts (A–Z, space, apostrophe)
* Remove extra spaces
* Compute duration/word stats & plots
* Flag outliers
* Drop known bad files (`spkr2902_sample1870.wav`, `spkr1988_sample233.wav`)
* Write `label_files/dataset_clean.json`

```bash
jupyter notebook result.ipynb
# In the notebook: run all cells top-to-bottom
```

**Expected output:**
```
label_files/dataset_clean.json  # created at the end of the notebook
```

### B) Use the PyTorch Dataset for evaluation

`dataset.py` does not re-clean text. It trusts `dataset_clean.json`.

```python
from torch.utils.data import DataLoader
from dataset import ASREvalDataset, collate_fn

labels_path = "./label_files/dataset_clean.json"
wav_dir = "./wav_files"

ds = ASREvalDataset(
    labels_path, 
    wav_dir, 
    target_sr=16000, 
    return_text=True, 
    strict_exist_check=False
)

dl = DataLoader(
    ds, 
    batch_size=8, 
    shuffle=False, 
    collate_fn=collate_fn
)

batch = next(iter(dl))
print(batch["waveforms"].shape, batch["lengths"][:5])
print(batch.get("transcripts", [])[:3])
```

## 📊 Key Features

- **Data Cleaning**: Automated transcript normalization and outlier detection
- **PyTorch Integration**: Ready-to-use Dataset class for model evaluation
- **Reproducible Pipeline**: Clear separation of raw and cleaned data
- **Fast Environment Setup**: Uses uv for quick dependency management
