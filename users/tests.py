from mock import patch

from django.test import TestCase

from users.helpers import UsernamesResolutionHelper


class UsernamesResolutionHelperTests(TestCase):
    def setUp(self):
        self.duplicate_affected_users = UsernamesResolutionHelper(
            resolve_type='duplicates')
        self.disallowed_affected_users = UsernamesResolutionHelper(
            resolve_type='disallowed')

    def test_update_users_with_duplicate_names(self):

        updated_user_list = self.duplicate_affected_users.update_users()

        self.assertEqual(updated_user_list[0].username, 'abdiel1')
        self.assertEqual(updated_user_list[1].username, 'abdiel2')

        self.assertEqual(updated_user_list[2].username, 'abdullah9')
        self.assertEqual(updated_user_list[3].username, 'abdullah10')

    def test_update_users_with_disallowed_names(self):

        updated_user_list = self.disallowed_affected_users.update_users()

        self.assertEqual(updated_user_list[0].username, 'about1')
        self.assertEqual(updated_user_list[1].username, 'about2')
        self.assertEqual(updated_user_list[2].username, 'about3')
        self.assertEqual(updated_user_list[3].username, 'about4')

        self.assertEqual(updated_user_list[4].username, 'grailed1')
        self.assertEqual(updated_user_list[5].username, 'grailed2')
        self.assertEqual(updated_user_list[6].username, 'grailed3')
        self.assertEqual(updated_user_list[7].username, 'grailed4')

    @patch('users.helpers.UsernamesResolutionHelper.update_users')
    def test_get_users_for_duplicate_usernames_dry_run(self, mock_update_users):
        test_get_dry_run_users = UsernamesResolutionHelper(
            resolve_type='duplicates')

        users = test_get_dry_run_users.get_users()

        self.assertEqual(users[0].username, 'abdiel1')
        self.assertEqual(users[1].username, 'abdiel1')
        mock_update_users.assert_not_called()

    @patch('users.helpers.UsernamesResolutionHelper.update_users')
    def test_get_users_for_duplicate_usernames_non_dry_run(self, mock_update_users):
        test_get_updated_users = UsernamesResolutionHelper(
            resolve_type='duplicates', dry_run=False)

        users = test_get_updated_users.get_users()

        mock_update_users.assert_called_once()

    @patch('users.helpers.UsernamesResolutionHelper.update_users')
    def test_get_users_for_disallowed_usernames_dry_run(self, mock_update_users):
        test_get_dry_run_users = UsernamesResolutionHelper(
            resolve_type='disallowed')

        users = test_get_dry_run_users.get_users()

        self.assertEqual(users[0].username, 'about')
        self.assertEqual(users[1].username, 'about')
        mock_update_users.assert_not_called()

    @patch('users.helpers.UsernamesResolutionHelper.update_users')
    def test_get_users_for_disallowed_usernames_non_dry_run(self, mock_update_users):
        test_get_updated_users = UsernamesResolutionHelper(
            resolve_type='disallowed', dry_run=False)

        users = test_get_updated_users.get_users()

        mock_update_users.assert_called_once()
