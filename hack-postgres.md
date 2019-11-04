# Spell to execute shell commands and read their output using a postgres client
```
CREATE TEMP TABLE foo(a text);
COPY foo FROM PROGRAM 'whoami';
```
