The following utilities rely on openai API
### Customize chatgpt with your own data




### Environment

##### Activate conda environment
If necessary, re-create the conda environment before activate it.
`conda deactivate`

`conda remove --name chatbot_owndata_env_dev --all`

`conda update -n base -c defaults conda`

Create a virtual env with conda

`conda env create -f chatbot_owndata_env_dev.yml`

`conda activate chatbot_owndata_env_dev`

Make sure OPENAI_API_KEY is set in your environment variables
`source ~/.bashrc`
===========================


### Add your data
Create a new directory named ‘output’ anywhere you like and put PDF, TXT or CSV files inside it. You can add multiple files if you like but remember that more data you add, more the tokens will be used. This example usd prepare_datasets.py to prepare the docs exported from a huggingface dataset.

### Run standalone 
#### run one time only prepare docs
    python prepare_datasets.py
#### run first time to build index
    python chatbot_using_owndata_v4.py -t
#### for the following runs, you can remove -t
    python chatbot_using_owndata_v4.py

###
if gradio cannot create a shared link, try the following:
wget https://cdn-media.huggingface.co/frpc-gradio-0.2/frpc_darwin_amd64
mv frpc_darwin_amd64 frpc_darwin_arm64_v0.2
sudo mv frpc_darwin_arm64_v0.2 /Users/joannesun/anaconda3/envs/chatbot_owndata_env_dev/lib/python3.11/site-packages/gradio/

Sometimes the pip and conda have conflicts in package versions.
Please make sure they are consistent.

### Sample output

Running on public URL: https://a07d31181da85dd6.gradio.app
This share link expires in 72 hours.

Sample results:

![ScreenShot](/screenshots/owndata_1.png)
![ScreenShot](/screenshots/owndata_2.png)
![ScreenShot](/screenshots/owndata_unknown.png)
