Summary:

This script is a simple website scanner that checks whether a list of URLs or a single URL contains a specified string. If a URL is found to contain the string, the script prints a message saying "found" and the URL. If a URL does not contain the string, the script prints a message saying "fail" and the URL. The script also provides the option to save the results to an output file and to only show positive results.

Usage:

This script is used from the command line and has the following options:

-uf/--url_file: A file containing a list of URLs to be checked.

-u/--single_url: A single URL to check.

-mc/--check_string: The string to check for in the response.

-o/--output: An output file name to save the results.

-p/--positive: Only show positive results (URLs that contain the check_string).

Example:

> cat dummy-site.txt | qsreplace 'fuzzme' | grep 'fuzzme' | sort -u > Urls-to-test.txt
> python script.py -uf Urls-to-test.txt -mc "check string" -o reflected-parameters.txt -p

In the above example, the script will check the URLs in the file "urls.txt" for the string "check string". The results will be saved to the file "output.txt" and only positive results will be shown.

Note: The qsreplace command mentioned in the prompt is not related to this script and is not used in this script.



