create env

```bash
conda create -n wineq python=3.9 -y
```

activate env
```bash
conda activate wineq
```
install the requirements
```bash
pip install -r .\requirements.txt
```
install the requirements
```bash
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
```
```bash
git init
```
```bash
dvc init
```
```bash
dvc add .\data_given\winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
git remote add origin https://github.com/ashwinprabhukp/winequality_mlops.git
git branch -M main
git push origin main
```