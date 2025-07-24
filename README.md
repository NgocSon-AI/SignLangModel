# SignLangModel
Sign Language Model create by Ngoc Son

## My Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline
- app.py



## Project Configuration

```bash
#install aws cli from the following the link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
#configure aws crediential (scret key & access key)

aws configure
```


```bash
#Create a S3 bucket for model pusher. name is mentioned in the constant

```



## How to run project:

```bash
conda create -n SignLang python=3.10 -y
```

```bash
conda activate SignLang
```

```bash
pip install -r requirements.txt
```

```bash
python3 app.py
```