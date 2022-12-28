from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import User
from allauth.socialaccount.models import SocialAccount
import json
from gcp_backend.utility import hash_password
from .models import User
import uuid
import jwt
from gcp_backend.settings import COOKIE_ENCRYPTION_SECRET
from rest_framework.response import Response

class UserAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # Modifing the create user method to create a user in our table
        user = super(UserAccountAdapter, self).save_user(request, user, form)
        cookie = request.COOKIES.get('org_id')
        payload = jwt.decode(cookie, COOKIE_ENCRYPTION_SECRET, algorithms=['HS256'])
        # print user
        if User.objects.filter(email=user.email).exists():
            return Response({'message': 'User already exists'}, status=303)

        password = hash_password(str(uuid.uuid4()))
        new_user = User.objects.create(
            name = user.get_full_name(),
            email = user.email,
            password = password,
            is_verified = True,
            organization_id = payload['org_id'],
        )
        new_user.save()
        
    # Login is done authomaticaly by allauth need to send a jwt token in response 



# handle register & login


# dir(user) -> [
# 'DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned', 
# 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# '_check_column_name_clashes', '_check_constraints', '_check_default_pk', 
# '_check_field_name_clashes', '_check_fields', '_check_id_field', 
# '_check_index_together', '_check_indexes', '_check_local_fields', 
# '_check_long_column_names', '_check_m2m_through_same_relationship', 
# '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', 
# '_check_ordering', '_check_property_name_related_field_accessor_clashes', 
# '_check_single_primary_key', '_check_swappable', '_check_unique_together', 
# '_do_insert', '_do_update', '_emailaddress_cache', '_get_FIELD_display', 
# '_get_expr_references', '_get_field_value_map', '_get_next_or_previous_by_FIELD', 
# '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', 
# '_password', '_perform_date_checks', '_perform_unique_checks', 
# '_prepare_related_fields_for_save', '_save_parents', '_save_table', 
# '_set_pk_val', '_state', 'auth_token', 'bookmark_set', 'check', 
# 'check_password', 'clean', 'clean_fields', 'date_error_message', 
# 'date_joined', 'delete', 'email', 'email_user', 'emailaddress_set', 
# 'first_name', 'from_db', 'full_clean', 'get_all_permissions', 
# 'get_constraints', 'get_deferred_fields', 'get_email_field_name', 
# 'get_full_name', 'get_group_permissions', 'get_next_by_date_joined', 
# 'get_previous_by_date_joined', 'get_session_auth_hash', 
# 'get_short_name', 'get_user_permissions', 'get_username', 
# 'groups', 'has_module_perms', 'has_perm', 'has_perms', 
# 'has_usable_password', 'id', 'is_active', 'is_anonymous', 
# 'is_authenticated', 'is_staff', 'is_superuser', 'last_login', 
# 'last_name', 'logentry_set', 'natural_key', 'normalize_username', 
# 'objects', 'password', 'pinnedapplication_set', 'pk', 
# 'prepare_database_save', 'refresh_from_db', 'save', 
# 'save_base', 'serializable_value', 'set_password', 
# 'set_unusable_password', 'socialaccount_set', 'unique_error_message', 
# 'user_permissions', 'userdashboardmodule_set', 'username', 'username_validator', 
# 'validate_constraints', 'validate_unique']

#https://accounts.google.com/signin/v2/challenge/dp?
# client_id=1002371913820-cclg1ll9e4shgasndltk6jhdpegk8li2.apps.googleusercontent.com&
# redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&
# scope=email%20profile&
# response_type=code&
# state=x7iGeWT8LGq1&
# access_type=online&
# service=lso&o2v=1&
# flowName=GeneralOAuthFlow&cid=7&
# TL=AC7eWV2G5lZTO9bxword616iUnrtJ81f0LGcPijOpEo2jbu66KUD6nTxW94JZNiL&
# navigationDirection=forward

# call back url 
# GET 
# /accounts/google/login/callback/?
# state=x7iGeWT8LGq1&
# code=4%2F0AWgavdfqWZ1xKuOFguOiLaB9SHYZyROpX7GN9t0fUgCzaZxYDpkEAn8y3BhkmeY6PQTgeg&
# scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+openid&
# authuser=0&
# prompt=consent HTTP/1.1