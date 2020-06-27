lexical_analyzer.exe can be executed by windows cmd.
put your <input_file_name> file in the same directory with lexical_analyzer.exe,
and please type on cmd window.

lexical_analyzer <input_file_name>

e.g) 
cmd
C:\Users\admin\Desktop\test>lexical_analyzer code1.c
...
...
then, you can find .out file that includes the result of our program in the same directory.

also,
syntax_analyzer.exe can be executed by windows cmd.
after executing lexical_analyzer, please type on cmd window.

syntax_analyzer <output_of_lexical_analyzer>

e.g) 
cmd
C:\Users\admin\Desktop\test>syntax_analyzer code1.out
...
...
then, you can find .out file if <output_of_lexical_analyzer> is rejected.
if not, you can see accept message on cmd window.
 