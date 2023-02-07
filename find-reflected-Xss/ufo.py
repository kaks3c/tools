import argparse
import requests
import re
import colorama
import sys

colorama.init()

def print_name():
    print(colorama.Fore.RED     + "       ____   ")
    print(colorama.Fore.RED +     " __ __/ __/__ ")
    print(colorama.Fore.YELLOW +  "/ // / _// _ \ ")
    print(colorama.Fore.GREEN +   "\_,_/_/  \___/ ")
    print(colorama.Fore.MAGENTA + "             dev: +-+ c0ded-human\n")

def check_response(urls, check_string):
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=args.follow_redirect)
            response.raise_for_status()
            if re.search(check_string, response.text, re.IGNORECASE):
                print(f"\033[1;37m[\033[1;32mfound\033[1;37m]\033[0m {url} \033[1;37m[\033[1;32mreflect: {check_string}\033[1;37m]\033[0m")
                if args.output:
                    if args.positive:
                        with open(args.output, "a") as f:
                            f.write(f"{url}\n")
            else:
                if not args.positive:
                    print(f"\033[1;37m[\033[1;31mfail\033[1;37m]\033[0m {url}")
        except requests.exceptions.RequestException as e:
            if not args.no_error:
                print(f"\033[1;37m[\033[1;31m!\033[1;37m]\033[0m Exception occurred while processing {url}: {e}")

#arguments
parser = argparse.ArgumentParser()
parser.add_argument("-uf", "--url_file", help="file containing a list of urls to be checked")
parser.add_argument("-u", "--single_url", help="single URL to check")
parser.add_argument("-mc", "--check_string", help="string to check for in the response")
parser.add_argument("-o", "--output", help="output file name to save the results")
parser.add_argument("-p", "--positive", help="only show positive results (URLs that contains the check_string)", action="store_true")
parser.add_argument("-fr", "--follow_redirect", help="follow redirections if specified", action="store_true")
parser.add_argument("-ne", "--no_error", help="don't show error messages", action="store_true")

args = parser.parse_args()

print_name()

if args.url_file:
    try:    
        with open(args.url_file, "r") as f:
            urls = f.read().splitlines()
        print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Target loaded: " + str(len(urls)))
        if args.check_string:
            print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Match String: \033[1;37m[\033[1;32m{}\033[1;37m]\033[0m".format(args.check_string))
        if args.output:
            print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Output Path:  {}\n".format(args.output))
        check_response(urls, args.check_string)
    except FileNotFoundError as e:
        print(f"\033[1;37m[\033[1;31merror\033[1;37m]\033[0m The file '{args.url_file}' was not found. {e}")
    except KeyboardInterrupt:
        print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Exiting..."),
    except Exception as e:
        print(f"\033[1;37m[\033[1;31merror\033[1;37m]\033[0m An error occurred: {e}")
elif args.single_url:
    try:
        if args.check_string:
            print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Match String: \033[1;37m[\033[1;32m{}\033[1;37m]\033[0m".format(args.check_string))
        if args.output:
            print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Output Path: {}\n".format(args.output))
        check_response([args.single_url], args.check_string)
    except KeyboardInterrupt:
        print("\033[1;37m[\033[1;94minfo\033[1;37m]\033[0m Exiting..."),
    except Exception as e:
        print(f"\033[1;37m[\033[1;31merror\033[1;37m]\033[0m An error occurred: {e}")
else:
    print(f"\033[1;37m[\033[1;31merror\033[1;37m]\033[0m No URL provided. Please provide a URL list or a single URL using the '-uf' or '-u' flags, respectively.")
