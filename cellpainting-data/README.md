# chemical perturbations
## 1. download images 以下载 `0-19`(20个文件夹) 为例
```bash
cd chemical perturbations/download_images
python download_script.py --start 0 --end 20
```
end 最大是 115794
## 2. download infos
在`chemical perturbations/download_infos/get_infos.py`中修改`numbers`的范围，然后运行

```bash
cd chemical perturbations/download_infos
python get_infos.py
```
# genetic perturbations
## 1. download images 以下载 `0-19`(20个文件夹) 为例
```bash
cd genetic perturbations/download_images
python download_script.py --start 0 --end 20
```
end 最大是 23111
## 2. download infos
在`genetic perturbations/download_infos/get_infos.py`中修改`numbers`的范围，然后运行

```bash
python get_infos.py
```
# 命令行形式
```bash
curl 'https://phenaid.ardigen.com/api-jumpcpexplorer/gene-info/0' \
  -H 'authority: phenaid.ardigen.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cookie: _gcl_au=1.1.423162906.1689325031; _ga=GA1.1.479542853.1689325031; ln_or=eyIzODQzOTk0IjoiZCJ9; __hstc=95507139.d67872d0b23d3b8a41fe8fee5b1dbb2f.1689325044697.1689325044697.1689325044697.1; hubspotutk=d67872d0b23d3b8a41fe8fee5b1dbb2f; __hssrc=1; _fbp=fb.1.1689325048920.58393134; _ga_CCN9ZW80L8=GS1.1.1689325031.1.1.1689326048.0.0.0; __hssc=95507139.4.1689325044698' \
  -H 'referer: https://phenaid.ardigen.com/jumpcpexplorer/' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
  -o output1.txt
```