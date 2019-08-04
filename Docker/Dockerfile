FROM continuumio/anaconda3:latest
#FROM continuumio/miniconda3:latest

ENV PATH /opt/conda/bin:$PATH


WORKDIR /Users/chrispickford/Documents/Coding/Python/Projects/
RUN ls


# Updating Anaconda packages
RUN conda update conda
#RUN conda update anaconda
#RUN conda update --all



COPY ./TimeSeriesKb/Docker/Src/main.py ./home/TimeSeriesKb/
COPY ./TimeSeriesKb/Docker/Src/config.py ./home/TimeSeriesKb/
COPY ./TimeSeriesKb/Materials/SQL/all_data.sql ./home/TimeSeriesKb/
COPY ./TimeSeriesKb/Materials/Environment/general_no-builds.yml ./home/
COPY ./DataCrane/ ./home/Packages/DataCrane/
COPY ./CodeCandy/ ./home/Packages/CodeCandy/

WORKDIR ./home/TimeSeriesKb
#RUN chmod a+rwx /home/
ENV PATH /home:$PATH
RUN ls

RUN conda env create --name TimeSeriesKb --file ./../general_no-builds.yml

RUN echo "conda activate TimeSeriesKb" > ~/.bashrc
ENV PATH /opt/conda/envs/TimeSeriesKb/bin:$PATH

CMD ["python", "./main.py"]

