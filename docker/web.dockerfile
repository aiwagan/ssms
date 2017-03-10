# base image
FROM centos:7

# install os dependencies
RUN yum update -y
RUN yum groupinstall "Development Tools" -y
RUN yum install libxslt libxslt-devel libxml libxml-devel -y

# install app dependencies
WORKDIR /ssms
RUN make install

# start app

