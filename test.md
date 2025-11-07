**Speech Recognition Dataset Preparation (Ello Screener)**
----------------------------------------------------------

This repo provides a reproducible pipeline to:

1.  **explore & clean** labels in a notebook,

2.  **save** a cleaned `dataset_clean.json`, and

3.  **load** audio + labels via a minimal **PyTorch Dataset**.

We use **uv** for fast, isolated Python environments.

* * * * *

**0) Prerequisites**
--------------------

-   **Python** 3.10+

-   **uv** installed:

    `curl -LsSf https://astral.sh/uv/install.sh | sh`

-   **WAV files only** (no FFmpeg required)

* * * * *

**1) Repo Structure**
---------------------

`.
├─ label_files/
│  ├─ dataset.json              # raw labels (given)
│  └─ dataset_clean.json        # created by the notebook (output)
├─ wav_files/                   # WAV audio files (given)
├─ dataset.py                   # minimal PyTorch Dataset (trusts cleaned JSON)
├─ result.ipynb                 # EDA + cleaning + stats + outliers
└─ README.md`

* * * * *

**2) Setup with uv**
--------------------

**Option A --- quick install**

`uv venv
source .venv/bin/activate
uv pip install torch torchaudio pandas numpy matplotlib jupyter ipykernel ipywidgets`

**Option B --- via `pyproject.toml` (optional)**

`uv sync
source .venv/bin/activate`

* * * * *

**3) Reproduce Results**
------------------------

### **A) Run the notebook to explore & clean**

This will:

-   analyze **casing** & **unexpected characters**

-   normalize transcripts (allow only **A--Z**, **space**, and **'**)

-   remove **extra spaces**

-   compute **duration/word** stats & plots

-   detect **outliers** via duration--word regression

-   drop fully silent files (**spkr2902_sample1870.wav**, **spkr1988_sample233.wav**)

-   **write** `label_files/dataset_clean.json`

`jupyter notebook result.ipynb
# Run all cells top-to-bottom.`

**Expected output:**

`label_files/dataset_clean.json`

### **B) Load the cleaned data with the PyTorch Dataset**

`dataset.py` **does not re-clean** text; it trusts `dataset_clean.json`.

`from torch.utils.data import DataLoader
from dataset import ASREvalDataset, collate_fn

labels_path = "./label_files/dataset_clean.json"
wav_dir = "./wav_files"

ds = ASREvalDataset(labels_path, wav_dir, target_sr=16000, return_text=True, strict_exist_check=False)
dl = DataLoader(ds, batch_size=8, shuffle=False, collate_fn=collate_fn)

batch = next(iter(dl))
print(batch["waveforms"].shape, batch["lengths"][:5])
print(batch.get("transcripts", [])[:3])`
