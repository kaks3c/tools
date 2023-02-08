## 7 Feb, 2023 Updates:
1. -fr/--follow_redirect: follow redirections if specified.

2. -ne/--no_error: Don't show error messages.

3. Filtered and clean Output file format.

![Sample image](https://github.com/c0ded-human/bugbounty/blob/main/find-reflected-Xss/sample.png)



## Summary:

This script is a simple website scanner that checks whether a list of URLs or a single URL contains a specified string. If a URL is found to contain the string, the script prints a message saying "found" and the URL. If a URL does not contain the string, the script prints a message saying "fail" and the URL. The script also provides the option to save the results to an output file and to only show positive results.

## Requirements
* Python 3.x
* requests library
* colorama library
* re library 

`` pip install re colorama requests  ``
## Usage:

This script is used from the command line and has the following options:

-uf/--url_file: A file containing a list of URLs to be checked.

-u/--single_url: A single URL to check.

-mc/--check_string: The string to check for in the response.

-o/--output: An output file name to save the results.

-p/--positive: Only show positive results (URLs that contain the check_string).

-fr/--follow_redirect: follow redirections if specified.

-ne/--no_error: Don't show error messages.

### Example:

```$ cat dummy-site.txt | qsreplace 'fuzzme' | grep 'fuzzme' | sort -u > Urls-to-test.txt```

```$ python3 ufo.py -p -se -uf Urls-to-test.txt -mc "fuzzme" -o reflected-parameters.txt```

In the above example, the script will check the URLs in the file "Urls-to-test.txt" for the string "fuzzme". The results will be saved to the file "reflected-parameters.txt" and only positive results will be shown.

** Note: The qsreplace command mentioned in the prompt is not related to this script and is not used in this script. **

## Here is some advance usage:

1. ```$ cat dummy-site.txt | qsreplace '</fuzzme>' | tee -a xss-1.txt```

   ```$ python3 ufo.py -p -se -uf xss-1.txt-mc "</fuzzme>" -o result.txt```
   
2. ```$ cat dummy-site.txt | qsreplace '1%3C1%2Ffuzz%3E1' | tee -a xss-1.txt```
     
   ```$ python3 ufo.py -p -se -uf xss-1.txt-mc "1<1/fuzz>1" -o result.txt```


### The script was developed by a developer/security-researcher named c0ded-human 



