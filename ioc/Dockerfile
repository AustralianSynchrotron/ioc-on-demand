FROM australiansynchrotron/epics:centos7
WORKDIR /ioc
RUN adduser ics && chown ics: /ioc
USER ics
ENV USER ics
LABEL pyepics-workshop-image-type="ioc"
COPY src /ioc
RUN make
WORKDIR /ioc/iocBoot/iocToto
ENTRYPOINT ["./st.cmd"]
