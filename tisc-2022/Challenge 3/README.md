# Solution (part 1)

Hex dump the file with any tool and find the flag immediately as it is prepended by `TISC` 

### Flag

TISC{f76635ab}

### References

1. https://hexed.it/

# Solution (part 2)

Use autopsy and extract hidden files. Hex dump the `message.png_$RAND` file and extract out everything from "Kv." until right before " I f  y o u ... ". Last 4 bytes should be 9B 34 00 2E. Saved it as a new bin file and mount it using TrueCrypt. Hex dumping `message.png_$RAND` should also hint that the number `32` is significant for the puzzle. Use the password `f76635ab` to extract out `outer.jpg`. The solution seems to be finding a permutation of collision (i/l as 1, o as 0, s as 5) which has the same crc32 hash as the f76635ab (which is a hash collision). We know it is crc32 from the blood pressure pictures extracted from autopsy initially which gives us crc and the hint from hex dumping `message.png_$RAND` gives us 32. To do this, either use hashcat to generate a wordlist or you can use python and get `c01lis1on` as the password. Mount the file using TrueCrypt and use `c01lis1on` as the password this time to obtain flag.ppsm. Extract the audio clip by changing the flag.ppsm to flag.zip and extracting the file. Put the audio file through cyberchef and obtain the md5 hash for the flag

### Flag

TISC{f9fc54d767edc937fc24f7827bf91cfe}

### References

1. https://hitzop.com/the-fray-you-found-me/

2. https://gchq.github.io/CyberChef/#recipe=MD5()

3. https://www.aha-music.com/identify-songs-music-recognition-online/rec/8832c150ffb4ee802cb096b7fa86f3b3#record-div

4. https://hashcat.net/forum/thread-5861.html

5. https://emn178.github.io/online-tools/crc32.html

6. https://hexed.it/

7. https://images.google.com/



