"""igcommit - The base check class

Copyright (c) 2016, InnoGames GmbH
"""


class BaseCheck(object):
    """The parent class of all checks

    Checks are expanded to different objects by cloning.  The subclasses
    has to extend for_commit_list(), for_commit(), and/or for_committed_file()
    methods to clone the check.
    """
    ready = False
    failed = False

    def for_commit_list(self, commit_list):
        return None

    def for_commit(self, commit):
        return None

    def for_committed_file(self, committed_file):
        return None

    def print_problems(self):
        header_printed = False
        for problem in self.get_problems():
            if not header_printed:
                print('=== {} ==='.format(self))
                header_printed = True
            print('* ' + problem)
        if header_printed:
            print('')

    def __str__(self):
        return type(self).__name__