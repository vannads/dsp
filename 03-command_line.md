# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

Task | Command | Notes/example result
-----|---------|-------
Show current working directory path | pwd | /Users/svannadil
Creating a directory | mkdir temp00 | Creates temp00 under /Users/svannadil
Deleting a directory | rmdir temp00 | Removes temp00 under /Users/svannadil
Creating a file using touch command | touch test.txt | Creates a new empty file test.txt, if exists update modification date
Delecting a file | rm test.txt | Removes test.txt
Renaming a file | mv test.txt test01.txt | Renames test.txt as test01.txt
Listing hidden files | ls -a | List all, including hidden files
Copying a file from one directory to another | cp temp01/test01.txt temp02/ | Copies file test01.txt from directory temp01 to directory temp02
Copy multiple files into a directory | cp file1.txt file2.py file3.js target/ | Copies file1, file2, and file3 into directory target/
Recursively copy from one directory to another | cp -R source/ target/ | Recursively copies from source/ to target/ 

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > Answer below:
Command | Description
-----|---------
ls | List directory contents
ls -a | List directory contents, including directories whose name begins with a dot (.)
ls -l | List directory contents in long format
ls -lh | List directory contents in long format, use unit suffixes (B, K, M, G, T etc.) to reduce the number of digits to 3 or less
ls -lah | same as above, but include directories whose name begins with a dot (.)
ls -t | Sort by time modified (recently modified first) before sorting the operands by lexicographical order
ls -Glp | List directory contents in long format, show a slash ('/') after directory names, and enable colorized output
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > Answer below:

Command | Description
-----|---------
ls -g | List directory contents in long format, exclude owner name
ls -go | List directory contents in long format, exclude owner name and group name
ls -goat | List directory contents in long format, including directories whose name begins with a dot (.), exclude owner name and group name, with newest files first
ls -m | List files across the page seperated by commas
ls -l dirName | List contents of the directory, dirName, in long format


---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

