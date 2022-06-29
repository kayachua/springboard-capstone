FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

COPY main.py .
COPY models/bertweet_stock_tweet models/bertweet_stock_tweet
CMD ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "main.py"]
