Speech Recognition Dataset Preparation (Ello Screener)
======================================================

This repo provides a reproducible pipeline to:

1.  explore & clean labels in a notebook,
    
2.  save a cleaned dataset\_clean.json, and
    
3.  load audio + labels via a minimal PyTorch Dataset.
    

We use **uv** for fast, isolated Python environments.

0) Prerequisites
----------------

*   Python 3.10+
    
*   curl -LsSf https://astral.sh/uv/install.sh | sh
    
*   WAV files only
    

1) Repo Structure
-----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   .  ├─ label_files/  │  ├─ dataset.json              # raw labels (given)  │  └─ dataset_clean.json        # created by the notebook (output)  ├─ wav_files/                   # WAV audio files (given)  ├─ dataset.py                   # minimal PyTorch Dataset (trusts cleaned JSON)  ├─ result.ipynb                 # EDA + cleaning + stats + outliers  └─ README.md   `

2) Setup with uv
----------------

**Option A — quick install**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uv venv  source .venv/bin/activate  uv pip install torch torchaudio pandas numpy matplotlib jupyter ipykernel ipywidgets   `

**Option B — via pyproject.toml (optional)**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uv sync  source .venv/bin/activate   `

3) Reproduce Results
--------------------

### A) Run the notebook to **explore & clean**

This will:

*   analyze casing & unexpected characters,
    
*   normalize transcripts (allow only A–Z, space, and '),
    
*   remove extra spaces,
    
*   compute duration/word stats & plots,
    
*   detect outliers via duration–word regression,
    
*   drop fully silent files (spkr2902\_sample1870.wav, spkr1988\_sample233.wav),
    
*   **write** label\_files/dataset\_clean.json.
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   jupyter notebook result.ipynb  # Run all cells top-to-bottom.   `

Expected output:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   label_files/dataset_clean.json   `

### B) Load the cleaned data with the PyTorch Dataset

dataset.py **does not re-clean** text; it trusts dataset\_clean.json.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   from torch.utils.data import DataLoader  from dataset import ASREvalDataset, collate_fn  labels_path = "./label_files/dataset_clean.json"  wav_dir = "./wav_files"  ds = ASREvalDataset(labels_path, wav_dir, target_sr=16000, return_text=True, strict_exist_check=False)  dl = DataLoader(ds, batch_size=8, shuffle=False, collate_fn=collate_fn)  batch = next(iter(dl))  print(batch["waveforms"].shape, batch["lengths"][:5])  print(batch.get("transcripts", [])[:3])   `

4) Key Findings (replace with your actual numbers)
--------------------------------------------------

*   **Text cleaning:** Enforced A–Z, space, '; collapsed multiple spaces.
    
*   **Silence/outliers:** Removed two fully silent files; reviewed top residual outliers.
    
*   **Stats:** Mean duration ≈ _X_ s, mean words ≈ _Y_; durations roughly scale with word counts.
    

5) Tips / Troubleshooting
-------------------------

*   **Missing WAVs:** Set strict\_exist\_check=True to fail fast if any files are missing.
    
*   **Sample rate:** Use target\_sr=16000 for consistent evaluation; otherwise audio remains at native SR.
    
*   **Env:** Always source .venv/bin/activate before launching Jupyter.
    

6) License / Credits
--------------------

*   Exercise prompt courtesy of **Ello**.
    
*   Code authored by me for the technical screener.
