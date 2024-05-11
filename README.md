NAME
        wordbuster - a tool to create wordlists or combinations

SYNOPSIS
        wordbuster [-r min max | -l number] [-p chars] [-o file]

DESCRIPTION
        This page documents briefly the wordbuster command. Wordbuster
        is a Python tool to create wordlists or dictionaries. Wordbuster
        supports different creating modes and will understand many languages,
        like Uzbek, English and Russian.

USAGE
        To use Wordbuster, you just need to supply it a list of characters
        and the length of word. If length is not specified, wordbuster will
        create words consisting of up to 4 characters.

        Once Wordbuster creates the wordlist, it will print the details of
        wordlist also saved into a file called ~/wordbuster_history.txt.
        Wordbuster will read this file when it restarts.

        To see the latest created wordlist, use
                python3 wordbuster.py --history

OPTIONS
        A summary of options is shown below.
        
        -h, --help
        	Shows summary of options.
        
        -V, --version
        	Shows version of program.

        -m, --manual
          Shows manual page text

        -H, --history
          Shows history from wordbuster_history.txt

        -r, --range
          Sets minimum and maximum length of word

        -l, --length
          Shortcut for --range X X
        
        --upper
          Uses upper letters set
        --lower
          Uses lower letters set
        --alpha
          Uses uppercase and lowercase letters set
        --num
          Uses digits set
        --all
          Uses all letters and numbers
        
        -p, --pass
          Gives characters you want to include only
        -v, --verbose
          Shows essential messages
          Default: on

	If you write -h(--help), -V(--version), -H(--history) or -m(--manual), other given arguments doesn't work. If not given any characters, then Wordbuster use 26 lower letters.
	
	Note: you can't use -r, --range and -l, --length simultaneously. Also, -p, --pass with options such as --upper, --lower, --alpha, --num, or --all. However, you can mix --upper and --num.

MODES
        Wordbuster can work in the following modes:
	
        Brute-force
          This is the most powerful mode. Wordbuster will try any character combination.
        
        No repetition
          In  this  mode, wordbuster will try to create the list using given characters once each word.

EXAMPLES
        Example 1
        python3 wordbuster.py -r 1 3 --pass abcd -o passwords.txt. Wordbuster will create wordlist that starts with a and ends at ddd and write all of combinations to a file named passwords.txt

        Example 2
        python3 wordbuster.py -l 2 --upper --num -o wordlist.txt. Wordbuster will write the wordlist to a file called wordlist.txt. The file will start at AA and end at 99.

FILES
        wordbuster_history.txt
          is where every action is documented.

AUTHOR
        Wordbuster tool and program manual page were written by Saidbek Rahimbekov.
