from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.auth_controller import AuthController
from app.middlewares.auth_middleware import admin_required, token_required, two_fa_required 


user_bp = Blueprint('users', __name__)
auth_bp = Blueprint('auth', __name__) 

# User Routes
user_bp.add_url_rule('/emailvalidate', view_func=UserController.temp_users, methods=['POST'])
user_bp.add_url_rule('/checkotp', view_func=UserController.check_otp, methods=['POST'])
user_bp.add_url_rule('/register', view_func=UserController.register_user, methods=['POST'])
user_bp.add_url_rule('/users', view_func=UserController.get_all_users, methods=['POST'])


# Authentication Routes
auth_bp.add_url_rule('/login', view_func=AuthController.login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=token_required(AuthController.logout), methods=['POST'])  # Requires token
auth_bp.add_url_rule('/enable-2fa', view_func=token_required(AuthController.enable_2fa), methods=['POST'])
auth_bp.add_url_rule('/verify-2fa', view_func=token_required(AuthController.verify_2fa), methods=['POST'])
auth_bp.add_url_rule('/refresh', view_func=AuthController.refresh_token, methods=['POST'])  # Refresh JWT token

