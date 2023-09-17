import os, subprocess
commit = "5ef669de080814067961f28357256e8fe27544f4"
# Задание имени и создание папки
sdwu = "stable-diffusion-webui"
sdwu1 = "sd-webui"
wup = "webui.py"
fpath = f"/content/{sdwu}/"
os.system(f"mkdir -p {fpath}")
# Клонирование репозитория
subprocess.run(["git", "clone", f"https://github.com/AUTOMATIC1111/{sdwu}", fpath])
# Переключение на нужный рабочий коммит
subprocess.run(["git", "checkout", commit], cwd=fpath, capture_output=True, text=True)
# Установка репозиториев для WebUI
launch = f"{fpath}modules/launch_utils.py"
with open(f'{launch}', 'r') as fp:
  lines = fp.readlines()
  for line in lines:
    if line.find('STABLE_DIFFUSION_COMMIT_HASH') != -1:stable_diffusion_commit_hash = line.split('"')[1]
    if line.find('TAMING_TRANSFORMERS_COMMIT_HASH') != -1:taming_transformers_commit_hash = line.split('"')[1]
    if line.find('K_DIFFUSION_COMMIT_HASH') != -1:k_diffusion_commit_hash = line.split('"')[1]
    if line.find('CODEFORMER_COMMIT_HASH') != -1:codeformer_commit_hash = line.split('"')[1]
    if line.find('BLIP_COMMIT_HASH') != -1:blip_commit_hash = line.split('"')[1]
os.system(f"git clone https://github.com/Stability-AI/stablediffusion.git {fpath}repositories/stable-diffusion-stability-ai && cd {fpath}repositories/stable-diffusion-stability-ai && git checkout {stable_diffusion_commit_hash}")
os.system(f"git clone https://github.com/crowsonkb/k-diffusion.git {fpath}repositories/k-diffusion && cd {fpath}repositories/k-diffusion && git checkout {k_diffusion_commit_hash}")
os.system(f"git clone https://github.com/sczhou/CodeFormer.git {fpath}repositories/CodeFormer && cd {fpath}repositories/CodeFormer && git checkout {codeformer_commit_hash}")
os.system(f"git clone https://github.com/salesforce/BLIP.git {fpath}repositories/BLIP && cd {fpath}repositories/BLIP && git checkout {blip_commit_hash}")
os.system(f"git clone https://github.com/isl-org/MiDaS.git {fpath}repositories/midas")
# Установка дополнений
os.system(f"git clone https://github.com/thomasasfk/{sdwu1}-aspect-ratio-helper {fpath}extensions/{sdwu1}-aspect-ratio-helper")
os.system(f"git clone https://github.com/DominikDoom/a1111-{sdwu1}-tagcomplete {fpath}extensions/tag-autocomplete")
#Скачивание конфигов
os.system(f"rm -f {fpath}config.json && rm -f {fpath}ui-config.json")
os.system(f"wget https://raw.githubusercontent.com/Romanos575/NotSD/main/config.json -P {fpath}")
os.system(f"wget https://raw.githubusercontent.com/Romanos575/NotSD/main/ui-config.json -P {fpath}")
# Штатная установка зависимостей средствами launch.py
os.chdir(fpath)
os.system("python launch.py --share --opt-sdp-attention --ngrok test --no-download-sd-model --deepdanbooru --exit")
# Скачивание моделей, эмбедов и т.д.
models_folder = f"{fpath}models/Stable-diffusion"
embeds_folder = f"{fpath}embeddings"
model_dl = f"wget -nv -t 10 --show-progress --progress=bar -q --content-disposition -P {models_folder}"
os.system(f"{model_dl} https://huggingface.co/Magamanny/Koji/resolve/main/koji_v21.safetensors")
os.system(f"wget https://huggingface.co/embed/negative/resolve/main/bad-hands-5.pt -P {embeds_folder}")
os.system(f"wget https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.safetensors -P {embeds_folder}")
# Создание папки лор
loras_folder = f"{fpath}models/Lora"
os.system(f"mkdir -p {loras_folder}")
