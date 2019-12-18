#Building

FROM maven:3.6-jdk-8-slim as builder

RUN mkdir -p /build
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn package

#Running
FROM openjdk:8-slim

EXPOSE 1234
ENV APP_HOME /server
RUN mkdir p $APP_HOME
WORKDIR $APP_HOME
COPY --from=builder /build/target/server.jar server.jar
ENTRYPOINT ["java", "-jar", "server.jar"]
