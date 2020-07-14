FROM pytorch/pytorch

RUN set -x \
  && apt-get update -y \
  && apt-get install -y --no-install-recommends \
    xvfb xauth x11vnc x11-utils x11-xserver-utils xdotool \
    curl unzip software-properties-common vim sudo wget tree 

RUN conda install -c conda-forge opencv

COPY . /workspace

RUN chmod a+x /workspace/streaming/vnchost.sh
RUN chmod a+x /workspace/noVNC/utils/launch.sh

WORKDIR /workspace/app

ENV DISPLAY :1

CMD ["../streaming/vnchost.sh"]
