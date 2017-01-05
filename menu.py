def get_profile():
    print('Get Profile')


def get_rank():
    print('Get Rank')


def get_tokens():
    print('Get tokens')


me_menu_dict = {
    '0': ('Profile', get_profile),
    '1': ('Rank', get_rank),
    '2': ('Tokens', get_tokens)
}

main_menu_dict = {
    '0': ('Me', me_menu_dict),
    '1': ('Quit', 0)
}


def text_menu():
    while True:
        print('Main Menu')
        for k,v in sorted(main_menu_dict.items()):
            print("\t{}. {}".format(k, v[0]))

        selection = input('Please enter the number of your selection: ')

        if selection == '6':
            break
        else:
            while True:

                # going in one level to get the menu attached to the main menu
                # this is actually just the key to that submenu

                print("\n{} Menu\n".format(main_menu_dict[selection][0]))

                # The dict doesn’t give us data sorted
                # Dicts are called by key so order isn’t a problem.
                # but we WANT it sorted by key in this case
                # so we wrap the main_menu_dict in a sorted() call.

                for item in sorted(main_menu_dict[selection][1]):

                    """this is a bit more complex
                    because we embedded dicts in dicts in tuples

                    here we go

                    1. main_menu_dict[selection]
                       This returns the main menu selection key/val tuple
                           ('Me', me_menu_dict)

                       Which remember expands to the full dictionary
                           (‘Me’, {
                                   ‘0’: (‘Profile’, get_profile),
                                   ‘1’: (‘Rank’, get_rank),
                                   ‘2’: (‘Tokens’, get_tokens)
                                   })

                    2. main_menu_dict[selection][1]
                       returns the embedded MENU in the main menu tuple
                       which in main menu is the call to me_menu_dict in the tuple
                           {‘0’: (‘Profile’, get_profile),
                            ‘1’: (‘Rank’, get_rank),
                            ‘2’: (‘Tokens’, get_tokens)}

                    3. main_menu_dict[selection][1][item]
                       returns the value from the embedded menu - our next tuple
                           (Profile, <function get_profile at 0x7f08ee5b1840>)

                    4. main_menu_dict[selection][1][item][0]
                       is the first value in the tuple
                       Which is in the VALUE of the embedded menu
                           ‘Profile’

                    5. If we grabbed the second index in the tuple to
                       main_menu_dict[selection][1][item][1]
                       it would return the pointer to the function
                           <function get_profile at 0x7f08ee5b1840>

                       See how that’s a pointer to a memory location
                       of the function? In this case 0x7f08ee5b1840
                    """

                    # here we just print out the keys to the sub menu.
                    # See number four above.

                    print("\t{}. {}".format(item,
                                        main_menu_dict[selection][1][item][0]))

                # Our sub menu selection
                # We’re out of the for loop above, which just prints our menu.
                # now we want to know where the user wants to go
                print("Please enter the number of your selection.")
                new_selection = input('Hit enter to return to main menu: ')

                if new_selection == '':
                    break
                    """So now we have our last selection
                       This is from the SUB menu.
                       Let's go ahead and execute the function

                       This is a cool thing about Python,
                       in the dictionary we are storing a pointer
                       to each function, but not executing it since
                       there are no parens after the function name.
                       first class objects! So when we call below,
                       we add the parens and BAM! function call.
                    """
                else:
                    main_menu_dict[selection][1][new_selection][1]()