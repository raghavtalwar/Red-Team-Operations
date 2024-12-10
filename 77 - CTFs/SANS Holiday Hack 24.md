
## Challenge 1 - cURLing

```markdown
1) Unlike the defined standards of a curling sheet, embedded devices often have web servers on non-standard ports.  Use curl to retrieve the web page on host "curlingfun" port 8080.

curl -iL http://curlingfun:8080

2) Embedded devices often use self-signed certificates, where your browser will not trust the certificate presented.  Use curl to retrieve the TLS-protected web page at https://curlingfun:9090/

curl https://curlingfun:9090 -k

3) Working with APIs and embedded devices often requires making HTTP POST requests. Use curl to send a request to https://curlingfun:9090/ with the parameter "skip" set to the value "alabaster", declaring Alabaster as the team captain

curl https://curlingfun:9090 -k --data 'skip=alabaster'

4) Working with APIs and embedded devices often requires maintaining session state by passing a cookie.  Use curl to send a request to https://curlingfun:9090/ with a cookie called "end" with the value "3", indicating we're on the third end of the curling match.

curl https://curlingfun:9090 -k --cookie "end=3"

5) Working with APIs and embedded devices sometimes requires working with raw HTTP headers.  Use curl to view the HTTP headers returned by a request to https://curlingfun:9090/

curl https://curlingfun:9090 -k -iL

6) Working with APIs and embedded devices sometimes requires working with custom HTTP headers.  Use curl to send a request to https://curlingfun:9090/ with an HTTP header called "Stone" and the value "Granite".

curl -H "Stone: Granite" https://curlingfun:9090 -k

7) curl will modify your URL unless you tell it not to. For example, use curl to retrieve the following URL containing special characters: https://curlingfun:9090/../../etc/hacks

curl "https://curlingfun:9090/../../etc/hacks" -k --path-as-is

# YAY
Great work! 
Once HHC grants your achievement, you may close this terminal.
```