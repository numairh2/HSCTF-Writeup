# CTF NAME – LSBlue

* **Category:** Misc
* **Points:** 220
* **Solved:** During CTF
* **Author** wooshi

## Challenge
> Orca watching is an awesome pastime of mine!
> ![lsblue](https://user-images.githubusercontent.com/74195947/123028884-c306cf00-d3a5-11eb-9ec4-b25f8403320a.png)


## Solution
I first check Strings command! Sometimes it safes alot of time

<img width="205" alt="Screen Shot 2021-06-22 at 10 09 00 PM" src="https://user-images.githubusercontent.com/74195947/123029262-75d72d00-d3a6-11eb-827c-b5b16ce49b99.png">

By looking at what strings gave us, the flag is not in there.

I next look at the title, LSBlue... I saw LSB, which means 'least-significant bit', and it means that flag is under LSB.

After looking at different CTFs, I saw Zsteg which is a tool that detect stego-hidden data in PNG & BMP file extensions

After running Zsteg 

<img width="567" alt="Screen Shot 2021-06-15 at 10 09 53 PM" src="https://user-images.githubusercontent.com/74195947/123029719-2cd3a880-d3a7-11eb-84bb-84d3bfcb6302.png">

The flag was hidden in the LSB data

`flag{0rc45_4r3nt_6lue_s1lly_489131}`

