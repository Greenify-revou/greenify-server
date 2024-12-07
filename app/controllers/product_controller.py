# user_controller.py
from email_validator import validate_email, EmailNotValidError
from flask import json, request
from flask_jwt_extended import get_jwt_identity
from pydantic import ValidationError
from app.constants.response_status import Response
from app.services.product_services import ProductService 
from app.utils.validators import AddCategory, AddProduct   

class ProductController:
    
    @staticmethod
    def add_category():
        data = request.get_json()
        
        try:
            validate_category = AddCategory.model_validate(data)
        except ValidationError as e:
            return Response.error(f"{str(e)}", 400)
        
        response = ProductService.add_category(validate_category.model_dump())
        
        if response is None:
            return Response.error(message='Already exists', code=400)
        
        return response
    
    @staticmethod
    def add_product():
        data = request.get_json()
        
        try:
            validate_product = AddProduct.model_validate(data)
        except ValidationError as e:
            return Response.error(f"{str(e)}", 400)
        
        response = ProductService.add_product(validate_product.model_dump())
        
        if response is None:
            return Response.error(message='Oops, something went wrong', code=400)
        
        return response
    
    
    @staticmethod
    def landing_product():
        data = request.get_json()
        
        try:
            validate_product = AddProduct.model_validate(data)
        except ValidationError as e:
            return Response.error(f"{str(e)}", 400)
        
        response = ProductService.add_product(validate_product.model_dump())
        
        if response is None:
            return Response.error(message='Oops, something went wrong', code=400)
        
        return response
    
    
    @staticmethod
    def recommendation_product():
        user_id = json.loads(get_jwt_identity())['user_id']
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        recommendations = ProductService.get_recommendations(user_id, page, per_page)
        return Response.success(data=recommendations, message="Success get data recommendation", code=200)