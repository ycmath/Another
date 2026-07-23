# /// script
# dependencies = [
#   "torch==2.6.0", "torchvision==0.21.0", "opencv-python-headless==4.10.0.84",
#   "numpy<3", "pandas>=2.2", "huggingface-hub>=0.33", "tabulate"
# ]
# ///
import urllib.request, base64, gzip, subprocess, sys
url = "https://raw.githubusercontent.com/ycmath/Another/519e6e240505d7c9cd71e8f8fc3ddca3b6d92d4b/rcpl_x5v_staging/run_x5v_compact.py.gz.b64"
raw = urllib.request.urlopen(url, timeout=60).read().decode().strip()
code = gzip.decompress(base64.b64decode(raw))
path = "/tmp/run_x5v_compact.py"
open(path, "wb").write(code)
print("STAGED_SCRIPT_BYTES", len(code), flush=True)
subprocess.run([sys.executable, path], check=True)
