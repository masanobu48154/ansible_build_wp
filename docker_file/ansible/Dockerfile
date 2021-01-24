FROM ubuntu:20.04

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends python3 python3-pip software-properties-common ansible vim sudo openssh-server
ADD wordpress.tar.gz /tmp/

ENTRYPOINT ["/bin/bash"]
