import json

from flask import request
from app.constants.response_status import Response
from flask_jwt_extended import get_jwt_identity
from app.services.order_services import OrderService

class OrderController:
    
    @staticmethod
    def get_all_order():
        user_id = json.loads(get_jwt_identity())['user_id']
        response = OrderService.get_order(user_id)
        return Response.success(data=response, message="Orders fetched successfully", code=200)
    
    @staticmethod
    def create_order():
        user_id = json.loads(get_jwt_identity())['user_id']
        response = OrderService.create_order(user_id)
        return Response.success(data=response, message="Order created successfully", code=201)
    
    @staticmethod
    def payment_order():
        invoice_number = request.get_json()['invoice_number']
        user_id = json.loads(get_jwt_identity())['user_id']
        
        response = OrderService.payment_order(invoice_number, user_id)
        
        if response is None:
            return Response.error(message="Order not found", code=404)
            
        return Response.success(data=response, message="Order payment successfully", code=200)
    
    @staticmethod
    def cancel_order():
        invoice_number = request.get_json()['invoice_number']
        user_id = json.loads(get_jwt_identity())['user_id']
        
        response = OrderService.cancel_order(invoice_number, user_id)
        
        if response is None:
            return Response.error(message="Order not found", code=404)
            
        return Response.success(data=response, message="Order canceled successfully", code=200)
    
    @staticmethod
    def get_user_transaction_history(user_id):
        response = OrderService.get_user_transaction_history(user_id)
        return Response.success(data=response, message="Transaction history fetched successfully", code=200)
    
    def get_seller_transaction_history(seller_id):
        response = OrderService.get_seller_transaction_history(seller_id)
        return Response.success(data=response, message="Transaction history fetched successfully", code=200)
    