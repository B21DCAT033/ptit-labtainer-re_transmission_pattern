FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tcpdump git \
    && rm -rf /var/lib/apt/lists/*

# Copy scenario
COPY scenario /home/labtainer/scenario
WORKDIR /home/labtainer

# Install imodule
RUN git clone https://github.com/B21DCAT033/Re-transmission-Pattern.git imodule && \
    cd imodule && \
    tar xf imodule.tar

# Ensure permissions
RUN chmod +x scenario/labtainer-baseline.sh

CMD ["/home/labtainer/scenario/labtainer-baseline.sh"]
