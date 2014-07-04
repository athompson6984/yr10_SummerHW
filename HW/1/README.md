#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Computers read commands as ons and offs, or 1s and 0s.
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for your working. *(2 marks)*
```
binary: 1011 0101
1+4+16+32+128
denary: 181


```
###4 - Here is a function written in **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
A list
```

(b) What type of data is returned by this function? **(1 mark)**
```
Boolean
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
line 3
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
an error in which the program cannot understand what the user is trying to do (due to a spelling error or misuse of code)
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
line6: It is meant to be creating the mean of the all the numbers. This means that it should be dividing the tot variable by the total amount the numbers in the nums list.
To do this, line6 should be changed to mean <- tot/LEN(nums)
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
runtime errors are errors that can cause the program to not function properly (for example, giving it an infinite loop).
There is a runtime error in line4, where it continuously makes the last number in the nums list the tot variable. This means that tot will always be 3, rather than the variable adding all of the numbers in nums together.
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
nums <- [8,5,9,3,6,4]
x <- StartofList
WHILE sorted <- False
	Repeat
		If nums(x) is greater than nums(x+1)
			temp <- nums(x)
			nums(x) <- nums(x+1)
			nums(x+1) <- temp
		End If
		x <- x+1
	Until EndofList
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: In a bus network all  sections of the network (computers, servers or printers) are joined together on one cable. There is a terminator at each end of the cable to prevent signals being reflected back down.

Advantages: It is easy to install and cheap, as it does not require much cable. 

Disadvantages: If the main cable fails or is damaged, the entire network will fail. Data collisions will slow the network down as more sections are added. All computers on the network can see all of the data on the network, creating a security risk.
```

**Ring Topology (6 marks)**
```
Describe: Each device in the network is connected to two other devices, to create a ring. All information on the network is passed around the ring until it is recieved by the device that needs it.

Advantages: There will not be any data collisions, and so data can travel quickly around the network, even on large networks. 

Disadvantages: If the main cable fails or any device is faulty, the whole network will fail.
```

**Star Topology (6 marks)**
```
Describe: Each device on the network has its own cable with which it connects to a main hub or a switch. A hub will send data to every device on the network, wheras a switch will only send data to the destination device. 

Advantages: If one cable or device fails then it will not affect the rest of the network. It is higher performing as there will not be any data collisions.

Disadvantages: It is the most expensive to set up as it requires the most amount of cable. Extra hardware is required in the form of switches or hubs, which adds to the cost. If a hub or switch fails, all the devices which are connected to it will no longer have a connection.
```
