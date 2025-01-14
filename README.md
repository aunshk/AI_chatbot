# AI_chatbot
Build a Fully Local AI Chatbot with Ollama

--> My setup 	: 

CPU(s): 4 cores
RAM: 8GB 
OS : Rocky linux 8.10
Python : 3.12.0
pip: 24.3.1
(Use higher system configuration for better performance)

#ML Models : 
1. Mistral : open-weight, large language model (LLM) designed for natural language processing tasks, such as text generation, question answering, and summarization 

2. TinyLlama : it is a smaller, more efficient variant of large language models. designed to be lightweight and optimized for performance while maintaining competitive natural language processing capabilities.


############################################################
1.) ## setup ollama in linux ##


## Install Ollama:
curl -fsSL https://ollama.com/install.sh | sh

#expected output:
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.	


## download the ML model
ollama pull mistral # requires higher system configuration
ollama pull TinyLlama # lightweight model

## (optional) run ml model to test in backend 
ollama pull mistral 
ollama pull TinyLlama

##
# delete model:
ollama rm TinyLlama
ollama rm mistral


############################################################

2) ### install dependensis:

sudo yum install python3.12-devel

#install requests (it is a popular Python library that Sends an HTTP request to the specified URL and handles the response)
pip3.12 install requests

pip3.12 install orjson

## Note: if orjson failed to install then try upgrdaing the pip and try again	
	pip3.12 install --upgrade pip
	pip3.12 install orjson

pip3.12 install gradio

python3.12 -c "import gradio; print(gradio.__version__)"	

##########################################################

3) ## execution part:

# 1. start the ollama :
		ollama start
		
# 2. execute main.py script
		 python3.12 main.py
	# expected output:
		* Running on local URL:  http://0.0.0.0:7860
		  To create a public link, set `share=True` in `launch()`.
		  
# 3. open web browser and execute 
			http://{your-server-ip}:7860/


##########################################################

## server Monitoring :

# check CPU load when you add a promt and hit the submit buttion
		use top ot htop utility
		
# check RAM usage
		watch free -g #this will execute free -g command at every 2 seconds
