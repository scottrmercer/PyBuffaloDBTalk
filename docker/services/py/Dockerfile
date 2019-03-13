FROM jupyter/scipy-notebook


LABEL maintainer="rgalbo <rcgalbo@gmail.com" \
      description="scipy with a few things installed"

WORKDIR /app

COPY requirements.txt ./ 

RUN pip install --upgrade pip 
RUN pip --no-cache-dir install -r requirements.txt

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
