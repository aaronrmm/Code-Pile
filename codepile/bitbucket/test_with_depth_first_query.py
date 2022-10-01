import unittest

from codepile.bitbucket.api import BitbucketQueryConfig
from codepile.bitbucket.queries import query_public_repos
from codepile.bitbucket.types import BitbucketQueryResult


class BitbucketQueryTests(unittest.TestCase):
    def test_query_nothing(self):
        """ Ensure a query for 0 repos returns no results """
        query_config = BitbucketQueryConfig()
        result: BitbucketQueryResult = query_public_repos(query_config)
        self.assertEqual(result.starting_query, result.next_query)

    def test_query_one_leaf_only(self):
        """ Do a depth first search and take only the first result for each set of child nodes"""
        # TODO


if __name__ == "__main__":
    unittest.main()
