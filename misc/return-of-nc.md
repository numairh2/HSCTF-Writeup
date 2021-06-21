# HSCTF – Return of the Intro to Netcat


* **Category:** Misc
* **Points:** 160

## Challenge

> hey, netcat seems fun! (with a twist)
> 
> `nc return-of-the-intro-to-netcat.hsc.tf 1337`


## Solution

By looking at the chal name and the linux command given to us, this command is netcat. If confused check out the link below. 

netcat - https://en.wikipedia.org/wiki/Netcat

When we run this nc command we get something like this, 
<img width="655" alt="Screen Shot 2021-06-21 at 3 26 29 PM" src="https://user-images.githubusercontent.com/74195947/122823506-0fb6b100-d2a5-11eb-9589-fa97b0df976a.png">

The program prints out a linux python3 command which looks like it get something from a website and runs a program

This is no problem because we can the terminal to get the flag by copying the the python command and using a new window to run the command

After running the python command, we get the Solution which the nc program asked us

`Solution: s.AAB3ISeJuwIKUXHv67Jk3gVVE2cek6JXazbZxIxQYXTBTzB+yLMAsWRwOPUKtHuUJECyCR9ImHE94LgZKwMz2eLWFkgSKOIODSWLmGnahJEChCxITmEoNJPfD6DXUYKMYB1MZHVFCgTd7l0ipz8gCsF2/Knt8+9hyiYydbmi60TD1oY/OWF4nDQ0ef96MJlE7PZaj1TDmXGGQUkJLkoqgnl+`

After putting the solution, the flag should show up as
`flag{the_cat_says_meow}`

