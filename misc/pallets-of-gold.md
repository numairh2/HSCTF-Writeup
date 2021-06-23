# HSCTF – pallets-of-gold

* **Category:** Misc
* **Points:** 107
* **Solved:** During the CTF

## Challenge

> It doesn't really look like gold to me...
> <img width="1199" alt="Screen Shot 2021-06-22 at 10 20 38 PM" src="https://user-images.githubusercontent.com/74195947/123030224-14b05900-d3a8-11eb-984a-e88ad391fd1d.png">

## Solution
I first check Strings command! Sometimes it safes alot of time

<img width="315" alt="Screen Shot 2021-06-22 at 10 23 46 PM" src="https://user-images.githubusercontent.com/74195947/123030490-84264880-d3a8-11eb-8b66-747ec00f770f.png">

After seeing that strings doesn't contain the flag, I checked the description and the picture and it seems that flag was in the picture.

So test my hypothesis, I used a tool called *stegsolve* which helps see different colors of that picture.

While playing around with the stegsolve, I was getting warmer to the flag when I saw the text.

I found the clear picture of the flag at **Red Plane 0**(this is half of the flag)

<img width="996" alt="Screen Shot 2021-06-22 at 10 36 21 PM" src="https://user-images.githubusercontent.com/74195947/123031668-46c2ba80-d3aa-11eb-91c3-24ac2aa60ee0.png">


`flag{p1te_chucks_remind_me_of_gifs}`
