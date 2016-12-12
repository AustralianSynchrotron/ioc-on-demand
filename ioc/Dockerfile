FROM australiansynchrotron/epics:centos7
WORKDIR /ioc
COPY src /ioc
RUN adduser ics && chown -R ics: /ioc
USER ics
ENV USER ics
RUN make clean && make
WORKDIR /ioc/iocBoot/iocToto
ENTRYPOINT ["./st.cmd"]
