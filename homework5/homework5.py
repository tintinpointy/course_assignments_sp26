#1. Git takes care of project history, while GitHub is the repository hosting platforms utilising git.
#2. Terminal device environment that takes input and displays texts, while commandline is the location of the terminal that takes inputs.
#3. Local repository is data stored on your computer, while remote repository is data stored on servers
#4. Version control is the history of data changes made on the computer
#5. A designated, temporary location used to work on data before sending it to a final location.
#6. Used to promote changes in the Git working directory to the staging area.
#7. Used to save a snapshot of your staged changes to the local Git repository.
#8. Uploads commits crom your local repository to a remote repository.
#9. An overview of the current state of your Git working directory and staging area.
#10. Fetches and downloads content from a remote repository and integrates the changes into your local repository.
#11. Prints the current absolute directory you're on.
#12. Lists the contents of the directory you're in.
#13. Allows the user to move from one directory to the next.
#14. Allows the user to edit a file.
#15. Allows the user to create a file.
#16. Used to move or rename a file.
#17. Allows you to remove a file from your working directory.
#18. Allows one to display the contents of files, concatenate multiple files, and create new files within the terminal environment.

#1. pwd
#2. ls
#3. cd ../brianna_repo, then get git pull
#4. cp homework.py ../judy_decal/homework/
#5. cd ../judy_decal/homework/
#6. cat homework.py
#7. git add homework.py
#8. git commit -m "Done with homework"
#9. git push
#10. Someone else pushed the changes to the remote repository that I don't have on my local machine yet. I need to use git pull to merge the files locally then git push again.
#11. ~/Recent/

def checkDataType(thing):
	print(type(thing))
checkDataType(3.14)
checkDataType(True)

def evenOrOdd(num):
	if num % 2 == 0:
		print("Even")
	else:
		print("Odd")
evenOrOdd(7)
evenOrOdd(10)

def duplicateList(list):
	list = list + list
	print(list)
duplicateList(['a','b','c'])

def square(num):
	return num * num
print(square(3))

duplicateList([6,7])