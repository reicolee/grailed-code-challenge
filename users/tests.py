from django.test import TestCase

from users.helpers import UsernamesResolutionHelper


class UsernamesResolutionHelperTests(TestCase):
    def setUp(self):
        self.user_with_duplicate_names_queries_one = [
            {id: 2, usernames: 'tom'}, {id: 14, usernames: 'tom'}]
        self.user_with_duplicate_names_queries_two = [{id: 2, usernames: 'tom'}, {
            id: 14, usernames: 'tom'}, {id: 15, usernames: 'tom1'}, {id: 18, usernames: 'tom2'}]
        self.user_with_disallowed_names_queries_one = [{id: 2, usernames: 'grailed'}, {
            id: 14, usernames: 'grailed'}, {id: 15, usernames: 'grailed'}, {id: 18, usernames: 'about'}, {id: 19, usernames: 'about'}, {id: 25, usernames: 'heroine'}]
        self.user_with_disallowed_names_queries_two = [{
            id: 14, usernames: 'profile'}, {id: 15, usernames: 'terms'}, {id: 18, usernames: 'privacy'}, {id: 19, usernames: 'profile'}, {id: 25, usernames: 'settings'}]
        self.user_with_disallowed_names_queries_three = [{
            id: 14, usernames: 'profile'}, {id: 15, usernames: 'terms'}, {id: 18, usernames: 'terms1'}, {id: 19, usernames: 'profile'}, {id: 25, usernames: 'profile1'}, {id: 29, username: 'profile2'}]
        return

    def test_update_users_with_duplicate_names(self):
        return

    def test_update_users_with_duplicates_with_existing_names(self):

        return

    def test_get_useres(self):
        return
