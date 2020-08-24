# Input and Output

Let's start off simple bying opening a file to edit. Open returns a __file object__ that contains methods and attributes that can be used to collect information and the file you opened as well as manipulate them. It is important to recognized that a __file__ and __file object__ are differnt.

A file in Python is different then that in Windows OS. A file in Windows may be a binary, image, or document. They are mostly organized by keeping them in folders.

In Python, a file is catergorized as either a text or binary, the difference between both is important. 

### Text Files

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax.

#### End of Line EOL

Every line is terminated with a special character known as EoL, but the most common is the comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.

A backslash character can also be used, and it tells the interpreter that the following should be treated as a new line. Backslish is useful when you don't want to start a new line in the text itself but in the code.

### Binary

A binary file is considered any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that knows or understands the file's structure. In other words, they must be applications that can read and interpret binary.

## Open Function

In order to open a file for writing or use in Python, you must rely on the built-in Python __open__ file function.

Open generally returns a file object, so it is most commonly used with two arguments.

```python
file_object  = open(“filename”, “mode”) where file_object is the variable to add the file object. 
```

### Mode

Including a mode argument is optional because the default value is '__r__'.

|Mode|Description|
|:-:|:-:|
|r|file is only being read|
|w|edit and write new information (any existing files with the same name will be erased when this mode is activated)|
|a|append mode, which adds new data to the end; new info is automatically amended to the end|
|r+|special read and write mode, handles both actions when working with a file|

```
F = open(“workfile”,”w”) 
Print f 
```